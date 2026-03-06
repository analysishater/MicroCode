with open('input4.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]


lines.pop(0)
root=[]
all_nodes=[]
couples=[]
for i in lines:
    k=i[0]
    
    count=1
   
    while i[count] !=" " :
        k=k+i[count]
        count=count+1
    if  not int(k) in root:
        root.append(int(k))
        if not int(k) in all_nodes:
           all_nodes.append(int(k))
    count=count+1
    j=i[count]
    count=count+1
    while count< len(i):
        j=j+i[count]
        count=count+1
    couples.append([int(k),int(j)])
    if not int(j) in all_nodes:
        all_nodes.append(int(j))

root.sort()
couples1=[]
for i in root :
    med=[i]
    for j in range(0,len(couples)):
        if couples[j][0]==i:
            med.append(couples[j][1])
    couples1.append(med)

i=len(couples1)-1

while i>0:
    j=couples1[i]# a list
    number=j[0]
    count=i-1
    c=False
    while c==False:
        if number in couples1[count]:
            c=True

            for l in range(1,len(j)):
                couples1[count].append(j[l])
                
        else:
            count=count-1
            if count<0:
                break
    i=i-1

sum=0

for i in range(0,len(couples1)) :
    j=couples1[i]
    n1=j[0]
    for count in range(1,len(j)):
        sum=sum +(n1-j[count])*(n1-j[count])


print(sum%1000000007)
sum=0
all_nodes.sort()
print(all_nodes)
#second part 
for ii in range(0,len(all_nodes)):
    for ji in range(ii+1,len(all_nodes)):
        c=False
        count=0
        while c==False and count <len(couples1):
            if all_nodes[ii] in couples1[count] and all_nodes[ji] in couples1[count]:
                c=True
                head=couples1[count][0]
                depth=0
                count=count-1
                while count>-1:
                    if head in couples1[count]:
                        depth=depth+1
                        head=couples1[count][0]
                    count=count-1
                sum=sum+depth
            else:
                count=count+1

print(sum % 1000000007)

                



