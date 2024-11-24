interface WaiterOperations{
    void serveCustomer();
    void collectBill();
}

interface ChefOperations{
    void collectKitchenTicket();
    void cookFood();
}

interface CashierOperations{
    void billOrder();
    void returnChange();
}

class Waiter implements WaiterOperations{

    @Override
    public void serveCustomer() {
       // serve customer
    }

    @Override
    public void collectBill() {
        // collect Bill
    }
}

class Chef implements ChefOperations{
    @Override
    public void collectKitchenTicket() {
        // Collection KOT
    }

    @Override
    public void cookFood() {
        // cook Food
    }
}



public class CorrectExample {
   public static void main(String[] args) {
    
   }    
}
