package tut1;

import java.util.Scanner;

public class Problem7 {

	public static void main(String[] args) {
		System.out.println("Amount of the purchase: ");
		Scanner a = new Scanner(System.in);
		double amount = a.nextDouble();
		double stateSalesTax = amount*5/100;
		double countySalesTax = amount*2.5/100;
		double totalSalesTax = stateSalesTax + countySalesTax;
		double totalOfTheSale = amount + totalSalesTax;
		
		System.out.println("Amount of the purchase: " + amount);
		System.out.println("State sales tax: " + stateSalesTax);
		System.out.println("County sales tax: " + countySalesTax);
		System.out.println("Total sales tax: " + totalSalesTax);
		System.out.println("Total of the sale: " + totalOfTheSale);

	}

}
