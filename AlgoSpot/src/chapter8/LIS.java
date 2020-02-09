package chapter8;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class LIS {

  private int[] elements;
  private int elementsLength;
  private int[] cache;

  public LIS(int[] _elements) {
    this.elements = _elements;
    this.elementsLength = elements.length;
    this.cache = new int[elementsLength];
  }

  public int maxSequence() {
    int max = 0;
    for (int i = 0; i < elementsLength; i++) {
      int ref = getLengthofSequence(i);
      if (ref > max) {
        max = ref;
      }
    }
    return max;
  }

  public int getLengthofSequence(int index) {
    for (int i = (index + 1); i < elementsLength; i++) {
      int length = 1;
      if (elements[index] < elements[i]) {
        if (cache[i] != 0) {
          length += cache[i];
        } else {
          length += getLengthofSequence(i);
        }
        if (length > cache[index]) {
          cache[index] = length;
        }
      }
    }
    if (cache[index] == 0) {
      cache[index] = 1;
    }
    return cache[index];
  }

  public static void main(String[] args) {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    try {
      int numOfTestCase = Integer.parseInt(br.readLine().trim());

      if (numOfTestCase > 50) {
        return;
      }

      while ((numOfTestCase--) > 0) {
        int numOfElements = Integer.parseInt(br.readLine().trim());

        String[] inputDatas = br.readLine().trim().split(" ");
        int[] elements = new int[numOfElements];

        for (int i = 0; i < numOfElements; i++) {
          elements[i] = Integer.parseInt(inputDatas[i]);
        }

        LIS l = new LIS(elements);
        System.out.println(l.maxSequence());
      }

    } catch (NumberFormatException | IOException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
  }
}