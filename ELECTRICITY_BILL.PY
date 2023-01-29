# THIS IS THE CODE FOR AND CALCULATE TOTAL ELECTRICITY BILL ACCORDING TO THE GIVEN CONDITION

s=int(input('Enter the amount of units consumed'))

if s<= 50:
    amount = s*0.5
    print('amount is to be paid will be',amount)

elif s<= 150 and s > 50:
    amount = (50*0.5) + ((s-50)*0.75)
    print ('amount is to paid will be',amount)

elif s <= 250 and s > 150:
    amount = (50*0.5) + (100*0.75) + ((s-150)*1.2)
    print('amount is to paid will be',amount)

else:
    amount=(50*0.5) + (100*0.75) + (100*1.2) + ((s-250)*1.5)
    print('amount to be paid will be',amount)