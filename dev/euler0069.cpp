/* Totient maximum
 *
 * Euler's Totient function, $\varphi(n)$ [sometimes called the phi function],
 * is used to determine the number of numbers less than $n$ which are
 * relatively prime to $n$.  For example, as 1, 2, 4, 5, 7, and 8, are all
 * less than nine and relatively prime to nine, $\varphi(9)=6$.
 *
 * $n$ | Relatively Prime | $\varphi(n)$ | $n/\varphi(n)$
 * ----|------------------|--------------|---------------
 * 2   | 1                | 1            | 2
 * 3   | 1,2              | 2            | 1.5
 * 4   | 1,3              | 2            | 2
 * 5   | 1,2,3,4          | 4            | 1.25
 * 6   | 1,5              | 2            | 3
 * 7   | 1,2,3,4,5,6      | 6            | 1.1666...
 * 8   | 1,3,5,7          | 4            | 2
 * 9   | 1,2,4,5,7,8      | 6            | 1.5
 * 10  | 1,3,7,9          | 4            | 2.5
 *
 * It can be seen that $n=6$ produces a maximum $n/\varphi(n)$ for $n\leq 10$.
 *
 * Find the value of $n\leq 1,000,000$ for which $n/\varphi(n)$ is a
 * maximum.
 */

#include <iostream>
#include <deque>
#include "eulerlib.hpp"
using namespace std;

int main() {
 int maxN = 0;
 double maxRatio = 0;
 for (int n=2; n<=1000000; n++) {
  double ratio = 1.0;
  const deque<intpair> fctrs = factor(n);
  deque<intpair>::const_iterator iter;
  for (iter = fctrs.begin(); iter != fctrs.end(); iter++) {
   ratio *= 1.0 - 1.0/double(iter->first);
  }
  if (ratio > maxRatio) {
   maxRatio = ratio;
   maxN = n;
  }
 }
 cout << maxN << endl;
 return 0;
}
