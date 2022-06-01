# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 20:21:32 2021

@author: Tomica
"""
def zadatak3_d():
    
    x=5
    y=100
    flag=0;
    arrnumber=[];
    br=0;
    br=0;
    
    for i in range(x,y):
        flag=0
        for j in range(2,int(i/2)):
            
            if(i%j==0):
               
               flag=1;
               
               
        if flag==0:
            arrnumber.append(i)
            br=br+1;                                                              
            
    print(arrnumber)  
    z=len(arrnumber)   
    flag=0;
    print("unesi paran broj:") 
    print("")
    broj=int(input())
    if(broj%2==1):
        print("unijeli ste neparan broj.")
    else:
        
        for i in range(0,z-1):
            for j in range(1+i,z):
                   if(arrnumber[i]+arrnumber[j]==broj):
                       print("brojevi",arrnumber[i],"i",arrnumber[j],"daju paran broj",broj)
                       flag=1;
                       
        if flag==0:
            print("nema parnog broja.")
            
def main():
    zadatak3_d()       
        
if __name__ == "__main__":
    main()           
            