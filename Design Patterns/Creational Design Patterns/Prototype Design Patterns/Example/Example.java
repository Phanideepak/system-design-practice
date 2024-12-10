package Example;
interface Prototype{
    Prototype getClone();
}

class EmployeeRecord implements Prototype{
    private Integer id;
    private String name;
    private String designation;
    private Double salary;
    private String address;

    EmployeeRecord(){

    }

    EmployeeRecord(int id, String name, String designation, Double salary, String address){
        this.id = id;
        this.name = name;
        this.designation = designation;
        this.salary = salary;
        this.address = address;
    }

    public void showRecord(){
        System.out.println(id + " ," + name + " , " + salary + " , " + designation + " , " + address);
    }

    @Override
    public Prototype getClone() {
         return new EmployeeRecord(id, name, designation, salary, address);
    }
}

public class Example {
    public static void main(String[] args) {
        EmployeeRecord emp = new EmployeeRecord(1,"James","SDE",1000000.0, "Sky Lanes");
        emp.showRecord();

        EmployeeRecord cloned = (EmployeeRecord) emp.getClone();

        cloned.showRecord();
    }    
}
