package tut1;

import java.util.Scanner;

public class Problem8 {

	public static void main(String[] args) {
		System.out.println("Miles: ");
		Scanner a1 = new Scanner(System.in);
		double miles = a1.nextDouble();
		
		System.out.println("Gallons: ");
		Scanner a2 = new Scanner(System.in);
		double gallons = a2.nextDouble();
		System.out.println("MPG: " + miles/gallons);

	}

}
