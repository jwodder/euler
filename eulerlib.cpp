#include <cstdlib>  /* abs */
#include <deque>
#include <stdexcept>
#include <utility>  /* pair */
#include "eulerlib.hpp"
using namespace std;

deque<int> primeCache;

bool _isPrime(int n) {
 deque<int>::const_iterator iter;
 for (iter = primeCache.begin(); iter != primeCache.end(); iter++) {
  int k = *iter;
  if (k*k > n) return true;
  if (n % k == 0) return false;
 }
 return true;
}

int nextPrime() {
 if (primeCache.empty()) {
  primeCache.push_back(2);
  return 2;
 } else if (primeCache.size() == 1) {
  primeCache.push_back(3);
  return 3;
 } else {
  int j = primeCache.back() + 2;
  while (!_isPrime(j)) j += 2;
  primeCache.push_back(j);
  return j;
 }
}

PrimeIter::PrimeIter() : iter(primeCache.begin()) { }

int PrimeIter::next() {
 if (iter == primeCache.end()) return nextPrime();
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
  if (p*p > n && n != 1) {
   fctrs.push_back(intpair(n,1));
   break;
  }
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
