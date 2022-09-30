#include <iostream>

int main() {
	//STATIC ARRAYS
	int intStaticArray1[5] = {1,2,3,4,5};

	int intStaticArray2[4];
	intStaticArray2[0] = 100;
	intStaticArray2[1] = 200;
	intStaticArray2[2] = 300;
	intStaticArray2[3] = 400;

	for (int i = 0; i < 5; i++) {
		std::cout << intStaticArray1[i] <<std::endl;
	}

	//LINKED LIST
	

	return 0;
}