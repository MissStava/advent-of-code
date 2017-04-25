package org.shilton;

public class Day2 {

    private int position = 5;

    public int getPosition() {
        return position;
    }

    public void move(String direction) {
        if (direction.equals("L") && position > 4) {
            position -= 1;
        } else if (direction.equals("R") && position < 6) {
            position += 1;
        } else if (direction.equals("D") && position < 8) {
            position += 3;
        } else if (direction.equals("U") && position > 2){
            position -= 3;
        }
    }
}
