import csv
import os
from datetime import datetime

line_count=0
found=0
not_found=0

with open('Financelobby Scrap.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for d in csv_reader:
        x=d[2]
        path = "data/"
        dir_list = os.listdir(path)
        n=False
        for dir in dir_list:
            with open('data/'+dir) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                
                for c in csv_reader:
                    if(c[10].find(x) != -1):
                        n=c[9]
                        break
                    elif c[13].find(x) != -1:
                        n=c[9]
                        break
                    elif(c[10] == x):
                        n=c[9]
                        break
                    elif c[13] == x:
                        n=c[9]
                        break
                    
        if n:
            found+=1
        else:
            not_found+=1
        
        d.append(n)
        with open('output.csv', mode='a') as open_file:
            open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            open_writer.writerow(d)
        line_count+=1

        
        print('scan='+str(line_count)+' found='+str(found)+' not-found='+str(not_found)+' time='+datetime.now().strftime("%H:%M:%S"))
        
        
        