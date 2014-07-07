#include <iostream>
#include <deque>
#include <vector>
#include "eulerlib.hpp"
using namespace std;

int I(int n) {
 deque< vector<int> > terms;
 deque<intpair> fctrs = factor(n);
 deque<intpair>::const_iterator iter;
 for (iter = fctrs.begin(); iter != fctrs.end(); iter++) {
  int p = iter->first, k = iter->second;
  int pk = intexp(p,k);
  int coef = n / pk * modInverse(n/pk, pk);
  if (p % 2 == 0 && k>1) {
   vector<int> residues(4, coef);
   residues[1] *= -1;
   residues[2] *= (1 << k-1) - 1;
   residues[3] *= (1 << k-1) + 1;
   terms.push_back(residues);
  } else {
   vector<int> residues(2, coef);
   residues[1] *= -1;
   terms.push_back(residues);
  }
 }
 int max = 0;
 vector< vector<int> > crossed = cross<int, vector<int> >(terms.begin(), terms.end());
 vector< vector<int> >::const_iterator citer;
 for (citer = crossed.begin(); citer != crossed.end(); citer++) {
  int x = sum<int>(citer->begin(), citer->end()) % n;
  if (x != n-1 && x > max) max = x;
 }
 return max;
}

int main() {
 long long accum = 0;
 for (int i=3; i<=20000000; i++) {
  int x = I(i);
  cout << i << '\t' << x << endl;
  accum += x;
 }
 cout << accum << endl;
 return 0;
}
