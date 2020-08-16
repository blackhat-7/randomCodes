import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;

public class MultiplyLarge {
    
    public static LinkedList<Integer> multiply(LinkedList<Integer> n1, LinkedList<Integer> n2) {
        LinkedList<Integer> ans = new LinkedList<>();
        Collections.reverse(n1); Collections.reverse(n2);
        Iterator<Integer> it = n1.iterator();
        int i = 0;
        while (it.hasNext()) {
            int digit1 = it.next();

            Iterator<Integer> it2 = n2.iterator();
            int j = i;
            int carry = 0, x, d;
            while(it2.hasNext()) {
                if (j < ans.size()) {
                    d = digit1 * it2.next() + carry + ans.get(j);
                    x = d%10;
                    carry = d/10;
                    ans.set(j, x);
                } else {
                    d = digit1 * it2.next() + carry;
                    x = d%10;
                    carry = d/10;
                    ans.add(x);
                }
                j++;
            }
            ans.add(carry);
            i++;
        }
        Collections.reverse(ans);
        return ans;
    }

    public static void main(String[] args) {
        LinkedList<Integer> n1 = new LinkedList<>();
        LinkedList<Integer> n2 = new LinkedList<>();

        n1.addAll(Arrays.asList(6,5,4,1,5,4,1,5,4,1,5,1,4,5,4,5,4,5,4,1,5,4,1,5,4,5,4));
        n2.addAll(Arrays.asList(6,3,5,1,6,5,6,1,5,6,3,1,5,6,3,1,6,5,4,5,1,4,5,1,4,6,5,1,4,6,5,4));

        LinkedList<Integer> ans = multiply(n1, n2);
        System.out.println(ans.toString());
    }
}
