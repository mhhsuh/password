password = "a123"
x = 3
while x > 0:	
	x = x - 1	
	key_in = input('please key in your password: ')		
	if key_in == password:
		print('login success')
		break
	else:
		print('login fail')
		if x > 0:
			print('you have', x , ' more time to try')
		else:
			print('your account is locked, no further chance')




