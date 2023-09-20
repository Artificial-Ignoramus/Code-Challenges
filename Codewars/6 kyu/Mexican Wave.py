def wave( people ):
	ans = []
	len1 = len( people )
	
	for i in range( len1 ):
		if people[i] == " ":
			continue
			
		s = ""
		
		for j in range( len1 ):
			if i == j:
				s += people[j].upper()
			else:
				s += people[j]
				
		ans.append( s )
		
	return ans
