package Example;

interface Keyboard{

}

interface Mouse{

}

class WiredKeyboard implements Keyboard{

}

class WiredMouse implements Mouse{

}

class Macbook{
    private final WiredKeyboard keyboard;
    private final WiredMouse mouse;

    public Macbook(){
        keyboard = new WiredKeyboard();
        mouse = new WiredMouse();
    }
}


public class Example {
    public static void main(String[] args) {
        
    }
}
