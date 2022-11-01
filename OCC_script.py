import glob
import os
import re

list_of_files = glob.glob('counters_*.log');  #here we look for counters*.log file in the current directory
latest_file = max(list_of_files, key=os.path.getctime);
print(latest_file)


#----list for date----
date_list=[];
#lsit for request --
request=[];


initial_value=0;

current_state=0;

match_string='Gy-CCR-.*request'
file=open('counters_2022110113.log', "r");
initial_valOpen=open('initial_value.txt','r');

initial_valread=initial_valOpen.readline();


print('------open file check')
print(initial_valread)
print(type(initial_valread));


lines=file.readlines()

for line in lines:

	if 'Gy-CCR-Update.request' in line or 'Gy-CCR-Initial.request' in line or 'Gy-CCR-Termination.request' in line:
		#print(line)
		#print('regex test')
		#num=re.findall(r'(\d+)(?!.*\d)', line)
		#print(num)
		#num = re.findall(r'\d+', line)
		#print(num[2])
		
		
		split_test=line.split(",")
		#print(split_test[0]) #for date 
		date_list.append(split_test[0]);
		requst_lastValue=split_test[len(split_test)-1];
		
		
		
		#print(requst_lastValue) #for last value
		request.append(requst_lastValue);
		
		
		#for date matchig
		#print('date matching----------------');
		#print(split_test[0]);
		#print(split_test[1]);
	
		#if(split_test[0]==split_test[1]):
			#print('date matching check');
		
		
print('-------------date & request value--------------');
print(request)
print(len(date_list));
int_convertion=int(request[0]);
print(type(initial_valread));
#print(request[0]);	

#print(request[0]);	


i=0;
for iterator in range(len(date_list)//3):
	if(date_list[i] == date_list[i+1] == date_list[i+2]):
		#print('date is matched');
		print('first:',request[i],' 2nd:',request[i+1],' 3rd:', request[i+2]);
		current_state=current_state+int(request[i])+int(request[i+1])+int(request[i+2]);
		print('sum of three 3 values');
		print(current_state);
	else:
		print('not matched')
	i=i+3;
	print('------------diffencece chck-------------')
	print(current_state-int(initial_valread));
	initial_value=initial_value+current_state;
	print('--initial value----',initial_value);
	
file_write=open('initial_value.txt','w')
file_write.write(str(initial_value));

file_write.close()
	
initial_valOpen.close();		
		
file.close()


