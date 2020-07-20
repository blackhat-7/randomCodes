package prefixSum;
import java.util.*;

public class MaxOccurEleInRange {
    public static void main(String[] args) {
        
        int MAX = 1000000;
        int[] L = {1, 4, 9, 13, 21};
        int[] R = {15, 8, 12, 20, 30}; 
        int n = L.length;

        int[] freq = new int[MAX];
        for (int i = 0; i < n; ++i) {
            ++freq[L[i]];
            --freq[R[i] + 1];
        }
        int maxOccEle = 0, maxFreq = 0;
        int f = 0;
        for (int i = 0; i < MAX; ++i) {
            f += freq[i];
            if (f > maxFreq) {
                maxOccEle = i;
                maxFreq = f;
            }
        }
        System.out.println(maxOccEle);
    }
    
}