interface MobileShop{
    void modelNo();
    void price();
}

class Iphone implements MobileShop{

    @Override
    public void modelNo() {
        System.out.println("Iphone 6");
    }

    @Override
    public void price() {
        System.out.println("Price is 65000");
    }
}

class SamsungPhone implements MobileShop {

    @Override
    public void modelNo() {
        System.out.println("Samsung A7");
    }

    @Override
    public void price() {
        System.out.println("Price is 45000");
    }
}

class BlackBerry implements MobileShop {

    @Override
    public void modelNo() {
        System.out.println("BlackBerry");
    }

    @Override
    public void price() {
        System.out.println("Price is 55000");
    }
}

class Shopkeeper{
    private MobileShop iphone;
    private MobileShop samsung;
    private MobileShop blackberry;

    public Shopkeeper(){
        iphone = new Iphone();
        samsung = new SamsungPhone();
        blackberry = new BlackBerry();
    }
    void iphoneSale(){
        iphone.modelNo();
        iphone.price();
    }
    void samsungSale(){
        samsung.modelNo();
        samsung.price();
    }
    void blackberrySale(){
        blackberry.modelNo();
        blackberry.price();
    }
}

public class FacadeDesignPatternDemo {
    public static void main(String[] args) {

    }
}
