a = [1, 2, 4, 2, 5, 2, 6] 
b = [] 
for x in a: 
    if x != 2: 
       b.append(x) 
print(b)
nums = [9, 2, 11, 7, 11, 3] 
largest =None 
second =None 
for x in nums: 
    if largest is None or x > largest: 
        if largest is None or x != largest: 
           second=largest 
        largest=x 
    elif x!=largest and (second is None or x>second):
        second=x
print("second largest distinct=",second)
a = [10, 20, 30, 40, 50] 
first = a[0]  
for i in range(len(a)- 1): 
    a[i] = a[i + 1]  
a[-1] = first 
print(a) 
a=[1, 2, 3, 4, 5] 
k=int(input("Enter index k (0..5): ")) 
value=99 
a.append(0) 
for i in range(len(a)- 1, k,-1): 
    a[i]=a[i- 1] 
a[k]=value
print(a)
a=[5, 6, 7, 8, 9, 10] 
k=int(input("Enter index k (0..5):"))
for i in range(k,len(a)-1):
    a[i] = a[i+1] 
a.pop()
print(a)
line=input("enter a line:")
words=line.split()
longest=""
for w in words:
    if len(w)>len(longest):
       longest=w
print("longest:",longest)
print("lenght:",len(longest))
s=input("enter a line:")
word=s.split()
result="-".join(words)
print(result)
a=[3,3,2,3,1,2,4,4]
u=[]
for x in a:
    if x not in u:
        u.append(x)
print(u)
a=[1,1,1,2,2,3,4,4]
seen=[]
for x in a:
    if x in seen:
        continue
    count=0
    for y in a:
        if y==x:
            count+=1
    print(x,"->",count)
    seen.append(x)
a=[8, 3, 5, 2, 9, 1]
n=len(a)
for passno in range(n-1):
    for i in range(n-1-passno):
        if a[i]>a[i+1]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
print(a)