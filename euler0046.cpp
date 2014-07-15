/* It was proposed by Christian Goldbach that every odd composite number can be
 * written as the sum of a prime and twice a square.
 *
 * \begin{eqnarray*}
 *  9 & = & 7 + 2\times 1^2 \\
 * 15 & = & 7 + 2\times 2^2 \\
 * 21 & = & 3 + 2\times 3^2 \\
 * 25 & = & 7 + 2\times 3^2 \\
 * 27 & = & 19 + 2\times 2^2 \\
 * 33 & = & 31 + 2\times 1^2
 * \end{eqnarray*}
 *
 * It turns out that the conjecture was false.
 *
 * What is the smallest odd composite that cannot be written as the sum of a
 * prime and twice a square?
 */

#include <iostream>
#include <deque>
#include <vector>
using namespace std;

deque<int> primes;

bool isPrime(int n) {
 deque<int>::const_iterator iter;
 for (iter = primes.begin(); iter != primes.end(); iter++) {
  int k = *iter;
  if (k*k > n) return true;
  if (n % k == 0) return false;
 }
 return true;
}

int nextPrime() {
 if (primes.empty()) {
  primes.push_back(2);
  return 2;
 } else if (primes.size() == 1) {
  primes.push_back(3);
  return 3;
 } else {
  int j = primes.back() + 2;
  while (!isPrime(j)) j += 2;
  primes.push_back(j);
  return j;
 }
}

/** A compressed vector<bool> that only stores values at odd indices */
struct OddVecBool {
 vector<bool> data;
 OddVecBool() : data() { }
 void resizeForMax(int n) {data.resize((n-1)/2+1); }
 void setBit(int i) {data[(i-1)/2] = true; }

 int findFalse(int start, int stop) const {
  start = (start-1)/2;
  stop = (stop-1)/2;
  vector<bool>::const_iterator iter = data.begin() + start;
  for (; start<stop; start++) {
   if (!*iter++) return 2*start+1;
  }
  return -1;
 }
};

int main() {
 (void) nextPrime();
 (void) nextPrime();
 OddVecBool writable;
 writable.resizeForMax(3 + 2*9);
 writable.setBit(3);
 writable.setBit(3 + 2*1);
 writable.setBit(3 + 2*4);
 writable.setBit(3 + 2*9);
 for (;;) {
  int lastPrime = primes.back();
  int pnext = nextPrime();
  writable.resizeForMax(pnext + 2*pnext*pnext);
  writable.setBit(pnext);
  for (int i = 1; i < lastPrime+1; i++) {
   writable.setBit(pnext + 2*i*i);
  }
  deque<int>::const_iterator iter;
  for (iter = primes.begin(); iter != primes.end(); iter++) {
   for (int i = lastPrime+1; i < pnext+1; i++) {
    writable.setBit(*iter + 2*i*i);
   }
  }
  int i = writable.findFalse(lastPrime, pnext);
  if (i != -1) {
   cout << i << endl;
   break;
  }
 }
 return 0;
}