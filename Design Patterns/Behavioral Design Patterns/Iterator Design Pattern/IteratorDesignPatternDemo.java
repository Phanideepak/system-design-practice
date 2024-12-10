interface Iterator{
    boolean hasNext();
    Object next();
}

interface Container{
    Iterator getIterator();
}
class CollectionOfNames implements Container{
    private String names[] = {"Alex","Badcow"};
    @Override
    public Iterator getIterator() {
        return new CollectionOfNamesIterator();
    }
    private class CollectionOfNamesIterator implements Iterator{
        int i;
        @Override
        public boolean hasNext() {
            return i < names.length;
        }
        @Override
        public Object next() {
            return this.hasNext() ? names[i++] : null;
        }
    }
}

public class IteratorDesignPatternDemo {
    public static void main(String[] args) {
        CollectionOfNames ans = new CollectionOfNames();

        Iterator iterator = ans.getIterator();
        while(iterator.hasNext()){
            System.out.println((String) iterator.next());
        }
    }
}
