public class Main {

    public static void main(String[] args) {
        testUserLocationProducer();
//        testUserNotificationProducer();
    }

    private static void testUserLocationProducer() {
        UserLocationProducer producer = new UserLocationProducer();
        try {
            producer.generate_data();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private static void testUserNotificationProducer() {
        UserNoficationProducer producer = new UserNoficationProducer();
        producer.notifyUser("12", "123");
    }
}
