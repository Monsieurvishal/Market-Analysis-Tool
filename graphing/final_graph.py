from collections import Counter 
# from collections import Counter convert repetative elements in a list into a dictionary.
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
    
def get_plot(data):
    
    print(data)
    
    age_list=[]
    sales_and_age=[]
    sales_and_age1=[]
    blue = []#To know the count of blue,green,yellow and orange elements present
    green = []
    yellow =[]
    orange = []
    num_per_age = [0 for i in range(10)]#List to keep the track of number of aged group like 1to10 till above 90
    
    for row in data:
        if (row[2]>0 and row[2]<=10):
            row[2]='0to10'
            num_per_age[0]+=1
        elif(row[2]>10 and row[2]<=20):
            row[2]='10to20'
            num_per_age[1]+=1
        elif(row[2]>20 and row[2]<=30):
            row[2]='20to30'
            num_per_age[2]+=1
        elif(row[2]>30 and row[2]<=40):
            row[2]='30to40'
            num_per_age[3]+=1
        elif(row[2]>40 and row[2]<=50):
            row[2]='40to50'
            num_per_age[4]+=1
        elif(row[2]>50 and row[2]<=60):
            row[2]='50to60'
            num_per_age[5]+=1
        elif(row[2]>60 and row[2]<=70):
            row[2]='60to70'
            num_per_age[6]+=1
        elif(row[2]>70 and row[2]<=80):
            row[2]='70to80'
            num_per_age[7]+=1
        elif(row[2]>80 and row[2]<=90):
            row[2]='80to90'
            num_per_age[8]+=1
        else:
            row[2]='above90'
            num_per_age[9]+=1
            
    for i in range(0,100,10):
        age_list.append(str(i)+"to"+str(i+10))
             #pandas.Series( data, index, dtype, name)
             #data takes various forms like ndarray, list, constants
             #dtype is for data type. If None, data type will be inferred
    series = pd.Series(num_per_age,index=age_list, name='age distribution')
    series.plot.pie(figsize=(6, 6))
    plt.show()
    
    for row in data:#this takes the count of blue,green,yellow,orange
        blue.append(eval(row[4])["blue"])
        #the eval function evaluates the “String” like a python expression and returns the result as an integer.
        blue_sum = sum(blue)
        #function sum() which sums up the numbers in the list.
        green.append(eval(row[4])["green"])
        green_sum = sum(green)
        yellow.append(eval(row[4])["yellow"])
        yellow_sum = sum(yellow)
        orange.append(eval(row[4])["orange"])
        orange_sum = sum(orange)       
    df=pd.DataFrame({'blue': [blue_sum],'green': [green_sum],'yellow': [yellow_sum],'orange': [orange_sum]})
    df.plot(kind='bar',color=['b','g','r','y'])
    plt.show()
    
    for row in data:
        temp1=row[1]
        temp2=row[2]
        temp3=str(temp1)+str(temp2)
        sales_and_age.append(temp3)
    sales_and_age1= dict(Counter(sales_and_age))
    df=pd.DataFrame(sales_and_age1, index=['sales vs age'])
    df.plot(kind='bar')
    plt.show()
    
    register_matplotlib_converters()
    timestamp_list = []
    for row in data:
        timestamp_list.append(datetime.strptime(row[0],"%m/%d/%Y, %H:%M:%S"))
    df = pd.DataFrame({'timestamp_list': timestamp_list,'blue': blue,'green': green,'yellow': yellow,'orange': orange})

    plt.plot(timestamp_list,blue,color="blue")
    plt.plot(timestamp_list,green,color="green")
    plt.plot(timestamp_list,yellow,color="yellow")
    plt.plot(timestamp_list,orange,color="orange")

    plt.show()
        
        
        
        
        

    

    
