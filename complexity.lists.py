import time
import random

def append_time(lili,k) :
    lala = lili*1
    start = time.perf_counter() # first timestamp
    
    for i in range(k):
        lala.append("toto")

    end = time.perf_counter() # second timestamp

    elapsed = end - start
    print("elapsed time = {:.12f} seconds".format(elapsed))
    print("avg time for 1 append : ", elapsed/k)
    return lala 
    
def inserthead_time(lili,k) :
    lala = lili*1
    start = time.perf_counter() # first timestamp
    
    for i in range(k):
        lala.insert(0,"toto")

    end = time.perf_counter() # second timestamp

    elapsed = end - start
    print("elapsed time = {:.12f} seconds".format(elapsed))
    print("avg time for 1 append : ", elapsed/k)
    return lala 
    
def access_time(lili,k):
    lala = lili*1
    start = time.perf_counter() # first timestamp
    
    for i in range(k) :
        access = lala[random.randrange(0, len(lili))]
        
    end = time.perf_counter() # second timestamp
    elapsed = end - start
    print("elapsed time = {:.12f} seconds".format(elapsed))
    print("avg time for 1 append : ", elapsed/k)
    
def create_big_list_from_file(fichier,encodingdong) :
    fic=open(fichier,"r", 1024, encoding= encodingdong)
    lulu=[]
    for line in fic:
        lulu.append(fic.readline().rstrip())
    fic.close()
    return lulu

#Main Prog
l = ["haha", "hihi", "hoho", "huhu"]  
n = 1000000

#l_new = access_time(l,n)
#print(l)

aaa = create_big_list_from_file("words.txt","utf-8")
print(aaa[:20])

