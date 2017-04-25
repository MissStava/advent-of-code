package org.shilton;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

/*
 * Answer to part 1 is 95549
 * Answer to part 2 is D87AD
 */
public class Day2 {

	public static void main(String[] args) throws IOException {
		
		List<String> lines = Files.readAllLines(Paths.get("./src/main/resources/file/day2.txt"));
		
		int position = 5;
		String code = "";
		
		for (String line : lines) {
			for (int i = 0; i < line.length(); i++) {
				switch (line.charAt(i)) {
				case 'U':
					if (position != 3 && position != 2 && position != 1)
						position -= 3;
					break;
				case 'L':
					if (position != 7 && position != 4 && position != 1)
						position -= 1;
					break;
				case 'D':
					if (position != 9 && position != 8 && position != 7)
						position += 3;
					break;
				case 'R':
					if (position != 9 && position != 6 && position != 3)
						position += 1;
					break;
				}
			}
			code += position;
		}
		
		System.out.println("code = " + code);
		
		int x = 1;
		int y = 3;
		code = "";
		position = 5;
		                      //0    1    2    3    4    5    6
		char positions[][] = {{'x', 'x', 'x', 'x', 'x', 'x', 'x'}, // 0
							  {'x', 'x', 'x', '1', 'x', 'x', 'x'}, // 1
							  {'x', 'x', '2', '3', '4', 'x', 'x'}, // 2
							  {'x', '5', '6', '7', '8', '9', 'x'}, // 3
							  {'x', 'x', 'A', 'B', 'C', 'x', 'x'}, // 4
							  {'x', 'x', 'x', 'D', 'x', 'x', 'x'}, // 5
							  {'x', 'x', 'x', 'x', 'x', 'x', 'x'}};// 6
		
		for (String line : lines) {
			for (int i = 0; i < line.length(); i++) {			
				switch (line.charAt(i)) {
				case 'U':
					if (positions[y-1][x] != 'x')
						y--;
					break;
				case 'L':
					if (positions[y][x-1] != 'x')
						x--;
					break;
				case 'D':
					if (positions[y+1][x] != 'x')
						y++;
					break;
				case 'R':
					if (positions[y][x+1] != 'x')
						x++;
					break;
				}
			}
			code += positions[y][x];
		}
		
		System.out.println("code = " + code);
		
	}
}
