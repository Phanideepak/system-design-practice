interface Food{
    String prepareFood();
    double foodPrice();
}

class VegFood implements  Food{

    @Override
    public String prepareFood() {
        return "Veg Food";
    }

    @Override
    public double foodPrice() {
        return 50.0;
    }
}

abstract class FoodDecorator implements Food{
    private Food newFood;
    public FoodDecorator(Food newFood){
        this.newFood = newFood;
    }

    @Override
    public String prepareFood() {
        return newFood.prepareFood();
    }

    @Override
    public double foodPrice() {
        return newFood.foodPrice();
    }
}

class NonVegFood extends FoodDecorator{

    public NonVegFood(Food newFood) {
        super(newFood);
    }

    public String prepareFood(){
        return super.prepareFood()+ "With roasted chicken and curry";
    }

    public double foodPrice(){
        return super.foodPrice()+150;
    }
}

class ChineseFood extends FoodDecorator{
    public ChineseFood(Food newFood) {
        super(newFood);
    }

    public String prepareFood(){
        return super.prepareFood()+ "With fried rice and manchurian";
    }

    public double foodPrice(){
        return super.foodPrice()+65;
    }
}

public class DecoratorDesignDemo{
    public static void main(String[] args) {

    }
}