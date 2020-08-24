public class SuperClass {
    public void aboutMe() {
        System.out.println("I am the superclass");
    }

    public static void main(String[] args) {
        SuperClass cl = new Subclass1();
        cl.aboutMe();
        // cl.onlyAboutMe();
    }
}

class Subclass1 extends SuperClass {
    @Override
    public void aboutMe() {
        System.out.println("I am a subclass of Superclass");
    }
    public void onlyAboutMe() {
        System.out.println("I am Subclass1");
    }
}