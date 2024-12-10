import java.util.ArrayList;
import java.util.List;

interface Packing{
    String pack();
}

interface Item {
    String name();
    Packing pack();
    float price();
}

class Wrapper implements Packing{
    @Override
    public String pack() {
        return "Packing Food";
    }
}

class Bottle implements Packing{
    @Override
    public String pack() {
        return "Packing Bottle";
    }
}

abstract class Burger implements Item{
    @Override
    public Packing pack() {
        return new Wrapper();
    }

    public abstract float price();
}

abstract class ColdDrink implements Item{
    @Override
    public Packing pack() {
        return new Bottle();
    }
    public abstract float price();
}

class VegBurger extends Burger{
    @Override
    public String name() {
        return "Veg Burger";
    }
    @Override
    public float price() {
        return 125.0f;
    }
}

class NonVegBurger extends  Burger{
    @Override
    public String name() {
        return "Non Veg Burger";
    }

    @Override
    public float price() {
        return 250.0f;
    }
}

class Coke extends ColdDrink{
    @Override
    public String name() {
        return "Coke";
    }

    @Override
    public float price() {
        return 30.0f;
    }
}

class Pepsi extends ColdDrink{
    @Override
    public String name() {
        return "Pepsi";
    }

    @Override
    public float price() {
        return 40.0f;
    }
}

class Meal{
    private List<Item> items = new ArrayList();
    public void addItem(Item item){
        items.add(item);
    }
    public float getPrice(){
        return (float) items.stream().mapToDouble(item-> item.price()).sum();
    }
    public void showItems(){
        for (Item item : items) {
            System.out.print("Item : " + item.name());
            System.out.print(", Packing : " + item.pack().pack());
            System.out.println(", Price : " + item.price());
        }
    }
}

class MealBuilder{
    Meal prepareVegMeal(){
        Meal meal = new Meal();
        meal.addItem(new VegBurger());
        meal.addItem(new Coke());

        return meal;
    }

    Meal prepareNonVegMeal(){
        Meal meal = new Meal();
        meal.addItem(new NonVegBurger());
        meal.addItem(new Pepsi());

        return meal;
    }
}

public class SecondExampleDemo {
    public static void main(String[] args) {
        MealBuilder mealBuilder = new MealBuilder();
        Meal vegMeal = mealBuilder.prepareVegMeal();
        vegMeal.showItems();

        Meal nonVegMeal = mealBuilder.prepareNonVegMeal();
        nonVegMeal.showItems();
    }
}
