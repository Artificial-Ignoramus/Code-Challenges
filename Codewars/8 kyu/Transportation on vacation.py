def rental_car_cost( d ):
	return d * 40 - ( 50 if d > 6 else 20 if d > 2 else 0 )
