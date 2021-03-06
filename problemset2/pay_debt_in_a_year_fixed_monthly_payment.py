'''           
	      Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310
      
                

                  
	      Test Case 2:
	      balance = 4773
	      annualInterestRate = 0.2
	      
	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 440
      
                

                  
	      Test Case 3:
	      balance = 3926
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 360
'''
balance = 3329
annualInterestRate = 0.2
'''
Function to calculate the least amount (+/- 10) of fixed montly payment to pay off 
the whole credit card balance in a year.
'''
def lowestPayment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    minimumFixedMonthlyPayment = 0
    remaining_balance = balance
	# this loop lets the balance be negative, but that's allright according to the excercise authors
    while remaining_balance > 0:
        minimumFixedMonthlyPayment += 10
        months = 12
        for i in range(months+1):
            if i == 0:
                remaining_balance = balance
            else:
                monthlyUnpaidBalance = remaining_balance - minimumFixedMonthlyPayment
                remaining_balance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
                #print("Month "+ str(i) + " Remaining balance: " + str(round(remaining_balance,2)))
    print("Lowest payment: " + str(minimumFixedMonthlyPayment))
lowestPayment(balance, annualInterestRate)