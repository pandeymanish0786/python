import sys
list_comp=sys.getsizeof([x*10 for x in range(1000)])
gen_exp=sys.getsizeof([x*10 for x in range(1000)])
print("to do the same thing,it takes....  ")
print(f"list comprehension {list_comp} bytes")
print(f"generator_expression {gen_exp} bytes")
