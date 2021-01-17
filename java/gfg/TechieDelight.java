import java.util.Map;
import java.util.HashMap;
class TechieDelight {
    public static void main(String[] args) {
        int[] dims = { 10, 30, 5, 60 };
        System.out.print("Minimum cost is " + MatMulMinCost(dims, 0, dims.length - 1, new HashMap<String, Integer>()));
    }

    public static int MatMulMinCost(int[] shapes, int start, int end, Map<String,Integer> lookup) {
        if (end - start <= 1)
            return 0;
        String key = start + " " + end;
        if (!lookup.containsKey(key)) {
            int minCost = Integer.MAX_VALUE;
            for (int i=start+1; i<=end-1; i++) {
                int cost = MatMulMinCost(shapes, start, i, lookup) + 
                    MatMulMinCost(shapes, i, end, lookup) +
                    shapes[start]*shapes[i]*shapes[end];
                if (cost < minCost)
                    minCost = cost;
            }
            lookup.put(key, minCost);
        }
        return lookup.get(key);
    }
}
