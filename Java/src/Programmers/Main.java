package Programmers;

import java.util.Arrays;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {
        AppearOnce appearOnce = new AppearOnce();
        System.out.println(appearOnce.appearOnce("abcabcadc"));
    }
}

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