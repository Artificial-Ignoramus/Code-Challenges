def disemvowel( string_ ):
	ans = ""
	
	for ch in string_:
		if ch not in "aeiouAEIOU":
			ans += ch
			
	return ans
