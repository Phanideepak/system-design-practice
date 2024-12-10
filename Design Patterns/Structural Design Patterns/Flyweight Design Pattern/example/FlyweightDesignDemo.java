package example;

import java.util.HashMap;

interface FigureShape{
    void draw();
}

class Circle implements FigureShape{
    public Circle(String color){
        this.color = color;
    }
    private String color;
    private int x,y,radius;
    public void setX(int x) { this.x = x; }
    public void setY(int y) { this.y = y;}
    public void setRadius(int radius) { this.radius = radius; }
    @Override
    public void draw() {
        System.out.println("Circle: Draw() [Color : " + color + ", x : " + x + ", y :"
                + y + ", radius :" + radius);
    }
}

class ShapeFactory{
    private static HashMap circleMap = new HashMap();

    public static FigureShape getCircle(String color){
        Circle circle = (Circle) circleMap.get(color);

        if(circle == null){
            circle = new Circle(color);
            circleMap.put(color, circle);
            System.out.println("creating circle of color: "+color);
        }
        return circle;
    }
}

public class FlyweightDesignDemo {
    private static String colors[] = {"Red","Violet","Green","Indigo","Yellow","Orange","Blue","Brown","Sky Blue"};
    public static void main(String[] args) {
        for(int i=0;i<20;i++){
            Circle circle = (Circle) ShapeFactory.getCircle(colors[i]);
            circle.setX(getRandomX());
            circle.setY(getRandomY());
            circle.setRadius(100);
            circle.draw();
        }
    }
    private static String getRandomColor(){
        return colors[(int) (Math.random() * colors.length)];
    }
    private static int getRandomX(){
        return (int) (Math.random()*100);
    }

    private static int getRandomY(){
        return (int) (Math.random()*100);
    }
}
