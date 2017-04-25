package org.shilton;

import static org.assertj.core.api.Assertions.*;

import org.junit.Test;

public class Day2Test {

    @Test public void
    startingPositionIs5() {
        Day2 day = new Day2();
        assertThat(day.getPosition()).isEqualTo(5);
    }

    @Test public void
    positionIs2AfterU() {
        Day2 day = new Day2();
        day.move("U");
        assertThat(day.getPosition()).isEqualTo(2);
    }

    @Test public void
    positionIs4AfterL() {
        Day2 day = new Day2();
        day.move("L");
        assertThat(day.getPosition()).isEqualTo(4);
    }

    @Test public void
    positionIs6AfterR() {
        Day2 day = new Day2();
        day.move("R");
        assertThat(day.getPosition()).isEqualTo(6);
    }

    @Test public void
    positionIs8AfterD() {
        Day2 day = new Day2();
        day.move("D");
        assertThat(day.getPosition()).isEqualTo(8);
    }

    @Test public void
    positionIs2AfterUU() {
        Day2 day = new Day2();
        day.move("U");
        day.move("U");
        assertThat(day.getPosition()).isEqualTo(2);
    }

    @Test public void
    positionIs4AfterLL() {
        Day2 day = new Day2();
        day.move("L");
        day.move("L");
        assertThat(day.getPosition()).isEqualTo(4);
    }

    @Test public void
    positionIs6AfterRR() {
        Day2 day = new Day2();
        day.move("R");
        day.move("R");
        assertThat(day.getPosition()).isEqualTo(6);
    }

    @Test public void
    positionIs8AfterDD() {
        Day2 day = new Day2();
        day.move("D");
        day.move("D");
        assertThat(day.getPosition()).isEqualTo(8);
    }
}
