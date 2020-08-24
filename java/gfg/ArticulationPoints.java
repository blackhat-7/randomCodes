import java.util.*;

public class ArticulationPoints {
    private int V;   // No. of vertices 
  
    // Array  of lists for Adjacency List Representation 
    private LinkedList<Integer> adj[]; 
  
    // Constructor 
    ArticulationPoints(int v) 
    { 
        V = v; 
        adj = new LinkedList[v]; 
        for (int i=0; i<v; ++i) 
            adj[i] = new LinkedList<>(); 
    } 
  
    //Function to add an edge into the ArticulationPoints 
    void addEdge(int v, int w) 
    { 
        adj[v].add(w);  // Add w to v's list. 
        adj[w].add(v);    //Add v to w's list 
    }

    int time = 0;
    int APutil(boolean[] ap, int[] disc, int[] low, int parent, int u) {
        
        disc[u] = low[u] = ++time;
        int children = 0;

        for (int v : adj[u]) {
            if (disc[v] == -1) {
                children++;
                low[u] = Math.min(low[u], APutil(ap, disc, low, u, v));
                if (parent != -1 && low[v] >= disc[u]) {
                    ap[u] = true;
                }
            } else if (v != parent) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
        if (parent == -1 && children > 1)
            ap[u] = true;
        return low[u];
    }

    void AP() {
        boolean[] ap = new boolean[this.V];
        int[] disc = new int[this.V];
        int[] low = new int[this.V];
        int parent = -1;
        Arrays.fill(disc, -1);
        for (int i=0; i<this.V; i++) {
            if (disc[i] == -1)
                APutil(ap, disc, low, parent, i);
        }
        for (int i=0; i<this.V; i++) {
            if (ap[i]) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }

    // Driver method 
    public static void main(String args[]) 
    { 
        // Create ArticulationPointss given in above diagrams 
        System.out.println("Articulation points in first ArticulationPoints "); 
        ArticulationPoints g1 = new ArticulationPoints(5); 
        g1.addEdge(1, 0); 
        g1.addEdge(0, 2); 
        g1.addEdge(2, 1); 
        g1.addEdge(0, 3); 
        g1.addEdge(3, 4); 
        g1.AP(); 
        System.out.println(); 
  
        System.out.println("Articulation points in Second ArticulationPoints"); 
        ArticulationPoints g2 = new ArticulationPoints(4); 
        g2.addEdge(0, 1); 
        g2.addEdge(1, 2); 
        g2.addEdge(2, 3); 
        g2.AP(); 
        System.out.println(); 
  
        System.out.println("Articulation points in Third ArticulationPoints "); 
        ArticulationPoints g3 = new ArticulationPoints(7); 
        g3.addEdge(0, 1); 
        g3.addEdge(1, 2); 
        g3.addEdge(2, 0); 
        g3.addEdge(1, 3); 
        g3.addEdge(1, 4); 
        g3.addEdge(1, 6); 
        g3.addEdge(3, 5); 
        g3.addEdge(4, 5); 
        g3.AP();

        System.out.println("next");
        ArticulationPoints g4  = new ArticulationPoints(3);
        g4.addEdge(0, 1);
        g4.addEdge(1, 2);
        g4.AP();
        System.out.println();
    } 
}