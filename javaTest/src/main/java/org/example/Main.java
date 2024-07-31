package org.example;


import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        test();
    }

    public static void test() {
        try {
            Document doc = Jsoup.connect("https://en.wikipedia.org/").get();
            var test = doc;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }


    }

}
