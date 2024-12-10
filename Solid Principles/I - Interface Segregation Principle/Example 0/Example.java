interface RestaurantEmployee{
    void billOrder();
    void cookFood();
    void serveCustomer();
}

class Waiter implements RestaurantEmployee{

    @Override
    public void billOrder() {
        throw new UnsupportedOperationException("Job not supported for waiter");
    }

    @Override
    public void cookFood() {
        throw new UnsupportedOperationException("Job not supported ");
    }

    @Override
    public void serveCustomer() {
       // Serve Customer
    }
}



public class Example {
   public static void main(String[] args) {
    
   }    
}
