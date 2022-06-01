# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 12:36:39 2022

@author: Mastoviti
"""




tocka=["001","001","110"]
build=["ABD","BAC","DCA"]
destroy=["ABD","BAC","DCA"]


red=0
stupac=0
cijena=0
rusenjecijena=0
cijena=[]
ukupnocc=0
x=0
brojgradova=0
brojac=0;

sumbuild=0
sumdestroy=0
nizbuild=[]
nizdestroy=[]




def getcijena(build,i,j):
    value=build[red][stupac]
    c=ord(value)-64
    return c



class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
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
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


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
             g.add_edge(red, stupac,cijena)
             nizdestroy.append([red,stupac,cijena])
             print(red,stupac,cijena,"red,stupac,cijena,destroy")
             stupac=stupac+1

        

    stupac=0
    red=red+1  
 
stupac=0
red=0
g.kruskal_algo()

for line in tocka:
    for x in line:
        if(red==stupac):
            stupac=stupac+1
        elif(x=="0"):
             cijena=getcijena(build,red,stupac)
             g.add_edge(red, stupac,cijena)
             nizdestroy.append([red,stupac,cijena])
             print(red,stupac,cijena,"red,stupac,cijena,build")
             stupac=stupac+1

        

    stupac=0
    red=red+1  
 
stupac=0
red=0
g.kruskal_algo()   
# for line in tocka:
#     for x in line:
#         if(red==stupac):
#             stupac=stupac+1
#         elif(x=="1"):
#             print()
        
nizdestroy=sorted(nizdestroy,key=lambda nizdestroy:nizdestroy[2],reverse=True)
nizbuild=sorted(nizbuild,key=lambda nizbuild:nizbuild[2])

x=g.kruskal_algo()