import java.util.*;

class ABROADS {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int q = sc.nextInt();

        Graph g = new Graph(n);

        int[] p = new int[n];
        for(int i=0; i<n; i++) {
            p[i] = sc.nextInt();
        }

        int[][] paths = new int[m][2];
        for(int i=0; i<m; i++) {
            paths[i][0] = sc.nextInt();
            paths[i][1] = sc.nextInt();
            g.add(paths[i][0], paths[i][1]);
        }

        for(int i=0; i<q; i++) {
            String a = sc.nextLine();
            if (a=="P") {
                int b = sc.nextInt();
                int c = sc.nextInt();
                p[b] = c;
            }
            else {
                int road = sc.nextInt()-1;
                g.mat[paths[road][0]][paths[road][1]] = 0;
            }
            g.highestP();
        }

    }
}

class Graph {
    int V;
    int[][] mat;
    Graph(int v) {
        V = v;
        for(int i=0; i<v; i++) {
            for(int j=0; j<v; j++) {
                mat[i][j] = 0;
            }
        }
    }

    void add(int s, int e) {
        mat[s][e] = 1;
        mat[e][s] = 1;
    }

    public void highestP() {
    }
}