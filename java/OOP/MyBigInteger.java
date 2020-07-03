import java.util.*;

public class MyBigInteger {
    private LinkedList<Integer> num;

    public MyBigInteger(int n) {
        num = numToArray(n);
    }

    public static void main(String[] args) {
        MyBigInteger bi = new MyBigInteger(52343);
        bi.print();
    }

    public LinkedList<Integer> numToString(int n) {
        LinkedList<Integer> s = new LinkedList<>();
        while(n != 0) {
            int digit = n%10;
            s.addLast(digit);
            n = n/10;
        }
        return s;
    }

    public MyBigInteger add(MyBigInteger other) {
        Iterator itr1 = num.iterator();
        Iterator itr2 = other.num.iterator();
        int carry = 0;
        while (itr1.hasNext() && itr2.hasNext()) {
            
        }
    }

    public void print() {
        System.out.println(Arrays.toString(num.toArray()));
    }

}