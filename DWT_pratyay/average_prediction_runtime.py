text_file = "./log/out.txt"
keyword = "Time for Predicting the result"
keyword2 = " Seconds"
time_list = []

file = open(text_file, 'r')
lines = file.readlines()

for line in lines:
    if keyword in line:
       line1 = line.strip(keyword)
       seconds = line1.split(' ')
       time_list.append(seconds[0])

total_time = 0
for time in range(0,len(time_list)):
    total_time = total_time + float(time_list[time])
    

print("Average Prediction Time: " + str(total_time/len(time_list))+ " Seconds")
