import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

class Edge implements Comparable<Edge> {
    int src;
    int dest;
    int cost;

    Edge(int s, int d, int c) {
        src = s;
        dest = d;
        cost = c;
    }

    @Override
    public int compareTo(Edge o) {
        if(this.cost > o.cost) return 1;
        else if(this.cost < o.cost) return -1;
        else return 0;
    }
    @Override
    public String toString() {
        return src + "-" + dest + " : " + cost;
    }
    @Override
    public boolean equals(Object o) {
        if(!(o instanceof Edge)) return false;
        Edge e = (Edge) o;
        return src == e.src && dest == e.dest && cost == e.cost;
    }
}

class Graph {
    int vertices;
    List<Edge> edges;
    List<LinkedList<Edge>> adjList;

    Graph(int v) {
        vertices = v;
        edges = new ArrayList<>();
        adjList = new ArrayList<LinkedList<Edge>>(vertices);
        for(int i=0; i<vertices; ++i) {
            adjList.add(new LinkedList<>());
        }
    }

    //directed
    public void addEdge(int s, int d, int w) {
        Edge e = new Edge(s, d, w);
        edges.add(e);
        adjList.get(s).add(e);
    }

    public void removeEdge(Edge e) {
        edges.remove(e);
        adjList.get(e.src).remove(e);
    }

    public void bfs(int s) {
        boolean visited[] = new boolean[vertices];
        Queue<Integer> q = new LinkedList<>();
        q.add(s);
        visited[s] = true;
        while(!q.isEmpty()) {
            s = q.poll();
            System.out.print(s + " ");
            for(Edge d : adjList.get(s)) {
                if(!visited[d.dest]) {
                    q.add(d.dest);
                    visited[d.dest] = true;
                }
            }
        }
        System.out.println();
    }

    public void relaxNeighbours(int v, Set<Integer> settled, PriorityQueue<Edge> pq, int dist[]) {
        for(Edge i : adjList.get(v)) {
            if(!settled.contains(i.dest)) {
                if(dist[i.dest] > dist[v]+i.cost) {
                    int prevDist = dist[i.dest];
                    dist[i.dest] = dist[v] + i.cost;
                    pq.add(new Edge(i.src, i.dest, dist[i.dest]));
                    System.out.println("Distance from " + v + " to " + i.dest + " changed from " + prevDist + " to " + dist[i.dest] + " and added edge to pq");
                }
            }
        }
    }

    public void singleSourceShortestPathDjikstra(int s) {
        int dist[] = new int[vertices];
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        Set<Integer> settled = new HashSet<>();
        for(int i=0; i<vertices; ++i) {
            dist[i] = Integer.MAX_VALUE;
        }
        pq.add(new Edge(-1, s, 0));
        dist[s] = 0;
        while(settled.size() != vertices && pq.size() != 0){
            int v = pq.remove().dest;
            settled.add(v);
            System.out.println(v + " is settled");
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
            for(Edge i : adjList.get(s)) {
                if(!visited[i.dest]) {
                    st.push(i.dest);
                }
            }
        }
        System.out.println();
    }

    public void findNeighbours(int v, boolean visited[]) {
        visited[v] = true;
        for(Edge i : adjList.get(v)) {
            if(!visited[i.dest])
                findNeighbours(i.dest, visited);
        }
    }

    public int findMotherVertex() {
        boolean visited[] = new boolean[vertices];
        int candidate = 0;
        for(int i=0; i<vertices; ++i) {
            if(!visited[i]) {
                findNeighbours(i, visited);
                candidate = i;
            }
        }
        boolean finalCheck[] = new boolean[vertices];
        findNeighbours(candidate, finalCheck);
        for(int i=0; i<vertices; ++i) {
            if(!finalCheck[i]) {
                return -1;
            }
        }
        return candidate;
    }

    public void allPossiblePaths(int s, int d, List<List<Integer>> allPaths, List<Integer> path) {     //bfs approach
        if (s == d) {
            allPaths.add(path);
            return;
        }
        for(Edge i : adjList.get(s)) {
            path.add(i.dest);
            allPossiblePaths(i.dest, d, allPaths, new ArrayList<>(path));
            path.remove(path.size()-1);
        }
        return;
    }

    private boolean isCyclicDirected(int src, boolean visited[], boolean stack[]) {
        if(stack[src])
            return true;
        if(visited[src])
            return false;
        stack[src] = true;
        visited[src] = true;
        for(Edge i : adjList.get(src)) {
            if(isCyclicDirected(i.dest, visited, stack)) {
                return true;
            }
        }
        stack[src] = false;
        return false;
    }

    public boolean isCyclicDirected() {
        boolean visited[] = new boolean[vertices];
        boolean stack[] = new boolean[vertices];
        for(int i=0; i<vertices; ++i) {
            if(isCyclicDirected(i, visited, stack)) {
                return true;
            }
        }
        return false;
    }

    private int find(int parent[], int i) {
        if(parent[i] == -1)
            return i;
        return find(parent, parent[i]);
    }

    private void union(int parent[], int x, int y) {
        int parentX = find(parent, x);
        int parentY = find(parent, y);
        parent[parentX] = parentY;
    }

    public boolean isCyclicUndirected() {
        int parent[] = new int[vertices];
        for(int i=0; i<vertices; ++i) parent[i] = -1;
        for(Edge i : edges) {
            int parentX = find(parent, i.src);
            int parentY = find(parent, i.dest);
            if(parentX == parentY) return true;
            union(parent, parentX, parentY);
            
        }
        return false;
    }

    private void topologicalSortUtil(int src, Stack<Integer> stk, boolean visited[]) {
        visited[src] = true;
        for(Edge i : adjList.get(src)) {
            if(!visited[i.dest]) {
                topologicalSortUtil(i.dest, stk, visited);
            }
        }
        stk.push(src);
    }

    public int[] topologicalSort() {
        Stack<Integer> stk = new Stack<>();
        boolean visited[] = new boolean[vertices];
        for(int i=0; i<vertices; ++i) {
            if(!visited[i])
                topologicalSortUtil(i, stk, visited);
        }
        int sortedVertices[] = new int[vertices];
        for(int i=0; i<vertices; ++i) {
            sortedVertices[i] = stk.pop();
        }
        return sortedVertices;
    }

    public Graph kruskalsMST() {
        Graph mst = new Graph(vertices);
        Collections.sort(edges);
        for(Edge i : edges) {
            mst.addEdge(i.src, i.dest, i.cost);
            if(mst.isCyclicUndirected()) {
                mst.removeEdge(i);
            }
            if(mst.edges.size() >= vertices-1)
                break;
        }
        return mst;
    } 

    public int[] bellmanFord(int source) {
        //set distance for all vertices to inf
        int dist[] = new int[vertices];
        for(int i=0; i<vertices; ++i) {
            dist[i] = Integer.MAX_VALUE;
        }
        dist[source] = 0;

        // keep modifying the edges v-1 times or till it does not modify anymore
        boolean modified = true;
        int count = vertices-1;
        while(count > 0 && modified) {
            modified = false;
            for(Edge e : edges) {
                int u = e.src, v = e.dest, w = e.cost;
                if(dist[u] != Integer.MAX_VALUE && dist[u]+w < dist[v]) {
                    dist[v] = dist[u] + w;
                    modified = true;
                }
            }
            --count;
        }

        //check for negative cycles
        for(Edge e : edges) {
            int u = e.src, v = e.dest, w = e.cost;
            if(dist[u] != Integer.MAX_VALUE && dist[u]+w < dist[v]) {
                System.out.println("Negative Cycle exists");
                return null;
            }
        }
        return dist;
    }


    public static void main(String[] args) {
        Graph g = new Graph(5);
        g.addEdge(0, 1, -1);
        g.addEdge(0, 2, 4);
        g.addEdge(1, 4, 2);
        g.addEdge(1, 2, 3);
        g.addEdge(1, 3, 2);
        g.addEdge(4, 3, -3);
        g.addEdge(3, 2, 5);
        g.addEdge(3, 1, 1);

        System.out.println(Arrays.toString(g.bellmanFord(0)));
    }
}
