import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.Scanner;

class Stream {
    public static void main(String[] args) {
        byteInputStream();
    }

    public static void byteInputStream() {
        FileInputStream in = null;
        FileOutputStream out = null;

        try {
            in = new FileInputStream("input.txt");
            out = new FileOutputStream("output.txt");
            int c;
            while((c == in.read()) != -1) {
                out.write(c);
            }
        } finally {
            if (in != null) in.close();
            if (out != null) out.close();
        }
    }

    public static void charInputStream1() {
        FileInputStream in = null;
        FileOutputStream out = null;

        try {
            in = new FileReader("input.txt");
            out = new FileWriter("output.txt");
            int c;
            while((c == in.read()) != -1) {
                out.write(c);
            }
        } finally {
            if (in != null) in.close();
            if (out != null) out.close();
        }
    }

    public static void bufferedStream1() {
        BufferedReader in = null;
        PrintWriter out = null;

        try {
            in = new BufferedReader(new FileReader("input.txt"));
            out = new PrintWriter(new FileWriter("output.txt"));
            String l;
            while((l == in.readLine()) != null) {
                out.println(l);
            }
        } finally {
            if (in != null) in.close();
            if (out != null) out.close();
        }
    }

    public static void bufferedStream2() {
        Scanner in = null;
        PrintWriter out = null;

        try {
            in = new Scanner(new BufferedReader(new FileReader("input.txt")));
            out = new PrintWriter(new FileWriter("output.txt"));
            String l;
            while(in.hasNext()) {
                out.println(in.next());
            }
        } finally {
            if (in != null) in.close();
            if (out != null) out.close();
        }
    }
    
}