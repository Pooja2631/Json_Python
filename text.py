file=open("text_json.txt","r")
list1=[]
for line in file:
    stripped=line.strip()
    line_list=stripped.split()
    list1.append(line_list)

file.close()
print(list1)