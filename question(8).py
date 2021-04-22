# # f=open("preeti.text","x")
# # q.8Tumhare pass four employes ki details hai list mai:- ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and 
# # emp4. har ek employee ka dictionary main name,designation,age and salary honi chahiye. aur ye sab dictionary ki keys hai 
# # jismai maine list main value di hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai. \

# import json
# filename = 'preeti.txt'
# dict1 = {}
# fields =['name', 'Designation', 'age', 'salary']
# with open(filename) as fh:
#     l = 1
#     for line in fh:
#         description = list( line.strip().split(None, 4))
#         # print(description)
#         sno ='emp'+str(l)
#         i = 0
#         dict2 = {}
#         while i<len(fields):
#                 dict2[fields[i]]= description[i]
#                 i = i + 1
#         dict1[sno]= dict2
#         l = l + 1       
# out_file = open("Thakur.json", "w")
# json.dump(dict1, out_file, indent = 4)
# out_file.close()

import json
a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
e=["Abhishek","manager","29","63000"] 
de=["Name","desigtation","age","salary"]
dic={}
dic1={}
dic2={}
dic3={}
d={}
i=0
while i<len(a):
    j=0
    while j<len(a):
        dic[de[i]]=a[j]
        dic1[de[i]]=b[j]
        dic2[de[i]]=c[j]
        dic3[de[i]]=e[j]
        j+=1
    d["emp1"]=dic
    d["emp2"]=dic1
    d["emp3"]=dic2
    d["emp4"]=dic3
    i+=1
print(json.dumps(d,indent=4))
# aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4.
#  har ek employee ka dictionary main name,designation,
# age and salary honi chahiye. aur ye sab dictionary ki keys hai jismai
#  maine list main value di hai. Iska use kar ke aapko
#  ek json file create karni hai?