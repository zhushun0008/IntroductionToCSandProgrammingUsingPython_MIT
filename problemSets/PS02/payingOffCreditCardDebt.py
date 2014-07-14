def payingTheMinimun(balance, annualInterestRate, monthlyPaymentRate):
    """
        balance - the outstanding balance on the credit card
        annualInterestRate - annual interest rate as a decimal
        monthlyPaymentRate - minmum monthly payment rate as a decimal
    """
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlypayment = balance * monthlyPaymentRate
    remainingBalance = balance - minimumMonthlypayment
    months = 12
    lastBalance = remainingBalance
    totalPaid = 0
    for i in range(months):
        totalPaid = totalPaid + minimumMonthlypayment
        print('Month :' + str(i + 1))
        print('Minimum monthly payment: ' + str(round(minimumMonthlypayment, 2)))
        currentBalance = lastBalance +  monthlyInterestRate * lastBalance
        print('Remaining balance: ' + str(round(currentBalance, 2)))
        minimumMonthlypayment = currentBalance * monthlyPaymentRate
        remainingBalance = currentBalance - minimumMonthlypayment
    
        lastBalance = remainingBalance
        
    print('Total paid: ' + str(round(totalPaid, 2)))
    print('Remaining balance: ' + str(round(currentBalance, 2)))
           
def payingDebtOffInOneYear(balance, annualInterestRate):
    """
        balance - the outstanding balance on the credit card
        annualInterestRate - annual interest rate as a decimal
    """
    monthlyInterestRate = annualInterestRate / 12.0
    fixedMonthlyPayment = 0
    remainingBalance = balance
    currentBalance = balance
    totalPaid = 0
    while currentBalance >= 0:
        fixedMonthlyPayment += 10 
        remainingBalance = balance - fixedMonthlyPayment
        months = 12
        lastBalance = remainingBalance
        for i in range(months):
            totalPaid = totalPaid + fixedMonthlyPayment
            print('Month :' + str(i + 1))
    
            currentBalance = lastBalance +  monthlyInterestRate * lastBalance
            print('Remaining balance: ' + str(round(currentBalance, 2)))
    
            remainingBalance = currentBalance - fixedMonthlyPayment
        
            lastBalance = remainingBalance

    return(fixedMonthlyPayment)
    
    
    
def payingDebtOffInOneYearWithBisctionSearch(balance, annualInterestRate):
    """
        balance - the outstanding balance on the credit card
        annualInterestRate - annual interest rate as a decimal
    """
    monthlyInterestRate = annualInterestRate / 12.0
    remainingBalance = balance

    totalPaid = 0
    lowBound = balance / 12.0
    upperBouund = (balance * (1+monthlyInterestRate)**12) / 12.0
    fixedMonthlyPayment = 0
    while True:
        currentBalance = balance
        fixedMonthlyPayment = (lowBound + upperBouund) / 2.0 
        remainingBalance = balance - fixedMonthlyPayment
        months = 12
        lastBalance = remainingBalance

        for i in range(months):
            totalPaid = totalPaid + fixedMonthlyPayment
            print('Month :' + str(i + 1))
            currentBalance = lastBalance +  monthlyInterestRate * lastBalance
            print('Remaining balance: ' + str(round(currentBalance, 2)))
            remainingBalance = currentBalance - fixedMonthlyPayment
            lastBalance = remainingBalance
            
        if  currentBalance >= 0 :
            lowBound = fixedMonthlyPayment
        elif currentBalance <= -1:
           upperBouund = fixedMonthlyPayment
        else :
            break 

    return(fixedMonthlyPayment)    
    
#payingTheMinimun(5000, 0.18, 0.02)
print('The lowest payment: ' + str(round(payingDebtOffInOneYearWithBisctionSearch(320000, 0.2), 2)))

