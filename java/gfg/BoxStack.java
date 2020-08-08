import java.util.*;

public class BoxStack {
    private static class Box {
        int l, w, h;
        Box(int l, int w, int h) {
            this.l = l;
            this.w = w;
            this.h = h;
        }
    }

    public static int maxHeight(List<Box> boxes) {
        int n = boxes.size();
        List<Box> rBoxes = new ArrayList<>(3*n);
        for (Box b : boxes) {
            rBoxes.add(new Box(Math.max(b.l, b.w), Math.min(b.l, b.w), b.h));
            rBoxes.add(new Box(Math.max(b.w, b.h), Math.min(b.w, b.h), b.l));
            rBoxes.add(new Box(Math.max(b.l, b.h), Math.min(b.l, b.h), b.w));
        }

        rBoxes.sort(new Comparator<Box>(){
            public int compare(Box t, Box o) {
                if (t.l == o.l || t.w == o.w) return t.h - o.h;
                if (t.l > o.l && t.w > o.w) return 1;
                return -1;
            }    
        });
        int[] dp = new int[3*n];
        for (int i=0; i<3*n; ++i) {
            Box b1 = rBoxes.get(i);
            for (int j=0; j<i; ++j) {
                Box b2 = rBoxes.get(j);
                if (b1.l > b2.l && b1.w > b2.w) {
                    dp[i] = Math.max(dp[i], dp[j]);
                }
            }
            dp[i] += b1.h;
        }
        return Arrays.stream(dp).max().getAsInt();

    }

    public static void main(String[] args) {
        List<Box> boxes = Arrays .asList(new Box(4, 2, 5),
										new Box(3, 1, 6),
										new Box(3, 2, 1),
										new Box(6, 3, 8));

		System.out.println("The maximum height is " + maxHeight(boxes));
    }
}


















