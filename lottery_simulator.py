# Lottery Simulator

import random

def lottery_numbers():
    lotteryNumbers =  [] 
    for number in range(0,6):
        number = random.randint(1,99)
        lotteryNumbers.append(number)
    return lotteryNumbers

def bettor(lottery):
    lotteryNumbers = lottery
    playerNumbers = lottery_numbers()
    numbersMatched = 0
    for number in range(0,6):
            #print(number)
            #print(number in lotteryNumbers)
        if number in lotteryNumbers:
            numbersMatched += 1 
        else:
            pass
        #print('MAtched: ',numbersMatched )
    
    if numbersMatched >= 3:
        print('you Win')
          
         
    if numbersMatched == 0:
        print('Lost')
        pass
 
lotteryNumbers = lottery_numbers()    
x=0
while x<10000:
    bettor(lotteryNumbers)
    x+=1    
