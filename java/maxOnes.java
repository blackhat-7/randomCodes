import java.util.*;

public class maxOnes {

    public static int recur(char matr[][], int n, int i, int j, int points){
    	if(i==n || j==n) {
    		return points;
    	}
    	else {
    		points = (matr[i][j] == 'x') ? (points +1) : points;
    		int right = recur(matr, n, i, j+1, points);
    		int down = recur(matr, n, i+1, j, points);
    		
    		if (right > down) {
    			return right;
    		}
    		else {
    			return down;
    		}	
    	}
    	
    }

    public static int solve(char matr[][], int n){
        int ans = recur(matr, n, 0, 0, 0);
        return ans;
    }

    public static void main(String[] args){
        int n;
        Scanner s = new Scanner(System.in);
        n = s.nextInt();

        char matr[][] = new char[n][n];
        for (int i=0;i<n;i++){
            String temp = s.next();
            for (int j=0;j<n;j++){
                matr[i][j] = temp.charAt(j);
            }
        }

        System.out.println(solve(matr,n));
        s.close();

    }

}
