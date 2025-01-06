import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.Scanner;

public class fibonacciarr {
    public static void fibo(int num)
    {
        if(num < 0){ // If input is negative
            throw new InputMismatchException("e");  // throw an exception so user is prompted again
        }
        else if(num == 0){ //If input is zero/if a sequence has nothing in it
            System.out.println("[]");
            System.exit(0);  // Close program
        }
        // Create an array.  The length of the array is determined by the parameter
        int[]fibseq = new int[num];
        if(num == 1) {  // A fibonacci sequence that is only one element long is 0
            System.out.println("["+0+"]");
            System.exit(0);
        }
        else if(num == 2) { // A fibonacci sequence that is only two elements long is 0 and 1
            System.out.println("["+0 + ", " + 1+"]");
            System.exit(0);
        }
        else {
            // Give the array the first two numbers of the sequence
            fibseq[0] = 0;
            fibseq[1] = 1;
            for (int i = 2; i < fibseq.length; i++) // for the rest of the sequence
            {
                fibseq[i] = fibseq[i - 1] + fibseq[i - 2]; // the next number is the sum of the previous two
            }
            System.out.println(Arrays.toString(fibseq)); //print the fibonacci sequence
        }
    }

    public static void main(String[] args) {

        int uint;  // Variable that will hold user input
        boolean firsttime = true;
        while (true)  // Program won't leave loop until it reaches a break statement
        {
            Scanner uinput = new Scanner(System.in);  // Scanner object for reading user input
            try {
                if (firsttime)  // If this is your first time in the loop
                {
                    System.out.print("How many numbers in this sequence?: ");  // Prompt the user for list length
                } else {
                    System.out.print("Please enter a positive integer: ");  // Prompt the user again
                }
                // The next integer entered by the user will be saved under this variable.
                // Invalid inputs are caught and perpetuate the loop.
                uint = uinput.nextInt();
                fibo(uint);  // Produce a list of fibonacci numbers.  User's input is the length of the list
                break;  // If user input is valid, leave the while loop
            } catch (InputMismatchException e)  // Invalid input is caught here to prevent a crash

            {
                firsttime = false; // Next time through the loop is not the first time
            }
        }
    }
}
