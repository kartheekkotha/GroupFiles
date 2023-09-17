import os

dict = {}
directory = str(input("Give the directory of all the files: "))
print(f"Total Number of files are: { len(os.listdir(directory))}")
for filename in os.listdir(directory):
    nameFile , extension = os.path.splitext(filename)
    if(os.path.isfile(os.path.join(directory,filename))):
        if(extension in dict):
            dict[extension]+=1 
        else:
            dict[extension] = 1

for i in dict:
    print(str(i) + ": " + str(dict[i]))

for newName in dict:
    path = os.path.join(directory , newName)
    if(os.path.exists(path)):
        pass
    else:
        os.mkdir(path)

for file in os.listdir(directory):
    if(file in dict):
        pass
    else:
        fileExtension = os.path.splitext(file)[1]
        newPath = os.path.join(directory , fileExtension)
        if(os.path.exists(newPath)):
            if(os.path.exists(newPath+file)):
                pass
            else:
                scr_path = os.path.join(directory,file)
                dst_path = os.path.join(newPath,file)
                os.rename(scr_path , dst_path)
        else:
            print("Error")
            break

for i in dict:
    newPath = os.path.join(directory,i)
    print(f"Number of elements in the folder {i} is: {len(os.listdir(newPath))}\tCount in dictonary : {dict[i]}")