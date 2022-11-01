import glob
import os
import re

list_of_files = glob.glob('counters_*.log');  #here we look for counters*.log file in the current directory
latest_file = max(list_of_files, key=os.path.getctime); #select the latest file
print(latest_file) #it will show the latest modified file


#----list for date----
date_list=[];
#lsit for request --
request=[];

file=open(latest_file, "r"); # for open the input log file
initial_valOpen=open('initial_value.txt','r'); #for open file to write the previous state value
initial_valread=initial_valOpen.readline(); #this line read the previous state value from write file

#set condition for first time execution of the program or for the previous state empty
if(initial_valread==''):
	initial_valread='0';

lines=file.readlines() #it reads the logs files



#loop for split date and request count and append those value in a list
for line in lines:

	if 'Gy-CCR-Update.request' in line or 'Gy-CCR-Initial.request' in line or 'Gy-CCR-Termination.request' in line:
	
		split_test=line.split(",") #here we split the first line by ,
		date_list.append(split_test[0]); # we filter date and time  and keep it in the list
		requst_lastValue=split_test[len(split_test)-1]; #we filter the request and keep it in the list
		request.append(requst_lastValue);
		


#loop for summation of request and difference of current value with previous value

i=0;
for iterator in range(len(date_list)//3):
	current_state=0; #it is a counter for hold current state value
	
	if(date_list[i] == date_list[i+1] == date_list[i+2]):
		#print('date is matched');
		print('first:',request[i],' 2nd:',request[i+1],' 3rd:', request[i+2]);
		current_state=current_state+int(request[i])+int(request[i+1])+int(request[i+2]);
		print('current state: (sum of 3 request) : ',current_state);
		
		
	else:
		print('not matched')
	i=i+3; #we increment by 3 bcz we have three request

	print('difference',current_state - int(initial_valread));
	
	initial_valread=current_state; #assign current value as previous/initial value
	print('--Previous State----',initial_valread);
	
	
	
#this module for write the current value as previous in the file	
file_write=open('initial_value.txt','w')
file_write.write(str(initial_valread));



#for every open file. we need to close the file otherwise it may leak the memory
file_write.close()
initial_valOpen.close();				
file.close()


