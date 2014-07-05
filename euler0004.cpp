/* A palindromic number reads the same both ways. The largest palindrome made
 * from the product of two 2-digit numbers is $9009 = 91\times 99$.
 *
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */

/* Note: Assuming the largest palindrome is 6 digits long, it can be shown to
 * be a multiple of 11, and thus at least one of its factors must be a multiple
 * of 11. */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

typedef pair<int,int> intpair;

struct PairCmp {
 bool operator()(const intpair& x, const intpair& y) const {
  return x.first * x.second < y.first * y.second;
 }
};

bool isPalindrome(int n) {
 static char buf[7];
 snprintf(buf, 7, "%d", n);
 size_t len = strlen(buf);
 for (size_t i=0; i<len/2; i++) {
  if (buf[i] != buf[len-i-1]) return false;
 }
 return true;
}

int main(void) {
 priority_queue<intpair, vector<intpair>, PairCmp> nextHeap;
 nextHeap.push(make_pair(990, 999));
 for (;;) {
  intpair x = nextHeap.top();
  if (x.first < 100 || x.second < 100) continue;
  nextHeap.pop();
  int n = x.first * x.second;
  if (isPalindrome(n)) {
   cout << n << endl;
   return 0;
  }
  nextHeap.push(make_pair(x.first - 11, x.second));
  nextHeap.push(make_pair(x.first, x.second - 1));
 }
 return 1;
}
