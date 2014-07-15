#include <cstdlib>  /* abs */
#include <deque>
#include <stdexcept>
#include <utility>  /* pair */
#include "eulerlib.hpp"
using namespace std;

deque<int> primes;

static bool isPrime(int n) {
 deque<int>::const_iterator iter;
 for (iter = primes.begin(); iter != primes.end(); iter++) {
  int k = *iter;
  if (k*k > n) return true;
  if (n % k == 0) return false;
 }
 return true;
}

static int nextPrime() {
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

PrimeIter::PrimeIter() : iter(primes.begin()) { }

int PrimeIter::next() {
 if (iter == primes.end()) return nextPrime();
 else return *iter++;
}

deque<intpair> factor(int n) {
 deque<intpair> fctrs;
 if (n == 0) {
  fctrs.push_back(intpair(0,1));
  return fctrs;
 }
 if (n < 0) {
  fctrs.push_back(intpair(-1, 1));
  n *= -1;
 }
 PrimeIter ps;
 while (n != 1) {
  int p = ps.next(), k=0;
  while (n % p == 0) {
   n /= p;
   k++;
  }
  if (k>0) fctrs.push_back(intpair(p,k));
 }
 return fctrs;
}

int modInverse(int a, int n) {
 int i = abs(n), h = modulo(a, n), v = 0, d = 1;
 while (h>0) {
  int t = i/h, x=h;
  h = i % x;
  i = x;
  x = d;
  d = v - t*x;
  v = x;
 }
 return modulo(v, n);
}

int modulo(int a, int n) {
 if (n == 0) return a;
 n = abs(n);
 int x = a % n;
 return x < 0 ? x+n : x;
}

int intexp(int x, int y) {
 if (y < 0) throw invalid_argument("intexp: exponent must be nonnegative");
 if (y == 0) return 1;
 int i;
 for (i=1; !(y & i); i <<= 1) x *= x;
 int agg = x;
 for (i <<= 1, x *= x; i <= y; i <<= 1, x *= x)
  if (y & i) agg *= x;
 return agg;
}