package chapter9;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class NUMBERGAME {

  private static final int MAXIMUM_BOARD_SIZE = 50;
  private static final int EMPTY_VALUE = -987654321;
  private static int[][] cache = new int[MAXIMUM_BOARD_SIZE][MAXIMUM_BOARD_SIZE];

  public static void main(String[] args) {
    playGame();
  }

  public static void playGame() {
    try {
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
      int cases = Integer.parseInt(reader.readLine());

      while (cases-- > 0) {
        for (int index = 0; index < MAXIMUM_BOARD_SIZE; index++) {
          Arrays.fill(cache[index], EMPTY_VALUE);
        }
        int length = Integer.parseInt(reader.readLine());
        int[] board = new int[length];
        String[] input = reader.readLine().split(" ");
        for (int index = 0; index < length; index++) {
          board[index] = Integer.parseInt(input[index]);
        }
        int diffValue = getDiffValue(board, 0, length - 1);
        writer.append(String.valueOf(diffValue));
        writer.append("\n");
      }
      writer.flush();
      writer.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public static int getDiffValue(int[] board, int leftindex, int rightindex) {
    //기저 사례 제
    if (leftindex > rightindex) {
      return 0;
    }
    //메모이제이션
    int ret = cache[leftindex][rightindex];
    if (ret != EMPTY_VALUE) {
      return ret;
    }
    //실제 계산
    ret = Math.max(board[leftindex] - getDiffValue(board, leftindex + 1, rightindex),
        board[rightindex] - getDiffValue(board, leftindex, rightindex - 1));
    if (rightindex - leftindex >= 1){
      ret = Math.max(ret, - getDiffValue(board, leftindex + 2, rightindex));
      ret = Math.max(ret, - getDiffValue(board, leftindex, rightindex - 2));
    }
    cache[leftindex][rightindex] = ret;
    return ret;
  }
}
