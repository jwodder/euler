/* Goldbach's other conjecture
 *
 * It was proposed by Christian Goldbach that every odd composite number can be
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

// TODO: Use priority_queue (or whatever it's called) instead of set.

#include <iostream>
#include <set>
#include "eulerlib.hpp"
using std::set;

struct Node {
 PrimeIter* piter;
 int prime, n, val;

 Node(PrimeIter* p) : piter(p), n(0) {val = prime = piter->next(); }

 Node(int p, int m) : piter(NULL), prime(p), n(m), val(p + 2*m*m) { }

 void addNext(set<Node>& queue) const {
  if (piter != NULL) queue.insert(Node(piter));
  queue.insert(Node(prime, n+1));
 }

 bool operator<(const Node& other) const {
  return val < other.val || (val == other.val && (prime < other.prime
   || (prime == other.prime && n < other.n)));
 }
};

int main() {
 PrimeIter piter;
 (void) piter.next();
 set<Node> queue{Node(&piter)};
 int i = 3;
 for (;;) {
  set<Node>::iterator siter = queue.begin();
  Node node = *siter;
  queue.erase(siter);
  if (node.val > i) {
   std::cout << i << std::endl;
   break;
  } else if (node.val == i) {
   i += 2;
  }
  node.addNext(queue);
 }
 return 0;
}
