#define a 2
#define b 2
#define EXIT_SUCCESS 0

#include <stdio.h>

int main(int argc, char *argv[]) {
  printf("%i", a + b);
  printf("%i", a / b);
  return EXIT_SUCCESS;
}
