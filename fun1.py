def add(x, y):
	return x + y

result = add(3, 4)
print(result)

def average(numbers):
	# avg = sum(numbers) / len(numbers)
	return sum(numbers) / len(numbers)

# a = average ([1, 2,3]) # 若沒有回傳就無法將 function 的結果記錄下來
print(average ([1, 2,3]))
print(average ([23, 32, 6]))
print(average ([180, 34, 92]))