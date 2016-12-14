package org.shilton;

import java.awt.*;
import java.io.*;
import java.util.HashSet;
import java.util.Set;

import static java.lang.Integer.valueOf;
import static java.nio.charset.StandardCharsets.UTF_8;
import static java.nio.file.Files.readAllBytes;
import static java.nio.file.Paths.get;

/*
The answer to part 1 is 242
 */

public class Day1 {

    private static Direction direction;
    private static Point location;
    private static Set<String> visitedLocations;

    public static void main(String[] args) throws IOException {

        direction = Direction.NORTH;
        location = new Point(0, 0);
        visitedLocations = new HashSet<>();

        Day1 day1part1 = new Day1();
        day1part1.readInstructionsDay1Part1();
        System.out.println(day1part1.howManyBlocksAwayIsSanta());

        direction = Direction.NORTH;
        location = new Point(0, 0);
        visitedLocations = new HashSet<>();

        Day1 day1part2 = new Day1();
        day1part2.readInstructionsDay1Part2();
        System.out.println(day1part2.howManyBlocksAwayIsSanta());
    }

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

        move(valueOf(aMove.substring(1)));
    }

    public void readInstructionsDay1Part1() throws IOException {

        String fileString = new String(readAllBytes(get("/home/local/IMPELLO/shilton/projects/advent-of-code/2016/day1/src/main/resources/file/day1.txt")), UTF_8);

        String[] moves = fileString.split(", ");

        for (String move : moves) {
            process(move);
        }
    }

    public void readInstructionsDay1Part2() throws IOException {

        String fileString = new String(readAllBytes(get("/home/local/IMPELLO/shilton/projects/advent-of-code/2016/day1/src/main/resources/file/day1.txt")), UTF_8);
        String[] moves = fileString.split(", ");

        boolean hqFound = false;

        for (String move : moves) {

            if (!hqFound) {
                process(move);

                String currentLocation = location.toString();
                System.out.println("currentLocation = " + currentLocation);

                if (visitedLocations.contains(currentLocation))
                    hqFound = true;
                else
                    visitedLocations.add(currentLocation);
            }
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
