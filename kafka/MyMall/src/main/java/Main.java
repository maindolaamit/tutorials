import org.apache.spark.sql.Column;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.streaming.OutputMode;
import org.apache.spark.sql.streaming.StreamingQuery;
import org.apache.spark.sql.streaming.StreamingQueryException;
import org.apache.spark.sql.types.StructType;

import java.util.concurrent.TimeoutException;

public class Main {
    static double R = 6371.0087714150598f;
    private static double[] MALL_GPS_LOCATION = {28.457553f, 77.026344f};

    private static Column getDistanceInMeters(double[] loc1, double[] loc2) {
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

        distance = Math.pow(distance, 2);

        return Math.sqrt(distance);
    }

    public static void main(String[] args) {

        SparkSession spark = SparkSession
                .builder().appName("CustomerData")
                .config("spark.master", "local").getOrCreate();

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

        df.filter("spendingScore > 70").show();

        String bootstrapServer = "127.0.0.1:9092";
        String userLocationTopic = "send-locations";

        Dataset<Row> streamDF = spark
                .readStream()
                .format("kafka")
                .option("kafka.bootstrap.servers", bootstrapServer)
                .option("subscribe", userLocationTopic)
                .load();
        double[] location = {12.12121, 212.12121};
        Dataset<Row> locationStreamDF = streamDF
                .withColumn("distance", getDistanceInMeters(location, MALL_GPS_LOCATION));
        locationStreamDF.filter("distance > 1000"); // Filter users with distance greater than 1000 meters


        try {
            StreamingQuery query = locationStreamDF
                    .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
                    .writeStream()
                    .outputMode(OutputMode.Append())
                    .format("console")
                    .start();
            query.awaitTermination();
        } catch (StreamingQueryException e) {
            e.printStackTrace();
        } catch (TimeoutException e) {
            e.printStackTrace();
        }

    }
}
