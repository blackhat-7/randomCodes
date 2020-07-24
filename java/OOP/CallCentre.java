import java.util.*;

public class CallCentre {
    private static CallCentre instance = null;
    private int numRanks = 3;
    HashMap<Integer, ArrayList<Employee>> employees;

    public CallCentre() {
        employees = new HashMap<>();
        for (int i=1; i<=numRanks; ++i) {
            employees.put(i, new ArrayList<Employee>());
        }
    }

    public static CallCentre getInstance() {
        if (instance == null) {
            instance = new CallCentre();
        }
        return instance;
    }

    public Employee dispatchCall(Client c) {
        for (int rank=numRanks; rank>0; --rank) {
            List<Employee> curr = employees.get(rank);
            for (Employee e : curr) {
                if (!e.isBusy) {
                    return e.handleCall(c);
                }
            }
        }
        System.out.println("All employees are busy.");
        return null;
    }

    public void hire(Employee[] employeeList) {
        for (Employee e : employeeList) {
            employees.get(e.rank).add(e);
        }
    }

    public static void main(String[] args) {

        CallCentre callCentre = CallCentre.getInstance();

        Director director1 = new Director(1);
        Manager manager1 = new Manager(2, director1);
        Manager manager2 = new Manager(3, director1);
        Respondent respondent1 = new Respondent(4, manager1);
        Respondent respondent2 = new Respondent(5, manager1);
        Respondent respondent3 = new Respondent(6, manager2);
        Respondent respondent4 = new Respondent(7, manager2);

        Client client1 = new Client("David");
        Client client2 = new Client("Sachin");
        Client client3 = new Client("Alex");

        Employee[] hired = {director1, manager1, manager2, respondent1, respondent2, respondent3, respondent4};
        callCentre.hire(hired);

        client1.call(callCentre);
        client2.call(callCentre);
        client3.call(callCentre);
        client1.call(callCentre);
        client2.call(callCentre);
    }
}

abstract class Employee {
    int ID;
    int rank;
    boolean isBusy;
    public Employee(int id) {
        this.ID = id;
        isBusy = false;
    }
    public abstract Employee handleCall(Client c);
}

class Respondent extends Employee {
    Manager boss;
    public Respondent(int id, Manager boss) {
        super(id);
        rank = 3;
        this.boss = boss;
    }
    public Respondent handleCall(Client c) {
        System.out.println("Hello "+c.name+", Respondent "+ID+" answered the call.");
        isBusy = true;
        return this;
    }
}

class Manager extends Employee {
    Director boss;
    public Manager(int id, Director boss) {
        super(id);
        rank = 2;
        this.boss = boss;
    }
    public Manager handleCall(Client c) {
        System.out.println("Hello "+c.name+", Manager "+ID+" answered the call.");
        isBusy = true;
        return this;
    }
}

class Director extends Employee {
    public Director(int id) {
        super(id);
        rank = 1;
    }
    public Director handleCall(Client c) {
        System.out.println("Hello "+c.name+", Director "+ID+" answered the call.");
        isBusy = true;
        return this;
    }
}

class Client {
    String name;
    Employee currentlyTalking;
    public Client(String name) {
        this.name = name;
    }

    public void call(CallCentre c) {
        if (currentlyTalking == null)
            currentlyTalking = c.dispatchCall(this);
        else
            System.out.println("Already talking to "+currentlyTalking.ID);
    }
    public void keepCall() {
        if (currentlyTalking != null) {
            currentlyTalking.isBusy = false;
            currentlyTalking = null;
        } else {
            System.out.println("Not talking to anybody.");
        }
    }
}