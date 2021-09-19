import java.util.*;

class Pair {
    int x;
    int y;
    Integer move;
    Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
    Pair(int x, int y, Integer move) {
        this.x = x;
        this.y = y;
        this.move = move;
    }
}

class Solution {
    private static List<String> orders = new ArrayList<>();
    private static int[] dx = {1, -1, 0, 0};
    private static int[] dy = {0, 0, 1, -1};
    
    public int solution(int[][] board, int r, int c) {
        Set<Integer> cardSet = new HashSet<>();
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (board[i][j] != 0) {
                    cardSet.add(board[i][j]);
                }
            }
        }
        List<Integer> cardList = new ArrayList<>(cardSet);
        Collections.sort(cardList);
        
        // STEP 2: getting all combinations possible to render
        findAllCombinations(cardList, 0, new String());
        
        // STEP 3: BFS Search
        int min = Integer.MAX_VALUE;
        for (String combination: orders) {
            String[] order = combination.split("");
            int total_move = 0;
            int[] position = {r, c};
            int[][] copy_board  = new int[4][4];
			for(int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					copy_board[i][j] = board[i][j];
				}
			}
            for (String target_card: order) {
                int card_num = Integer.parseInt(target_card);
                // 첫 번째 카드 찾기
                total_move += cardSearch(position, card_num, copy_board);
                copy_board[position[0]][position[1]] = 0;
                total_move += 1;
                // 두 번째 카드 찾기
                total_move += cardSearch(position, card_num, copy_board);
                copy_board[position[0]][position[1]] = 0;
                total_move += 1;
            }
            min = Math.min(min, total_move);
        }
        return min;
    }
    public static int cardSearch(int[] position, int target_card, int[][] copy_board) {
        Queue<Pair> queue = new LinkedList<>();
        boolean[][] check = new boolean[4][4];
        int x = position[0];
        int y = position[1];
        check[x][y] = true;
        queue.add(new Pair(x, y, 0));
        
        // 상하좌우 위 아래 왼 오
        while (!queue.isEmpty()) {
            Pair next = queue.poll();
            int px = next.x;
            int py = next.y;
            int pmove = next.move;
            if (copy_board[next.x][next.y] == target_card) {
                position[0] = next.x;
                position[1] = next.y;
                return pmove;
            }
            for (int i = 0; i < 4; i++) {
                int nx = px + dx[i];
                int ny = py + dy[i];
                if (nx < 0 || nx > 3 || ny < 0 || ny > 3) {
                    continue;
                }
                if (check[nx][ny] == true) {
                    continue;
                }
                check[nx][ny] = true;
                queue.add(new Pair(nx, ny, pmove + 1));
            }
            // Ctrl 상하좌우 이동
            for (int i = 0; i < 4; i++) {
                Pair CtrlEndPoint = checkCtrlMoveRoute(px, py, i, copy_board);
                int nx = CtrlEndPoint.x;
                int ny = CtrlEndPoint.y;
                if (nx == x && ny == y) {
                    continue;
                }
                if (check[nx][ny]) {
                    continue;
                }
                check[nx][ny] = true;
                queue.add(new Pair(nx, ny, pmove + 1));
            }
        }
        return 0;
    }
    
    public static Pair checkCtrlMoveRoute(int x, int y, int direction, int[][] copy_board) {
        int px = x + dx[direction];
        int py = y + dy[direction];
        while (px >= 0 && px < 4 && py >= 0 && py < 4) {
            if (copy_board[px][py] != 0) {
                return new Pair(px, py);
            }
            px = px + dx[direction];
            py = py + dy[direction];
        }
        // 만약 카드가 없으면 끝에서 종료
        return new Pair(px - dx[direction], py - dy[direction]);
    }

    public static void findAllCombinations(List<Integer> card, int depth, String combinations) {
        if (depth == card.size()) {
            orders.add(combinations);
            return;
        }
        for (int i = 0; i < card.size(); i++) {
            int element = card.get(i);
            if (!combinations.contains(Integer.toString(element))) {
                findAllCombinations(card, depth + 1, combinations.concat(Integer.toString(element)));
            }
        }
    }
}
