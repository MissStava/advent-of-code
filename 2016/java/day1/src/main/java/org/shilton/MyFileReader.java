package org.shilton;

import java.io.IOException;

import static java.nio.charset.StandardCharsets.UTF_8;
import static java.nio.file.Files.readAllBytes;
import static java.nio.file.Paths.get;

public class MyFileReader {

    public static String readStringFromFilename(final String filename) {

    	String fileString = "";
    	try {
			fileString = new String(readAllBytes(get("./src/main/resources/file/" + filename)), UTF_8);
		} catch (IOException e) {
			e.printStackTrace();
		}
    	return fileString;
    }
}
