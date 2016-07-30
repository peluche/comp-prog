#include <stdio.h>

int divisors[10000002];

void sieve_ish(int n, int divisors[]) {
  for (int i = 1; i < n; i++) {
    if (divisors[i] < 4) {
      for (int j = i; j < n; j += i) {divisors[j]++;}
    }
  }
}

int main() {
  int t, n;
  sieve_ish(10000002, divisors);
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    scanf("%d", &n);
    if (divisors[n] < 4) {printf("NO\n");}
    else {printf("YES\n");}
  }
  return 0;
}
