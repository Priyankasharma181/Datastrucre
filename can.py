Number = int(input("enter the number that how many element do you want in your List  :"))
newList = []
i = 0
while i<Number:
    elements = int(input("enter the element :"))
    newList.append(elements)
    i+=1
def birthdayCakeCandles(candles):
    count = 0 
    # maxHeight = max(candles)
    # for i in candles:
    #     if i == maxHeight:
    #         count += 1
    a = candles[0]
    i = 0
    while i<len(candles):
        if candles[i]> a:
            a = candles[i]
            count+=1
        i+=1    

    return 'tallest candels are {}'.format(count)
print(birthdayCakeCandles(newList))    

