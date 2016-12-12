package org.shilton;

import java.awt.*;
import java.io.*;
import java.net.URL;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Scanner;

import static java.nio.charset.StandardCharsets.UTF_8;
import static java.nio.file.Files.readAllBytes;
import static java.nio.file.Paths.get;

public class Day1 {

    public static void main(String[] args) throws IOException {
        Day1 day1 = new Day1();
        day1.readInstructions();
        System.out.println(day1.howManyBlocksAwayIsSanta());
    }

    private Direction direction = Direction.NORTH;
    private Point location = new Point(0, 0);

    private void turnLeft() {
        if (direction == Direction.NORTH)
            direction = Direction.WEST;
        else if (direction == Direction.WEST)
            direction = Direction.SOUTH;
        else if (direction == Direction.SOUTH)
            direction = Direction.EAST;
        else if (direction == Direction.EAST)
            direction = Direction.NORTH;
    }

    private void turnRight() {
        if (direction == Direction.NORTH)
            direction = Direction.EAST;
        else if (direction == Direction.EAST)
            direction = Direction.SOUTH;
        else if (direction == Direction.SOUTH)
            direction = Direction.WEST;
        else if (direction == Direction.WEST)
            direction = Direction.NORTH;
    }

    private void move(final int stepsToMove) {
        int xPos = location.x;
        int yPos = location.y;

        if (direction == Direction.NORTH)
            location = new Point(xPos, yPos + stepsToMove);
        else if (direction == Direction.EAST)
            location = new Point(xPos + stepsToMove, yPos);
        else if (direction == Direction.SOUTH)
            location = new Point(xPos, yPos - stepsToMove);
        else if (direction == Direction.WEST)
            location = new Point(xPos - stepsToMove, yPos);
    }

    private void process(final String aMove) {
        if (aMove.charAt(0) == 'R')
            turnRight();
        else
            turnLeft();

        move(aMove.charAt(1));
    }

    public void readInstructions() throws IOException {

        String fileString = new String(readAllBytes(get("/home/local/IMPELLO/shilton/projects/advent-of-code/2016/day1/src/main/resources/file/day1.txt")), UTF_8);

        String[] moves = fileString.split(", ");

        for (String move : moves) {
            process(move);
        }
    }

    public int howManyBlocksAwayIsSanta() {
        int x = Math.abs(location.x);
        int y = Math.abs(location.y);

        return x + y;
    }

    private enum Direction {
        NORTH,
        EAST,
        SOUTH,
        WEST
    }
}
