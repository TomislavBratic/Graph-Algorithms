# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def zadatak2():
    
    n=10
    x=1
    y=1
    
    
    
    for i in range(x,10):
        for j in range(0,x):
            if(x/2<=j+0.5):
                print(y%n)
                y=y-1;
            else:
                print(y%n)
                y=y+1;
                
        print("")
        x=x+2;
        y=i+1;
        
def main():
    zadatak2()       
        
if __name__ == "__main__":
    main()