public class CDBuilder {
    public CDType buildSonyCD(){
        CDType cd = new CDType();
        cd.addItem(new Sony());
        return cd;
    }

    public CDType buildSamsungCD(){
        CDType cd = new CDType();
        cd.addItem(new Samsung());
        return cd;
    }
}
