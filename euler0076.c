/* Counting summations
 *
 * It is possible to write five as a sum in exactly six different ways:
 *
 * 4 + 1
 * 3 + 2
 * 3 + 1 + 1
 * 2 + 2 + 1
 * 2 + 1 + 1 + 1
 * 1 + 1 + 1 + 1 + 1
 *
 * How many different ways can one hundred be written as a sum of at least two
 * positive integers?
 */

#include <stdio.h>

int partitionQty(int qty, int mx) {
 /* Returns the number of ways `qty` can be written as a sum of integers each
  * no greater than `mx` */
 if (qty == 0) return 1;
 else {
  int sum = 0;
  for (int i = qty < mx ? qty : mx; i > 0; i--) {
   sum += partitionQty(qty-i, i);
  }
  return sum;
 }
}

int main(void) {
 printf("%d\n", partitionQty(100, 99));
 return 0;
}
