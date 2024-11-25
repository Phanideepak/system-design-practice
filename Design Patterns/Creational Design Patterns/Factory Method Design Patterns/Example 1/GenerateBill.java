import java.util.Objects;

abstract class Plan {
    protected double rate;
    abstract void getRate();
    
    public void calculateBill(int units){
        System.out.println(units*rate);
    }
}

class DomesticPlan extends Plan{

    @Override
    void getRate() {
        rate = 3.5;
    }
}

class CommercialPlan extends Plan{

    @Override
    void getRate() {
       rate = 5.5;
    }
}

class InstitutionalPlan extends Plan{

    @Override
    void getRate() {
        rate = 7.5;
    }
    
}

class PlanFactory{

    public Plan getPlan(String planType){
        if(Objects.isNull(planType)){
            return null;
        }
        if(planType.equalsIgnoreCase("DOMESTICPLAN")){
            return new DomesticPlan();
        } 
        if(planType.equalsIgnoreCase("COMMERCIALPLAN")){
            return new CommercialPlan();
        }
        if(planType.equalsIgnoreCase("InstitutionalPlan")){
            return new InstitutionalPlan();
        }
        return null;
    }
}


public class GenerateBill{
    public static void main(String[] args) {
        PlanFactory factory = new PlanFactory();
        Plan plan = factory.getPlan("COMMERCIAL");
        
        plan.calculateBill(1000);
    }
}