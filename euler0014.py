#!/usr/bin/python
r"""Longest Collatz sequence

    The following iterative sequence is defined for the set of positive
    integers:

    \begin{eqnarray*}
    n & \to & n/2 \mbox{ ($n$ is even)} \\
    n & \to & 3n+1 \mbox{ ($n$ is odd)}
    \end{eqnarray*}

    Using the rule above and starting with 13, we generate the following
    sequence:

    $$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$$

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms.  Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    **NOTE:** Once the chain starts the terms are allowed to go above one
    million."""

lengths = {1: 1}
longest = 1
for i in xrange(2, 1000001):
    chain = []
    j = i
    while j not in lengths:
	chain.append(j)
	if j % 2: j = 3*j + 1
	else: j //= 2
    l = lengths[j]
    for k in reversed(chain):
	l += 1
	lengths[k] = l
    if l > lengths[longest]:
	longest = i
print longest
