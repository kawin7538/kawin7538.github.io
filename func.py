#-*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:17:58 2018

Last Modified 12 Dec 2018

@author: Kawin-PC

Kawin Chinpong
"""

#   How to use function from files:
#       You can simply use only find_pathway function 
#       (the other function is composition of find_pathway function, 
#       may not be used directly)

import pandas as pd
import numpy as np

def get_station():
    station=pd.read_csv("country.csv")[['country_name','station_open']]
    station=[(i+1,station['country_name'][i]) for i in range(len(station)) if station['station_open'][i]=='Yes']
    station.sort(key=lambda x:x[1])
    return station

def calculate_price(ans):
    #Function that calculate price from starting point to destination
    #This function use for sorting in find_pathway function
    #Input:
    #   dictionary that has structure:
    #       location    : list of first and last station in each train_name
    #       train_name  : list of train name used
    #       train_type  : list of type of train name in same index number
    #       train_count : list of number of station pass using same index 
    #                     train_name
    #Output:
    #   One real number, price
    
    #Call Price from csv file
    price=pd.read_csv("trainPrice.csv")
    #Initialize sum_price value to 0
    sum_price=0
    #Loop index i in every element in ans['train_count']
    for i in range(len(ans['train_count'])):
        #Check if train_type is not inter
        if 'INTER' !=ans['train_type'][i]:
            #Add sum_price with price[train_name[i]][train_count[i]]
            sum_price=sum_price+price[ans['train_name'][i]][ans['train_count'][i]]
    #return sum_price outside
    return sum_price

def string_Price(answer):
    #Function that convert answer from dictionary form:
    #   location    : list of first and last station in each train_name
    #   train_name  : list of train name used
    #   train_type  : list of type of train name in same index number
    #   train_count : list of number of station pass using same index 
    #                 train_name
    #to one string that have the pattern below:
    #   "From starting point to destination"
    #   "Sum price : XX baht"
    #   next each line tell how to go destination and show price of each step
    #       " i. use TRAIN_NAME from STARTING to DESTINATION , XX Baht"
    #   last line tell price again
    
    #Call price from csv file
    price=pd.read_csv("trainPrice.csv")
    #Call country from csv file
    country=pd.read_csv("country.csv")
    #Create set of output
    set_output=[]
    #Loop for all available answer
    for ans in answer:
        #Define variable output as empty string
        output=''
        #Define sum_price as 0
        sum_price=0
        #Loop index i for every train_count
        for i in range(len(ans['train_count'])):
            #Set output with newline and number i+1
            output=output+'\n%s. '%(i+1)
            #Check if train_type is INTER (for walk only)
            if 'INTER' in ans['train_type'][i]:
                #Add 'walk 'backward of string 
                output=output+'walk '
            else:
                #Add 'use '+train_name to output
                output=output+"use %s "%(ans['train_name'][i])
            #Add 'from SS to DD when SS is country[location[i]-1] and DD is 
            #country[location[i+1]-1]
            output=output+"from %s to %s "%(country['country_name'][ans['location'][i]-1],country['country_name'][ans['location'][i+1]-1])
            #Check if 'INTER' not in train_type[i]
            if 'INTER' not in ans['train_type'][i]:
                #Add price backward and add price to sum_price
                output=output+", %s Baht(s)"%(price[ans['train_name'][i]][ans['train_count'][i]])
                sum_price=sum_price+price[ans['train_name'][i]][ans['train_count'][i]]
        #Add sum_price to output
        output=output+'\n\nSum Price : %s Baht'%(sum_price)
        #reformatting output = 'from SS to DD'+'sum price XX baht'+output
        #output='\nFrom %s to %s\n\n'%(country['country_name'][ans['location'][0]-1],country['country_name'][ans['location'][-1]-1])+'Sum Price : %s Baht'%(sum_price)+'\n%s'%(output)
        output='Sum Price : %s Baht'%(sum_price)+'\n%s'%(output)
        #append output to set_output
        set_output.append(output)
    new_set_output=[]
    new_set_output.append('Best Offer\n\n'+set_output[0])
    temp_set_output=set_output.copy()
    temp_set_output.sort(key=lambda x:x.count('walk'))
    if len(temp_set_output[0].split('\n'))<len(set_output[0].split('\n')) and temp_set_output[0]!=set_output[0]:
        new_set_output.append('For Less Walk Option\n\n'+temp_set_output[0])
    for i in set_output:
        if i.count('use MRT')==0 and i.count('use ARL')==0:
            if not any(x.count(i)!=0 for x in new_set_output):
                new_set_output.append('For BTS Lover\n\n'+i)
                break;
    for i in set_output:
        if i.count('use BTS')==0 and i.count('use ARL')==0:
            if not any(x.count(i)!=0 for x in new_set_output):
                new_set_output.append('For MRT Lover\n\n'+i)
                break;
    for i in set_output:
        if i.count('use BTS')==0 and i.count('use MRT')==0:
            if not any(x.count(i)!=0 for x in new_set_output):
                new_set_output.append('For ARL Lover\n\n'+i)
                break;
    for i in set_output:
        if i.count('use BTS')==0:
            if not any(x.count(i)!=0 for x in new_set_output):
                new_set_output.append('For non-addict BTS\n\n'+i)
                break;
    for i in set_output:
        if i.count('use MRT')==0:
            if not any(x.count(i)!=0 for x in new_set_output):
                new_set_output.append('For non-addict MRT\n\n'+i)
                break;
    for i in set_output:
        if i.count('use ARL')==0:
            if not any(x.count(i)!=0 for x in new_set_output):
                new_set_output.append('For non-addict ARL\n\n'+i)
                break;
    for i in set_output:
        if i.count('use BTS')!=0 and i.count('use MRT')!=0 and i.count('use ARL')!=0:
            if not any(x.count(i)!=0 for x in new_set_output):
                new_set_output.append('For All Train Lover\n\n'+i)
                break;
    #return list of string
    return new_set_output
        
  

def create_map(train_df):
    #Function to create map from trainLine.csv
    #Input:
    #   train_df dataframe that have structure:
    #       train_name : string of train name
    #       train_type : string of type train
    #       train_location : string that look like list-object
    #Output:
    #   dictionary that have index i and value (list of tuple of next_location,
    #   train_name and train_type)
    
    #variable sizee contain the number of station (how many station)
    sizee=len(pd.read_csv("country.csv"))
    #This loop convert train_location of train_df from string to list of number
    for i in range(len(train_df['train_location'])):
        train_df['train_location'][i]=[int(j) for j in train_df['train_location'][i].strip('[]').split(',')]
    #answer variable contain dictionary of city i and next way from city i,
    #initialize value with empty dictionary
    answer={}
    #access to each station
    for i in range(1,sizee+1):
        #initialize answer cell i to empty list
        answer[i]=[]
        #access to each line
        for j in range(len(train_df['train_location'])):
            #check if this line has station i
            if i in train_df['train_location'][j]:
                #find index that have element i from list
                k=train_df['train_location'][j].index(i)
                #if index k is not leftmost element then append to answer[i]
                if k!=0:
                    answer[i].append((train_df['train_location'][j][k-1],train_df['train_name'][j],train_df['train_type'][j]))
                #if index k is not rightmost elemetn then append to answer[i]
                if k!=len(train_df['train_location'][j])-1:
                    answer[i].append((train_df['train_location'][j][k+1],train_df['train_name'][j],train_df['train_type'][j]))
    #send value answer to main function or function that called
    return answer

def ans_transform(inputt):
    #Function to change format of answer from pattern tuple of list of point,
    #train name and train_type below
    #   ( [point] , [train_name] , [train_type] ) 
    #To dictionary that has structure
    #   location    : list of first and last station in each train_name
    #   train_name  : list of train name used
    #   train_type  : list of type of train name in same index number
    #   train_count : list of number of station pass using same index 
    #                 train_name
    
    #Build empty dictionary name ans
    ans={}
    #Create index 'location' assign value with list that has one element , 
    #   ID of first station
    ans['location']=[inputt[0][0]]
    #Create index 'train_name' with empty list
    ans['train_name']=[]
    #Create index 'train_type' with empty list
    ans['train_type']=[]
    #Create index 'train_count' with empty list
    ans['train_count']=[]
    #Iteration for every index of inputt[0] except element 0
    for i in range(1,len(inputt[0])):
        #Check if train_name in dict is empty (first time of loop) or 
        #train_name in last station in dict does not same as train name from
        #present station
        if len(ans['train_name'])==0 or ans['train_name'][-1]!=inputt[1][i-1]:
            #push location element i to location in dictionary
            ans['location'].append(inputt[0][i])
            #push train name element i-1 to train_name in dictionary
            ans['train_name'].append(inputt[1][i-1])
            #push train type element i-1 to train_type in dictionary
            ans['train_type'].append(inputt[2][i-1])
            #push 1 to train_count in dictionary
            ans['train_count'].append(1)
        #Else condition
        else:
            #Change last location in dictionary to location element i
            ans['location'][-1]=inputt[0][i]
            #Add value of train_count in diction by 1
            ans['train_count'][-1]=ans['train_count'][-1]+1
    #Return dictionary
    return ans
    

def find_pathway_until(starting_point,destination):
    #Function to find pathway from starting_point to destination
    #with breadth first search algorithm
    #Input:
    #   starting_point(integer)
    #   destination (integer)
    #Output:
    #   dictionary in form
    #       location: list of first station and last station for each line
    #       train_name: list of train line name used 
    #       train_type: list of train type used
    #       train_count: list of count to use train_name
    #   relation of output:
    #       declare i is integer , output can read as
    #       "Use train_name[i] that has type train_type[i], distance is
    #           train_count[i] stations from location[i] to location[i+1]"
    
    #call train line data from trainLine.csv
    train_df=pd.read_csv("trainLine.csv")
    #create map from create_map function (Full information from create_map())
    train_map=create_map(train_df)
    #queue variable is list of tuple of 3 variables
    #   - list of point visited(list of integer)
    #   - list of train_name that travel from point[i] to point[i+1]
    #   - list of train_type of train_name
    queue=[([starting_point],[],[])]
    #ans collect element of queue that can travel from starting_point to 
    #destination, initialize with empty list
    ans=[]
    #Iteration until can't travel anymore (length of queue is 0)
    while len(queue)!=0:
        #now variable save first element of queue and dequeue it from queue
        now=queue.pop(0)
        #check if last element of visited point is same as destination
        if now[0][-1]==destination:
            #convert now variable from (tuple of list of point visited,list of 
            #train name and list of train_type) to (dictionary of location,
            #train_name,train_type and train_count) (Full information from 
            #function ans_transform())
            now=ans_transform(now)
            #add now variable that come from ans_transform to list ans
            #and look in next element immediately
            ans.append(now)
            continue
        #next_way variable save the way we can go from train_map in last 
        #element of visited point
        next_way=train_map[now[0][-1]]
        #access in each element in next_way
        for i in next_way:
            #check if this way didn't travel before,then enqueue it into 
            #queue
            if i[0] not in now[0]:
                queue.append((now[0]+[i[0]],now[1]+[i[1]],now[2]+[i[2]]))
    #Sorting element from price return the best price way (return index 0)
    ans.sort(key=lambda x:calculate_price(x))
    print(len(ans))
    return ans
    
def find_pathway(starting_point,destination,all_lines=False):
    #Function to check condition of station (input) and run the process
    #Input:
    #   starting_point(integer)
    #   destination (integer)
    #output:
    #   1,2 or 3 if have error with starting_point or destination
    #   or string of step if index is normal
    
    #Call country(station number with name) from country.csv
    country_df=pd.read_csv("country.csv")
    #Check if starting_point not in list of country then return 1
    if starting_point not in list(country_df['index']):
        return 1;
    #check if destination not in list of country then return 2
    elif destination not in list(country_df['index']):
        return 2;
    #check if destination is same point as starting_point, then return 3
    elif starting_point == destination:
        return 3;
    #else return string of step to travel
    else:
        output= string_Price(find_pathway_until(int(starting_point),int(destination)))
        return output
    
#This condition use to run this file for main file only , for include or import
#will not run command below
if __name__ == "__main__":
    #print([i for find_pathway(36,26)])
    #for i in find_pathway(36,26):
    print(get_station())
    #print(get_station())