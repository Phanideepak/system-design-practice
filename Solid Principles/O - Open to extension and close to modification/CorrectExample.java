import java.util.*;
import java.io.*;

class Marker{
    private String name;
    private String color;
    private Integer price;
    private Integer year;

    public int getPrice(){
        return price;
    }
}

class Invoice{
    Integer quantity;
    Marker marker;

    Invoice(Integer quantity, Marker marker){
        this.quantity = quantity;
        this.marker = marker;
    }

    int calculateTotal(){
        return marker.getPrice() * quantity;
    }
}

// Create an interface to InvoiceDao

interface InvoiceDao{
    void save(Invoice invoice);
}

class DatabaseInvoiceDao implements InvoiceDao{

    @Override
    public void save(Invoice invoice) {
        // Add DB Related Operations
    }
    
}

class FileInvoiceDao implements InvoiceDao{

    @Override
    public void save(Invoice invoice) {
        // Add File Saving operations.
    }
    
}

public class CorrectExample{
    public static void main(String[] args) {
        
    }
}