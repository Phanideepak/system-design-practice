// Target Interface
interface CreditCard{
    void giveBankDetails();
    String getCreditCard();
}

// This is the adapter class.
class BankDetails{
    private String bankName;
    private String accHolderName;
    private Long accNumber;

    public void setBankName(String bankName){
        this.bankName = bankName;
    }

    public String getBankName(){
        return bankName;
    }

    public void setAccHolderName(String accHolderName){
          this.accHolderName = accHolderName;
    }

    public String getAccHolderName(){
        return accHolderName;
    }

    public void setAccNumber(Long accNumber){
        this.accNumber = accNumber;
    }

    public Long getAccNumber(){
        return accNumber;
    }
}


class BankCustomer extends BankDetails implements CreditCard{

    @Override
    public void giveBankDetails() {
        setAccHolderName("Prudhvi Raj");
        setAccNumber(3243253572572395723l);
        setBankName("SBI");
    }

    @Override
    public String getCreditCard() {
        Long accNo = getAccNumber();
        String accHolderName = getAccHolderName();
        String bankName = getBankName();
        return "accNo: " + accNo + " bankName: " + bankName + " of " + accHolderName ;
    } 
}



public class AdapterPatternDemo{
    public static void main(String[] args) {
        CreditCard targetInterface = new BankCustomer();
        targetInterface.giveBankDetails();
        System.out.println(targetInterface.getCreditCard());
    }
}