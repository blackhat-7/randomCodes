// import java.util.*;

public class ReverseBits {
    public static void printBin(int n) {
        String b = String.format("%32s", Integer.toBinaryString(n)).replace(' ', '0');
        System.out.println(b);
    }

    public static void main(String[] args) {
        int wordSize = 32;
        int num = 0xAAAAAAAA;
        int revNum = 0;
        printBin(num);
        for (int i=0; i<wordSize; ++i) {
            revNum &= ~(1 << (wordSize-i-1));
            revNum |= (num&1) << (wordSize-i-1);
            num >>>= 1;
        }
        printBin(revNum);
        // LinkedList<Integer> n = new LinkedList<>();
        // int[] arr = n.stream().mapToInt(i -> i).toArray();
    }
}
