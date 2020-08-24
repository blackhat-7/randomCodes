import java.util.*;
import java.io.*;
import java.lang.*;

class Foobar {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    void solve1() throws IOException {
        String s = br.readLine();
        long num = 0;
        char ch = s.charAt(0);
        Stack<Tuple> stack = new Stack<>();
        for (int i=1; i<s.length(); i++) {
            if (Character.isAlphabetic(s.charAt(i))) {
                if (Character.isLowerCase(ch)) {
                    if (stack.size() != 0 &&  stack.peek().d == ch)
                        stack.peek().e += num;
                    else
                        stack.push(new Tuple(num, ch));
                    ch = s.charAt(i);
                } else {
                    if (stack.size() == 0 || Character.toUpperCase(stack.peek().d) != ch || stack.peek().e < num) {
                        System.out.println("NO");
                        return;
                    }
                    stack.peek().e -= num;
                    if (stack.peek().e == 0) {
                        stack.pop();
                    }
                }
                ch = s.charAt(i);
                num = 0;
            } else {
                num = 10 * num + Integer.parseInt(String.valueOf(s.charAt(i)));
            }
        }
        if (stack.size() == 0 || Character.toUpperCase(stack.peek().d) != ch || stack.peek().e < num) {
            System.out.println("NO");
            return;
        }
        stack.peek().e -= num;
        if (stack.peek().e == 0) {
            stack.pop();
        }
        if (stack.size() > 0) {
            System.out.println("NO");
            return;
        }
        System.out.println("YES");
    }

	public static void main (String[] args) throws IOException {
        Foobar fb = new Foobar();
        long t = Long.parseLong(br.readLine());
        while (t-- > 0) {
            fb.solve1();
        }
	}

    static class Tuple {
        int a, b, c;
        char d;
        long e;
        Tuple(long e, char d) { this.e = e; this.d = d;}
        Tuple(int a, int b) { this.a = a; this.b = b;}
        Tuple(int a, int b, int c) { this.a = a; this.b = b; this.c = c; }
        
    }

    int gcd(int x, int y) {
        while (y != 0) {
            int temp = y;
            y = x%y;
            x = temp;
        }
        return x;
        //return (y == 0) ? x : gcd(y, x%y);
    }
}
