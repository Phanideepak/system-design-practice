import java.util.ArrayList;
import java.util.List;

public class CDType{
   private List<Packing> items = new ArrayList<Packing>();

   public void addItem(Packing pack){
        items.add(pack);
   }

   public void getCost(){
       for(Packing pack : items){
           System.out.println(pack.pack());
       }
   }

   public void showItems(){
       for(Packing pack : items){
           System.out.println(pack.pack());
           System.out.println(pack.price());
       }
   }
}
