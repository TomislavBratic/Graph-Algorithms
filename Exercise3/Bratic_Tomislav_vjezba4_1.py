# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def zadatak1():
    
    f=open("matrica.txt","r"); 
    summ=0;
    niz=[];
    
    for line in f:
        line=line.strip().split();
        print(line);
        for x in range(len(line)):
            summ=summ+int((line[x]));
            
        niz.append(summ);
        summ=0;
    print(niz);    

 
   
    
   
        
def main():
    zadatak1()     
    
    
        
if __name__ == "__main__":
    main()