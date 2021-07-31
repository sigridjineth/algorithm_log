import java.util.*;

class Pair {
    int x, y, z, night;
    Pair(int x, int y, int z, int night) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.night = night;
    }
}

public class 벽부수고_이동하기3_Q16933 {
    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, 1, -1};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int l = sc.nextInt();
        sc.nextLine();
        int[][] a = new int[n][m];
        int[][][][] d = new int[n][m][l+1][2];
        for (int i=0; i<n; i++) {
            String s = sc.nextLine();
            for (int j=0; j<m; j++) {
                a[i][j] = s.charAt(j) - '0';
            }
        }
        d[0][0][0][0] = 1;
        Queue<Pair> q = new LinkedList<Pair>();
        q.offer(new Pair(0, 0, 0, 0));
        while (!q.isEmpty()) {
            Pair p = q.remove();
            int x = p.x;
            int y = p.y;
            int z = p.z;
            int night = p.night;
            for (int k=0; k<4; k++) {
                int nx = x+dx[k];
                int ny = y+dy[k];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if (a[nx][ny] == 0 && d[nx][ny][z][1-night] == 0) {
                    d[nx][ny][z][1-night] = d[x][y][z][night] + 1;
                    q.offer(new Pair(nx, ny, z, 1-night));
                }
                if (night == 0 && z+1 <= l && a[nx][ny] == 1 && d[nx][ny][z+1][1-night] == 0) {
                    d[nx][ny][z+1][1-night] = d[x][y][z][night] + 1;
                    q.offer(new Pair(nx, ny, z+1, 1-night));
                }
            }
            if (d[x][y][z][1-night] == 0) {
                d[x][y][z][1-night] = d[x][y][z][night] + 1;
                q.offer(new Pair(x, y, z, 1-night));
            }
        }
        int ans = -1;
        for (int j=0; j<2; j++) {
            for (int i=0; i<=l; i++) {
                if (d[n-1][m-1][i][j] == 0) continue;
                if (ans == -1) {
                    ans = d[n-1][m-1][i][j];
                } else if (ans > d[n-1][m-1][i][j]) {
                    ans = d[n-1][m-1][i][j];
                }
            }
        }
        System.out.println(ans);
    }
}
