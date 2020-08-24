package OOP;

public class CookieJar {
    private volatile int cookieNum;
    private volatile boolean available;
    public CookieJar() {
        this.cookieNum = 0;
        this.available = false;
    }
    public static void main(String[] args) {
        CookieJar jar = new CookieJar();
        Marge marge = new Marge(jar);
        Homer homer = new Homer(jar);
        new Thread(marge).start();
        new Thread(homer).start();
    }

    public void putCookie(Marge marge, int cookieNum) {
        synchronized(this) {
            while(available) {
                try {
                    wait();
                } catch (InterruptedException e) { }
            }
            available = true;
            System.out.println(marge + " has put cookie " + cookieNum);
            this.cookieNum = cookieNum;
            notifyAll();
        }
    }
    public void getCookie(Homer homer) {
        synchronized(this) {
            while (!available) {
                try {
                    wait();
                }
                catch (InterruptedException e) { }
            }
            available = false;
            System.out.println(homer + " has eaten cookie " + this.cookieNum);
            notifyAll();
        }
    }
}

class Marge implements Runnable {
    CookieJar jar;
    public Marge(CookieJar jar) {
        this.jar = jar;
    }
    @Override
    public void run() {
        for (int i=0; i<5; ++i) { bake(i); }
    }    
    public void bake(int cookieNum) {
        jar.putCookie(this, cookieNum);
        try	{		
            Thread.sleep((int)Math.random()	*	500);		
        } catch	(InterruptedException ie) {}	
    }
    public String toString() {
        return "Marge";
    }
}

class Homer implements Runnable {
    CookieJar jar;
    public Homer(CookieJar jar) {
        this.jar = jar;
    }
    @Override
    public void run() {
        for (int i=0; i<5; ++i) { eat(); }
    }
    public void eat() {
        jar.getCookie(this);
        try	{		
            Thread.sleep((int)Math.random()	*	500);		
        } catch	(InterruptedException ie) {}	
    }
    public String toString() {
        return "Homer";
    }
}