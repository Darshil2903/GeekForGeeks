# def listmaking():
# 	us=True
# 	while us==True:
# 		print('>>press "q " to quit')
# 		user=input("Enter the number  :")
		
# 		if "q" in user:
# 			break

# 		else:
# 			B.append(int(user))


# def change(pos1,pos2):ERR
# 	f1=li.pop(pos1-1)
# 	f2=li.pop(pos2-2)
# 	li.insert(pos2-2,f1)
# 	li.insert(pos1-1,f2)
# 	print(li)R

# li = [1,2,3,4,5,6,7,8]
# pos1= int(input("enter the 1 positin : "))
# pos2= int(input("enter the 2 position : "))
# change(pos1,pos2)

                    # ************** this above program is to change the number in list ****************


     
# li=[]

# lis=True
# while lis==True:
# 	you=int(input("enter the number and to quit press 000: "))
# 	if you ==000:
# 		lis=False

# 	else:
# 		li.append(you)


# pos1=len(li)-1
# pos2=0

# f1=li.pop(pos1)
# f2=li.pop(pos2)

# li.append(f2)
# li.insert(0,f1)
# print(li)

# ******************************** this above program will change the last digit of list to first and first digit to last******************************




# li=[]

# lis=True
# while lis==True:
# 	you=int(input("enter the number and to quit press 000: "))
# 	if you ==000:
# 		lis=False

# 	else:
# 		li.append(you)

# for i in range(len(li)):
# 	f=li.pop(len(li)-1)
# 	li.insert(i,f)
		
# print(li)	


# *****************************************above program will reverse the list there is another way t do which is given below ****************************************


# li=[]

# lis=True
# while lis==True:
# 	you=int(input("enter the number and to quit press 000: "))
# 	if you ==000:
# 		lis=False

# 	else:
# 		li.append(you)


# li.reverse()
# print(li)

# *********************************the another way to reverse the list**********************************************



		



##############################################   GEEKS FOR GEEKS QUESTION  ############################################






# Given two arrays a[] and b[] respectively of size n and m, the task is to print the count of elements in the intersection (or common elements) of the two arrays.

# For this question, the intersection of two arrays can be defined as the set containing distinct common elements between the two arrays. 

# Example 1:

# Input:
# n = 5, m = 3
# a[] = {89, 24, 75, 11, 23}
# b[] = {89, 2, 4}

# Output: 1

# Explanation: 
# 89 is the only element 
# in the intersection of two arrays.
# Example 2:

# Input:
# n = 6, m = 5
# a[] = {1, 2, 3, 4, 5, 6}
# b[] = {3, 4, 5, 6, 7} 

# Output: 4

# Explanation: 
# 3 4 5 and 6 are the elements 
# in the intersection of two arrays.
# Your Task:



# li1=[]
# li2=[]
# lis=True

# while lis==True:
# 	you=int(input("enter the number for 1 list and to quit press 000: "))
# 	if you ==000:
# 		lis=False

# 	else:
# 		li1.append(you)

# liss=True
# while liss==True:
# 	your=int(input("enter the number for 2 list and to quit press 000: "))
# 	if your ==000:
# 		liss=False

# 	else:
# 		li2.append(your)

	
# count=0
# for i in range(len(li2)):
# 	for j in range(len(li1)):
# 		if li2[i]==li1[j]:
# 			count+=1


# print(count)


############################################   above program is to solve the geeks for geeks problem which is writen above   ################################################## 



########################################### GEEKS FOR GEEKS QUESTION #############################################################


# Given an array A[] of N integers and an integer X. The task is to find the sum of three integers in A[] such that it is closest to X.


# Example 1:

# Input:
# N = 4
# A[] = {-1 , 2, 1, -4}
# X = 1
# Output: 2
# Explaination: 
# Sums of triplets:
# (-1) + 2 + 1 = 2
# (-1) + 2 + (-4) = -3
# 2 + 1 + (-4) = -1
# 2 is closest to 1.

# Example 2:

# Input:
# N = 5
# A[] = {1, 2, 3, 4, -5}
# X = 10
# Output: 9
# Explaination: 
# Sums of triplets:
# 1 + 2 + 3 = 6
# 2 + 3 + 4 = 9
# 1 + 3 + 4 = 7
# ...
# 9 is closest to 10.


# lis=[3,4,8,7,-9]
# lis2=lis
# lis3=lis


# x= int(input("enter the number for which you are finding the closest sum : "))
# a=lis3.index(x)
# lis.pop(a)
# b=0

# clas=True
# while clas== True:

# 	for i in lis:
# 		for j in lis2:
# 			for k in lis3:
# 				l=i+j+k
# 				if l>b:
# 					b=l



# print(b)
	



# **************************************************GEEKS FOR GEEKS****************************************************

# Given an array arr of n elements which is first increasing and then may be decreasing, find the maximum element in the array.
# Note: If the array is increasing then just print then last element will be the maximum value.

# Example 1:

# Input: 
# n = 9
# arr[] = {1,15,25,45,42,21,17,12,11}
# Output: 45
# Explanation: Maximum element is 45.
# Example 2:

# Input: 
# n = 5
# arr[] = {1, 45, 47, 50, 5}
# Output: 50
# Explanation: Maximum element is 50.
# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function findMaximum() which takes the array arr[], and n as parameters and returns an integer denoting the answer.

# Expected Time Complexity: O(logn)
# Expected Auxiliary Space: O(1)

# Constraints:
# 3 ≤ n ≤ 106
# 1 ≤ arri ≤ 106



# lis=[]
# answer=0
# def get(answer,lis):
# 	for i in range(len(lis)):
# 		if lis[i] > answer:
# 			answer=lis[i]

# 	print(answer)


# game=True
# while game !=False:
# 	user=input("Enter the number or press a to get answer: ")
# 	if user=="a":
# 		get(answer,lis)
# 		game= False



# 	else:
# 		a=int(user)
# 		lis.append(a)




# *******************************above code finds the highest number in the list( to solve question of geeks for geeks ***************** 









# **************************************geeks for geeks question ****************************************************

# Given an unsorted array arr[] of n positive integers. Find the number of triangles that can be formed with three different array elements as lengths of three sides of triangles. 

# Example 1:

# Input: 
# n = 3
# arr[] = {3, 5, 4}
# Output: 
# 1
# Explanation: 
# A triangle is possible 
# with all the elements 5, 3 and 4.
# Example 2:

# Input: 
# n = 5
# arr[] = {6, 4, 9, 7, 8}
# Output: 
# 10
# Explanation: 
# There are 10 triangles
# possible  with the given elements like
# (6,4,9), (6,7,8),...

# triangle=0
# lis =[3,5,4]

# for i in range(len(lis)):
# 	for k in range(i+1):
# 		for j in range(k+1):

# 			if i!=k and i!=j and j!=k:
# 				triangle=triangle +1


# print(triangle)



# ***********above code solves the geeks for geeks question*******************************************




# ************************geeks for geeks ********************************************	
# Given an array nums[] of size n, construct a Product Array P (of same size n) such that P[i] is equal to the product of all the elements of nums except nums[i].

 

# Example 1:

# Input:
# n = 5
# nums[] = {10, 3, 5, 6, 2}
# Output:
# 180 600 360 300 900
# Explanation: 
# For i=0, P[i] = 3*5*6*2 = 180.
# For i=1, P[i] = 10*5*6*2 = 600.
# For i=2, P[i] = 10*3*6*2 = 360.
# For i=3, P[i] = 10*3*5*2 = 300.
# For i=4, P[i] = 10*3*5*6 = 900.
# Example 2:

# Input:
# n = 2
# nums[] = {12,0}
# Output:
# 0 12





# def win(lis,ans):
# 	for i in range(len(lis)):
# 		a=lis[i]
# 		lis.pop(i)
# 		for li in lis:
# 			ans=ans*li
# 		lis.insert(i,a)	
# 		print(ans)
# 		ans=1

# lis=[]
# ans=1
# game=True
# while game ==True:
# 	user=input("Enter the number or press a to get answer: ")
# 	if user=="a":
# 		win(lis,ans)
# 		game=False

# 	else:
# 		lis.append(int(user))





# **********************************above codde is to solve the geeks for geeks question *****************************************





# ***********************geeks for geeks *****************************************************************

# Given an unsorted array arr[] of size N, rotate it by D elements in the counter-clockwise direction. 

 

# Example 1:

# Input:
# N = 5, D = 2
# arr[] = {1,2,3,4,5}
# Output: 3 4 5 1 2
# Explanation: 1 2 3 4 5  when rotated
# by 2 elements, it becomes 3 4 5 1 2.
# Example 2:

# Input:
# N = 10, D = 3
# arr[] = {2,4,6,8,10,12,14,16,18,20}
# Output: 8 10 12 14 16 18 20 2 4 6
# Explanation: 2 4 6 8 10 12 14 16 18 20 
# when rotated by 3 elements, it becomes 
# 8 10 12 14 16 18 20 2 4 6.
 


# user= input("enter the number of elements you want to replace ")

# lis=[1,2,3,4,5]

# for i in range(int(user)):
# 	a=lis[0]
# 	lis.pop(0)
# 	lis.append(a)

# print(lis)



# ******************************above code is to solve the geeks for geeks question *******************************************




# **********************************************geeks for geeks question******************************************************



# For an integer N find the number of trailing zeroes in N!.

# Example 1:

# Input:
# N = 5
# Output:
# 1
# Explanation:
# 5! = 120 so the number of trailing zero is 1.
# Example 2:

# Input:
# N = 4
# Output:
# 0
# Explanation:
# 4! = 24 so the number of trailing zero is 0.


	
# user = int (input("enter the number:"))
# n=1
# for i in range (1,int(user)):
# 	n=n*i



# print(n)


# ****above code is solving the problem of geeks for geeks*****





# *************************geeks for geeks******************
# Implement a Queue using two stack s1 and s2.

# Example 1:

# Input:
# enqueue(2)
# enqueue(3)
# dequeue()
# enqueue(4)
# dequeue()
# Output: 2 3
# Explanation:
# enqueue(2) the queue will be {2}
# enqueue(3) the queue will be {3 2}
# dequeue() the poped element will be 2 
# the stack will be {3}
# enqueue(4) the stack will be {4 3}
# dequeue() the poped element will be 3.  
# Example 2:

# Input:
# enqueue(2)
# dequeue()
# enqueue(3)
# dequeue()
# Output: 2 -1


# li=[]
# a=None
# de=[]

# while True:
# 	user = input("do you want to enque or deque the item? or type q to quit :")
	
# 	if user=="q":
# 		print(de)
# 		break


# 	if user == 'enque':
# 		num=input("Enter the number to enque :")
# 		li.insert(0,int(num))

# 	if user=="deque":

# 		a=len(li)
# 		if len(li)==1:
# 			de.append(-1)

# 		else:
# 			my=li.pop(a-1)
# 			de.append(my)




# **************************************geeks for geeks **********************************************
# Given a non-negative number represented as a list of digits, add 1 to the number (increment the number represented by the digits). The digits are stored such that the most significant digit is first element of array.
 

# Example 1:

# Input: 
# N = 3
# arr[] = {1, 2, 4}
# Output: 
# 1 2 5
# Explanation:
# 124+1 = 125, and so the Output
# Example 2:

# Input: 
# N = 3
# arr[] = {9,9,9}
# Output: 
# 1 0 0 0
# Explanation:
# 999+1 = 1000, and so the output


# li=[]
# us=True
# while us==True:
# 	print('>>press "q " to quit')
# 	user=input("Enter the number  :")
	
# 	if "q" in user:
# 		break

# 	else:
# 		li.append(int(user))

# try:
# 	i =""

# 	for item in li:
# 		a=str(item)
# 		i=i+a


# 	i=int(i)
# 	ans=i+1

# 	print(ans)
# 	print("Thanks for using it" )


# except:
# 	print("Thanks for using it ")





# ******************************GEEKS FOR GEEKS*****************************



# he cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
# Note: There may be multiple possible solutions. Return any one of them. Any correct solution will result in an output of 1, whereas wrong solutions will result in an output of 0.

# Example 1:

# Input:
# N = 7
# A[] = {100,180,260,310,40,535,695}
# Output:
# 1
# Explanation:
# One possible solution is (0 3) (4 6)
# We can buy stock on day 0,
# and sell it on 3rd day, which will 
# give us maximum profit. Now, we buy 
# stock on day 4 and sell it on day 6.
# Example 2:

# Input:
# N = 5
# A[] = {4,2,2,2,4}
# Output:
# 1
# Explanation:
# There are multiple possible solutions.
# one of them is (3 4)
# We can buy stock on day 3,
# and sell it on 4th day, which will 
# give us maximum profit.

# user=int(input('Enter the how much you wand to make profit :'))



# stock=[100,180,260,310,40,535,695]
# li=[]
# for i in range(len(stock)):
# 	for j in range(len(stock)):
# 		a=stock[i]
# 		b=stock[j]
# 		c=b-a
	
# 		if c>user:
# 			li.append(c)



# li.sort()
# li.reverse()
# STOCKS=stock


# a=[]
# try:
# 	f=li[0]
# 	g=li[1]
# except:
# 	f=li[0]
# try:
# 	a.append(f)
# 	a.append(g)
# except:
# 	a.append(f)

# print(f"you can earn max to max {f} rs")
# user1=input("do you want to have another option (if t is not convinient) press y for yes and n for no :")
# if user1=="y":
# 	print(f"you can earn {g} rs profit if you dint like previous one")

 
# ++++++++++++++++++++++++++above code is solving geeks for geeksquestion ++++++++++++



# ***************************GEEKS FOR GEEKS ********************************

# Given a fraction. Convert it into a decimal. 
# If the fractional part is repeating, enclose the repeating part in parentheses.
 

# Example 1:

# Input: numerator = 1, denominator = 3
# Output: "0.(3)"
# Explanation: 1/3 = 0.3333... So here 3 is 
# recurring.
# Example 2:

# Input: numerator = 5, denominator = 2
# Output: "2.5"
# Explanation: 5/2 = 2.5


# user1=int(input("Enter the numerator :"))
# user2= int(input("Enter the denominator :"))
# ans=""
# h=0
# a=user1/user2
# a=str(a)
# c=a.find(".")
# v=a[c+1]
# ans1=[]
# li=[]
# ha=c+2
# answer=''

# for i in range(c):
# 	ans1.append(a[i])

# for item in ans1:
# 	b=str(item)

# 	ans=ans+b

# for j in range(c+1,len(a)):
# 	li.append(a[j])

# for k in range(c+2,len(a)):
# 	if a[k]!=a[c+1]:
# 		answer=answer+'False'

# 	else:
# 		answer=answer+'True'

# if len(a)==ha:
# 	a=float(a)
# 	print(int(a))

# elif len(a)<5 or len(a)<6:
# 	print(float(a))


# elif 'False' in answer :
# 	print(float(a))
# else:
# 	print(f"{ans}.({v})")


# ***********************Above code is to solve the above problem***********************




# *****************************GEEKS FOR GEEKS QUESTION*****************************


# Given a positive integer N. You have to find Nth natural number after removing all the numbers containing digit 9.


# Example 1:

# Input:
# N = 8
# Output:
# 8
# Explanation:
# After removing natural numbers which contains
# digit 9, first 8 numbers are 1,2,3,4,5,6,7,8
# and 8th number is 8.
# Example 2:

# Input:
# N = 9
# Output:
# 10
# Explanation:
# After removing natural numbers which contains
# digit 9, first 9 numbers are 1,2,3,4,5,6,7,8,10
# and 9th number is 10.


# user= int(input("Enter the number :" ))
# li=[]

# run=1

# while len(li) !=user:
# 	b=str(run)
# 	a="9"in b
	
# 	if a==False :
# 		li.append(run)

# 	run+=1

# print(li[user-1])


# *********************Above code is sovinging the geeks for geeks question***************

	

	 
# ****************************GEEKS FOR GEEKS QUESTION********************************


# Given a sorted array with possibly duplicate elements. The task is to find indexes of first and last occurrences of an element X in the given array.

# Note: If the element is not present in the array return {-1,-1} as pair.

 

# Example 1:

# Input:
# N = 9
# v[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}
# X = 5
# Output:
# 2 5
# Explanation:
# Index of first occurrence of 5 is 2
# and index of last occurrence of 5 is 5.
# Example 2:

# Input:
# N = 9
# v[] = {1, 3, 5, 5, 5, 5, 7, 123, 125}
# X = 7
# Output:
# 6 6



# li=[1, 3, 5, 5, 5, 5, 7, 123, 125]
# ans=[]

# x=int(input("Enter the Number :"))

# for i in range(len(li)):
# 	if li[i]==x:
# 		ans.append(i)

# n=len(ans)
# try:
# 	a=ans[0]
# 	b=ans[len(ans)-1]

# 	if a==b:
# 		fi=a
# 		fl= -1



# 	else:
# 		fi=a
# 		fl=b
# except:
# 	fi=-1
# 	fl=-1

# if fl==-1 and fi==-1:
# 	print((fi,fl))
# elif fl!=-1:
# 	print(fi+1,fl+1)

# else:
# 	print((fi+1,fl))


# *********************above code is to solve the above question***************************




# **********************************GEEKS FOR GEEKS *************************************************

# Given a sorted array A[] of N positive integers having all the numbers occurring exactly twice, except for one number which will occur only once. Find the number occurring only once.

# Example 1:

# Input:
# N = 5
# A = {1, 1, 2, 5, 5}
# Output: 2
# Explanation: 
# Since 2 occurs once, while
# other numbers occur twice, 
# 2 is the answer.
# Example 2:

# Input:
# N = 7
# A = {2, 2, 5, 5, 20, 30, 30}
# Output: 20
# Explanation:
# Since 20 occurs once, while
# other numbers occur twice, 
# 20 is the answer.






# li=[2, 2,2, 5, 5,5, 20, 30, 30]
# ans=set()
# for items in li :
# 	b=items
# 	a=li.count(b)
# 	if a != 2:
# 		ans.add(items)

# print(ans)

	
	
		
	
# ********************************above code is to solve the above question********************************




# *********************************************GEEKS FOR GEEKS********************************************		
# Given two numbers represented by two linked lists of size N and M. The task is to return a sum list.

# The sum list is a linked list representation of the addition of two input numbers from the last.

# Example 1:

# Input:
# N = 2
# valueN[] = {4,5}
# M = 3
# valueM[] = {3,4,5}
# Output: 3 9 0  
# Explanation: For the given two linked
# list (4 5) and (3 4 5), after adding
# the two linked list resultant linked
# list will be (3 9 0).
# Example 2:

# Input:
# N = 2
# valueN[] = {6,3}
# M = 1
# valueM[] = {7}
# Output: 7 0
# Explanation: For the given two linked
# list (6 3) and (7), after adding the
# two linked list resultant linked list
# will be (7 0).






# li1=[]
# user1=input("Enter the number :")
# for i in range(len(user1)):
# 	k=user1[i]
# 	li1.append(int(k))

# li2=[]
# user2=input("Enter the number :")
# for j in range(len(user2)):
# 	m=user2[j]
# 	li2.append(int(m))


# ans=[]

# a=""
# b=""
# for items in li1:
# 	a=a+str(items)

# for item in li2:
# 	b=b+str(item)

# a=int(a)
# b=int(b)
# d=str(a+b)


# for i in range (len(d)):
# 	f=d[i]
# 	ans.append(int(f))
# print(ans)




# *********************************above code is to solve the avove code**********************************



# ***************************************GEEKS FOR GEEKS ************************************************

# Given K sorted arrays arranged in the form of a matrix of size K*K. The task is to merge them into one sorted array.
# Example 1:

# Input:
# K = 3
# arr[][] = {{1,2,3},{4,5,6},{7,8,9}}
# Output: 1 2 3 4 5 6 7 8 9
# Explanation:Above test case has 3 sorted
# arrays of size 3, 3, 3
# arr[][] = [[1, 2, 3],[4, 5, 6], 
# [7, 8, 9]]
# The merged list will be 
# [1, 2, 3, 4, 5, 6, 7, 8, 9].
# Example 2:

# Input:
# K = 4
# arr[][]={{1,2,3,4}{2,2,3,4},
#          {5,5,6,6},{7,8,9,9}}
# Output:
# 1 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9 
# Explanation: Above test case has 4 sorted
# arrays of size 4, 4, 4, 4
# arr[][] = [[1, 2, 2, 2], [3, 3, 4, 4],
# [5, 5, 6, 6]  [7, 8, 9, 9 ]]
# The merged list will be 
# [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 
# 6, 6, 7, 8, 9, 9 ].






	

	
# li1= [1, 2, 2, 2]
# li2=[3, 3, 4, 4]
# li3=[5, 5, 6, 6]
# li4=[7, 8, 9, 9 ]
# ans=[]

# for items in  li1:
# 	ans.append(items)

# for item in li2:
# 	ans.append(item)
# for x in li3:
# 	ans.append(x)


# ans.sort()
# print(ans)


# ************************************GEEKS FOR GEEKS ************************************************


# Given a string S consisting of opening and closing parenthesis '(' and ')'. Find length of the longest valid parenthesis substring.

# Example 1:

# Input: S = ((()
# Output: 2
# Explaination: The longest valid 
# parenthesis substring is "()".
# Example 2:

# Input: S = )()())
# Output: 4
# Explaination: The longest valid 
# parenthesis substring is "()()".


# string1=")()())"
# Open=0
# close=0

# for i in range (len(string1)):
# 	if string1[i]=="(" :
		
# 		Open =Open+1

# 	if string1[i]==")" :
		
# 		close =close+1


# a=close
# b=Open
# if a>b:			
# 	print(b*2)
# if a==b:
# 	print(b*2)
# if b>a:
# 	print(a*2)


# ***********************************above code is to solve the above problem*******************************
		


# *************************************geeks for geeks************************************************


# Given an array of integers of size N and a number K., Your must modify array arr[] exactly K 
# number of times. Here modify array means in each operation you can replace any array element 
# either arr[i] by -arr[i] or -arr[i] by arr[i]. You need to perform this operation in such a way
#  that after K operations, the sum of the array must be maximum.


# Example 1:

# Input:
# N = 5, K = 1
# arr[] = {1, 2, -3, 4, 5}
# Output:
# 15
# Explanation:
# We have k=1 so we can change -3 to 3 and
# sum all the elements to produce 15 as output.
# Example 2:

# Input:
# N = 10, K = 5
# arr[] = {5, -2, 5, -4, 5, -12, 5, 5, 5, 20}
# Output:
# 68
# Explanation:
# Here  we have k=5 so we turn -2, -4, -12 to
# 2, 4, and 12 respectively. Since we have
# performed 3 operations so k is now 2. To get
# maximum sum of array we can turn positive
# turned 2 into negative and then positive
# again so k is 0. Now sum is
# 5+5+4+5+12+5+5+5+20+2 = 68

# B=[]
# listmaking()
# a=int(input("Enter the number of time you want to modify:"))

# z=0
# for i in range(a):
# 	B.sort()
# 	if B[i] < 0:
# 		c= -2*B[i]
# 		B.append(c)
# 	else:
# 		d= -2*B[i]
# for j in range(len(B)):
# 	z=z+B[j]

# print(z)


# ********************************above is the code to solve the above problem**********************



# ***************************************geeks for geeks*******************************************

# You are given a string S, the task is to reverse the string using stack.

 

# Example 1:


# Input: S="GeeksforGeeks"
# Output: skeeGrofskeeG

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function reverse() which takes the string S as an input parameter and returns the reversed string.

 

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)

 

# Constraints:
# 1 ≤ length of the string ≤ 100


# s="darshil"
# ans=""
# a=len(s)
# for i in range(1,a+1):
# 	c=i*-1
# 	ans= ans+(s[c])
# print(ans)


 # ********************************above is the code to solve the above problem**********************





 # ***************************************geeks for geeks*******************************************


#  Input:
# N = 3
# arr[] = {{1, 2}, {2, 3}, {3, 4}}
# Output:
# 3
# Explanation:
# If you position yourself at point (1,2)
# and fire the arrow aiming at the point (3,4).
# Then all the balloons will burst.
# Example 2:

# Input: 
# N = 3
# arr[] = {{2,2}, {0,0}, {1,2}} 
# Output:
# 2
# Explanation: 
# If you position yourself at point (2,2)
# and fire the arrow aiming at the point (0,0).
# Then the two balloons present at the two points
# will burst.

# arr= [[1, 2], [2, 3], [3, 4]]





