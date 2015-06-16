import os
import exceptions

def retrieveFile():
    try:
        bestStudent={}
        # 'r' for read(default), 'w' for write, 'a' for append 
        f=open("studentgrade.txt")
    except(IOError),e:
        print "error here",e
    else:
        for line in f:
            name,grade=line.split()
            bestStudent[name]=grade
        f.close()

        outFile = open("studentranked.txt","w")
        for i in sorted(bestStudent.keys(),reverse=True):
            print i+" get "+bestStudent[i]
            outFile.write(i+" get "+bestStudent[i]+"\n")
        outFile.close()

def dirPlay():
    print os.listdir("c:\Intel")
    print os.path.isdir("c:\Intel")
    

         
def main():
    retrieveFile()

if __name__ =='__main__':main()
