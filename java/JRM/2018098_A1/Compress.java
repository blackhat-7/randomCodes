import java.util.*;

class Compress {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String c = Character.toString(s.charAt(0));
        int count = 1;
        for(int i=1; i<s.length(); i++) {
            if (s.charAt(i)==c.charAt(c.length()-1)) {
                count++;
            }
            else {
                c+=(Integer.toString(count));
                if (i<s.length()) {
                    c+=s.charAt(i);
                }
                count = 1;
            }
        }
        c+=count;
        System.out.println(c);
    }
}