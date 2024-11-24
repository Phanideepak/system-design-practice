import java.util.ArrayList;
import java.util.List;

public class CDType{
   private List<ItemPacking> items = new ArrayList<ItemPacking>();

   public void addItem(ItemPacking pack){
        items.add(pack);
   }

   public void getCost(){
       for(ItemPacking pack : items){
           System.out.println(pack.pack());
       }
   }

   public void showItems(){
       for(ItemPacking pack : items){
           System.out.println(pack.pack());
           System.out.println(pack.price());
       }
   }
}
