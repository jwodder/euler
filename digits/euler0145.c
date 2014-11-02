/* How many reversible numbers are there below one-billion?
 *
 * Some positive integers $n$ have the property that the sum [ $n$ +
 * reverse($n$) ] consists entirely of odd (decimal) digits.  For instance, 36
 * + 63 = 99 and 409 + 904 = 1313.  We will call such numbers *reversible*; so
 * 36, 63, 409, and 904 are reversible.  Leading zeroes are not allowed in
 * either $n$ or reverse($n$).
 *
 * There are 120 reversible numbers below one-thousand.
 *
 * How many reversible numbers are there below one-billion ($10^9$)?
 */

#include <stdio.h>

int main(void) {
 int qty = 120;
 for (int n=1000; n < 1000000000; n++) {
  if (n % 10 == 0) continue;
  char digits[11];
  int i=n, j=0;
  while (i>0) {
   digits[j++] = i % 10;
   i /= 10;
  }
  char addedDigits[11] = {0};
  _Bool reversible = 1;
  for (int k=0; k<j; k++) {
   char c = digits[k] + digits[j-k-1];
   addedDigits[k] += c % 10;
   if (addedDigits[k] % 2 == 0) {
    reversible = 0;
    break;
   }
   addedDigits[k+1] += c / 10;
  }
  if (reversible && (addedDigits[j] == 0 || addedDigits[j] % 2 == 1)) qty++;
 }
 printf("%d\n", qty);
 return 0;
}
