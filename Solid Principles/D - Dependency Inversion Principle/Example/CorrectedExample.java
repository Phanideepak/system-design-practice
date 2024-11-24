package Example

interface Keyboard{

}

interface Mouse{

}

class WiredKeyboard implements Keyboard{

}

class WiredMouse implements Mouse{

}

class BluetoothKeyboard implements Keyboard{

}

class BluetoothMouse implements Mouse{

}

class Macbook{
    private final Keyboard keyboard;
    private final Mouse mouse;

    public Macbook(Keyboard keyboard, Mouse mouse){
        this.keyboard = keyboard;
        this.mouse = mouse;
    }
}


public class CorrectedExample {
    public static void main(String[] args) {
        
    }
}
