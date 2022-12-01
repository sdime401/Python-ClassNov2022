def copytor(lines):
        # open both files
    with open('file1.txt','r') as firstfile, open('file2.txt','a') as secondfile:
    # read content from first file
        for line in firstfile:
            secondfile.write(line) #Append content of the first file to the second file
    
copytor("line")