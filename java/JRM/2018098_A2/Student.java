class Student {
    String name;
    int age;
    int roll;
    String branch;
    static int latestRoll;

    Student() {
        name = "Steve";
        age = 10;
        roll = ++latestRoll;
        branch = "ECE";
    }

    Student(String n, int a, int r, String b) {
        name = n;
        age = a;
        roll = r;
        branch = b;
        latestRoll = r;
    }

    void display() {
        System.out.println("Name : " + this.name + "\n" + "Age : " + Integer.toString(this.age) + "\n" + "Roll No. : " + Integer.toString(this.roll) + "\n" + "Branch : " + this.branch);
    }

    public static void main(String[] args) {
        Student a = new Student();
        Student b = new Student();
        Student c = new Student();
        Student d = new Student();
        Student e = new Student();
        Student f = new Student("Shaunak", 19, 6, "CSE");
        Student g = new Student("Abinash", 20, 6, "ESE");
        Student h = new Student("Abhinav", 15, 6, "CSAI");
        Student i = new Student("Ankit", 5, 6, "CSAM");
        Student j = new Student("Shashikant", 30, 6, "CSB");
        
        e.display();
    }
}