import json
dic = {"name":"pooja","class":"12th","school":"g.g.s.s.s.school"}
file2=open("json_file1.json","w")
json.dump(dic,file2,indent=4)

file2.close()