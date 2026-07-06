# Q52 Python Solution

arr=list(map(int,input('Enter array: ').split()))
even=sum(1 for x in arr if x%2==0)
print('Even =',even,'Odd =',len(arr)-even)
