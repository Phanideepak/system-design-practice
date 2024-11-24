interface Bank{
    String getBankName();
}

class SBI implements Bank{
    private String bankName;

    SBI(){
        bankName = "SBI Bank";
    }

    @Override
    public String getBankName() {
        return bankName;
    }
}

class HDFC implements Bank{
    private String bankName;

    HDFC(){
        bankName = "HDFC Bank";
    }

    @Override
    public String getBankName() {
        return bankName;
    }
}

class ICICI implements Bank{
    private String bankName;

    ICICI(){
        bankName = "ICICI Bank";
    }

    @Override
    public String getBankName() {
        return bankName;
    }
}


abstract class Loan{
    protected double rate;
    abstract void getInterestRate(double rate);

    public void calculateLoanPayment(double loanamount, int years){
        double EMI;  

        int n;  
 
        n=years*12;  
        rate=rate/1200;  
        EMI=((rate*Math.pow((1+rate),n))/((Math.pow((1+rate),n))-1))*loanamount;  
 
        System.out.println("your monthly EMI is "+ EMI +" for the amount"+loanamount+" you have borrowed");    
    }
}

class HomeLoan extends Loan{
    @Override
    void getInterestRate(double rate) {
         super.rate = rate;
    }
}

class BusinessLoan extends Loan{
    @Override
    void getInterestRate(double rate) {
         super.rate = rate;
    }
}

class EducationLoan extends Loan{
    @Override
    void getInterestRate(double rate) {
         super.rate = rate;
    }
}


abstract class AbstractFactory{
    abstract Bank getBank(String bank);
    abstract Loan getLoan(String loan);
}

class BankFactory extends AbstractFactory{

    @Override
    Bank getBank(String bank) {
        if(bank == "SBI"){
            return new SBI();
        }
        if(bank == "ICICI"){
            return new ICICI();
        }
        if(bank == "HDFC"){
            return new HDFC();
        }
        return null;
    }

    @Override
    Loan getLoan(String loan) {
        return null;
    }
}


class LoanFactory extends AbstractFactory{
    @Override
    Bank getBank(String bank) {
        return null;
    }

    @Override
    Loan getLoan(String loan) {
        if(loan == "HomeLoan"){
            return new HomeLoan();
        }
        if(loan == "BusinessLoan"){
            return new BusinessLoan();
        }

        if(loan == "EducationLoan"){
            return new EducationLoan();
        }

        return null;
    }
}

class FactoryCreator{
    public static AbstractFactory getFactory(String choice){
        if(choice.equalsIgnoreCase("Bank")){  
            return new BankFactory();  
         } else if(choice.equalsIgnoreCase("Loan")){  
            return new LoanFactory();  
         }  
         return null;
    }
}

public class Example{
    public static void main(String[] args) {
        AbstractFactory factory = FactoryCreator.getFactory("Loan");
        System.out.println(factory.getBank("SBI").getBankName());
        Loan loan = factory.getLoan("HomeLoan");
        loan.getInterestRate(9.4);
        loan.calculateLoanPayment(100000, 10);
    }
}
