#define a 2
#define b 2
#define EXIT_SUCCESS 0

#include <iostream>
#include <string>

class MyClass {
public:
  MyClass() = default;
  ~MyClass() = default;
  static std::string Hello() { return "world"; }

private:
};

int main(int argc, char *argv[]) {
  auto f = MyClass();
  std::cout << MyClass().Hello() << std::endl << a + b << a / b << std::endl;
  return EXIT_SUCCESS;
}
