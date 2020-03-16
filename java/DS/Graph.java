class Graph {
    int[][] mat;
    int V;
    Graph(int v) {
        V = size;
        mat = new int[v][v];
    }

    void addEdge(int s, int e, int w) {
        mat[s][e] = w;
        mat[e][s] = w;
    }

    void printMat() {
        for(int i=0; i<V; i++) {
            for(int j=0; j<V; j++) {
                System.out.println(mat);
            }
        }
    }

    int find(int[] parent, int i) {
        if (parent[i]==-1) {
            return i;
        }
        return find(parent, parent[i]);
    }

    void union(int[] parent, int x, int y) {
        int xset = find(parent, x);
        int yset = find(parent, y);

        parent[xset] = yset;
    }
}