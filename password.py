password = "a123"
x = 0
x = int(x)
while True:	
	if x < 3:
		key_in = input('please key in your password: ')		
		if key_in == 'a123':
			print('login success')
			break
		else:
			y = 2 - x
			print('login fail, you have', y, ' more time to try')
			x = x + 1
	else:
		break


