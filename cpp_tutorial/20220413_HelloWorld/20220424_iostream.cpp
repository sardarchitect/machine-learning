#include <iostream>  // for std::cout and std::cin

int add(int x, int y);

int main()
{
	std::cout << "Enter two numbers separated by a space: ";

	int x{ }; // define variable x to hold user input (and zero-initialize it)
	int y{ }; // define variable y to hold user input (and zero-initialize it)
	std::cin >> x >> y; // get two numbers and store in variable x and y respectively

	std::cout << "You entered: " << x << " and " << y << '\n';
	std::cout << "Their sum is: " << add(x,y) << '\n';

	return 0;
}