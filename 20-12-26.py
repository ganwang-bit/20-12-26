>>> L1=[3,2,1,6,5,9]
>>> for index, i in enumerate(L1):
	print(index, i)

	
0 3
1 2
2 1
3 6
4 5
5 9
>>> de out(x):
	
SyntaxError: invalid syntax
>>> def out(x):
	y=5
	def in():
		
SyntaxError: invalid syntax
>>> def out(x):
	y=5
	def inner():
		n=x+y
		print("n={0}".format(n))
	return inner

>>> r=out(1)
>>> r()
n=6
>>> 
