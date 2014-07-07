#ifndef EULERLIB_H
#define EULERLIB_H

#include <deque>
#include <functional>  /* multiplies */
#include <numeric>  /* accumulate */
#include <utility>
#include <vector>

typedef std::pair<int,int> intpair;

struct PrimeIter {
 std::deque<int>::const_iterator iter;
 PrimeIter();
 int next();
};

std::deque<intpair> factor(int);
int modInverse(int, int);
int modulo(int, int);
int intexp(int, int);

template<class T, class Iter>
T sum(Iter first, Iter last) {
 return std::accumulate<Iter, T>(first, last, T(0));
}

template<class T, class Iter>
T product(Iter first, Iter last) {
 return std::accumulate<Iter, T>(first, last, T(1), std::multiplies<T>());
}

template<class T, class TSeq, class Iter>
std::vector< std::vector<T> > cross(Iter first, Iter last) {
 typename std::vector<TSeq> seqs(first, last);
 std::vector<typename TSeq::const_iterator> pointers(seqs.size());
 int qty = 1;
 for (size_t i=0; i<seqs.size(); i++) {
  pointers[i] = seqs[i].begin();
  qty *= seqs[i].size();
 }
 typename std::vector< std::vector<T> > crossed(qty);
 typename std::vector< std::vector<T> >::iterator outiter;
 for (outiter = crossed.begin(); outiter != crossed.end(); outiter++) {
  *outiter = std::vector<T>(seqs.size());
  for (size_t i=0; i<seqs.size(); i++) (*outiter)[i] = *pointers[i];
  for (int i=seqs.size()-1; i>=0; i--) {
   if (++pointers[i] == seqs[i].end()) pointers[i] = seqs[i].begin();
   else break;
  }
 }
 return crossed;
}

#endif
