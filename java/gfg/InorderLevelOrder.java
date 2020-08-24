// { Driver Code Starts
import java.util.*;

class Node
{
    int data;
    Node left, right;
    
    Node(int item)
    {
        data = item;
        left = right = null;
    }    
        public void setLeft(Node left) 
    {
        this.left = left;
    }
  
    public void setRight(Node right) 
    {
        this.right = right;
    }
        
    
}


class ConstructBT
{
    Node root;
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
	    int t = sc.nextInt();
	    
	    while(t-- > 0)
	    {
	        int n = sc.nextInt();
	        
	        int inord[] = new int[n];
	        int level[] = new int[n];
	        for(int i = 0; i < n; i++)
	            inord[i] = sc.nextInt();
	            
	        for(int i = 0; i < n; i++)
	             level[i] = sc.nextInt();
	             
	        InorderLevelOrder g = new InorderLevelOrder();
	        Node node =  g.buildTree(inord, level);
	        printPreOrder(node);
	        System.out.println();
	        
	        
        }
        sc.close();
    }
    
   static void printPreOrder(Node node)
   {
       if(node == null)
          return;
          
        System.out.print(node.data + " ");
        printPreOrder(node.left);
        printPreOrder(node.right);
   }
}
// } Driver Code Ends



/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

/*Complete the function below*/
class InorderLevelOrder
{
    Node util(int[] inorder, int[] level, int low, int high) {
        if (low == high)
            return new Node(level[low]);
        int val = level[low];
        int index = Arrays.binarySearch(inorder, low, high, val);
        Node root = new Node(val);
        if (index > low) {
            root.left = util(inorder, level, low, index-1);
        }
        if (index < high) {
            root.right = util(inorder, level, index+1, high);
        }
        return root;
    }

    Node buildTree(int inord[], int level[])
    {
        Node root = null;
        util(inord, level, 0, inord.length-1);
        return root;
        
    }
    
   
}
















