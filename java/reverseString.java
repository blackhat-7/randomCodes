import java.util.*;
import java.lang.*;
import java.io.*;

public class reverseString {
    public static boolean isPalindromic(String s) {
        int n = s.length();
        for (int i=0; i<n/2; ++i) {
            if (s.charAt(i) != s.charAt(n-i-1)) {
                return false;
            }
        }
        return true;
    }
    
    public static List<String> helper(String s, int start, HashMap<Integer, List<String>> map) {
        
        int key = start;
        if (!map.containsKey(key)) {
            List<String> partitions = new ArrayList<>();
            for (int i=start+1; i<=s.length(); ++i) {
                String sub = s.substring(start, i);
                if (isPalindromic(sub)) {
                    if (i < s.length()) {
                        List<String> end = helper(s, i, map);
                        for (String e : end) {
                            partitions.add(sub + " " + e);
                        }
                    }
                    else {
                        partitions.add(sub);
                    }
                }
            }
            map.put(key, partitions);
        }
        return map.get(key);
    }
    
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
        List<String> res = helper(s, 0, new HashMap<Integer, List<String>>());
        res.forEach(System.out::println);
		
	}
}