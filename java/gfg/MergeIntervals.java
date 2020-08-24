import java.util.*;

public class MergeIntervals {
    private static class Interval {
        private int x, y;
        private Interval(int x, int y) {
            this.x = x; this.y = y;
        }
        @Override
        public String toString() {
            return "[" + x + ", " + y + "]";
        }
    }    

    public static List<Interval> mergeIntervals(List<Interval> intervals) {
        intervals.sort((a, b) -> a.x - b.x);
        Stack<Interval> stack = new Stack<>();
        stack.add(intervals.get(0));

        for(Interval i : intervals) {
            if (i.x <= stack.peek().y) {
                stack.peek().y = Math.max(i.y, stack.peek().y);
            } else {
                stack.add(i);
            }
        }
        return stack;
    } 

    public static void main(String[] args)
	{
		List<Interval> intervals = Arrays.asList(
				new Interval(1, 5), new Interval(2, 3),
				new Interval(4, 6), new Interval(7, 8),
				new Interval(8, 10), new Interval(12, 15)
		);

		intervals = mergeIntervals(intervals);
        for (Interval i : intervals) {
            System.out.print(i);
        }
	}
}
