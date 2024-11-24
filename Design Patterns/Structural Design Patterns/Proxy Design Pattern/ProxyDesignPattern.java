interface OfficeInternetAccess{
    void grantInternetAccess();
}

class RealInternetAccess implements OfficeInternetAccess{
    private String employeeName;
    public RealInternetAccess(String employeeName) {
        this.employeeName = employeeName;
    }
    @Override
    public void grantInternetAccess() {
        System.out.println("Internet access granted for "+ employeeName);
    }
}

class ProxyInternetAccess implements OfficeInternetAccess{
    private String employeeName;
    private RealInternetAccess realInternetAccess;

    public ProxyInternetAccess(String employeeName){
        this.employeeName = employeeName;
    }
    @Override
    public void grantInternetAccess() {
        if (getRole(employeeName) > 4)
        {
            realInternetAccess = new RealInternetAccess(employeeName);
            realInternetAccess.grantInternetAccess();
        }
        else
        {
            System.out.println("No Internet access granted. Your job level is below 5");
        }
    }

    public int getRole(String employeeName){
        return 9;
    }
}

public class ProxyDesignPattern {
    public static void main(String[] args) {
        OfficeInternetAccess access = new ProxyInternetAccess("Imu Laevo");
        access.grantInternetAccess();
    }
}
