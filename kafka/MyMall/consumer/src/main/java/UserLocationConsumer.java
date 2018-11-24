import com.fasterxml.jackson.databind.deser.std.StringDeserializer;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.spark.api.java.function.ForeachFunction;
import org.apache.spark.sql.Column;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.streaming.OutputMode;
import org.apache.spark.sql.streaming.StreamingQuery;
import org.apache.spark.sql.streaming.StreamingQueryException;
import org.apache.spark.sql.types.StringType;
import org.apache.spark.sql.types.StructType;
import org.apache.spark.streaming.Durations;
import org.apache.spark.streaming.api.java.JavaInputDStream;
import org.apache.spark.streaming.api.java.JavaPairDStream;
import org.apache.spark.streaming.api.java.JavaStreamingContext;
import org.apache.spark.streaming.kafka010.ConsumerStrategies;
import org.apache.spark.streaming.kafka010.KafkaUtils;
import org.apache.spark.streaming.kafka010.LocationStrategies;
import scala.Function1;
import scala.Tuple2;
import scala.runtime.BoxedUnit;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.TimeoutException;

public class UserLocationConsumer {
    double R = 6371.0087714150598f;

    private double getDistanceInMeters(double[] loc1) {
        final double[] loc2 = {28.457553f, 77.026344f};
        // Convert into radian
        double lat1 = Math.toRadians(loc1[0]);
        double lon1 = Math.toRadians(loc1[1]);
        double lat2 = Math.toRadians(loc2[0]);
        double lon2 = Math.toRadians(loc2[1]);
        // Take difference and Convert into radian
        double latDistance = Math.toRadians(lat2 - lat1);
        double lonDistance = Math.toRadians(lon2 - lon1);
        double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2)
                + Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2))
                * Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        double distance = R * c * 1000; // convert to meters

        distance = Math.abs(Math.pow(distance, 2));

        return Math.sqrt(distance);
    }

    private Dataset<Row> getCustomerDF(SparkSession spark) {
        StructType schema = new StructType()
                .add("customerId", "string")
                .add("gender", "string")
                .add("age", "long")
                .add("annualIncome", "long")
                .add("spendingScore", "long");

        Dataset<Row> df = spark.read()
                .option("mode", "DROPMALFORMED")
                .schema(schema)
                .csv("customers.csv");

        return df.filter("spendingScore > 70");
    }

    public void startConsuming() {
        SparkSession spark = SparkSession
                .builder().appName("UserLocationConsumerApp")
                .config("spark.master", "local").getOrCreate();

        Dataset<Row> customerDF = getCustomerDF(spark);

        String bootstrapServer = "127.0.0.1:9092";
        String userLocationTopic = "send-locations";
        Dataset<Row> streamDF = spark
                .readStream()
                .format("kafka")
                .option("kafka.bootstrap.servers", bootstrapServer)
                .option("subscribe", userLocationTopic)
                .option("startingOffsets", "latest")
                .load();

        // Add column distance to the Dataframe and apply distance filter
        Dataset<Row> locationStreamDF = streamDF.selectExpr("CAST(key AS STRING) customerId", "CAST(value AS STRING) " +
                "location");
        // Add distance to the DataSet
        locationStreamDF = locationStreamDF
                .withColumn("distance", this.getDistanceInMeters(locationStreamDF.col("location")));
        locationStreamDF.filter("distance > 1000"); // Filter users with distance greater than 1000 meters

        // Join the Dataset with Customer
        Dataset<Tuple2<Row, Row>> joinedDF = customerDF.joinWith(locationStreamDF,
                locationStreamDF.col("customerId").equalTo(customerDF.col("customerId")));

        // Write key-value data from a DataFrame to a specific Kafka topic specified in an option
        try {
            StreamingQuery ds = joinedDF
                    .selectExpr("CAST(customerId AS STRING)")
                    .writeStream()
                    .format("kafka")
                    .option("kafka.bootstrap.servers", bootstrapServer)
                    .option("topic", "notify-user")
                    .start();
        } catch (TimeoutException e) {
            e.printStackTrace();
        }
    }

    private Column getDistanceInMeters(Column location) {
        return null;
    }
}
