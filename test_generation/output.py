import unittest
import string
import re
from input import *
import itertools
class TestEquivalent(unittest.TestCase):
	pass
def bubbleSort(numbers): # Bubble Sort Algorithm
    nums = list(numbers)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if numbers[j][0] < numbers[i][0]:
                numbers[j], numbers[i] = numbers[i], numbers[j]

def split_seq(seq, size):
        newseq = []
        splitsize = 1.0/size*len(seq)
        for i in range(size):
                newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
        return newseq
def handlingDocstring(docstring):
    listString = string.split(docstring,'\n')
    for n,x in enumerate(listString):
            x = map(int, re.findall(r'\d+', x))
            listString[n] = x
    for x in listString :
        if len(x) == 0:
                listString.remove(x)
    for n,x in enumerate(listString) :
        if len(x) == 4:
            listString[n] = split_seq(x,2)
        if len(x) == 6:
            listString[n] = split_seq(x,3)
    for i in listString:
    	bubbleSort(i)
    for i in listString:
    	if len(i)==2:
    		if i[0][1]>=i[1][0]:
    			raise Exception("wrong input")
       	if len(i)==3:
         	if i[0][1]>=i[1][0] or i[1][1]>=i[2][0]:
         		raise Exception("wrong input")
    for i in listString:
        for j in i:
            j[0] = (j[0]+j[1])/2
            j.remove(j[1])
    for i in listString:
        if len(i) == 1:
            tg0 = i[0][0]
            i[0] = tg0
        elif len(i) == 2:
            tg0 = i[0][0]
            i[0] = tg0
            tg1 = i[1][0]
            i[1] = tg1
        else:
            tg0 = i[0][0]
            i[0] = tg0
            tg1 = i[1][0]
            i[1] = tg1
            tg2 = i[2][0]
            i[2] = tg2
    return listString
def test_generator(*l):
	def test(self):
		self.assertEqual(main(*l),"Ok!")
	return test
if __name__ == '__main__':
	ar = handlingDocstring(main.__doc__)
	if len(ar) == 1:
		for n,element in enumerate(itertools.product(ar[0])):
			test_name = 'test_%s' % n
			test = test_generator(element)
			setattr(TestEquivalent,test_name,test)
	elif len(ar) == 2:
		for n,element in enumerate(itertools.product(ar[0],ar[1])):
			test_name = 'test_%s' % n
			test = test_generator(element)
			setattr(TestEquivalent,test_name,test)        	
	elif len(ar) == 3:
		for n,element in enumerate(itertools.product(ar[0],ar[1],ar[2])):
			test_name = 'test_%s' % n
			test = test_generator(element)
			setattr(TestEquivalent,test_name,test)
	elif len(ar) == 4:
		for n,element in enumerate(itertools.product(ar[0],ar[1],ar[2],ar[3])):
			test_name = 'test_%s' % n
			test = test_generator(element)
			setattr(TestEquivalent,test_name,test)
	elif len(ar) == 5:
		for n,element in enumerate(itertools.product(ar[0], ar[1],ar[2],ar[3],ar[4])):
			test_name = 'test_%s' % n
			test = test_generator(element)
			setattr(TestEquivalent,test_name,test)
	elif len(ar) == 6:
		for n,element in enumerate(itertools.product(ar[0], ar[1],ar[2],ar[3],ar[4],ar[5])):
			test_name = 'test_%s' % n
			test = test_generator(element)
			setattr(TestEquivalent,test_name,test)
	elif len(ar) == 7:
		for n,element in enumerate(itertools.product(ar[0], ar[1],ar[2],ar[3],ar[4],ar[5],ar[6])):
			test_name = 'test_%s' % n
			test = test_generator(element)
			setattr(TestEquivalent,test_name,test)
	elif len(ar) == 8:
		for n,element in enumerate(itertools.product(ar[0], ar[1],ar[2],ar[3],ar[4],ar[5],ar[6],ar[7])):
			test_name = 'test_%s' % n
			test = test_generator(element)
			setattr(TestEquivalent,test_name,test)
	elif len(ar) == 9:
		for n,element in enumerate(itertools.product(ar[0], ar[1],ar[2],ar[3],ar[4],ar[5],ar[6],ar[7],ar[8])):
			test_name = 'test_%s' % n
			test = test_generator(element)
			setattr(TestEquivalent,test_name,test)
	elif len(ar) == 10:
		for n,element in enumerate(itertools.product(ar[0], ar[1],ar[2],ar[3],ar[4],ar[5],ar[6],ar[7],ar[8],ar[9])):
			test_name = 'test_%s' % n
			test = test_generator(element)
			setattr(TestEquivalent,test_name,test)
	unittest.main()