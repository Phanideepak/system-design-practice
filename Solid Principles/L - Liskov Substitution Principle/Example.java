interface Bike{
    void turnOnEngine();
    void accelerate();
}

class MotorCycle implements Bike{
    Boolean isEngine = false;
    Integer speed;

    @Override
    public void turnOnEngine() {
         isEngine = true;
    }

    @Override
    public void accelerate() {
       speed = speed + 20;
    }
}

class Cycle implements Bike{
    Integer speed;

    @Override
    public void turnOnEngine() {
        throw new UnsupportedOperationException("Bike does not have engine");
    }

    @Override
    public void accelerate() {
        speed = speed + 5;
    }
}


public class Example {
    public static void main(String[] args) {
        
    }    
}
