class Edge {
    constructor(s, d, w) {
        this.src = s;
        this.dest = d;
        this.weight = w;
    }
}

class Pair {
    constructor(k, v) {
        this.key = k;
        this.val = v;
    }
}

class Graph {
    constructor(V) {
        this.adj = {}
        for (let i=0; i<V; i++) {
            this.adj[i] = []
        }
    }

    addEdge(edge) {
        this.adj[edge.src].push(new Pair(edge.dest, edge.weight));
        this.adj[edge.dest].push(new Pair(edge.src, edge.weight));
    }

    bfs(src) {
        let q = []
        q.push(src);
        let visited = new Array(this.V);
        visited.fill(false);
        visited[src] = true;
        while (q.length != 0) {
            let u = q.shift();
            process.stdout.write(u + " ");
            this.adj[u].forEach((edge) => {
                if (!visited[edge.key]) {
                    q.push(edge.key);
                    visited[edge.key] = true;
                }
            });
        }
        console.log();
    }

    dfs(src) {
        let visited = new Array(this.V);
        visited.fill(false);
        this.dfsUtil(src, visited);
        console.log();
    }
    dfsUtil(src, visited) {
        visited[src] = true;
        process.stdout.write(src + " ");
        this.adj[src].forEach((edge) => {
            if (!visited[edge.key]) {
                visited[edge.key] = true;
                this.dfsUtil(edge.key, visited);
            }
        });
    }
}

g = new Graph(3);

g.addEdge(new Edge(0, 2, 2));
g.addEdge(new Edge(2, 1, 2));
g.addEdge(new Edge(0, 1, 2));

g.bfs(0);
g.dfs(0);
