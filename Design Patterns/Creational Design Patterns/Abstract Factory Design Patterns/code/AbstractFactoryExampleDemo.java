interface Notification{
    String getNotification();
    String sendNotification(String recipient);
}

class SMSNotification implements Notification{
    @Override
    public String getNotification() {
        return "SMS";
    }

    @Override
    public String sendNotification(String recipient) {
        System.out.println("SMS Message Sent");
        return "SMS Message Sent";
    }
}

class EmailNotification implements Notification{
    @Override
    public String getNotification() {
        return "Email";
    }

    @Override
    public String sendNotification(String recipient) {
        System.out.println("Email Message sent");
        return "Email mail sent";
    }
}

interface Order {
    String getOrder();
    void markOrderDelivered();
}

class CustomOrder implements Order{

    @Override
    public String getOrder() {
        return "Custom Order";
    }

    @Override
    public void markOrderDelivered() {
        System.out.println("Customer order delivered");
    }
}

class MerchantOrder implements Order{

    @Override
    public String getOrder() {
        return "Merchant order";
    }

    @Override
    public void markOrderDelivered() {
        System.out.println("Merchant order delivered");
    }
}

interface AbstractFactory{
     Order getOrder(String order);
     Notification getNotification(String notification);
}

class ORderFactory implements AbstractFactory{

    @Override
    public Order getOrder(String order) {
        if(order == "MERCHANT")
            return new MerchantOrder();
        if(order == "CUSTOMER")
            return new CustomOrder();
        return null;
    }

    @Override
    public Notification getNotification(String notification) {
        return null;
    }
}

class NotificationFactory implements AbstractFactory{
    @Override
    public Order getOrder(String order) {
        return null;
    }

    @Override
    public Notification getNotification(String notification) {
        if(notification == "SMS")
            return new SMSNotification();
        if(notification == "EMAIL")
            return new EmailNotification();
        return null;
    }
}


class FactoryCreator{
    AbstractFactory getFactory(String factory){
        if(factory == "NOTIFICATION"){
            return new NotificationFactory();
        }
        if(factory == "ORDER"){
            return new ORderFactory();
        }
        return null;
    }
}

public class AbstractFactoryExampleDemo {
    public static void main(String[] args) {

    }
}
