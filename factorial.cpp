#include <iostream>
using namespace std;

// Function to calculate factorial iteratively
unsigned long long factorialIterative(int n) {
    unsigned long long result = 1;
    for (int i = 1; i <= n; ++i) {
        result *= i;
    }
    return result;
}

// Function to calculate factorial recursively
unsigned long long factorialRecursive(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorialRecursive(n - 1);
}

int main() {
    int num;
    cout << "Enter a number to find its factorial: ";
    cin >> num;

    if (num < 0) {
        cout << "Factorial is not defined for negative numbers." << endl;
    } else {
        cout << "Factorial (Iterative) of " << num << " is: " << factorialIterative(num) << endl;
        cout << "Factorial (Recursive) of " << num << " is: " << factorialRecursive(num) << endl;
    }

    return 0;
}
