##1.

#sphere_area_vol.py
#script to calculate the area and volume of a sphere
import math
def main():
    print('This script calculates the area and volume of a sphere')
    radius = eval(input("Enter the radius: "))
    pi = math.pi
    volume = 4/3*pi*radius**3
    area = 4*pi*radius**2
    print('area: {}'.format(area))
    print('volume: {}'.format(volume)) 
    print("This is just for showing version control")
main()


##2.

#price_pizza.py
import math
def main():
    print('This script calculates price per square inch of a pizza')
    radius = eval(input("Enter the diameter: "))/2
    cost = eval(input("Enter the price: "))
    pi = math.pi
    area = pi*radius**2
    per_square = cost/area
    print(per_square)
                                    
main()

##3.

import math
def main():
    print('This calculates the molecular mass of a hydrocarbon')
    H = eval(input("Enter the number of hydrogen atoms "))*1.0079
    C = eval(input("Enter the number of carbon atoms "))*12.011
    O = eval(input("Enter the number of oxygen atoms "))*15.9994
    mass_list = [H,C,O]
    total = sum(mass_list)
    print("The mass of the molecule is {}".format(total))
                             
main()


##4.
import math
def main():
    print('This calculates the distance of a lighting strike')
    time = eval(input("Enter the time between flash and report "))
    distance = 1100*time / 5280
    print('the lighting struck {} miles away'.format(distance))

main()

##5.
import math
def main():
	print('This calculates the price of a coffe shipment')
    mass = eval(input("Enter the weight of the order "))
    cost = 1.5 + 11.36*mass
    print("The cost is {}".format(cost))

main()


##6.

import math
def main():
	print('This script returns the slope of the line between two points')
    x1 = eval(input("Enter an X coordinate "))
    y1 = eval(input("Enter an Y coordinate "))
    x2 = eval(input("Enter an X coordinate "))
    y2 = eval(input("Enter an Y coordinate "))
    slope = (y2 - y1) / (x2 = x1)
    print("The slope is {}".format(slope))

main()


##7

import math
def main():
	print('This script returns the distance of the line between two points')
    x1 = eval(input("Enter an X coordinate "))
    y1 = eval(input("Enter an Y coordinate "))
    x2 = eval(input("Enter an X coordinate "))
    y2 = eval(input("Enter an Y coordinate "))
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("The distance is {}".format(slope))

main()


##8.

import math
def main():
	print('This script returns the Gregorian epact for a year')
	year = eval(input("Enter an four digit year "))
	c = year//100
	epact = (8 + (c//4) - c + ((8*c + 13)//25) + 11*(year%19))%30
    print("The epact for year {} is {}".format(year, epact))

main()



##9.
def main():
	print('This script returns the area of a triangle')
	
	##get the side lengths
	
    a = eval(input("Enter length of first side "))
    b = eval(input("Enter length of second side "))
    c = eval(input("Enter length of third side "))
    
    ##perform area calculation
    
    s = (a+b+c)/2
    A = sqrt(s*(s-a)*(s-b)*(s-c))
    print('The area is {}'.format(A))
    
    
##10
def main():
	print('This script determines the length a ladder needed to reach a point on a wall')
    height = eval(input("Enter height of point on wall "))
    angle = eval(input("Enter the angle the ladder leans at "))
    length = height/(sin(angle))
    print('Length of ladder needed is {}'.format(length))
    

##11

import math
def main():
    print('This script returns the sum of the first natural numbers up to a given value')
    n = eval(input("Enter the nth natural number "))
    
    ##build a series of the numbers
    
    num_list = list(range(1,(n+1)))
    answer = sum(num_list)
    print('the sum is {}'.format(answer))
    
main()

##12

import math
def main():
    print('This script returns the sum of cubes of the first natural numbers up to a given value')
    n = eval(input("Enter the nth natural number "))
    
    ##build a series of the numbers
    
    num_list = list(range(1,(n+1)))
    print(num_list)
    answer = 0
    for i in num_list:
        answer += i**3
    print('the sum is {}'.format(answer))
    
main()


##13

import math
def main():
    print('This script sums a given set of numbers')
    n = eval(input("Enter the how many numbers you'll wanna sum "))
    num_list = []
    for i in range(n):
        x = eval(input("Enter a number "))
        num_list.append(x)
    print('the sum is {}'.format(sum(num_list)))
    
main()

##14
#average.py
#This script averages a series of numbers
import math
def main():
	print('This script averages a set of numbers supplied by the user')
	n = eval(input("Eneter how many numbers you would like to average")
	numbers = []
	for i in range(n):
		x = eval(input("Please enter a number")
		numbers.append(x)
	
main()

##15

##pi_estimator.py

import math
print("This script estimates pi with user-supplied precision")
def main():
	
	##get user input
	
	n = eval(input("Enter the number of iterations you wish to use"))
	fractions = []
	
	##main loop to assemble fractions to sum
	
	for i in range(0,n):
		x = n + 1
		fractions.append(4/x)
		
	##sum the fractions
		
	pi_estimate = sum(fractions)
	
	##print results
	
	print("Estimate of pi = {}".format(pi_estimate))
	difference = math.pi - pi_estimate
	print("Difference bewteen math.pi and estimate = {}".format(difference))
	

##16
#Fibanacci.py
#This script computes the nth Fibanacci number

import math
print("This script estimates pi with user-supplied precision")
def main():
	
	#get user input
	
    n = eval(input("Enter the number of iterations you wish to use "))
    
    #set up variables to begin iterating
    
    f_numbers = [1]
    p1 = 1
    p2 = 0
    
    #loop for user supplied n
    
    for i in range(n-1):
            x = p1+p2
            f_numbers.append(x)
            p2 = p1
            p1 = x
    
    ##print results
    
    print("The F number is {}".format(x))
main()


##17
#square_root.py
#This script estimates the square root of a given number

import math
print("This script estimates the square root of a given number")
def main(start_guess):
	
	#get user input
	
    x = eval(input("Enter the number you want to estimate square root of "))
    iterations = eval(input("Enter the number of iterations you wish to use "))
    
    #assign first guess based on argument passed to main function
    
    guess = (start_guess + (x/start_guess))/2
    
    #iterate
    
    for i in range(iterations):
        guess = (guess + (x/guess))/2
    difference = abs(math.sqrt(x) - guess)
    
    #print results
    
    print("Estimated square root of {} is {}".format(x, guess))
    print("Difference from math.sqrt estimate is {}".format(difference))

main(2)
		

		


