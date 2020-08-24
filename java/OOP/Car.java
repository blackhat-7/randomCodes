package OOP;

import java.util.*;



interface Transporter {
    public void drive();
}

class Car implements Cloneable {
    public int numEngines;
    public Car(final int n) {
        numEngines = n;
        System.out.println("Car initialized");
    }
    public void drive() {
        System.out.println("Driving Car");
    }
    public Car clone() {
        try {
            final Car copy = (Car) super.clone();
            return copy;
        } catch (final CloneNotSupportedException e) {
            return null;
        }
    }
    
    public static void main(final String[] args) {
        final MyGenericList<Pair<Integer, String>> mgl = new MyGenericList<Pair<Integer, String>>();
        mgl.add(new Pair<Integer, String>(1, "One"));
        mgl.add(new Pair<Integer, String>(2, "Two"));
        mgl.add(new Pair<Integer, String>(3, "Three"));
        System.out.println(mgl.get(2).getValue());
        mgl.print();
    }

    
}

class Sedan extends Car implements Transporter {
    ArrayList<Integer> a = new ArrayList<>();
    public int numSeats;
    public Sedan(final int n, final int m) {
        super(n);
        numSeats = m;
        a.add(1);
        System.out.println("Sedan initialized");
    }
    @Override
    public void drive() {
        System.out.println("Driving sedan");
    }
    public Sedan clone() {
        final Sedan copy = (Sedan) super.clone();
        return copy;
    }
}

class MyGenericList <T> {
    ArrayList<T> genericList;

    public MyGenericList() {
        this.genericList = new ArrayList<T>();
    }
    public void add(final T o) {
        this.genericList.add(o);
    }
    public T get(final int i) {
        return this.genericList.get(i);
    }
    public void print() {
        Iterator itr = genericList.iterator();
        while(itr.hasNext()) {
            System.out.println(itr.next().toString());
        }
    }
}

class Pair <T1, T2> {
    private final T1 key;
    private final T2 val;
    public Pair(final T1 key, final T2 val) {
        this.key = key;
        this.val = val;
    }
    public T1 getKey() { return key; }
    public T2 getValue() { return val; }
    @Override
    public String toString() {
        return key.toString() + ": " + val.toString();
    }
}