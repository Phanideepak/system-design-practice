import java.util.List;

abstract class AbstractCustomer{
    protected String name;

    abstract String getName();
    abstract Boolean isNull();
}

class RealCustomer extends AbstractCustomer{

    public RealCustomer(String name){
        this.name = name;
    }

    @Override
    String getName() {
        return name;
    }

    @Override
    Boolean isNull() {
        return false;
    }
}

class NullCustomer extends AbstractCustomer{

    @Override
    String getName() {
        return "Customer Not Found in the database";
    }

    @Override
    Boolean isNull() {
        return true;
    }
}

class CustomerFactory{
    private static List<String> names = List.of("Abhi", "Deepak", "Dulip");

    static AbstractCustomer getCustomer(String name){

        if(names.stream().anyMatch(subname-> name.equalsIgnoreCase(name))){
            return new RealCustomer(name);
        }

        return new NullCustomer();
    }
}

public class NullObjectDesignPattern {
    public static void main(String[] args) {
        AbstractCustomer customer1 = CustomerFactory.getCustomer("Rob");
        AbstractCustomer customer2 = CustomerFactory.getCustomer("Bob");
        AbstractCustomer customer3 = CustomerFactory.getCustomer("Julie");
        AbstractCustomer customer4 = CustomerFactory.getCustomer("Laura");

        System.out.println("Customers");
        System.out.println(customer1.getName());
        System.out.println(customer2.getName());
        System.out.println(customer3.getName());
        System.out.println(customer4.getName());
    }
}
