import time
import random
import doctest

def append_time(lili,k) :

	""" Function that calculates the time it needs to append a certain number of items.

	Args:
		lili (list)	: 	List of items.
		k (int)		:	Number of time "toto" is appended in the list.
	
	Returns:
		lala (list)	:	List of the initial list lili with k times "toto" added to it.

	DocTest:
		>>> hw = ["Hello", "world"]
		>>> i = 3
		>>> xhw = append_time(hw, i)
		>>> xhw == ["Hello","world","toto","toto","toto"]
		True
	"""

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

	""" Function that calculates the time it needs to append a certain number of items at the begining of a list.

	Args:
		lili (list)	: 	List of items.
		k (int)		:	Number of time "toto" is appended in the list.
	
	Returns:
		lala (list)	:	List of the initial list lili with k times "toto" added to it at the begining.

	DocTest:
		>>> hw2 = ["Hello", "world"]
		>>> j = 3
		>>> xhw2 = inserthead_time(hw2, j)
		>>> xhw2 == ["toto","toto","toto","Hello","world"]
		True
	"""

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

	""" Function that calculates the time it needs to access random values in a list.

	Args:
		lili (list)	: 	List of items.
		k (int)		:	Number of random values you want to access.
	
	Returns:
		None.

	DocTest:
		>>> hw3 = ["Hello", "world","toto","titi","tutu"]
		>>> m = 3
		>>> access_time(hw3, m)
	"""

	lala = lili*1
	start = time.perf_counter() # first timestamp
    
	for i in range(k) :
		access = lala[random.randrange(0, len(lili))]
        
	end = time.perf_counter() # second timestamp
	elapsed = end - start
	print("elapsed time = {:.12f} seconds".format(elapsed))
	print("avg time for 1 append : ", elapsed/k)
    
def create_big_list_from_file(fichier,encodingdong) :

	""" Function that creates a list from a file taking every line as item. 

	Args:
		fichier	(file path)	: 	File containing the items in line.
		encodingdong (string)	:	Encoding of the file.
	
	Returns:
		lulu (list)		:	List of the items contained in the file.
	
	DocTest:
		>>> xhw4 = create_big_list_from_file("petit_test.txt", "utf-8")
		>>> xhw4 == ["Hello","world","coucou"]
		True
	"""

	fic=open(fichier,"r", 1024, encoding= encodingdong)
	lulu=[]
	for line in fic:
		lulu.append(fic.readline().rstrip())
	fic.close()
	return lulu

#Main Prog
l = ["haha", "hihi", "hoho", "huhu"]  
n = 1000000
doctest.testmod()
#l_new = access_time(l,n)
#print(l)

#aaa = create_big_list_from_file("words.txt","utf-8")
#print(aaa[:20])

