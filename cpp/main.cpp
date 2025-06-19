#include <iostream>
#include <cmath>

using namespace std;
/*
 * Assignment 2 Guidelines:
 * For this assignment you are to implement a program that processes
 * a sequence of floating point values input by a user,
 * and then outputs the following statistics:
 * "	The number of values that were input
 * "	The sum of the values
 * "	The average of the values
 * "	The number of negative values
 * "	The largest/maximum value that was input
 * "	The smallest/minimum value that was input
 *
 * The program should begin by prompting the user to input a value.
 * Once that value has been processed appropriately,
 * the program should repeatedly ask the user if there is another value to be processed.
 * Each time the user responds in the affirmative
 * by inputting the letter "Y" (uppercase or lowercase)
 * the program should prompt the user to input another value, and process that value.
 *
 * Once the user responds in the negative, by inputting the letter "N" (uppercase or lowercase)
 * the program should output the set of statistics listed above, and then terminate.
 *
 * Your program output, which consists of the various prompts and the generated statistics,
 * should be presented in a very user-friendly way.
 *
 * I will supply you with data shortly before the assignment is due.
 * This data should be used for your assignment submission.
 * Prior to the receipt of this data, you should use your own data to test your code.
 *
 * In implementing and submitting this assignment you should
 * follow the programming guidelines that I have provided.
 *
 * Due Date: March 22, 2018
 *
 */


int main() {
    // var declaration
    int EntryCounter, negNumCounter;
    double numberInput, sumNum, maximumNum, minimumNum;
    char userDecision;

    // var initialized
    EntryCounter = negNumCounter = 0;

    // Post
    do{
        cout << "Please enter your number here: ";
        cin >> numberInput;
        if (numberInput < 0)
            negNumCounter++;
        sumNum += numberInput;
        maximumNum=(numberInput>maximumNum)?numberInput:maximumNum;
        minimumNum=(numberInput<minimumNum)?numberInput:minimumNum;

        cout << "Would you like to enter another number? ";
        cin >> userDecision;

        EntryCounter++;
    }while(userDecision == 'Y' || userDecision == 'y');
    // output results to the user.
    cout << "\n\nYou entered: " << EntryCounter << " inputs." << endl;
    cout << "Sum of the values you entered: " << sumNum << endl;
    cout << "Average of the values you entered: " << sumNum/EntryCounter << endl;
    cout << "Maximum or Largest Number: " << maximumNum << endl;
    cout << "Minimum or Smallest Number: " << minimumNum << endl;
    cout << "You have entered: " << negNumCounter << " negative numbers." << endl;


    return 0;
}

/*
Please enter your number here: 20
Would you like to enter another number? y
Please enter your number here: -23
Would you like to enter another number? y
Please enter your number here: 500.56
Would you like to enter another number? y
Please enter your number here: -342.2
Would you like to enter another number? y
Please enter your number here: 9
Would you like to enter another number? y
Please enter your number here: 70
Would you like to enter another number? y
Please enter your number here: -56
Would you like to enter another number? y
Please enter your number here: -99
Would you like to enter another number? n


You entered: 8 inputs.
Sum of the values you entered: 79.36
Average of the values you entered: 9.92
Maximum or Largest Number: 500.56
Minimum or Smallest Number: -342.2
You have entered: 4 negative numbers.
 */