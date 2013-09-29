import math
import decimal
e = 10**(-9)
decimal.ExtendedContext.prec = 50
def detect_triangle(a,b,c):
	if type(a)!= float and type(b)!= float and type(c)!= float:
		print "Wrong type!"
		return "Wrong type!"
	if a<0 or a>2**32-1  or b<0 or b>2**32-1 or c<0 or c>2**32-1 :
		print "Out of range!"
		return "Out of range!"
	if decimal.Decimal(a)<decimal.Decimal(b)+decimal.Decimal(c)\
	   and decimal.Decimal(b)<decimal.Decimal(a)+decimal.Decimal(c)\
	   and decimal.Decimal(c)<decimal.Decimal(a)+decimal.Decimal(b) :
		if a == b == c :
			print "Tam giac deu!"
			return "Tam giac deu!"
		elif a == b or b == c or a == c :
			if  math.fabs(decimal.Decimal(a)*decimal.Decimal(a) - (decimal.Decimal(b)*decimal.Decimal(b) + decimal.Decimal(c)*decimal.Decimal(c))) < decimal.Decimal(e) \
				or math.fabs(decimal.Decimal(b)*decimal.Decimal(b) - (decimal.Decimal(a)*decimal.Decimal(a) + decimal.Decimal(c)*decimal.Decimal(c))) < decimal.Decimal(e) \
				or math.fabs(decimal.Decimal(c)*decimal.Decimal(c) - (decimal.Decimal(b)*decimal.Decimal(b) + decimal.Decimal(a)*decimal.Decimal(a))) < decimal.Decimal(e) :
				print "Tam giac vuong can!"
				return "Tam giac vuong can!"
			else :
				print "Tam giac can!"
				return "Tam giac can!"
		elif math.fabs(decimal.Decimal(a)*decimal.Decimal(a) - (decimal.Decimal(b)*decimal.Decimal(b) + decimal.Decimal(c)*decimal.Decimal(c))) < decimal.Decimal(e) \
				or math.fabs(decimal.Decimal(b)*decimal.Decimal(b) - (decimal.Decimal(a)*decimal.Decimal(a) + decimal.Decimal(c)*decimal.Decimal(c))) < decimal.Decimal(e) \
				or math.fabs(decimal.Decimal(c)*decimal.Decimal(c) - (decimal.Decimal(b)*decimal.Decimal(b) + decimal.Decimal(a)*decimal.Decimal(a))) < decimal.Decimal(e) :
			print "Tam giac vuong!"
			return "Tam giac vuong!"
		else :
			print "Tam giac thuong!"
			return "Tam giac thuong!"
	else :
		print "Khong phai tam giac!"
		return "Khong phai tam giac!"
		
	