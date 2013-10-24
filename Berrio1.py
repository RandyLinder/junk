# Exercises Chapter 3

# Programming Exercises

# 1
# Area_Vol.py
# 	A program to calculate surface Area and Volume of a sphere
# by: Alejandro Berrio


def main():
	import math
	print('Hello, this program calculates areas and volumes of spheres.')
	radius = eval(input('What is the radius of the sphere? '))
	Vol = 4/3 * math.pi * radius**3
	Area = 4 * math.pi * radius**2
	print('The Area is', Area, 'and the Volume is ',Vol)


main()


#2
# pizza.py
# 	A program to calculate the cost per square inch of a circular pizza
# by: Alejandro Berrio


def main():
	import math
	print('Hello, this program calculates the cost per square inch of a circular pizza.')
	dia = eval(input('What is the diameter of the pizza? ')) 
	price = eval(input('what is the price of the pizza?'))
	radius = dia / 2
	Area = math.pi * radius**2
	cost = price / Area
	print('The cost of the pizza is', cost, 'dollar per square inch')

main()

# 3
# molweigth.py
# 	A program to calculate the molecular weight of a hydrocarbon
# by: Alejandro Berrio


def main():
	print('Hello, this program calculates the molecular weight of a hydrocarbon.')
	h,c,o = eval(input('How many H, C and O are in the hydrocarbon? '))
	molweight = h*1.0079 + c*12.011 + o*15.9994
	print('The molecular weight of a hydrocarbon is', molweight)


main()


# 4
# distance.py
# 	A program to calculate the distance to a lightning strike
# by: Alejandro Berrio


def main():
	print('Hello, this program calculates the distance to a lightning strike')
	time = eval(input('What is the time (in seconds) elapsed between the ﬂash and the sound of thunder? '))
	dist = time * 1100
	distance = dist / 5280
	print('The distance to a lightning strike is', distance, 'miles')


main()



#5
# coffee.py
# 	A program to calculate the cost of an order of coffee
# by: Alejandro Berrio


def main():
	print('Hello, this program calculates the cost of an order of coffee at $10.50 a pound plus shipping for $0.86 per pound + $1.50 ﬁxed cost for overhead')
	coffee = 10.5
	shipping = 0.86	
	overhead = 1.5
	order = eval(input('How many pounds of coffee do you want to order? '))
	cost = (order * (coffee + shipping + overhead))
	print('the cost of your order is : $',cost)
	
		

main()

#6
# slope.py
# 	A program to calculate the slope of a line 
# by: Alejandro Berrio


def main():
	print('Hello, this program calculates the slope of a line ')
	x1,y1 = eval(input('What are the the coordinates of point 1? '))
	x2,y2 = eval(input('What are the the coordinates of point 2? '))
	slope = (y2 - y1) / (x2 - x1)
	print('The slope of the line is', slope)

main()


#7
# distance.py
# 	A program to calculate the slope of a line 
# by: Alejandro Berrio

def main():
	import math
	print('Hello, this program determines the distance between two points ')
	x1,y1 = eval(input('What are the the coordinates of point 1? '))
	x2,y2 = eval(input('What are the the coordinates of point 2? '))
	distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	print('The distance between the points is', distance)
main()

#8
# epact.py
# 	A program to calculate the epact
# by: Alejandro Berrio

def main():
	print('Hello, this program determines the epact ')
	year = eval(input('What is the year? '))
	C = year // 100
	epact = (8 + (C//4) - C + (((8 * C) + 13)//25) + 11*(year % 19))%30
	print('The epact of the year', year, 'is', epact)
main()


#9
# triangle.py
# 	A program to calculate the area of a triangle
# by: Alejandro Berrio

def main():
	import math
	print('Hello, this program determines the area of a triangle ')
	a,b,c = eval(input('Which are the leghts of the three sides of the triangle? '))
	s = ((a + b + c) / 2)
	area = math.sqrt(s * (s-a) * (s-b) * (s-c))
	print('The area of the triangle is', area)
main()


#10
# ladder.py
# 	A program to calculate the lenght of a ladder
# by: Alejandro Berrio

def main():
	import math
	print('Hello, this program calculates the lenght of a ladder ')
	height,angle = eval(input('Which are the height and angle (degrees) of the ladder? '))
	anglerad = math.pi * angle / 180
	lenght = height / math.sin(anglerad)
	print('The lenght of the ladder is ', lenght)
main()



#11
# natural.py
# 	A program to findthe sum of the first n natural numbers
# by: Alejandro Berrio

def main():
	import math
	print('Hello, this program finds the sum of the first n natural numbers ')
	n = eval(input('Please enter a number? '))
	c = n+1
	x=list(range(1,c))
	sum = math.fsum(x)		
	print('The sum of the first',n,'numbers is ', sum)
main()



#12
# naturalcubes.py
# 	A program to find the sum of the first n natural numbers
# by: Alejandro Berrio

def main():
	print('Hello, this program finds the sum of the cubes of the first n natural numbers ')
	n = eval(input('Please enter a number? '))
	c = n+1
	x=list(range(1,c))
	a= 0
	for i in x:
		q = i**3
		sum = a + q
		a = q
	print('The sum of the first ',n,'cubes is ', sum)
main()

#13
# naturalcubes.py
# 	A program to find the sum of a series entered by the user
# by: Alejandro Berrio

def main():
	import math
	print('Hello, this program finds the sum of the series you enter ')
	n = list(eval(input('Please enter a number series? ')))
	sum = math.fsum(n)
	print('The sum of the series',n,'is ', sum)
main()

#14
# average.py
# 	A program to find the sum of the first n natural numbers
# by: Alejandro Berrio

def main():
	import math
	print('Hello, this program finds the average of the series you enter ')
	n = list(eval(input('Please enter a number series? ')))
	sum = math.fsum(n)
	add = 0
	for i in n:
		add = add + 1
	average = sum / add
	print('The average of the series',n,'is ', average)
main()


#15
# pi.py
# 	A program to find pi using series
# by: Alejandro Berrio

def main():
	import math
	print('Hello, this program finds pi ')
	pi= 0	
	value = 1
	n = eval(input('Please enter a number n? '))
	for i in range(1, n, 2):
		serie = value * (4/i)
		pi = pi + serie
		value = -value
	diff = math.pi - pi
	print('pi equals', pi,' and the accuracy is:', diff)
		
main()

#16
# fibonacci.py
# 	A program to find the fibonacci nth number
# by: Alejandro Berrio

def main():
	print('Hello, this program finds the nth fibonacci ')
	f1 = 1	
	f2 = 1
	n = eval(input('Please enter a number n? '))
	for i in range(2, n):
		f1, f2 = f2, f1 + f2
		print(f1,f2)
	print('the nth Fibonacci number is:', f2)

main()

#17
# sqrt.py
# 	A program to find the square root of x
# by: Alejandro Berrio

def main():
	import math
	print('Hello, this program finds the square root of x')
	x = eval(input('Please enter a number x? '))
	t = eval(input('Please enter a time t to improve the guess? '))
	guess = (x / 2)
	for i in range(1,t+1):
		guess = ((guess + (x / guess)) / 2)
		print(guess)
	sqrt = math.sqrt(x)
	diff = (guess - sqrt)
	print('the square root of:', x,' is:',guess,' and the accuracy is ',diff)


main()


