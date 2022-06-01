
"""
Created on Wed Dec  8 10:03:00 2021

@author: Mastoviti
"""
def zadatak1():
    import numpy as np
    
    
    def euler(i,temp,visited,path=[]):
        counter=-1
        path.append(i)
        for x in temp[i]:
            counter=counter+1;
            if(x==0):
                continue
            else:
                 
                 if visited[i][counter]==0:
                     visited[counter][i]=1
                     visited[i][counter]=1
                     #print(visited)
                     path=euler(counter,temp,visited,path)    
                   
        return(path)            
                  
    def check(arrodd):
       counter=0
       for x in arrodd:
           if(x%2==1):
               counter=counter+1
           else:
               continue;
               
       if(counter>2):
           return 0
       else:
           return 1
               
        
    def ispisrjesenje(arr,counter,brojac):
        y=0;
        print(arr)
        for x in arr:
            y=y+1;
        print("\n")
        print(y-1,"je broj bridova koje se prošlo")
        if(y-1==brojac):
            print("funkcija je uspješno prošla kroz sve točke")
        
        
    
    def findvertices(f):
        for lines in f:
            b=lines.strip().split()
            for x in range(len(b)):
                    if b[x]=='*Vertices':
                            y=int((b[x+1]));
                        
        f.close()
        return y    
        
    
    def listasusjedstva(f,niz,brojac,y):
                          
        with open('euler_net.txt') as f:
            for i in range(y+2):
                next(f)
            for line in f:
                        
                   b=line.strip().split()
                   if(b[0]=="*Edges"):
                       break;
                   else:
                        niz.append([b[0],b[1]])
                        brojac=brojac+1
        return brojac                   
    
    
    def matricasusjedstva(matrix,niz):
        for a,b in niz:
            a=int(a)
            b=int(b)
            matrix[a][b]=1
            matrix[b][a]=1
    
    
    def matricaincidencije(matrix1,niz):   
        x=0
        for a in niz:
            matrix1[x][int(a[0])]=1;
            matrix1[x][int(a[1])]=1;
            x=x+1
    
    
    def ispis(matrixtest):
        for line in matrixtest:
            print(line)
    
    
    
    def pronadimax(matrixtest,maxx):
        summ=0
        for line in matrixtest:
            for x in line:
                x=int(x)
                summ=x+summ;
               
            if maxx<summ:
                maxx=summ
            
            arrodd.append(summ)        
            summ=0        
            
        return(maxx)     
    
    def pronadigraf(matrix,visited,arrodd,y):
        
        temp=matrix
        counter=-1
        checkifeuler=0
        checkifeuler=check(arrodd)
        arr=[]
    
       
        for x in arrodd:
            counter=counter+1
            if(arrodd[counter]==0):
                print("tocka",counter,"nema susjede")
            elif(checkifeuler==1):
                   arr1=euler(counter,temp,visited,arr)
                   ispisrjesenje(arr1,counter,brojac)
                   print(visited)
                   
            else:
                print("Ovo nije eulerov graf!!")
                break;
        
            arr=[]
            visited=np.zeros((y+1,y+1),dtype=int)      
        
    
    
    f=open("euler_net.txt","r")
    i=0;
    niz=[]
    arrodd=[]
    brojac=0
    maxx=0
    
    y=findvertices(f)
    #print("broj vrhova u grafu je:",y)
    
    brojac=listasusjedstva(f,niz,brojac,y)
    
    #print("LISTA SUSJEDSTVA:\n")
    #print(niz)
    
    matrix = np.zeros((y+1,y+1),dtype=int)
    matrix1=np.zeros((brojac,y+1),dtype=int)
    
    matricasusjedstva(matrix, niz)
    print("MATRICA SUSJEDSTVA:\n")
    ispis(matrix)
    
    print(brojac,"je broj bridova")
    matricaincidencije(matrix1, niz)
    #print("MATRICA INCIDENCIJE:\n")
    #ispis(matrix1)
    
    visited=np.zeros((y+1,y+1),dtype=int)
    maxx=pronadimax(matrix,maxx)
    print("stupanj svakog vrha:\n")
    print(arrodd)
    print("maksimalni broj bridova je:",maxx)
    
    pronadigraf(matrix, visited, arrodd,y)



        
def main():
    zadatak1()     
    
    
        
if __name__ == "__main__":
    main()








      
    
    
    
    




                    


    




    
  
    



