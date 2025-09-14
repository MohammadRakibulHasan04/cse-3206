#include <iostream>

using namespace std;

int main() {
    double num1, num2;
    char operation;
    char choice;

    do {
        // Input
        cout << "Enter first number: "; //the first number
        cin >> num1;

        cout << "Enter an operator (+, -, *, /): "; //second comment 
        cin >> operation;

        cout << "Enter second number: ";
        cin >> num2;

        // Calculation and Output
        switch (operation) {
            case '+':
                cout << "Result: " << num1 + num2 << endl;
                break;
            case '-':
                cout << "Result: " << num1 - num2 << endl;
                break;
            case '*':
                cout << "Result: " << num1 * num2 << endl;
                break;
            case '/':
                if (num2 != 0) {
                    cout << "Result: " << num1 / num2 << endl;
                } else {
                    cout << "Error: Division by zero!" << endl;
                }
                break;
            default:
                cout << "Error: Invalid operator!" << endl;
        }

        // Ask if user wants another calculation
        cout << "Do you want to perform another calculation? (y/n): ";
        cin >> choice;
        cout << endl;

    } while (choice == 'y' || choice == 'Y');

    cout << "Calculator exited. Goodbye!" << endl;

    return 0;
}
