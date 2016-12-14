package org.shilton;

import java.awt.*;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

import static java.lang.Integer.valueOf;
import static java.nio.charset.StandardCharsets.UTF_8;
import static java.nio.file.Files.readAllBytes;
import static java.nio.file.Paths.get;

/*
The answer to part 1 is 242
 */

public class Day1b {

    private static Direction direction;
    private static String location;
    private static int xPos = 0;
    private static int yPos = 0;
    private static Set<String> visitedLocations;
    private static boolean locationFound = false;

    public static void main(String[] args) throws IOException {

        direction = Direction.NORTH;
        location = new String();
        visitedLocations = new HashSet<>();

        String fileString = new String(readAllBytes(get("/home/local/IMPELLO/shilton/projects/advent-of-code/2016/day1/src/main/resources/file/day1.txt")), UTF_8);
        String[] moves = fileString.split(", ");

        for (String move : moves) {
            String whichWayToTurn = move.substring(0,1);
            if (whichWayToTurn.equals("R"))
                turnRight();
            else
                turnLeft();

            int spacesToMove = Integer.valueOf(move.substring(1));
            move(spacesToMove);

            if (locationFound)
                break;
        }
    }

    private static void turnLeft() {
        if (direction == Direction.NORTH)
            direction = Direction.WEST;
        else if (direction == Direction.WEST)
            direction = Direction.SOUTH;
        else if (direction == Direction.SOUTH)
            direction = Direction.EAST;
        else if (direction == Direction.EAST)
            direction = Direction.NORTH;
    }

    private static void turnRight() {
        if (direction == Direction.NORTH)
            direction = Direction.EAST;
        else if (direction == Direction.EAST)
            direction = Direction.SOUTH;
        else if (direction == Direction.SOUTH)
            direction = Direction.WEST;
        else if (direction == Direction.WEST)
            direction = Direction.NORTH;
    }

    private static void move(final int stepsToMove) {
        for (int i = 0; i < stepsToMove; i++) {
            if (direction == Direction.NORTH)
                yPos++;
            else if (direction == Direction.EAST)
                xPos++;
            else if (direction == Direction.SOUTH)
                yPos--;
            else if (direction == Direction.WEST)
                xPos--;

            String currentLocation = xPos + "," + yPos;
            if (visitedLocations.contains(currentLocation)) {
                System.out.println("Been to this place twice - " + currentLocation);
                locationFound = true;
                break;
            } else
                visitedLocations.add(currentLocation);
        }
    }

    private enum Direction {
        NORTH,
        EAST,
        SOUTH,
        WEST
    }
}
