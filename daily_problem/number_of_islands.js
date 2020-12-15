// 섬의 개수 LEETCODE #200 DFS 문제풀이

let numIslands = function(grid) {
    function dfs(i, j) {
        // if there is no land, end
        if ((i < 0) || (i >= grid.length) || (j < 0) || (j >= grid[0].length) || (grid[i][j] != '1')) {
            return;
        };
        grid[i][j] = '#';
        
        dfs(i+1, j);
        dfs(i-1, j);
        dfs(i, j+1);
        dfs(i, j-1);
    };
    
    count = 0
    
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] === '1') {
                dfs(i, j);
                count += 1 // add count += 1 after transvering all lands
            }
        }
    }
    return count
};