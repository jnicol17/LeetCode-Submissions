// Solution for LeetCode Problem 807: Max Increase to Keep City Skyline
public class Solution {

	//	The grid is:
	//		[ [3, 0, 8, 4], 
	//		  [2, 4, 5, 7],
	//		  [9, 2, 6, 3],
	//		  [0, 3, 1, 0] ]
	//
	//		The skyline viewed from top or bottom is: [9, 4, 8, 7]
	//		The skyline viewed from left or right is: [8, 7, 9, 3]
	//
	//		The grid after increasing the height of buildings without affecting skylines is:
	//
	//		gridNew = [ [8, 4, 8, 7],
	//		            [7, 4, 7, 7],
	//		            [9, 4, 8, 7],
	//		            [3, 3, 3, 3] ]
	// 		so the output is 35 based on the increases that we can make
	public static void main(String[] args) {
		// input grid
		int[][] grid = {{3,0,8,4},{2,4,5,7},{9,2,6,3},{0,3,1,0}};
		Solution solution = new Solution();
		int output = solution.maxIncreaseKeepingSkyline(grid);
		// output = 35
		System.out.println(output);

	}
	
	
	public int maxIncreaseKeepingSkyline(int[][] grid) {
		// the grid is square (N by N)
	    int N = grid.length;
	    // col_max and row_max are used to determine how much we can increase each buildings height (must be less than min of the two)
	    int[] col_max = new int[N];
	    int[] row_max = new int[N];
	    
	    // setting the initial row and column maximum values
	    for (int r = 0; r < N; r++){
	        for (int c = 0; c < N; c++){
	            row_max[r] = Math.max(row_max[r], grid[r][c]);
	            col_max[c] = Math.max(col_max[c], grid[r][c]);
	        }
	    }
	    
	    // incrementing the answer based on how much we can increase the height of a given building, to still be <= the tallest building
	    // in its column and in its row (by taking the minimum of the two)
	    int answer = 0;
	    for (int r = 0; r < N; r++){
	        for (int c = 0; c < N; c++){
	            answer += Math.min(row_max[r], col_max[c]) - grid[r][c];
	        }
	    }
	    return answer;
	}

}
