interface Pair <K, V> {
    public K getKey();
    public V getValue();
}

public class MyPair <K, V> {
    private K key;
    private V value;

    public MyPair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K getKey() {
        return key;
    }
    public V getValue() {
        return value;
    }

    public static void main(String[] args) {
        MyPair<Integer, String> course = new MyPair<Integer,String>(201, "Advanced Programming");
        MyPair<Integer, String> courseCopy = course;
        System.out.println(course.getKey() + course.getValue());
        if (course == courseCopy) {
            System.out.println("sdfsdfsf");
        }
        // Object array[] = new Integer[10];
    }
}

// class Main {
//     public static void print(ArrayList<?> list){
//         for(Object o: list)
//             System.out.println(o);
//     }
//     public static void r() {
//         ArrayList<Integer> I = new ArrayList<Integer>();
        
//         I.add(1);
//         I.add(2);
//         ArrayList<String> S = new
        
//         ArrayList<String>();
        
//         S.add("Bob");
//         S.add("Paul");
//         print(I);
//         print(S);
//     }
// }

// class HelloWorld extends Application {
//     public static void main(String[] args) {
//         launch(args);
//     }

//     @Override
//     public void start(Stage primaryStage) {
//         primaryStage.setTitle("title");
//         Button b = new Button("Hello");

//         b.setOnAction(new EvenHandler<ActionEvent>() {
//             @Override
//             public void handle(ActionEvent e) {
//                 System.out.println("Hello");
//             }
//         }

//         //b.setOnAction(e -> { System.out.println("Hello");});       lambda expression
        
//         StackPane pane = new StackPane();
//         pain.getChildren().add(b);
//         Scene sc = new Scene(pane, 800, 600);
//         primaryStage.setScene(sc);
//         primaryStage.show();
//     }
// }

// class Point implements Comparable<Point>, Cloneable {

//     private ArrayList<Point> plist = ne ArrayList<>();
//     public Point equals(Object o1) {
//         if(o1 != null && getClass() == o1.getClass()) {
//             Point o = (Point) o1;
//             return x == o.x && y == o.y;
//         }
//         return false;
//     }

//     @Override
//     public int compareTo(Point o) {
//         if(x*y < o.x*o.y) return 1
//         else if(x*y == o.x*o.y) return 0
//         else return -1;
//     }

//     @Override
//     public Point clone() {
//         try {

//             Point copy = (Point) super.clone();
//             copy.plist = new ArrayList<>(plist);
//             return copy;

//         } catch (CloneNotSupportedException e) {

//             System.out.println(e.getMessage());
//             return null;

//         }
//     }

// }

// public class PointComparator implements Comparator<Point> {
//     @Override
//     public int compare(Point o, Point o1) {
//         if(o1.x*o1.y < o.x*o.y) return 1
//         else if(o1.x*o1.y == o.x*o.y) return 0
//         else return -1
//     }
// }

// class Point3D extends Point {
//     public static Point3D(Object o1) {
//         if(o1 != null && getClass() == o1.getClass()) {
//             Point3D o = (Point3D) o1;
//             return super.equals(o1) && z == o.z;
//         }
//         return false;
//     }
// }


