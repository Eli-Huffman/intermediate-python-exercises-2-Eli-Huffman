import random
import time

fibNum = random.randint(15,35)
firstNum = 0
secondNum = 1
count = 0
combined = 0
fibList = [0,1]
startTime = time.perf_counter()

while count < fibNum:
    combined = firstNum + secondNum
    firstNum = secondNum
    secondNum = combined
    fibList.append(combined)
    count += 1

endTime = time.perf_counter()

print("Fibinachi Number(",fibNum,")","=",combined)
print("Fibinachi Number(",fibNum,")",endTime-startTime, "seconds")