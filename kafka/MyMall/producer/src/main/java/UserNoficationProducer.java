import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;

public class UserNoficationProducer {

    KafkaProducer<String, String> producer;

    public UserNoficationProducer() {
        this.producer = Utility.createKafkaProducer();
    }

    /**
     * @param offerId This method will send Notification to the Kafka Topic
     */
    void notifyUser(final String userId, String offerId) {
        // Form the subject and body of message
        String subject = "Offer avaialable";
        // Search the offer details based on offer id
        String offerDetails = getOfferDetails(offerId);

        // Form the final message and send to Kafka topic
        final String body = "Congratulations !!!\nYou have a discount coupon of 20%. Offer valid till " +
                "11PM today.\nHurry up.";
        producer.send(new ProducerRecord<String, String>("notify-user", userId, body),
                new Callback() {
                    public void onCompletion(RecordMetadata recordMetadata, Exception e) {
                        if (e != null) {
                            System.out.println("Error Message = " + e.getMessage());
                        } else {
                            String msg = String.format("%s - Message sent successfully %s", userId, body);
                            System.out.println(msg);
                        }
                    }
                });
    }

    private String getOfferDetails(String offerId) {
        return null;
    }

    // Close the producer, will be called by the developer
    void closeProducer() {
        producer.close();
    }

}
