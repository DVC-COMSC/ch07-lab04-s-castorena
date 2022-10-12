
# ******************************
# Make your Code
# ******************************
import random

numbers1 = []
numbers2 = []
result = []
for i in range(10):
	numbers1.append(random.randint(0,100))
	numbers2.append(random.randint(0,100))

for i in range(len(numbers1)):
		result.append(numbers1[i] + numbers2[i])

print (numbers1)
print (numbers2)
print (result)
