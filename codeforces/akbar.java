import java.io.*;
import java.util.*;

class Soldier {
    int city;
    int strength;

    Soldier(int city, int strength) {
        this.city = city;
        this.strength = strength;
    }
}

class Tuple {
    int x, y, z;

    Tuple(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
}

public class akbar {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken()), r = Integer.parseInt(st.nextToken()),
                    m = Integer.parseInt(st.nextToken());
            HashMap<Integer, LinkedList<Integer>> g = new HashMap<Integer, LinkedList<Integer>>();
            for (int i = 1; i <= n; i++) {
                g.put(i, new LinkedList<>());
            }
            for (int i = 0; i < r; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken()), v = Integer.parseInt(st.nextToken());
                g.get(u).add(v);
                g.get(v).add(u);
            }
            List<Soldier> soldiers = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken()), v = Integer.parseInt(st.nextToken());
                soldiers.add(new Soldier(u, v));
            }
            Map<Integer, Integer> visited = new HashMap<>();
            if (bfs(g, visited, soldiers) || visited.size() != n)
                System.out.println("No");
            else
                System.out.println("Yes");
        }
        br.close();
    }

    static boolean bfs(HashMap<Integer, LinkedList<Integer>> g, Map<Integer, Integer> visited, List<Soldier> soldiers) {
        Queue<Tuple> q = new LinkedList<>();
        for (int i = 0; i < soldiers.size(); i++) {
            Soldier s = soldiers.get(i);
            q.offer(new Tuple(s.city, s.strength, i));
            visited.put(s.city, i);
        }
        while (!q.isEmpty()) {
            Queue<Tuple> new_q = new LinkedList<>();
            while (!q.isEmpty()) {
                Tuple t = q.poll();
                if (t.y > 0) {
                    for (int c : g.get(t.x)) {
                        if (visited.containsKey(c)) {
                            if (visited.get(c) != t.z)
                                return true;
                        } else {
                            new_q.offer(new Tuple(c, t.y - 1, t.z));
                            visited.put(c, t.z);
                        }
                    }
                }
            }
            q = new_q;
        }
        return false;
    }
}
