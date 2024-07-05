import java.util.InputMismatchException;
import java.util.Scanner;  // Program can now accept user input

public class beersong {
    public static void bottles(int num)
    {
        if (num > 99)
            System.out.println("The wall can fit, at most, 99 bottles of beer.");
        else if (num > 2)
        {
            System.out.println(num + " bottles of beer on the wall,");
            System.out.println(num + " bottles of beer,");
            System.out.println("Take one down, pass it around,");
            System.out.println((num-1)+ " bottles of beer on the wall.");
            System.out.println("...");
            bottles(num-1);
        }
        else if (num == 2)
        {
            System.out.println(num + " bottles of beer on the wall,");
            System.out.println(num + " bottles of beer,");
            System.out.println("Take one down, pass it around,");
            System.out.println((num-1)+ " bottle of beer on the wall.");
            System.out.println("...");
            bottles(num-1);
        }
        else if (num == 1)
        {
            System.out.println("1 bottle of beer on the wall,");
            System.out.println("1 bottle of beer,");
            System.out.println("Take one down, pass it around,");
            System.out.println("No more bottles of beer on the wall.");
            System.out.println("...");
            bottles(0);
        }
        else  // If user input is less than 1
        {
            System.out.println("No more bottles of beer on the wall,");
            System.out.println("No more bottles of beer,");
            System.out.println("Go to the store and buy some more,");
            System.out.println("99 bottles of beer on the wall.");
        }
    }

    public static void main(String[] args) {
        int bob;  // Variable that will hold user input
        boolean firsttime = true;
        while (true)  // Program won't leave loop until it reaches a break statement
        {
            Scanner uinput = new Scanner(System.in);  // Scanner object for reading user input
            try
            {
                if (firsttime)  // If this is your first time in the loop
                    System.out.print("How many bottles of beer are on the wall?: ");
                else
                    System.out.print("Please enter an integer: ");  // Prompt the user again
                bob = uinput.nextInt();  // The next integer entered by the user will be saved under this variable
                bottles(bob);
                break;  // If user input is valid, leave the while loop
            }
            catch (InputMismatchException e) {  // If user input is invalid...
                firsttime = false;  //...next time through the loop is not the first time
            }
        }
    }
}
