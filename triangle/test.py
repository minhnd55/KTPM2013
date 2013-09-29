from triangle import detect_triangle
import math
import unittest
e = 10**(-9)
class testDetect_triangle (unittest.TestCase):
	
	def test_sai_kieu(self) :
		self.assertEqual(detect_triangle(2,3,5),"Wrong type!")
	def test_ngoai_bien(self) :
		self.assertEqual(detect_triangle(2**32.0,2**32.0,2**32.0),"Out of range!")
	
	def test_tam_giac_deu_nominal(self) :
		self.assertEqual(detect_triangle(3.0,3.0,3.0),"Tam giac deu!")
	def test_tam_giac_deu_just_above_minimum(self) :
		self.assertEqual(detect_triangle(1.0,1.0,1.0),"Tam giac deu!")
	def test_tam_giac_deu_just_below_maximum(self) :
		self.assertEqual(detect_triangle(2**32-2.0,2**32-2.0-e,2**32-2.0),"Tam giac deu!")
	
	def test_tam_giac_vuong_can_nominal(self) :
		self.assertEqual(detect_triangle(5.0,5.0,math.sqrt(50)),"Tam giac vuong can!")
	def test_tam_giac_vuong_can_just_above_minimum(self) :
		self.assertEqual(detect_triangle(1.0,1.0,math.sqrt(2)),"Tam giac vuong can!")
	

	def test_tam_giac_can_nominal(self) :
		self.assertEqual(detect_triangle(3.0,3.0,5.5),"Tam giac can!")	
	def test_tam_giac_can_just_above_minimum(self) :
		self.assertEqual(detect_triangle(1.0,1.0,1.5),"Tam giac can!")
	def test_tam_giac_can_just_below_maximum(self) :
		self.assertEqual(detect_triangle(2**32-2.0,2**32-2.0,1.0),"Tam giac can!")
	
	def test_tam_giac_vuong_nominal(self) :
		self.assertEqual(detect_triangle(3.0,4.0,5.0),"Tam giac vuong!")
	def test_tam_giac_vuong_just_above_minimum(self) :
		self.assertEqual(detect_triangle(1.0,1.1,math.sqrt(1.0+1.1*1.1)),"Tam giac vuong!")
	

	def test_tam_giac_thuong_nominal(self) :
		self.assertEqual(detect_triangle(2.0,3.0,4.0),"Tam giac thuong!")
	def test_tam_giac_thuong_just_above_minimum(self) :
		self.assertEqual(detect_triangle(1.0,1.1,1.2),"Tam giac thuong!")
	def test_tam_giac_thuong_just_below_maximum(self) :
		self.assertEqual(detect_triangle(2**32-3.0,2**32-4.0,2**32-5.0),"Tam giac thuong!")
	
	
	def test_khong_phai_tam_giac_nominal(self) :
		self.assertEqual(detect_triangle(10.0,10.0,100.0),"Khong phai tam giac!")
	def test_khong_phai_tam_giac_just_above_minimum(self) :
		self.assertEqual(detect_triangle(0.1,0.1,1.0),"Khong phai tam giac!")
	def test_khong_phai_tam_giac_just_below_maximum(self) :
		self.assertEqual(detect_triangle((2**32-1.0)/3,(2**32-1.0)/3,2**32-1.0),"Khong phai tam giac!")
	
if __name__ == '__main__':
	unittest.main()
