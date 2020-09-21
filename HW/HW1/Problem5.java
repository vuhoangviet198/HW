package tut1;

import java.util.Scanner;

public class Problem5 {

	public static void main(String[] args) {
		System.out.println("Total square feet: ");
		Scanner a = new Scanner(System.in);
		double squareFeet = a.nextDouble();
		System.out.println("Acres: " + squareFeet/43560);

	}

}
