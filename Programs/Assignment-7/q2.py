time=[]
dis=[]

#Use input().split() to convert number of lists
dis=input('Enter the distances :').split()
time=input('Enter the time inputs :').split()

#Conversion for numeric operations or else it shows error 
dis=[float(d) for d in dis]
time=[float(t) for t in time]

#Check whether both the Lists have same amount of element or not 
if(len(time) != len(dis)):
    print('The correspnding dist and times must be same !')

#Showing the result
else :
   speed=[dis[i]/time[i] for i in range(len(dis))]
   print('speeds : ', speed)