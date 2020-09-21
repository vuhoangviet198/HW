package tut1;

import java.util.Scanner;

public class Problem4 {

	public static void main(String[] args) {
		System.out.println("Total sales: ");
		Scanner a = new Scanner(System.in);
		double totalSales = a.nextDouble();
		System.out.println("Profit: " + totalSales*23/100);

	}

}
