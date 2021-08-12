import math


result=[]
userinput=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flatten(userinput):
    for item in userinput:
      if isinstance(item,list):
        flatten(item)
      else:
          result.append(item)    
  


flatten(userinput)
print(result)