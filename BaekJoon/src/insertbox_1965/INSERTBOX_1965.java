package insertbox_1965;

import java.util.*;
import java.io.*;

public class INSERTBOX_1965 {

  private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
  private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter((System.out)));

  static int[] inputValue;
  static int[] maxDP;
  static int numberOfBoxes;
  static StringTokenizer splitBySpacing;
  static int answer;

  private static void createArray(int numberOfBoxes){
    inputValue = new int[numberOfBoxes];
    maxDP = new int[numberOfBoxes];
  }

  public static void main(String[] args) throws IOException {
    getInput();
    createArray(numberOfBoxes);
    getResult(splitBySpacing, numberOfBoxes);
    printResult();
  }

  private static void getInput() throws IOException {
    numberOfBoxes = Integer.parseInt(reader.readLine());
    splitBySpacing = new StringTokenizer(reader.readLine());
  }

  private static void getResult(StringTokenizer splitBySpacing, int numberOfBoxes) {
    int INITIALIZE_VALUE = 1;
    //update inputValue and initialize maxDP array
    for (int index = 0; index < numberOfBoxes; index++) {
      inputValue[index] = Integer.parseInt(splitBySpacing.nextToken());
      maxDP[index] = INITIALIZE_VALUE;
      checkBeforeDPAmount(index);
    }
  }

  private static void printResult() throws IOException {
    writer.write(String.valueOf(answer));
    writer.flush();
    writer.close();
  }

  private static void checkBeforeDPAmount(int currentIndex){
    for (int beforeIndex = 0; beforeIndex < currentIndex; beforeIndex++){
      if (inputValue[beforeIndex] < inputValue[currentIndex]){
        maxDP[currentIndex] = Math.max(maxDP[currentIndex], maxDP[beforeIndex] + 1);
      }
    }
    answer = Arrays.stream(maxDP).max().getAsInt();
  }
}