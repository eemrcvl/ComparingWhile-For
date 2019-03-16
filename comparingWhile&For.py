from timeit import default_timer as timer
import matplotlib.pyplot as plt
def forLoop():   
    i=0
    start=timer()          #timer starts
    for i in range(0,10000):
        i+=1    
    end=timer()            #timer stops
    total=end-start
    return total
def whileLoop():
    i=0
    start=timer()
    while i<1000:
        i+=1
    end=timer()
    total=end-start
    return total
#empty lists
l1=[] 
l2=[]
#append time of executions to lists
#for and while loops are executed 10000 times to get more different execution times
for j in range(0,10000): 
    l1.append(forLoop())      
    l2.append(whileLoop())

plt.plot(l1) #this draws the chart of "for" loops' execution times  
plt.plot(l2,color="red") #and this is for "while" loops
plt.show()


    
