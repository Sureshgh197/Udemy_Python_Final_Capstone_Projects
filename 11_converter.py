import sys

class Converter:
	
	def __init__(self,metric1,value):
		self.metric1=metric1
		self.value=value
		
		
		
	def temparatureConverter(self):
		# centigrade to fahrenhrit
		#fshrenheut to  centigrsde
		if self.metric1 == 1:
			###
			print(f'Fahrenheit of {self.value} °C is {(self.value*(9/5)+32)}')
		else:
			print(f'Fahrenheit of {self.value} °C is {(self.value-32)*(5/9)}')
			
	def convert_Length(self, m2):
	   Ll=['mm','cm','m','km']
	   m1v=self.value
	   m1=Ll[self.metric1-1]
	   m2t=Ll[m2-1]
	   SI ={'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000.}
	   print(m1v*(SI[m1]/SI[m2t]))
       
while True:
    	
		print('Choose the following Converters select corresponding numbers\n')
		cat = int(input('1. Temparature\n2. Length\n3. Mass\n4. Currency\n'))
		if cat == 1:
			print('Choose the following  available converters\n')
			metric1 = int(input('1. Centigrade to Fahrenheit\n2. Fahrenheit to Centigrade\n'))
			value = float(input('Enter the value:\n'))
			conv = Converter(metric1,value)
			conv.temparatureConverter()
			
			
		elif cat == 2:
			print('Choose the following  available converters\n')
			
			print('1. Millimeter\n2. Centimeter\n3. Meter\n4. Kilometer')
			
			m1=int(input('Please privide the From converter: Eg: 3 for meter\n'))
			m1v=float(input('Please provide from Value'))
			
			m2=int(input('Please privide the To converter:\n'))
			conv = Converter(m1,m1v)
			conv.convert_Length(m2)
	
			
			
		
		