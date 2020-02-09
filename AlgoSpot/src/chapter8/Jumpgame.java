package chapter8;

import java.util.Scanner;

public class Jumpgame {

  static int[][] map, cache; //map과 cache를 배열로 선언함
  static int N; //변수 설정

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int cases = sc.nextInt(); //처음에 테스트 케이스 수를 받는다
    while (cases-- > 0) { //하나씩 줄여나간다.
      N = sc.nextInt(); //두 번째에 격자 케이스 수를 받는다
      map = new int[N][N]; //격자를 만든다
      cache = new int[N][N]; //캐시를 만든다

      for (int y = 0; y < N; y++) { //격자 케이스 수(줄 수) 만큼 y를 돌리고
        for (int x = 0; x < N; x++) { //x를 돌린다.
          map[y][x] = sc.nextInt(); //만든다.
          cache[y][x] = -1; //그리고 -1로 초기화한다.
        }
      }

      System.out.println(jump(0, 0) ? "YES" : "NO"); //점프 메소드를 삼항 연산자로 실행한다.
    }
  }

  public static boolean jump(int y, int x) {

    if (y >= N || x >= N) {
      return false;
    }
    if (y == N - 1 && x == N - 1) {
      return true;
    }

    if (cache[y][x] == 1) {
      return false;
    } else {
      cache[y][x] = 1;
    }

    int jumpSize = map[y][x];
    return jump(y, x + jumpSize) || jump(y + jumpSize, x); //계속 재귀호출...
  }
}
