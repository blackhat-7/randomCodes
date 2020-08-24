import java.util.*;

public class StackSort {

    Stack<Integer> sortStack(Stack<Integer> mystack) {
        Stack<Integer> res = new Stack<>();
        Stack<Integer> buffer = new Stack<>();

        int currmax = Integer.MIN_VALUE;
        int futuremax = currmax;
        boolean empty = false;
        while (!empty) {
            empty = true;
            while (!mystack.isEmpty()) {
                int temp = mystack.pop();
                if (temp == currmax) {
                    res.push(temp);
                } else {
                    buffer.push(temp);
                    futuremax = Math.max(futuremax, temp);
                }
                if (empty) empty = !empty;
            }
            currmax = futuremax;
            futuremax = Integer.MIN_VALUE;
            while (!buffer.isEmpty()) {
                int temp = buffer.pop();
                if (temp == currmax) {
                    res.push(temp);
                } else {
                    futuremax = Math.max(futuremax, temp);
                    mystack.push(temp);
                }
                if (empty) empty = !empty;
            }
            currmax = futuremax;
            futuremax = Integer.MIN_VALUE;
        }

        return res;
    }
    
    public static void main(String[] args) {
        StackSort obj = new StackSort();
        Stack<Integer> mystack = new Stack<>();
        mystack.push(2);
        mystack.push(1);
        mystack.push(4);
        mystack.push(3);
        mystack.push(4);
        mystack.push(5);

        mystack = obj.sortStack(mystack);
        System.out.println(mystack.toString());

    }
}