midterms=[80,91,78]
finals=[54,89,90]
students=["dan","rock","shyam"]
final_grades={t[0]:max(t[1],t[2]) for t in zip(students,finals,midterms)}
final_grades=dict(
		zip(
			students,
			map(
				lambda pair:max(pair),
				zip(midterms,finals)
				)
			)
		)
avg_grades=dict(
		zip(
			students,
			map(
				lambda pair:(( pair[0]+pair[1])/2),
				zip(midterms,finals)
				)
			)
		)