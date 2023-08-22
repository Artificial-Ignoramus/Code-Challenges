from collections import Counter

def scramble( s1, s2 ):
	s1 = Counter( s1 )
	s2 = Counter( s2 )
	
	for ch in s2:
		if ch not in s1 or s2[ch] > s1[ch]:
			return False
		
	return True
