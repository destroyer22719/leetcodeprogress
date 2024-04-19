#include <stdio.h>
#include <stdbool.h>

bool is_between(const void *e) {
	int *val = (int *)e;
	return *val >= 0 && *val <= 11;
}

int main() {

  printf("%ld", sizeof(char));
}