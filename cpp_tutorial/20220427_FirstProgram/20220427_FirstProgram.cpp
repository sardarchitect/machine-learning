#include <iostream>

int main() {
	std::cout << "Enter an integer: ";
	
	int num{ };
	std::cin >> num;

	//num = num * 2; //bad solution since we are overwriting user's value
	//int doublenum{ num * 2 }; //okay solution but prefer not to use more memory by creating new variables

	std::cout << "Double your number is " << num * 2 <<'\n'; //preferred solution

	std::cout << "Triple of "<< num << " is " << num * 3 << '\n'; //preferred solution

	return 0;
}

// “You have to write a program once to know how you should have written it the first time.” 
