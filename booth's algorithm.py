from math import *


def binaryAdder(x,y,cin,i):   
	#	i=len(x)-1
		i=i-1  
		if i<0:        # termination candition 
			return x

		sum=x[i]+y[i]+cin
		x[i]=sum%2

		if sum==2 or sum==3:
			return binaryAdder(x,y,1,i)
		else:
			return binaryAdder(x,y,0,i)



def Zero(x,length):
	for i in range(length):
		x.append(0)
	return x


def complementor(x): #2's complementor
	one=[]        #for adding one of length equals to x to make 2's complement
	y=[]
	y=Zero(y,len(x))
	for i in range(len(x)):
			y[i]=int(not x[i])
			one.append(0)        
	one[len(x)-1]=1    # making last bit one 

	y=binaryAdder(y,one,0,len(y))

	return y

def toBinary(x,count):
	num=abs(x)
	BinaryVal=[]
	
	while(num>0):
		BinaryVal.append(num%2)
		num=floor(num/2)
		

	for k in range(count-len(BinaryVal)):   #to add additional bit to make it of 32 bits
		BinaryVal.append(0)

	BinaryVal=BinaryVal[::-1]
	
	if x < 0:
		BinaryVal = complementor(BinaryVal)

	return BinaryVal

def toDecimal(x):
	dec=0
	p=0
	for i in reversed(range(len(x))):
		dec += x[i]*(2**p)
		p=p+1

	return dec

def shiftRight(AC,Q2,Qn):
	Qn[0]=Q2[len(Q2)-1]
	
	for i in reversed(range(1,len(AC))):
		Q2[i]=Q2[i-1]

	Q2[0]=AC[len(AC)-1]

	for i in reversed(range(1,len(AC))):
		AC[i]=AC[i-1]





def Boothalgorithm(AC,M2,Mc,Q2,Qn,count):

	last=count -1           #last bit number

	
	while(count !=0):
		print("\n\nstep : ",(last+2)-count)
		print("---------------------------------------------------------")
		print(" AC : ",AC,end=' || ')
		print(" Q2 : ",Q2,end=' || ')
		print(" Qn : ",Qn)
		print("-------------------------------------------------------")
		if Q2[last]==Qn[0]:
			shiftRight(AC,Q2,Qn)    
		elif Q2[last]==1 and Qn[0]==0: 
			AC=binaryAdder(AC,Mc,0,len(AC))
			shiftRight(AC,Q2,Qn)
		else:
			AC=binaryAdder(AC,M2,0,len(AC))
			shiftRight(AC,Q2,Qn)
		count -=1

		

	print("\n\nresult :  ",AC+Q2,"\n\n")

	return AC+Q2  # by merging two list which is required ans 





def main():
	M=int(input("enter multiplicand : "))
	Q=int(input("enter Multiplier : "))
	count=4   #no of bits of the registers
	M2=toBinary(M,count)  #binary value of M
	Q2=toBinary(Q,count)
	print("Q2 is : {} and M2 is {} ".format(Q2,M2))
	Qn=[0]
	Mc=complementor(M2)    # 2's complement of M2 (M)

	print("Mc is {}".format(Mc))
	
	AC=[]
	AC=Zero(AC,count)      # initializing zeros to AC 
	

	#print(M2)
	#print(Q2) 
	 
	result=Boothalgorithm(AC,M2,Mc,Q2,Qn,count)

	if (M<0 and Q<0) or (M>0 and Q>0):
		result = toDecimal(result)
		print(f"The multiplication of {M} and {Q} is : {result}")

	elif M < 0 or Q < 0 :
		result = complementor(result)
		result=toDecimal(result)
		print(f"The multiplication of {M} and {Q} is : -{result}")      #for negative value multiplication converting the result into 2's complement

	
	



if __name__=="__main__":
	main()