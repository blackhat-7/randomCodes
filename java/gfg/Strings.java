import java.util.*;
import java.lang.*;

public class Strings {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("01234567");
        sb.replace(4, 6, "st");
        sb.deleteCharAt(5);
        sb = new StringBuilder(sb.substring(4, 6));
        System.out.println(sb);
        // PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
        // @Override
        // public int compare(Integer o1, Integer o2) {
        // if (o1 == o2)
        // return 0;
        // return (o1 < o2) ? -1 : 1;
        // }
        // });
        PriorityQueue<Integer> pq = new PriorityQueue<>((Integer i1, Integer i2) -> i2 - i1);
        pq.addAll(Arrays.asList(1, 2, 3, 4, 5));
        System.out.println(pq);
    }
}