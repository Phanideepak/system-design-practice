interface DrawAPI{
    void drawCircle(int radius, int x, int y);
}

class RedCircle implements DrawAPI{
    @Override
    public void drawCircle(int radius, int x, int y) {
        System.out.println("red circle "+ radius + " x: "+ x + " y :" +y);
    }
}

class GreenCircle implements DrawAPI{
    @Override
    public void drawCircle(int radius, int x, int y) {
        System.out.println("green circle "+ radius + " x: "+ x + " y :" +y);
    }
}

abstract class Shape{
    protected DrawAPI drawAPI;
    protected Shape(DrawAPI drawAPI){
        this.drawAPI = drawAPI;
    }
    abstract void draw();
}

class Circle extends Shape{

    private int x,y, radius;

    public Circle(int x, int y, int radius, DrawAPI drawAPI){
        super(drawAPI);
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    @Override
    void draw() {
        drawAPI.drawCircle(radius, x, y);
    }
}

public class BridgeDesignPatternDemo {
    public static void main(String[] args) {
        Shape redCircle = new Circle(100,100,100, new RedCircle());
        Shape greenCircle = new Circle(100,100,10, new GreenCircle());

        redCircle.draw();
        greenCircle.draw();
    }
}
