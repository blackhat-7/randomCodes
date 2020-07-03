import java.util.*;

public class joiurneyInMatrix
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[][] = new int[n][n];
        for (int i=0; i<n; ++i)
        {
            for (int j=0; j<n; ++j)
            {
                arr[i][j] = sc.nextInt();
            }
        }
        forward(arr, 0, 0, n);
        sc.close();
    }
    public static int forward(int[][] arr, int i, int j, int n)
    {
        if (i==n-1 && j==n-1)
        {
            return arr[i][j];
        }
        else if (i==j)
        {
            return arr[i][j] + forward(arr, i, j+1, n);
        }
        else if (i==n-1)
        {
            return arr[i][j] + forward(arr, i, j+1, n);
        }
        else if (j==n-1)
        {
            return arr[i][j] + forward(arr, i+1, j, n);
        }
        return Math.max(forward(arr, i+1, j, n), forward(arr, i, j+1, n));
    }
}
