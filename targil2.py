# Shlomo Salhoov 206787228

from functools import reduce
import time
##### question 1 #####
start_time1=time.time()
func=lambda x:x/2+2
# part 1 
l1=list(map(func,range(0,10000)))
# part 2
print(sum(l1))
end_time1=time.time()
# part 3
start_time2=time.time()
l=list(range(0,10000))
def func1(l):
     summ=0
     for x in l:
          x=x/2+2
          summ=summ+x
     return summ
print(func1(l))
end_time2=time.time()
print("time for the lambda func is")
print(end_time1-start_time1)
print("seconds")
print("time for the normal func is")
print(end_time2-start_time2)
print("seconds")
# part 4
print(reduce(lambda x,y:x+func(y), range(0,10000),0))

##### question 2 #####
even=list(filter(lambda x:x%2==0,range(1,1000)))
odd=list(filter(lambda x:x%2==1,range(1,1000)))
reduce(lambda x,y:x+y,list(reduce(lambda x,y:x*y,even,0)),0)
reduce(lambda x,y:x+y,list(reduce(lambda x,y:func(x)+y,odd,0)),0)

##### question 3 #####
# part 1
print(lambda str_date,repeat,skip:list(map(lambda x,str:str+x(skip) ,[str_date]*repeat)))

##### question 4 #####
# part 1


# part 2


# part 3


##### question 5 #####

