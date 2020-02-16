package programmers_physicalcloth;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class PhysicalCloth {

  private int answer = 0;

  public PhysicalCloth() {
    //void
  }

  public int getAnswer() {
    return this.answer;
  }

  public int solution(int n, int[] lost, int[] reserve) {
    //전체 인원 중 체육복을 도난당한 사람 빼고 현재 가능한 사람 모으기
    int lectureTakenAvailableMember = n - lost.length;

    //체육복을 잃어버린 사람들의 리스트 만들기
    List<Integer> lostMemberList = new ArrayList<Integer>();
    for (int lostMemberNum : lost) {
      lostMemberList.add(lostMemberNum);
    }

    //체육복 여분을 갖고 있는 사람들의 리스트 만들기
    List<Integer> reserveMemberList = new ArrayList<Integer>();
    for (int reserveMemberNum : lost) {
      reserveMemberList.add(reserveMemberNum);
    }

    //체육복을 잃어버렸지만, 원래부터 여분을 갖고 있던 사람을 처리한다.
    //iterator를 써야하나
    for (int lostMemberSearch : lostMemberList) {
      for (int reserveMemberSearch : reserveMemberList) {
        if (lostMemberSearch == reserveMemberSearch) {
          lostMemberList.remove(lostMemberSearch);
          reserveMemberList.remove(reserveMemberSearch);
        }
      }
    }
    return answer;
  }
}