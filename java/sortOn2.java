import java.util.*;

public class sortOn2 {
    public static void main(String[] args) {
        List<Map.Entry<Integer, Integer>> arr = new ArrayList<>();
        
        for(int i=0; i<5; ++i) {
            arr.add(new AbstractMap.SimpleEntry<Integer, Integer>(i, -i));
        }
        System.out.println(arr);
        arr.sort((Map.Entry<Integer, Integer> a, Map.Entry<Integer, Integer> b) -> (a.getValue() == b.getValue()) ? a.getValue() - b.getValue() : a.getKey() - b.getKey());
        System.out.println(arr);
    }
}

/* 
dict -> hashmap
set -> hashset
list -> arraylist


*/