package org.github.luolong47;

import cn.hutool.core.codec.Base64;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    void case01() {
        String s = "e6Z9i~]8R~U~QHE{RnY{QXg~QnQ{^XVlRXlp^XI5Q6Q6SKY8jUAA";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            sb.append((char)(s.charAt(i)-4));
        }
        String s1 = sb.toString();
        String s2 = Base64.decodeStr(s1);
        System.out.println(s2);
    }
}