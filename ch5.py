with open('input5.txt', 'r') as f:
    content = f.read().replace('\n', '').replace(' ', '')

operations=[]
operation=[]
index=0
sum=0

while index<len(content):

   if content[index] in ["A","B","C","D"]:
       match content[index]:
           case "A":
               sum=sum+247
           case "B":
               sum=sum+383 
           case "C":
               sum=sum+156
           case "D":
               sum=sum+512

       index=index+1

   else:
       operation.append("(")
       index=index+1
       depth_p=1  # FIXED: replaced operation.count("(") != operation.count(")") with depth counters (was O(n^2), caused timeout)
       depth_b=0  # FIXED: replaced operation.count("{") != operation.count("}") with depth counters
       while (depth_p != 0 or depth_b != 0):
              if content[index] in ["A","B","C","D"]:
                  match content[index]:
                       case "A":
                         operation.append(247)
                       case "B":
                         operation.append(383) 
                       case "C":
                         operation.append(156) 
                       case "D":
                         operation.append(512) 
                  index=index+1

              else:
                  c=content[index]
                  operation.append(c)
                  if c=='(':   depth_p+=1
                  elif c==')': depth_p-=1
                  elif c=='{': depth_b+=1
                  elif c=='}': depth_b-=1
                  index=index+1

       operation.append(content[index])
       index=index+1
       operation.append(content[index])
       index=index+1
       operation.append(content[index])
       index=index+1

       index1=len(operation)-1
       while index1>-1:
           if operation[index1]=="}" or operation[index1]=="{":
               index1=index1-1
           elif operation[index1]==")":
               operations.append("(")
               index1=index1-1
           elif isinstance(operation[index1], str) and operation[index1].isdigit():
               operations.append(int(operation[index1]))
               index1=index1-1
           elif operation[index1]=="(":
               operations.append(")")
               index1=index1-1
           elif isinstance(operation[index1], int):
               undersum=0
               while index1>-1 and isinstance(operation[index1], int):
                   undersum=undersum+operation[index1]
                   index1=index1-1
               operations.append(undersum) 
           else:
               index1=index1-1

       operation=[]
       index1=len(operations)-1
       times=[]
       while index1>-1:
           if operations[index1]==")":
               if times!=[]:
                   operation.append(times[0])
                   times.pop(0)
               else:
                   operation.append(" ")
               index1=index1-1

           elif operations[index1]=="(":
               index1=index1-1
               times[0]=times[0]*(operations[index1])
               if operation[len (operation)-1]!=" ":
                     times[0]=times[0]+(operation[len(operation)-1])
               
               operation.pop(len(operation)-1)
               index1=index1-1
           else:
               if times==[]:
                   times.append(operations[index1])
               else:
                   times[0]=times[0]+operations[index1]
               index1=index1-1

       sum=sum+times[0]
       operations=[]
       operation=[]

print(sum)