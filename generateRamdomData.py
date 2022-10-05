#!/usr/bin/env python
# coding: utf-8

# In[1]:


#the first step is to create some random data for our problem
#We assume N=6 nodes, M=2 (number of track)
#We also assume that c(i,j)=c(j,i) where c(i,j) is the cost (distance) from node i to j
import random
import numpy as np
import sys

#please ensure you have a folder named data in your workign directory

n = 6 # we generate a 6 node path 
NV=2 # number of trucks
file = "./data/data6n.txt"
M = np.zeros((n,n))
for i in range(0, n):
    for j in range(0, n):
        if i != j:
            M[i, j] = random.randint(1, n)   

np.savetxt(file, M, fmt='%d')

# to load the file:
# M=np.loadtxt("test.csv")


# In[2]:


#No we load the data
in_file = "./data/data6n.txt"
# the matrix of pairwise costs. this need not be a symmetric matrix but the diagonal entries are ignored
# and assumed to be zero (don't care)
M = np.loadtxt(in_file)


# In[3]:


M


# In[9]:


#We will be use pyQUBO to generate the QUBO for our model (see reference)
#Let's first write the Objective function
# min sum(c(i,j)*x(i,j,m))  therefore the obkjecitv functions takes the form
#c[0,1]*x[0,1,0]+c[0,2]*x[0,2,0]*+....+c[n-2,n-1,M-1]
# above is equiv to (x[i][j][m])
# c = dist from i to j
# m = truck

#lets build the objective matrix
#the objective matrix is a diagonal matrix
#also let's transofmr the variable x[i,j,m] in b[k]
#there wiull be N(N-1)*M/2 x[i,j,m] (with j>i) therefore in our case we will have 6*5*2/2=30
#this is the number of variable b, in other work b[k] with k in 0..29 (we will call 30 V)

#Lets define a function index(i,j,m,M,N)
#index is defined as follow
#index(i,j,m,N)=index(j,i,m,N)
#index is undefined for i=j
#index = int(i*N-i*(i+1)/2+j-(i+1))+m*N*(N-1)/2

def index(i, j, m, n):
    if i == j:
        raise ValueError
    elif i > j:
        return index(j, i, m, n)
    else:
        return int(i*n - i*(i+1)/2 + j - (i+1) +m*n*(n-1)/2)


# In[10]:


#lets define a distance vector
# M.shape returns dimensions of matrix M (n = number of rows, _ not interested in number of cols as matrix is square)
distance=[]
n, _ = M.shape
for i in range (0,n):
    for j in range (i+1,n):
        distance.append(M[i,j]+M[j,i])

        


# In[11]:


distance


# In[6]:


#we will use pyQUBO to creare our binary vector
from pyqubo import Array

V=len(distance*NV)
items = Array.create('b',shape=V,vartype="BINARY")


# In[ ]:


len(distance)


# In[ ]:


len(items)


# In[ ]:


15%15
    


# In[ ]:


Hobjective=sum(distance[i%len(distance)]*items[i] for i in range(V))


# In[ ]:


#lets now define the constraint
#All trucks have to leave and return to the depo (we assume node 0 is the depo)
#sum over j and over m  x[0,j,m]=2*M  (e.g. for 2 trucks sum(x[0,j,m])=4)

#using the pyqubo library

from pyqubo import Placeholder,Constraint

lmd=[]

for i in range(n):
    lmd.append(Placeholder("lmd_"+str(i))) # create a different lagrange placeholder for each node i
           
C=[] # vector of constraints


summa=[] # auxilliary vector for calcs

#i=o with 0 as the node depo                
for j in range(1,n):
            for m in range(NV):
                indx=index(0,j,m,n)
                #print(index(0,j,m,n),0,j,m)
                #print(distance[indx%len(distance)])
                #print(items[indx])
                summa.append(items[indx])

C.append(Constraint((sum(summa)-2*NV)**2,"depo_constraint"))


#for all other nodes
summa=[] #riazzeriamo la somma
for i in range(1,n):
    summa = []
    for j in range(n):
        if j!=i:
            for m in range(NV):
                indx=index(i,j,m,n)
                #print(index(i,j,m,n),i,j,m)
                #print(distance[indx%len(distance)])
                #print(items[indx])
                summa.append(items[indx])
    C.append(Constraint((sum(summa)-2)**2,"node_"+str(i)+"_constraint"))  

 
    
    


# In[ ]:


#now we can create the C constaint
ConstraintMatrix=0
for i in range(len(C)):
    ConstraintMatrix += lmd[i]*C[i]


# In[ ]:


model= (Hobjective+ConstraintMatrix).compile()


# In[ ]:


lmd_test_value=10
feed_dict={}
for i in range(len(lmd)):
    feed_dict['lmd_'+str(i)]=lmd_test_value


# In[ ]:


feed_dict


# In[ ]:


bqm= model.to_bqm(feed_dict=feed_dict)
bqm.normalize()

