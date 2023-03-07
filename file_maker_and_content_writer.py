"""
Created on Tue Mar  7 14:00:10 2023

@author: Mokhtar Mahmoudian === Mokhy31@gmail.com
"""
n = input("please enter the number of files you want to create : ")
list_of_files = []
for i in range(int(n)):
    list_of_files.append("file"+str(i)+".txt")
    

def file_maker():
        for item in list_of_files:
                  with open(item, "w") as f:
                      f.write(input(f"please enter the content of {item} : "))

def file_reader():
    for i in list_of_files:
        with open(i) as f:
                    content = f.read()
                    splited_file = content.split(" ") # the splited file is a list
                    print(f"{i} has {len(splited_file)} words")
                    horof =[]
                    for j in content:
                        if j !=" " :
                            horof.append(j)
                    print(f"{i} has {len(horof)} letters")        
file_maker()
file_reader() 
