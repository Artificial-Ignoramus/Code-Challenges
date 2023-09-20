def open_or_senior(data):
	return [ "Open" if age < 55 or handicap < 8 else "Senior" for age, handicap in data ]