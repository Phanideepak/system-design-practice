import java.util.List;
import java.util.ArrayList;

interface Employee{
    Integer getId();
    String getName();
    Double getSalary();
    void print();
    void add(Employee emp);
    void  remove(Employee emp);
    Employee getChild(int i);
}

class BankManager implements Employee{

    private int id;
    private String name;
    private Double salary;
    List<Employee> emps = new ArrayList<>();

    public BankManager(int id, String name, Double salary){
        this.id = id;
        this.name = name;
        this.salary = salary;
    }

    @Override
    public Integer getId() {
        return id;
    }

    @Override
    public String getName() {
       return name;
    }

    @Override
    public Double getSalary() {
       return salary;
    }

    @Override
    public void print() {
        for(Employee emp : emps){
            System.out.println(emp);
        }
    }

    @Override
    public void add(Employee emp) {
        emps.add(emp);
    }

    @Override
    public void remove(Employee emp) {
       emps.remove(emp);
    }

    @Override
    public Employee getChild(int i) {
        return emps.get(i);
    }
    
}


class Cashier implements Employee{

    private Integer id;
    private String name;
    private Double salary;

    public Cashier(int i, String string, int j) {
        //TODO Auto-generated constructor stub
    }

    @Override
    public Integer getId() {
       return id;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public Double getSalary() {
        return salary;
    }

    @Override
    public void print() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'print'");
    }

    @Override
    public void add(Employee emp) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Add Operation not supported for Leaf");
    }

    @Override
    public void remove(Employee emp) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Not applicable");
    }

    @Override
    public Employee getChild(int i) {
        return null;
    }
}

public class CompositeDesignPatternDemo{
    public static void main(String[] args) {
        Employee emp1 = new Cashier(101, "Sonam Kumar",20000);
        Employee emp2 = new Cashier(102, "mOHAN KUMAR", 3000);
        Employee manager = new BankManager(103, "Champak Setty", 100000.0);

        manager.add(emp1);
        manager.add(emp2);

        manager.print();
    }
}