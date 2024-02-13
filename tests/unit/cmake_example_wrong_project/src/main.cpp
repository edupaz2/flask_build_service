#include "main.h"

#include <iostream>

/* Commenting on purpose to force the build to fail
MyClass::MyClass() {
  std::cout << "ctor MyClass" << std::endl;
}

MyClass::~MyClass() {
  std::cout << "dtor MyClass" << std::endl;
}
*/

int main(int argc, char** argv) {
  MyClass mc;
  return EXIT_SUCCESS;
}
