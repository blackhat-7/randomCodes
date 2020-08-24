import java.util.*;

public class GraphColoring {

    public static void colorGraph(HashMap<Integer, List<Integer>> graph, int N) {
        int[] vertexColor = new int[N];
        Arrays.fill(vertexColor, -1);
        boolean[] availableColors = new boolean[N];
        for (int i=0; i<N; ++i) {
            System.out.println(graph.get(i).toString());
            Arrays.fill(availableColors, true);
            for (int neigh : graph.get(i)) {
                if (vertexColor[neigh] != -1)
                    availableColors[vertexColor[neigh]] = false;
            }
            System.out.println(Arrays.toString(availableColors));
            for (int j=0; i<N; ++j) {
                if (availableColors[j]) {
                    vertexColor[i] = j;
                    break;
                }
            }
        }
        for (int i=0; i<N; ++i) {
            System.out.println("Vertex " + i + " : " + vertexColor[i]);   
        }
    }

    public static void main(String[] args) {
        // List of graph edges as per above diagram
		//List<Edge> edges = Arrays.asList(
		//		new Edge(0, 1), new Edge(0, 4),
		//		new Edge(0, 5), new Edge(4, 5),
		//		new Edge(1, 4), new Edge(1, 3),
		//		new Edge(2, 3), new Edge(2, 4)
		//);

		// Set number of vertices in the graph
		final int N = 6;

		// create a graph from edges
        int[][] edges = {{0, 1}, {0, 4}, {0, 5}, {4, 5}, {1, 4}, {1, 3}, {2, 3}, {2, 4}};
        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        for (int i=0; i<N; ++i) {
            graph.put(i, new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

		// color graph using greedy algorithm
		colorGraph(graph, N);
    }
}
