public class factorial {
    public static int factorialrecursive(int num)
    {
        int answer = -1;  // Variable that will hold final result
        if (num < 0){  // If a negative number is passed in...
            System.out.println("undefined");  // ...the answer is undefined.  Factorials can't be negative
            System.exit(0);  // Close the program
        }
        else if (num == 0)  // If a 0 is passed in...
            return 1;  // ... 0! = 1
        else if(num == 1)  // If a 1 is passed in...
            return num;  // ... 1! = 1
        else
            // Parameter is multiplied by recursive call until a 1 is passed in
            answer = num * factorialrecursive(num-1);
                    return answer;  // Return overall product of recursive calls
    }

    public static int factorialiterarive(int num)
    {
        if (num < 0)  // If a 0 is passed in...
        {
            System.out.println("undefined");  // ...the answer is undefined.  Factorials can't be negative
            System.exit(0);  // Close the program
        }
        int answer = 1;  // Variable that will hold the final result.
        int count = 1;  // Variable used to fill array with numbers that will be multiplied
        int[]faclist = new int[num]; // Create array that will hold numbers to be multiplied

        // Fill the array with numbers 1 through num
        for(int i = 0; i < faclist.length; i++)
        {
            faclist[i] = count;
            count++;
        }

        // Iteratively find the factorial by multiplying every number in the array
        for (int i : faclist) {
            answer = i * answer;
        }
        return answer;  // Return overall product
    }


    public static void main(String[] args) {

        int testnum = factorialrecursive(5);
        int testnum2 = factorialiterarive(5);
        System.out.println(testnum);
        System.out.println(testnum2);
    }

}
