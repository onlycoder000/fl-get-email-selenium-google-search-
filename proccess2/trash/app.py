from duckduckgo_search import ddg
import csv
import time
import json


def s(keywords,f=0):
    f+=1
    results = ddg(keywords+' site:www.linkedin.com', max_results=10)
    if not results:
        print('#'+str(f)+' '+keywords+' Wating for ...')
        time.sleep(10)
        return s(keywords,f)
    return results


# with open('import.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for d in csv_reader:
#         if d[9] == False or d[9] == 'False':
#             vc=s(d[2]+' site:www.linkedin.com')
#         break
        

# vc=s('tdonnelly@westfieldbank.com')
# # j_data=json.loads(vc)
# print(vc)


results = ddg('tdonnelly@westfieldbank.com  site:www.linkedin.com', max_results=10)
print(results)