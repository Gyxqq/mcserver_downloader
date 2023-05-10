#打开https://mcversions.net/
import copy
import requests
import re

def gethtml(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"
a=gethtml("https://mcversions.net/")
#在a里面匹配/download/*.*
c=re.findall("/download/[0-9.]+",a)
b=list(set(c))
#打开download.txt
f=open("download.txt","w")
b.sort(key=c.index)
out=copy.copy(b)
for i in range(len(b)):
    b[i]="https://mcversions.net"+b[i]
    now=gethtml(b[i])
    print(now)
    # input()
    #https://piston-data.mojang.com/v1/objects/8f3112a1049751cc472ec13e397eade5336ca7ae/server.jar
    down=re.findall("https://piston-data.mojang.com/v1/objects/[0-9a-z]+/server.jar",now)
    down=list(set(down))
    down.sort(key=now.index)
    if len(down)==0:
        down=re.findall("https://launcher.mojang.com/v1/objects/[0-9a-z]+/server.jar",now)
        down=list(set(down))
        down.sort(key=now.index)        
    f.write(down[0]+"\n")
    f.write(" out=server_"+out[i][10:]+".jar"+"\n")
    print(down[0])




  





