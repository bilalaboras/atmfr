class  ATM:
	"""docstring for  """
	def __init__(self, balance, bank_name):
		self.withdrawls_list =[]
		self.balance=balance
		self.bank_name= bank_name
	def show_withdrawls(self):
		for withdrawal in self.withdrawls_list:
			print(withdrawal)
	
	def withdraw(self, request):
		
		print  "Current balance = "+str(self.balance)
		print "Welcome to "+ self.bank_name

		
		result =self.balance
		balance=self.balance

		if request > self.balance :
			print "Can't give you all this money !!"

		elif request < 0:	
			print "More than zero plz"

		else:
			result = self.balance - request
			self.withdrawls_list.append(request)

			while request >0:

				if request >=100:
					 request-=100
					 print "give 100 "

				elif request >=50:
				  	  request-=50
				  	  print "give 50"

				elif request >=10:
				  	  request-=10
				 	  print "give 10"

				elif request >= 5:
				  	  request -=5
				  	  print "give 5"

				elif request < 5:
					 print "give "+ str(request)
					 request = 0
		return result

	


balance1= 1000
balance2 = 5000

atm1 = ATM(balance1, "Smart Bank")

atm2 = ATM(balance2, "Baraka Bank")	


atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)


	
				

		
	
	    


		  
		 
		