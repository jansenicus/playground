# -*- coding:utf-8
#!/usr/bin/python
# ----------------------------------
# Jansen A. Simanullang
# (c) 13.12.2017
# ----------------------------------
def countDivisibles(A, B, K):

	#Variable to store the counter
	iCounter = 0;
 
	# Running a loop from A to B and check
	# if a number is divisible by K.
	for i in range (A, B+1):

		if (i % K == 0):

			iCounter = iCounter+ 1

	return iCounter


with open('input.in', 'r') as f:

	lines = f.readlines()
	T = int(lines[0].strip())

	for i in range(0, 3*T, 3):

		A = int(lines[i+1].strip())
		B = int(lines[i+2].strip())
		K = int(lines[i+3].strip())
			
		#print "Case "+str(i/3+1)+": "+str(A)+" ~ "+str(B)+" %"+str(K)+ "-->" +str(countDivisibles(A, B, K))
		print "Case "+str(i/3+1)+": " +str(countDivisibles(A, B, K))
		#print (countDivisibles(A, B, K))
