import java.util.*;
import java.lang.*;
import java.io.*;

public class RabinCarp {    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String p = br.readLine();

        List<Integer> matchAtIndices = search(s, p);
        System.out.println(matchAtIndices.toString());
    }

    public static List<Integer> search(String string, String pattern) {
        List<Integer> matchAtIndices = new ArrayList<>();
        
        int i, j, M = string.length(), N = pattern.length(), patHash = 0, strHash = 0, numAlpha = 256, msb = 1, mod = 101;
        
        for (i = 0; i < N-1; ++i) {
            msb = (msb * numAlpha) % mod;
        }

        for (i = 0; i < N; ++i) {
            patHash = ((patHash * numAlpha) + pattern.charAt(i)) % mod;
            strHash = ((strHash * numAlpha) + string.charAt(i)) % mod;
        }

        for (i = 0 ; i <= M - N; ++i) {
            if (patHash == strHash) {
                for (j = 0; j < N; ++j) {
                    if (pattern.charAt(j) != string.charAt(j+i)) break;
                }

                if (j == N) matchAtIndices.add(i);
            }

            if (i < M - N) {
                strHash = ((numAlpha * (strHash - string.charAt(i)*msb)) + string.charAt(i+N)) % mod;
                if (strHash < 0) strHash += mod;
            }
        }
        
        return matchAtIndices;
    }

}