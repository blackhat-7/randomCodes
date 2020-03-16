import java.util.*;
import java.io.*; 

public class EvenNumbers { 
	
	static int N = 200000; 
	
	static int n;
	 
	static int []tree = new int[2 * N]; 
		 
	static void build(int []arr) 
	{ 
		for (int i = 0; i < n; i++) 
			tree[n + i] = 1; 
		
		for (int i = n - 1; i > 0; --i) 
			tree[i] = tree[i << 1] + 
					tree[i << 1 | 1]; 
	} 
	
	static void updateTreeNode(int p, int value) 
	{ 
		
		tree[p + n] = (value%2==0) ? 1 : 0; 
		p = p + n; 
        
		for (int i = p; i > 1; i >>= 1) {
			tree[i >> 1] = tree[i] + tree[i^1];
		}
	} 
	
	static int query(int l, int r) 
	{ 
		int res = 0; 
		
		for (l += n, r += n; l <= r; l >>= 1, r >>= 1) 
		{ 
			if ((l & 1) > 0) 
				res += tree[l++]; 
		
			if ((r & 1) > 0) 
				res += tree[--r]; 
		} 
		
		return res; 
	} 

    static Scanner sc = new Scanner(System.in);
	static public void main(String[] args) 
	{ 
        n = sc.nextInt();
        int t = sc.nextInt();
		
		int[] a = new int[n];
		Arrays.fill(a, 0);
		build(a);

        for(int i=0; i<t; i++) {
            String q = sc.next();
            int l = sc.nextInt();
			int r = sc.nextInt();
            if (q.equals("a")) {
                updateTreeNode(l-1, r);
            }
            else {
                System.out.println(query(l-1, r-1));
            }
        }
	}
}
