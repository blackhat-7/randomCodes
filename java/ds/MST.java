import java.util.*;
import java.util.AbstractMap.SimpleEntry;

public class MST {
    private int vertices;
    private HashMap<Integer, LinkedList<SimpleEntry<Integer, Integer>>> adjList;
    
    public MST(int V) {
        this.vertices = V;
        this.adjList = new HashMap<Integer, LinkedList<SimpleEntry<Integer, Integer>>>();
        for (int i=0; i<V; ++i) {
            this.adjList.put(i, new LinkedList<SimpleEntry<Integer, Integer>>());
        }
    }

    public void add(int s, int e, int w) {
        LinkedList<SimpleEntry<Integer, Integer>> ll = adjList.get(s);
        ll.add(new SimpleEntry<Integer, Integer>(e, w));
    }

    public void print() {
        for (Map.Entry<Integer, LinkedList<SimpleEntry<Integer, Integer>>> m : adjList.entrySet()) {
            System.out.print(m.getKey() + ": ");
            for (SimpleEntry<Integer, Integer> i : m.getValue()) {
                System.out.print("(" + i.getKey() + "," + i.getValue() + ")" + " ");
            }
            System.out.println();
        }
    }

    private int minKey(int key[], boolean inMST[]) {
        int min = Integer.MAX_VALUE;
        int index = -1;
        for (int i=0; i<this.vertices; ++i) {
            if (!inMST[i] && key[i] < min) {
                index = i;
                min = key[i];
            }
        }
        return index;
    }

    public void prims() {
        int parent[] = new int[this.vertices];
        boolean inMST[] = new boolean[this.vertices];
        int key[] = new int[this.vertices];

        for (int i=0; i<this.vertices; ++i) {
            inMST[i] = false;
            key[i] = Integer.MAX_VALUE;
        }

        parent[0] = -1;
        key[0] = 0;

        for (int i=0; i < this.vertices-1; ++i) {
            int k = minKey(key, inMST);
            inMST[k] = true;

            for (SimpleEntry<Integer, Integer> s : this.adjList.get(k)) {
                if (!inMST[s.getKey()] && s.getValue() < key[s.getKey()]) {
                    key[s.getKey()] = s.getValue();
                    parent[s.getKey()] = k;
                }
            }
        }

        printMST(parent);
    }

    public void printMST(int parent[]) {
        System.out.println("Edge");
        for (int i=1; i<this.vertices; ++i) {
            System.out.println(parent[i] + " - " + i);
        }
    }


    public static void main(String[] args) {
        MST mst = new MST(5);
        mst.add(0, 1, 3);
        mst.add(0, 2, 3);
        mst.add(1, 2, 1);
        mst.add(2, 3, 2);
        mst.add(3, 1, 5);
        mst.add(4, 2, 1);
        mst.print();
        mst.prims();
    }
}