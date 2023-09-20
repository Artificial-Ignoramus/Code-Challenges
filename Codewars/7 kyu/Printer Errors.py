def printer_error(s):
	count = 0
	
	for ch in s:
		if ch not in "abcdefghijklm":
			count += 1
			
	return str( count ) + "/" + str( len( s ) )
