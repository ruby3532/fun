# function 函式/功能

# function 是用來收納程式碼的，他只是個功能：寫定義，不會自動執行

def wash(dry=False, water=8):
	print('加水', water, '分滿')
	print('加洗衣精')
	print('旋轉')
	if dry:
		print('烘衣')

wash(True) # 使用 function
wash(False)

def say_hi():
	print('hi')

say_hi()

# 使用參數(類似投幣孔的概念)
def add(x, y):
	print(x + y)

add(3, 4)
add(123, 23)

# 若有預設值
def plus(a=1, b=10):
	print(a + b)
plus(3)

