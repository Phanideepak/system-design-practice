interface OrderChangeService{
    void create();
    void markDelivered();
}

class CustomOrderService implements OrderChangeService{
    @Override
    public void create() {
        System.out.println("Customer Order Created");
    }

    @Override
    public void markDelivered() {
        System.out.println("Customer order marked delivered");
    }
}

class MerchantOrderService implements OrderChangeService{

    @Override
    public void create() {
        System.out.println("Merchant Order Created");
    }

    @Override
    public void markDelivered() {
        System.out.println("Merchant order marked delivered");
    }
}

class OrderFactory{
    OrderChangeService getService(String key){
        if(key == "MERCHANT"){
            return new MerchantOrderService();
        }
        if(key == "CUSTOMER"){
            return new CustomOrderService();
        }

        throw new RuntimeException("Key not found");
    }
}

public class OrderMarkDeliverDemo {
    public static void main(String[] args) {
        OrderFactory factory = new OrderFactory();
        OrderChangeService service = factory.getService("MERCHANT");
        service.create();
        service.markDelivered();
    }
}
