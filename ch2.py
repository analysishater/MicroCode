with open('input3.txt', 'r') as file:
    content = file.read()

lines = [int(item.strip()) for item in content.split(',') if item.strip().lstrip('-').isdigit()]
lines.append(468)
round=0
list=[]
c=True
while c==True:
    i=0
    c=False
    while c==False and i<len(lines):
        if lines[i]!=0:
            c=True
        else:
            i=i+1
    
    if c==True:
        list.append(i)
        k=i+2
        if i==0:
            while k<len(lines)-1 :
                if lines[k]!=0:
                   list.append(k)
                   k=k+2
                else:
                    k=k+1

        else:
            while k<len(lines) :
                if lines[k]!=0:
                   list.append(k)
                   k=k+2
                else:
        
                  k=k+1
        m=False
        while m==False:
            for j in list:
               lines[j]=lines[j]-1
               if lines[j]==0:
                   m=True
            round=round+1
        list=[]
print(round)
        
            

