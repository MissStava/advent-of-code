package org.shilton;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class MyFileReader {
    public static void main(String[] args) {

        MyFileReader myFileReader = new MyFileReader();
        myFileReader.read();
    }

    public void read() {

        File file1 = new File("/home/local/IMPELLO/shilton/projects/advent-of-code/2016/day1/src/main/resources/file/day1.txt");

        if (file1.exists()) {
            System.out.println("File exists");
        } else {
            System.out.println("File does not exist");
        }
    }
}
