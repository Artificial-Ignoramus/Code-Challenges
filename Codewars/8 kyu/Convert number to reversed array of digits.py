def digitize( n ):
	if n == 0:
		return [ 0 ]
	
	ans = []
	
	while n > 0:
		ans.append( n % 10 )
		n //= 10
		
	return ans
