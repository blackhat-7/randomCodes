public class Animal {
    // public void greeting() {
    //     System.out.println("gay");
    // }
    public static void main(String[] args) {
        Animal d = new Dog();
        d.greeting();
        ((Animal)d).greeting();
        ((Dog)d).greeting();
    }
}

interface An1mal {
    public void greeting();
}

class Dog extends Animal implements An1mal {
   @Override
   public void greeting() {
      System.out.println("Woof!");
   }
}

class BigDog extends Dog {
   @Override
   public void greeting() {
      System.out.println("Woow!");
   }
   
}
