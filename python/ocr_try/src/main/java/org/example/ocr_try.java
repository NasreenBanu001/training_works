package org.example;
import java.io.File ;
import net.sourceforge.tess4j.Tesseract ;
import net.sourceforge.tess4j.TesseractException ;
public class ocr_try {
    public static void main( String[ ] args ) {
        // creating an object of class Tesseract
        Tesseract tesseract = new Tesseract();
        try {
            tesseract.setDatapath("/home/provility/Downloads/Tess4J-3.4.8-src/Tess4J/tessdata");
            // specifying the image that has to be read
            String text = tesseract.doOCR(new File("/home/provility/Downloads/hand-written.png"));
            // printing the text corresponding to the image interpreted
            System.out.print(text);
        } catch (TesseractException e) {
        }
    }}

