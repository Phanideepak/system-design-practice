import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Person{
    private String name;
    private String gender;
    private String maritialStatus;
    public Person(String name, String gender, String maritialStatus) {
        this.name = name;
        this.gender = gender;
        this.maritialStatus = maritialStatus;
    }
    public String getName() {
        return name;
    }
    public String getGender() {
        return gender;
    }
    public String getMaritialStatus() {
        return maritialStatus;
    }
}

interface Criteria{
    List<Person> meetCriteria(List<Person> persons);
}

class CriteriaMale implements Criteria{
    @Override
    public List<Person> meetCriteria(List<Person> persons) {
        return persons.stream().
                filter(person -> person.getGender().equalsIgnoreCase("MALE"))
                .collect(Collectors.toList());
    }
}

class CriteriaFemale implements Criteria{
    @Override
    public List<Person> meetCriteria(List<Person> persons) {
        return persons.stream().
                filter(person -> person.getGender().equalsIgnoreCase("FEMALE"))
                .collect(Collectors.toList());
    }
}

class CriteriaSingle implements Criteria{
    @Override
    public List<Person> meetCriteria(List<Person> persons) {
        return persons.stream().
                filter(person -> person.getMaritialStatus().equalsIgnoreCase("SINGLE"))
                .collect(Collectors.toList());
    }
}

class AndCriteria implements Criteria{
    private Criteria criteria;
    private Criteria otherCriteria;

    public AndCriteria(Criteria criteria, Criteria otherCriteria){
        this.criteria = criteria;
        this.otherCriteria = otherCriteria;
    }

    @Override
    public List<Person> meetCriteria(List<Person> persons) {
        // AND Operations
        return otherCriteria.meetCriteria(criteria.meetCriteria(persons));
    }
}

class OrCriteria implements Criteria{
    private Criteria criteria;
    private Criteria otherCriteria;

    public OrCriteria(Criteria criteria, Criteria otherCriteria){
        this.criteria = criteria;
        this.otherCriteria = otherCriteria;
    }

    @Override
    public List<Person> meetCriteria(List<Person> persons) {
        // OR Operations
        List<Person> first = criteria.meetCriteria(persons);
        List<Person> second = otherCriteria.meetCriteria(persons);

        return Stream.concat(first.stream(), second.stream().filter(p-> !first.contains(p)))
                .collect(Collectors.toList());
    }
}

public class FilterDesignPatternDemo {
    public static void main(String[] args) {
        List<Person> persons = new ArrayList<Person>();
        persons.add(new Person("Abhinav","MALE", "SINGLE"));
        persons.add(new Person("Ammu","FEMALE", "SINGLE"));
        persons.add(new Person("Alekya","FEMALE", "SINGLE"));
        persons.add(new Person("Alekya Chowdary","FEMALE", "SINGLE"));
        persons.add(new Person("Ammulu","FEMALE", "MARRIED"));
        persons.add(new Person("Donic","MALE", "MARRIED"));
        persons.add(new Person("Abhi","MALE", "MARRIED"));
        persons.add(new Person("Binod","MALE", "SINGLE"));

        Criteria isMale = new CriteriaMale();
        Criteria isFemale = new CriteriaFemale();
        Criteria isSingle = new CriteriaSingle();
        Criteria isSingleFemale = new AndCriteria(isSingle, isFemale);
        Criteria isSingleOrMale = new OrCriteria(isSingle, isMale);

        System.out.println("Males: ");
        print(isMale.meetCriteria(persons));


        System.out.println("Females: ");
        print(isFemale.meetCriteria(persons));

        System.out.println("Female Singles: ");
        print(isSingleFemale.meetCriteria(persons));

        System.out.println("Singles or Males");
        print(isSingleOrMale.meetCriteria(persons));
    }

    private static void print(List<Person> persons){
        for(Person p : persons){
            System.out.print(p.getName() + " ");
            System.out.print(p.getGender() + " ");
            System.out.print(p.getMaritialStatus());
            System.out.println();
        }
        System.out.println();
    }
}
