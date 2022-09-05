#include <string>
#include <iostream>

double getDouble() {
	std::cout << "Enter a double value: ";
	double x{};
	std::cin >> x;
	return x;
}

char getOperator() {
	std::cout << "Enter one of the following: +, -, *, or /: ";
	char x{};
	std::cin >> x;
	return x;
}

double printResult(double x, double y, char z) {
	if (z == '+') {
		return x + y;
	}
	else if (z == '-') {
		return x - y;
	}
	else if (z == '*') {
		return x * y;
	}
	else if (z == '/') {
		return x / y;
	}
	else {
		std::cout << "Invalid operator entered. Only enter one of the following mathematical symbols: +, -, *, or /";
		return 0;
	}
}

int quiz1() {
	/*
	Write the following program: The user is asked to enter 2 floating point numbers (use doubles).
	The user is then asked to enter one of the following mathematical symbols: +, -, *, or /.
	The program computes the answer on the two numbers the user entered and prints the results.
	If the user enters an invalid symbol, the program should print nothing.

	Example of program:

		Enter a double value: 6.2
		Enter a double value: 5
		Enter one of the following: +, -, *, or /: *
		6.2 * 5 is 31
	*/
	double a{ getDouble() };
	double b{ getDouble() };
	char o{ getOperator() };
	double result{ printResult(a,b,o) };

	std::cout << a << o << b << " is " << result;

	return 0;
}

double getTowerHeight() {
	std::cout << "Enter height of tower in meters: ";
	double towerHeight{};
	std::cin >> towerHeight;
	return towerHeight;
}

void heightOfBallAtTimeX(double towerHeight, int sec) {
	constexpr double gravityConstant{ 9.8 };
	double distanceFallen{ (gravityConstant * (sec * sec)) / 2.0};

	if (distanceFallen >= towerHeight) {
		std::cout << "At " << sec << " seconds, the ball is on the ground. \n";
	} else {
		std::cout << "At " << sec << " seconds, the ball is at height: " << towerHeight - distanceFallen << " meters\n";
	}
	double ballHeight = towerHeight - distanceFallen;
}

int quiz2() {
	/*
	Write a short program to simulate a ball being dropped off of a tower.
	To start, the user should be asked for the height of the tower in meters.
	Assume normal gravity (9.8 m/s2), and that the ball has no initial velocity (the ball is not moving to start).
	Have the program output the height of the ball above the ground after 0, 1, 2, 3, 4, and 5 seconds.
	The ball should not go underneath the ground (height 0).

	Use a function to calculate the height of the ball after x seconds.
	The function can calculate how far the ball has fallen after x seconds using the following formula:
		distance fallen = gravity_constant * x_seconds2 / 2

	Desired output:

	Enter the height of the tower in meters: 100
	At 0 seconds, the ball is at height: 100 meters
	At 1 seconds, the ball is at height: 95.1 meters
	At 2 seconds, the ball is at height: 80.4 meters
	At 3 seconds, the ball is at height: 55.9 meters
	At 4 seconds, the ball is at height: 21.6 meters
	At 5 seconds, the ball is on the ground.

	Note: Depending on the height of the tower, the ball may not reach the ground in 5 seconds -- that’s okay. We’ll improve this program once we’ve covered loops.
	Note: The ^ symbol isn’t an exponent in C++. Implement the formula using multiplication instead of exponentiation.
	Note: Remember to use double literals for doubles, eg. 2.0 rather than 2.
	*/

	const double towerHeight{ getTowerHeight() };

	heightOfBallAtTimeX(towerHeight, 0);
	heightOfBallAtTimeX(towerHeight, 1);
	heightOfBallAtTimeX(towerHeight, 2);
	heightOfBallAtTimeX(towerHeight, 3);
	heightOfBallAtTimeX(towerHeight, 4);
	heightOfBallAtTimeX(towerHeight, 5);

	return 0;
}

int main() {
	//quiz1();
	quiz2();
	return 0;
}