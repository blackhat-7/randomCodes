import java.util.*;
import java.io.*;

public class IOpractice {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        Manager m = new Manager("Shaunak", 234);
        serialize(m);
        Manager x = deserialize();
        System.out.println(x.getData());
    }

    public static void serialize(Manager m) throws IOException {
        ObjectOutputStream out = null;
        try {
            out = new ObjectOutputStream(new FileOutputStream("random.txt"));
            out.writeObject(m);
        } finally {
            if (out != null) {
                out.close();
            }
        }
    }

    public static Manager deserialize() throws IOException, ClassNotFoundException {
        ObjectInputStream in = null;
        Manager m = null;
        try {
            in = new ObjectInputStream(new FileInputStream("random.txt"));
            m = (Manager) in.readObject();
        } finally {
            if (in != null) {
                in.close();
            }
        }
        return m;
    }

    public static void readWriteTextFile() throws IOException {
        Scanner in = null;
        PrintWriter out = null;
        try {
            in = new Scanner(new BufferedReader(new FileReader("random.txt")));
            out = new PrintWriter(new FileWriter("randomCopy.txt"));

            while (in.hasNext()) {
                out.println(in.next());
            }
        } finally {
            if (in != null) {
                in.close();
            }
            if (out != null) {
                out.close();
            }
        }
    }
}

class Employee implements Serializable {
    private static final long serialVersionUID = 1L;
    protected String name;
    Employee(String name) {
        this.name = name;
    }
}

class Manager extends Employee {
    private static final long serialVersionUID = 2L;
    protected int managerID;
    public Manager(String name, int id) {
        super(name);
        this.managerID = id;
    }
    public String getData() {
        return "Name: " + name + " ID: " + managerID;
    }
}