package org.shilton;

import java.awt.*;
import java.io.*;
import java.util.HashSet;
import java.util.Set;

import static java.lang.Integer.valueOf;

/*
The answer to part 1 is 242
The answer to part 2 is 150
 */

public class Day1 {

    private static Direction direction = new Direction();
    private static Point location = new Point(0, 0);
    private static Set<String> visitedLocations = new HashSet<>();

    private String[] moves;
    
    private Day1() {
    	String fileString = MyFileReader.readStringFromFilename("day1.txt");
    	moves = fileString.split(", ");
    }

    public static void main(String[] args) throws IOException {

        Day1 day1part1 = new Day1();
        day1part1.readInstructionsDay1Part1();
        System.out.println(day1part1.howManyBlocksAwayIsSanta());

        Day1 day1part2 = new Day1();
        day1part2.readInstructionsDay1Part2();
        System.out.println(day1part2.howManyBlocksAwayIsSanta());
    }

    private void move(final int stepsToMove) {
        int xPos = location.x;
        int yPos = location.y;

        if (direction.isNorth())
            location = new Point(xPos, yPos + stepsToMove);
        else if (direction.isEast())
            location = new Point(xPos + stepsToMove, yPos);
        else if (direction.isSouth())
            location = new Point(xPos, yPos - stepsToMove);
        else if (direction.isWest())
            location = new Point(xPos - stepsToMove, yPos);
    }

    private void process(final String aMove) {
        if (aMove.charAt(0) == 'R')
            direction.turnRight();
        else
            direction.turnLeft();

        move(valueOf(aMove.substring(1)));
    }

    public void readInstructionsDay1Part1() throws IOException {

        for (String move : moves) {
            process(move);
        }
    }

    public void readInstructionsDay1Part2() throws IOException {

        boolean hqFound = false;

        for (String move : moves) {

            if (!hqFound) {
                process(move);

                String currentLocation = location.toString();

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
}
