// Your First C++ Program

#include <iostream>
using namespace std;

// function to demonstrate for loop and if statement 
void check_numbers(int a, int b) {
    if (a > b) {
        cout << "The greater number is:" << a << endl;
    } else if (b > a) {
        cout << "The greater number is:" << b << endl;
    } else {
        cout << "The numbers are equal"<< endl;
    }
}
// prints hello world! and another line
int main() {
    cout << "Hello World!"<< endl; //endl breaks the line. sends cursor to the next line.
    cout << "This program uses indexed variables to check if numbers are greater."<< endl;
    cout << "\n"; //another way to make break
    int num_array[] = {1, 2, 3, 4, 5}; //variable assigned to array of numbers to use
    int num_array2[] = {5, 4, 3, 2, 1};
    for (int i = 0; i < 5; i++) { //for loop. initializes counter, what the counter tests, and the update(increments the value of variable 'i' by one or i = i +1)
        check_numbers(num_array[i], num_array2[i]); //indexing the variables so we can use the numbers 
    }
    return 0;
}