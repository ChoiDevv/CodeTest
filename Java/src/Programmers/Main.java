package Programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {

    }
}

// 한 번만 등장한 문자
class AppearOnce {
    public String appearOnce(String s) {
        String answer = "";

        for (int i = 0; i < s.length(); i++) {
            if (s.length() - s.replace(String.valueOf(s.charAt(i)), "").length() == 1) {
                answer += s.charAt(i);
            }
        }
        return Arrays.stream(answer.split("")).sorted().collect(Collectors.joining());
    }
}

// 인덱스 바꾸기
class ChangeIndex {
    public String changeIndex(String my_string, int num1, int num2) {
        String answer = "";
        String[] a = my_string.split("");

        for (int i = 0; i < a.length; i++) {
            if (i == num1) {
                answer += a[num2];
            }
            else if (i == num2) {
                answer += a[num1];
            }
            else {
                answer += a[i];
            }
        }

        return answer;
    }
}

// 배열 회전시키기
class ArrayRotation {
    public List<Integer> arrayRotation(int[] numbers, String direction) {
        ArrayList<Integer> answer = new ArrayList<>();

        if (Objects.equals(direction, "right")) {
            answer.add(numbers[numbers.length - 1]);
            for (int i = 0; i < numbers.length - 1; i++) {
                answer.add(numbers[i]);
            }
        } else {
            for (int i = 1; i < numbers.length; i++) {
                answer.add(numbers[i]);
            }
            answer.add(numbers[0]);
        }

        return answer;
    }
}