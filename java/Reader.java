import java.util.*;
import java.io.*;

public class Reader {
    public static void main(String[] args) throws IOException {
        Scanner sc = null;
        PrintWriter out = null;
        try {
            sc = new Scanner(new BufferedReader(new FileReader("input.txt")));
            out = new PrintWriter(new FileWriter("output.txt"));
            while(sc.hasNext()) {
                out.println(sc.next());
            }
        }
        finally {
            if (sc!=null) sc.close();
            if (out!=null) out.close();
        }
    }
}