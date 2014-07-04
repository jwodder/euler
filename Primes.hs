module Primes where
 primes :: Integral a => [a]
 primes = 2 : filter (isPrime [(p, p*p) | p <- primes]) [3,5..]
  where isPrime ((p,p2):xs) n | p2 > n       = True
			      | mod n p == 0 = False
			      | otherwise    = isPrime xs n
	isPrime [] _ = undefined

 -- |@factor n@ returns a list of pairs of prime factors of @n@ and their
 -- multiplicities/exponents.  If @n@ is @1@, an empty list is returned.  If
 -- @n@ is @0@, @[(0, 1)]@ is returned.  If @n@ is negative, the result is
 -- equal to @(-1, 1) : factor (-n)@.
 --
 -- This function is not recommended for use on large integers.
 factor :: Integral a => a -> [(a, Int)]
 factor = fst . factorWith (2 : [3,5..])

 -- |@factorWith primes n@ decomposes @n@ into a product of powers of elements
 -- of @primes@ (which are assumed to all be coprime and positive) and a
 -- coprime quotient.  Specifically, it returns a pair containing:
 --
 -- * a list of pairs of factors of @n@ in @primes@ and their
 --   multiplicities/exponents, and
 --
 -- * the product of any remaining factors of @n@ that do not appear in
 --   @primes@ (or @1@ if there are none).
 --
 -- If @n@ is @1@, @([], 1)@ is always returned.  If @n@ is @0@, @([(0, 1)],
 -- 1)@ is always returned.  If @n@ is negative, the result equals @(-1, 1) :
 -- factorWith primes (-n)@.
 factorWith :: Integral a => [a] -> a -> ([(a, Int)], a)
 factorWith _ 0 = ([(0,1)], 1)
 factorWith primal n | n < 0 = (-1, 1) &: factor' primal (-n)
		     | n > 0 = factor' primal n
		     | otherwise = error "Provably redundant and unreachable"
  where factor' _  1    = ([], 1)
	factor' [] m    = ([], m)
	factor' (p:q) m | mod m p == 0 = (p, k) &: factor' q x
	 where (k,x) = until (\(_,y) -> mod y p /= 0)
			     (\(j,y) -> (j+1, div y p)) (0, m)
	factor' (_:q) m = factor' q m
	x &: (xs, y) = (x:xs, y)
