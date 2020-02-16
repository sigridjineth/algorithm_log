package programmers_physicalcloth;


import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;


class solutionTest {

  //https://devlab.neonkid.xyz/2019/09/26/java/2019-09-26-Junit5-%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%9C-Java-Test-Code-%EC%9E%91%EC%84%B1/
  private static PhysicalCloth physicalcloth;

  @BeforeAll
  static void setup() {
    physicalcloth = new PhysicalCloth();
  }

  @DisplayName("정확도 테스트 1")
  @Test
  public void solutionTestFirstCase() {
    int totalNumber = 5;
    int[] lostMemberList = {2, 4};
    int[] reserveMemberList = {1, 3, 5};
    physicalcloth.solution(totalNumber, lostMemberList, reserveMemberList);
    assertEquals(5, physicalcloth.getAnswer());
  }

  @DisplayName("정확도 테스트 2")
  @Test
  public void solutionTestSecondCase() {
    int totalNumber = 5;
    int[] lostMemberList = {2, 4};
    int[] reserveMemberList = {3};
    physicalcloth.solution(totalNumber, lostMemberList, reserveMemberList);
    assertEquals(4, physicalcloth.getAnswer());
  }

  @DisplayName("정확도 테스트 3")
  @Test
  public void solutionTestThirdCase() {
    int totalNumber = 3;
    int[] lostMemberList = {3};
    int[] reserveMemberList = {1};
    physicalcloth.solution(totalNumber, lostMemberList, reserveMemberList);
    assertEquals(2, physicalcloth.getAnswer());
  }
  //@DisplayName("효율성 테스트");
}