import java.util.*;
import java.util.stream.Collectors;

public class LearnStream {
    
    private static enum Gender {
        MALE, FEMALE
    }

    private static class Person {
        private int id, age;
        private Gender gender;
        private Person(int id, Gender g) {
            this.id = id;
            this.gender = g;
            this.age = new Random().nextInt(40)+10;
        }
        @Override
        public String toString() {
            return "[" + id + ", " + age + ", " + gender + "]";
        }
        public int getId() { return id; }
        public int getAge() { return age; }
        public Gender getGender() { return gender; }
    }

    public static void main(String[] args) {
        List<Person> people = new ArrayList<>();
        for (int i=0; i<10; ++i) {
            people.add(new Person(i, ((i&1)==1) ? Gender.MALE : Gender.FEMALE));
        }
        List<Person> female = people.stream().filter(p -> p.gender == Gender.FEMALE).collect(Collectors.toList());
        female = female.stream().sorted(Comparator.comparing(Person::getId).reversed()).collect(Collectors.toList());
        female.forEach(System.out::println);
        boolean allAbove5 = people.stream().allMatch(p -> p.getId() > 5);
        System.out.println(allAbove5);
        Map<Gender, List<Person>> groupByGender = people.stream().collect(Collectors.groupingBy(Person::getGender));
        groupByGender.forEach((gender, listPeople) -> { System.out.println(gender); listPeople.forEach(System.out::println); });
        people.stream().filter(p -> p.getGender().equals(Gender.FEMALE)).max(Comparator.comparing(Person::getId)).map(Person::getId).ifPresent(System.out::println);


        Queue<Person> pq = new PriorityQueue<>(Comparator.comparing(Person::getAge).thenComparing(Person::getId));
        people.forEach(pq::add);
        for (int i=0; i<5; ++i) {
            System.out.println(pq.poll());
        }
        pq.clear();
        List<List<Integer>> lst = new ArrayList<>();
        lst.add(new ArrayList<>(Arrays.asList(234,2)));
        lst.add(new ArrayList<>(Arrays.asList(23,232)));
        lst.add(new ArrayList<>(Arrays.asList(4,12)));
        lst.add(new ArrayList<>(Arrays.asList(23,22)));
        Queue<List<Integer>> q = new PriorityQueue<>((a, b) -> {
            if (a.get(0) == b.get(0)) return b.get(1) - a.get(1);
            return a.get(0)-b.get0;
        });
        lst.forEach(q::add);
        for (int i=0; i<4; ++i) {
            System.out.println(q.poll());
        }
        
    }
}
