#include "io.h"
#include <iostream>

int readNumber() {
	std::cout << "Enter number: ";
	int x{};
	std::cin >> x;
	return x;
}

void writeAnswer(int ans) {
	std::cout << "Answer is " << ans << "\n";
}