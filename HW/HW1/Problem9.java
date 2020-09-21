package tut1;

import java.util.Scanner;

public class Problem9 {

	public static void main(String[] args) {
		System.out.println("Celcius: ");
		Scanner a = new Scanner(System.in);
		double cel = a.nextDouble();
		System.out.println("Fahrenheit: " + ((cel*9.5)+32) );

	}

}
