
file=open("sample.txt","r")
file2=open("report.txt","w")
d=dict()

for line in file:
    words=line.split()
    for word in words:  
        if word in d:
            d[word]=d[word]+1
        else:
            d[word]=1


   
    sorted_dict=dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
    for key,value in sorted_dict.items():
        entry=key+"|"+str(value)+'\n'
        file2.write(entry)

file.close()
file2.close()
