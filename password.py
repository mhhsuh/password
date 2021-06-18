password = "a123"
x = 3
while x > 0:		
	key_in = input('please key in your password: ')		
	if key_in == password:
		print('login success')
		break
	else:
		print('login fail, you have', x - 1, ' more time to try')
		x = x - 1



