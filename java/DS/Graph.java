import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

class Node implements Comparable<Node> {
    int dest;
    int cost;

    Node(int d, int c) {
        dest = d;
        cost = c;
    }

    @Override
    public int compareTo(Node o) {
        if(this.cost > o.cost) return 1;
        else if(this.cost < o.cost) return -1;
        else return 0;
    }
}

class Graph {
    protected int vertices;
    List<LinkedList<Node>> adjList;

    Graph(int v) {
        vertices = v;
        adjList = new ArrayList<LinkedList<Node>>(vertices);
        for(int i=0; i<vertices; ++i) {
            adjList.add(new LinkedList<>());
        }
    }

    public void addEdge(int s, int d, int w) {
        adjList.get(s).add(new Node(d, w));
        adjList.get(d).add(new Node(s, w));
    }

    public void bfs(int s) {
        boolean visited[] = new boolean[vertices];
        Queue<Integer> q = new LinkedList<>();
        q.add(s);
        visited[s] = true;
        while(!q.isEmpty()) {
            s = q.poll();
            System.out.print(s + " ");
            for(Node d : adjList.get(s)) {
                if(!visited[d.dest]) {
                    q.add(d.dest);
                    visited[d.dest] = true;
                }
            }
        }
        System.out.println();
    }

    public void relaxNeighbours(int v, Set<Integer> settled, PriorityQueue<Node> pq, int dist[]) {
        for(Node i : adjList.get(v)) {
            if(!settled.contains(i.dest)) {
                if(dist[i.dest] > dist[v]+i.cost) {
                    dist[i.dest] = dist[v] + i.cost;
                    pq.add(new Node(i.dest, dist[i.dest]));
                }
            }
        }
    }

    public void singleSourceShortestPathDjikstra(int s) {
        int dist[] = new int[vertices];
        PriorityQueue<Node> pq = new PriorityQueue<>();
        Set<Integer> settled = new HashSet<>();
        for(int i=0; i<vertices; ++i) {
            dist[i] = Integer.MAX_VALUE;
        }
        pq.add(new Node(s, 0));
        dist[s] = 0;
        while(settled.size() != vertices){
            int v = pq.remove().dest;
            settled.add(v);
            relaxNeighbours(v, settled, pq, dist);
        }
        System.out.println(Arrays.toString(dist));
    }

    public void DFS(int s) {
        boolean visited[] = new boolean[vertices];
        Stack<Integer> st = new Stack<>();
        for(int i=0; i<vertices; ++i) visited[i] = false;
        st.push(s);
        while(!st.isEmpty()) {
            s = st.pop();
            if(!visited[s]) {
                visited[s] = true;
                System.out.print(s + " ");
            }
            for(Node i : adjList.get(s)) {
                if(!visited[i.dest]) {
                    st.push(i.dest);
                }
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Graph g = new Graph(6);
        g.addEdge(0, 1, 2);
        g.addEdge(0, 2, 4);
        g.addEdge(1, 2, 1);
        g.addEdge(1, 3, 7);
        g.addEdge(2, 4, 3);
        g.addEdge(4, 5, 5);
        g.addEdge(3, 5, 1);
        g.addEdge(3, 4, 2);
        g.bfs(0);
        g.singleSourceShortestPathDjikstra(0);
        g.DFS(0);
    }
}