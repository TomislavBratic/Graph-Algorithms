# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:50:16 2022

@author: Mastoviti
"""




tocka=["001","001","110"]
build=["ABC","BAC","BCA"]
destroy=["ABC","BAC","BCA"]


red=0
stupac=0
cijena=0

cijena=[]
ukupnocc=0
x=0
y=0
brojgradova=0
brojac=0;

costdestroy=0
uktrosak=0
sumbuild=0
sumdestroy=0
nizbuild=[]
nizdestroy=[]


# def pronadinajmanucijenu(red,build):
#     stupac=0
#     stupac1=0
#     minn=[]
#     minn.append(ord(build[red][stupac])-64)
#     print(minn)
    
#     for x in build[red]:
#         if red==stupac:
#             minn.pop(stupac)
#             stupac=stupac+1
#         else:
#             min.pop()
      
#     print(red, stupac1, minn)
#     g.add_edge(red, stupac1, minn)      

    

def getcijena(build,i,j):
    value=build[red][stupac]
    c=ord(value)-65
    return c



class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w,c):
        self.graph.append([u, v, w,c])

    # Search function

    def find(self, parent, i):
       # print(i)
        if parent[i] == i:                      #preuzimanje unije
            #print(i,"je i koji se vraca")
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        ukupnorezultat=0
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        #print(self.graph)
        parent = []
        rank = []
        for node in range(self.V):
           # print(node,"je node")
            #print(self.V,"je self.V")
            parent.append(node)
            rank.append(0)
       # print(parent)    
        while e < self.V - 1:
            u, v, w,c= self.graph[i]
            i = i + 1
           # print(parent,"je parent")
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                #print(u,v,w,"je prvi x,y, cost")
                self.apply_union(parent, rank, x, y)
               
                if(c==0):
                    
                    ukupnorezultat=ukupnorezultat+w
                else:
                    
                    ukupnorezultat=ukupnorezultat-w
                print(result)
                
            # else:
            #    # print(u,v,w,"je drugi x,y,cost")
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))
        return ukupnorezultat            
        
        
        
        
for line in tocka:
    brojgradova=brojgradova+1;
    
#print(brojgradova,"je broj gradova")        
g = Graph(brojgradova)




 
for line in tocka:
    for x in line:
        if(red==stupac):
            stupac=stupac+1
        elif(x=="1"):
             cijena=getcijena(destroy,red,stupac)
             g.add_edge(red, stupac,cijena,1)
             print(red,stupac,cijena,"red,stupac,cijena,destroy")
             stupac=stupac+1
             sumdestroy=sumdestroy+cijena
            
        else:     
             cijena=getcijena(build,red,stupac)
             g.add_edge(red, stupac,cijena,0)
             print(red,stupac,cijena,"red,stupac,cijena,build")
             stupac=stupac+1
             y=y+cijena
             
            
    stupac=0
    red=red+1  
 
stupac=0
red=0

    
# for line in tocka:
#     for x in line:
#         if(red==stupac):
#             stupac=stupac+1
#         elif(x=="1"):
#             print()
        



x=g.kruskal_algo()

print(sumdestroy,"je sve jedinice")
print(y,"je sve nule")

print(x,"je Nakon Kruskala vrijednost")






     
        







