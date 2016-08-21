#include <stdio.h>
#include <limits.h>
#include <string.h>

int mem[13][13][4096];

int solve(int n, int *ns, int *ps, int pos, int old2, int old1, int used, int *normalize) {
  if (pos == n) { return 0; }
  if (mem[normalize[old2 + 1]][normalize[old1 + 1]][used] != -1) {
    return mem[normalize[old2 + 1]][normalize[old1 + 1]][used]; }
  int mini = INT_MAX;
  for (int i=0; i < n; i++) {
    if (used & (1 << i)) { continue; }
    int el = ns[i];
    int cost = 0;
    if (old2 >= 0) { cost = (old2 ^ old1 ^ el) * ps[pos]; }
    int val = solve(n, ns, ps, pos + 1, old1, el, used | (1 << i), normalize);
    val += cost;
    if (val >= 0 && val < mini) { mini = val; }
  }
  mem[normalize[old2 + 1]][normalize[old1 + 1]][used] = mini;
  return mini;
}

void norm(int n, int *ns, int *normalize) {
  int count = 1;
  normalize[0] = 0;
  for (int i=0; i < n; i++) {
    int last_occurence = 1;
    for (int j=i + 1; j < n; j++) {
      if (ns[j] == ns[i]) { last_occurence = 0; }
    }
    if (last_occurence) {
      normalize[ns[i] + 1] = count;
      count++;
    }
  }
}

int main() {
  int t, n, ns[12], ps[12];
  scanf("%d", &t);
  for (; t; t--) {
    memset(mem, -1, sizeof mem);
    scanf("%d", &n);
    for (int i=0; i < n; i++) {
      scanf("%d", &ns[i]);
    }
    int normalize[202];
    memset(normalize, -1, sizeof normalize);
    norm(n, ns, normalize);
    for (int i=0; i < n; i++) {
      scanf("%d", &ps[i]);
    }
    printf("%d\n", solve(n, ns, ps, 0, -1, -1, 0, normalize));
  }
  return 0;
}
