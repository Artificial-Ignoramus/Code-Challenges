def queue_time( customers, n ):
	m = len( customers )
	
	if m == 0:
		return 0
	
	if n == 1:
		return sum( customers )
	
	if n >= m:
		return max( customers )
	
	tills = customers[ : n ]
	#ans = max( tills #
		
	for i in range( n, m ):
		tills[ tills.index( min( tills ) ) ] += customers[i]
		
	return max( tills )
