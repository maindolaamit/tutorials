import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringSerializer;

import java.time.Duration;
import java.util.Properties;

public class UserNotificationConsumer {

    void sendNotifications() {
        KafkaConsumer consumer = createKafkaConsumer();
        while (true) {
            ConsumerRecords<String, String> records = consumer.poll(Duration.ofSeconds(10));

            // Loop for records and send notification
            for (ConsumerRecord<String, String> record : records) {
                String userId = record.key();
                String body = record.value();

                sendEmail(userId, body); // Send email notification
                sendSMS(userId, body); // Send SMS notification
            }
        }
    }

    private void sendSMS(String userId, String body) {
        System.out.println("Sent sms to user");
    }

    private void sendEmail(String userId, String body) {
        System.out.println("Sent Email to user");
    }

    /**
     * @return Kafka Producer<String,String></String,String>
     */
    public static KafkaConsumer<String, String> createKafkaConsumer() {
        String bootstrapServer = "127.0.0.1:9092";
        String topic = "notify-offers";
        Properties properties = new Properties();

        // Set properties
        properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServer);
        properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        properties.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

        return new KafkaConsumer<String, String>(properties);
    }
}
