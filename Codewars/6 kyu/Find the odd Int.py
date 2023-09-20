from collections import Counter

def find_it( seq ):
	c = Counter( seq )

	for i in c:
		if c[i] % 2 == 1:
			return i
