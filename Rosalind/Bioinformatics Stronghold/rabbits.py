months = {"1":1, "2":1}

def generate_population(n, k):
	for i in range(3, n + 1):
		months[str(i)] = months[str(i-1)] + k * months[str(i-2)]

	print(months.values())
	print(months[str(n)])

generate_population(30, 2)
