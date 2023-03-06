import os
import shutil

def renameFile(path,format):
    count=0
    path=os.getcwd()+'/'+path
    for f in os.listdir(path):
        newf=f.replace(f,"%d."%count+format)
        count+=1
        print(f)
        if os.path.isfile(os.path.join(path,f))==True:
            print(1)
            os.rename(os.path.join(path,f),os.path.join(path,newf))
def creatFile(path):
    path=os.getcwd()+"/"+path
    if os.path.exists(path):
        print("rebuild",path)
        for f in os.listdir(path):
            f=os.path.join(path,f)
            os.remove(f)
        os.rmdir(path)
        os.makedirs(path)
    else :
        print("build",path)
        os.makedirs(path)

def moveFile(prePath,newPath):
    creatFile(newPath)
    prePath=os.getcwd()+"/"+prePath
    newPath=os.getcwd()+"/"+newPath
    for f in os.listdir(prePath):
        preF=os.path.join(prePath,f)
        newF=os.path.join(newPath,f)
        shutil.copyfile(preF,newF)
    print("successfully move ",prePath,"\nto ",newPath)

def rewriteBlock(path,startLine,endLine,code):
    path=os.getcwd()+"/"+path
    with open(path,"r",encoding='utf-8') as f:
        lines=[]
        for line in f.readlines():
            if line !='\n':
                lines.append(line)
    f.close()
    
    with open(path,"w",encoding='utf-8') as f:
            flag=0
            for line in lines:
                if line==startLine+'\n':
                    flag=1
                    f.write('%s\n'%startLine)
                    for newL in code:
                        f.write('%s\n'%newL)
                if line==endLine+'\n':
                    flag=0
                if flag==1:
                    continue
                else:
                    f.write('%s'%line)
    print('successfully write block! ',path)
    f.close()