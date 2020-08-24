import java.util.*;

public class MyStreams {

    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>(Arrays.asList(1,2,3,4,5));
        nums.stream().map(x -> x*x).forEach(System.out::println);
    }
    
}