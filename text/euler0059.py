#!/usr/bin/python
"""XOR decryption

   Each character on a computer is assigned a unique code and the preferred
   standard is ASCII (American Standard Code for Information Interchange).  For
   example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

   A modern encryption method is to take a text file, convert the bytes to
   ASCII, then XOR each byte with a given value, taken from a secret key.  The
   advantage with the XOR function is that using the same encryption key on the
   cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107
   XOR 42 = 65.

   For unbreakable encryption, the key is the same length as the plain text
   message, and the key is made up of random bytes.  The user would keep the
   encrypted message and the encryption key in different locations, and without
   both "halves", it is impossible to decrypt the message.

   Unfortunately, this method is impractical for most users, so the modified
   method is to use a password as a key.  If the password is shorter than the
   message, which is likely, the key is repeated cyclically throughout the
   message.  The balance for this method is using a sufficiently long password
   key for security, but short enough to be memorable.

   Your task has been made easy, as the encryption key consists of three lower
   case characters.  Using `cipher1.txt` (right click and 'Save Link/Target
   As...'), a file containing the encrypted ASCII codes, and the knowledge that
   the plain text must contain common English words, decrypt the message and
   find the sum of the ASCII values in the original text."""

from __future__ import with_statement
from itertools  import cycle
from string     import ascii_letters, digits

with open('../data/cipher1.txt') as fp:
    bytes = map(int, fp.read().split(','))

acceptable = map(ord, ascii_letters + digits + " .,();!'")
# The value for `acceptable` was found by first calculating the possible
# decrypted texts that consisted of printable ASCII, manually inspecting them
# to find the correct decrypted text, and identifying the non-letters used.

lowercase = range(ord('a'), ord('z')+1)
passchars = (lowercase[:], lowercase[:], lowercase[:])
indices = [0, 0, 0]
while True:
    abc = tuple(arg[i] for (arg, i) in zip(passchars, indices))
    accum = 0
    for (i, (byte, passc)) in enumerate(zip(bytes, cycle(abc))):
	byte ^= passc
	#if 0x20 <= byte <= 0x7E: accum += byte
	if byte in acceptable: accum += byte
	else:
	    i %= 3
	    passchars[i].remove(passc)
	    for j in range(i+1, 3):
		indices[j] = len(passchars[j])
	    indices[i] -= 1
	    break
    else:
	#print ''.join(map(chr, abc))
	#print ''.join(chr(b^p) for (b,p) in zip(bytes, cycle(abc)))
	print accum
	break
    for i in range(len(indices)-1, -1, -1):
	indices[i] += 1
	if indices[i] >= len(passchars[i]):
	    indices[i] = 0
	else:
	    break
    else:
	break
