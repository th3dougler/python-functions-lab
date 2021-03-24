""" # 1 - 1

def pokemon_contains(incoming_letter):
	if incoming_letter in "pokemon":
		return True
	else:
		return False

result1 = pokemon_contains('k')
print(result1)
result1 = pokemon_contains('o')
print(result1)

# 1 - 2
def sum_two(a,b):
	answer = a + b
	return answer

a= 3
b= 4	
result3 = sum_two(a,b)
print(result3)
result4 = sum_two(5,6)
print(result4)

# 1 - 3
def multiply(num1,num2):
    return a*b

result5 = multiply(10,10)
print(result5)
result6 = multiply(5,6)
print(result6)

# 1 - 4
# 1) Lets Multiply Stuff
# 2) The Answer is... 30
def multiplication(a,b):
	my_answer = a*b
	print("Calculating...")
	return my_answer

print("Let's Multiply stuff...")
answer = multiply(5,6)
answer = str(answer)
print("The answer is..." + answer)

# 1 - 5
def subtract(foo, bar): return foo - bar

print( subtract(10,9) )
print( subtract(4,1) )
print( subtract(6,3))
print( subtract(-4,-11) )

# 1 - 6
def greater_than_5(foo): return True if foo > 5 else False

print ( greater_than_5(5) )
print ( greater_than_5(4) )
print ( greater_than_5(6) )
 """
 
 # 2 - 1
def sum_to(num):
    # sum of a range is equal to total numbers * average between first and last number 
    return num*(num+1)/2
print (sum_to(4))

# 2 - 2
def largest(num):    return max(num)

print(largest([10,4,2,231,91,54]))

# 2 - 3
def occurances(str, char):
    return str.count(char)

print (occurances("apple", 'p'))

# 2 - 4
def product(*args):
    result = 0
    for idx,num in enumerate(args):
            result = num if idx == 0 else result * num
    return result
    
print (product(1,2,3,4,5))