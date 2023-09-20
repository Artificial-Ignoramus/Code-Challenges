from collections import Counter

def duplicate_encode( word ):
	word = word.lower()
	c = Counter( word )

	return "".join( "(" if c[ch] == 1 else ")" for ch in word )
