import os
#Function for mass renaming files inside a directory

directory = r"Directory"

for count, filename in enumerate(os.listdir(directory)):
    dst = filename.split("-")
    temp =dst[0]
    dst[0] =dst[-1]
    dst[-1] = temp
    dst = "-".join(dst)

    #os.rename(old path, new path) 
    os.rename(directory + filename, directory + dst)


