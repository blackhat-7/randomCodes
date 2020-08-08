import java.util.HashSet;

public class ConsecutiveLargestSubarray {
    
    public static int helper(int[] arr) {
        int maxLen = 0;
        int maxStart = 0;
        for (int i=0; i<arr.length; ++i) {
            int start = arr[i];
            int max = arr[i], currMax = 1;
            HashSet<Integer> set = new HashSet<>();
            set.add(arr[i]);
            for (int j=i+1; j <arr.length; ++j) {
                if (arr[j] > max)
                    max = arr[j];
                if (!set.contains(arr[j]))
                    set.add(arr[j]);
                else 
                    break;
                if (set.size() == max-start+1) 
                    currMax = max-start+1;
            }
            if (currMax > maxLen) {
                maxStart = i;
                maxLen = currMax;
            }
        }
        for (int i=maxStart; i < maxStart+maxLen; ++i) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        return maxLen;
    }

    public static void main(String[] args) {
        int[] arr = {2, 0, 2, 1, 4, 3 ,1, 0};
        System.out.println(helper(arr));
    }
}
