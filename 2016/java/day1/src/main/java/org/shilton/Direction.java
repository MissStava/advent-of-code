package org.shilton;

public class Direction {
	
	private Directions direction;
	
	public Direction() {
		direction = Directions.NORTH;
	}
	
	public Directions getDirection() {
		return direction;
	}
	
    public void turnLeft() {
        if (direction == Directions.NORTH)
            direction = Directions.WEST;
        else if (direction == Directions.WEST)
            direction = Directions.SOUTH;
        else if (direction == Directions.SOUTH)
            direction = Directions.EAST;
        else if (direction == Directions.EAST)
            direction = Directions.NORTH;
    }

    public void turnRight() {
        if (direction == Directions.NORTH)
            direction = Directions.EAST;
        else if (direction == Directions.EAST)
            direction = Directions.SOUTH;
        else if (direction == Directions.SOUTH)
            direction = Directions.WEST;
        else if (direction == Directions.WEST)
            direction = Directions.NORTH;
    }
    
    public boolean isNorth() {
    	return direction == Directions.NORTH;
    }
    
    public boolean isEast() {
    	return direction == Directions.EAST;
    }
    
    public boolean isSouth() {
    	return direction == Directions.SOUTH;
    }
    
    public boolean isWest() {
    	return direction == Directions.WEST;
    }
	
	private enum Directions {
		NORTH,
	    EAST,
	    SOUTH,
	    WEST
	}
}
