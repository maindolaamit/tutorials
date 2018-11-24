import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.StringSerializer;

import javax.rmi.CORBA.Util;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;
import java.util.Random;

class UserLocationProducer {
    private double[] MALL_GPS_LOCATION = {28.457553f, 77.026344f};
    double R = 6371.0087714150598f;

    /**
     * Generate random GPS data for the customer
     */
    void generate_data() throws InterruptedException {
        try {
            BufferedReader df = new BufferedReader(new FileReader("customers.csv"));
            String line = "";
            // Loop for each customer and generate random data
            while ((line = df.readLine()) != null) {
                final String customerId = line.split(",")[0];

                // Skip first line
                if (customerId.toLowerCase().equals("customerid")) continue;

                // Randomly generate a delta for gps location
                double[] gpsLocation = {Math.random() * Math.random() * 0.1f, Math.random() * Math.random() * 0.1f};
                final double[] currLocation = getCurrentLocation(gpsLocation);
                // Randomly decide to send location for the user
                if (currLocation == null) continue;

                KafkaProducer<String, String> producer = Utility.createKafkaProducer();
                final String str = String.format("lat=%f,long=%f", currLocation[0], currLocation[1]);
                producer.send(new ProducerRecord<String, String>("send-locations", customerId, str),
                        new Callback() {
                            public void onCompletion(RecordMetadata recordMetadata, Exception e) {
                                if (e != null) {
                                    System.out.println("Error Message = " + e.getMessage());
                                } else {
                                    String msg = String.format("%s - Message sent successfully %s", customerId, str);
                                    System.out.println(msg);
                                }
                            }
                        });
                // Sleep for some time
                Thread.sleep(5000);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


//    /**
//     * @return Kafka Producer<String,String></String,String>
//     */
//    private KafkaProducer<String, String> createKafkaProducer() {
//        String bootstrapServer = "127.0.0.1:9092";
//        Properties properties = new Properties();
//        properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServer);
//        properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
//        properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
//        // Create Safe Producer
////        properties.setProperty(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, "true");
//        properties.setProperty(ProducerConfig.ACKS_CONFIG, "all");
//        properties.setProperty(ProducerConfig.RETRIES_CONFIG, Integer.toString(Integer.MAX_VALUE));
//        properties.setProperty(ProducerConfig.MAX_IN_FLIGHT_REQUESTS_PER_CONNECTION, "5");
//
//        // high throughput producer (at the expense of a bit of latency and CPU usage)
//        properties.setProperty(ProducerConfig.COMPRESSION_TYPE_CONFIG, "snappy");
//        properties.setProperty(ProducerConfig.LINGER_MS_CONFIG, "20");
//        properties.setProperty(ProducerConfig.BATCH_SIZE_CONFIG, Integer.toString(32 * 1024));
//
//        return new KafkaProducer<String, String>(properties);
//    }

    // Return the random location near MALL Location
    private double[] getCurrentLocation(double[] gpsLocation) {
        Random rand = new Random();
        int i = rand.nextInt(3);
        if (i == 0) {
            return new double[]{MALL_GPS_LOCATION[0] - gpsLocation[0], MALL_GPS_LOCATION[1] - gpsLocation[1]};
        } else if (i == 1) {
            return new double[]{MALL_GPS_LOCATION[0] + gpsLocation[0], MALL_GPS_LOCATION[1] + gpsLocation[1]};
        } else {
            return null;
        }
    }
}
