package Programmers;

import java.util.*;
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

// 외계행성의 나이
class Exoplanet {
    public String exoPlanet(int age) {
        String answer = "";
        String[] alphabet_list = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"};

        String[] string_age_list = String.valueOf(age).split("");

        for (int i = 0; i < string_age_list.length; i++) {
            answer += alphabet_list[Integer.parseInt(string_age_list[i])];
        }
        return answer;
    }
}

// 피자 나눠 먹기 (2)
class SharePizzaTwo {
    public int sharePizzaTwo(int n) {
        int pizza = 6;

        while (pizza % n != 0) {
            pizza += 6;
        }
        return pizza / 6;
    }
}

// 최댓값 만들기 (2)
class MakeMaxNumberTwo {
    public int makeMaxNumberTwo(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers);

        if (numbers[0] * numbers[1] > numbers[numbers.length - 1] * numbers[numbers.length - 2]) {
            answer = numbers[0] * numbers[1];
        } else {
            answer = numbers[numbers.length - 1] * numbers[numbers.length - 2];
        }
        return answer;
    }
}