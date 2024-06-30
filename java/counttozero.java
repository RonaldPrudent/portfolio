import java.util.InputMismatchException;
import java.util.Scanner;
import static java.lang.Math.abs;

public class counttozero {

    public static void ctz(int num)
    {
        int[]ctzlist = new int[abs(num)+1];  //An array for holding descending (or ascending) numbers
        int i = 0;  // Variable for iterating through array to fill it with numbers
        if (num<0)  // If user input is less than zero
        {
            while (num<1)  // loop until count reaches zero
            {
                ctzlist[i] = num; // put number in this array index
                i++;  // move up to the next array index
                num++;  // get one number closer to zero
            }
        }
        else  // If user input is greater than (or equal to) zero
        {
            while (num>-1)  // loop until count reaches zero
            {
                ctzlist[i] = num;
                i++;
                num--;
            }
        }
        for (int j : ctzlist) {  // For every index in the array
            System.out.print(j + " "); // print the number
        }
    }

    public static void main(String[] args){
        int uint;  // Variable that will hold user input
        boolean firsttime = true;
        while (true)  // Program won't leave loop until it reaches a break statement
        {
            Scanner uinput = new Scanner(System.in);  // Scanner object for reading user input
            try
            {
                if (firsttime)  // If this is your first time in the loop
                    System.out.print("Begin countdown from what number?: ");
                else
                    System.out.print("Please enter an integer: ");
                uint = uinput.nextInt();  // user input is saved in this variable
                ctz(uint); // Call method that counts to zero
                break; // escape loop if input is valid
            }
            catch (InputMismatchException e) {  // if input is invalid
                firsttime = false;  // The next time through the loop is not the first
            }
        }
    }
}
