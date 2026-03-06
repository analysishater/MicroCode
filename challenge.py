with open('input.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file if line.strip()]


numbers.pop(0)
print(numbers[0:5])
numbers.sort()
i=0
j=len(numbers)-1
c=False
while(i<j and c==False):
    if numbers[i]+numbers[j]==125267:
        c=True
        print(numbers[i]*numbers[j])
    elif numbers[i]+numbers[j]<125267:
        i=i+1
    else:
        j=j+1

        
i=0
j=len(numbers)-1
k=int(len(numbers)/2)
c=False
n=0
list=[]
while(i<k<j and c==False ):
    if numbers[i]+numbers[k]+numbers[j]==125267:
       list.append([numbers[i],numbers[k],numbers[j]])
       j=j-1
       k=k+1
    
    elif numbers[i]+numbers[k]+numbers[j]<125267:
        if k==i+1:
            k=k+1
        else:i=i+1
    else:
        j=j-1
        
print(list)
for i in list :
    if i[2]-i[0]>1000:
        print(i[2]*i[0]*i[1])
