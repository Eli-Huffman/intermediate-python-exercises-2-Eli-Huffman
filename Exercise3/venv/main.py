import numpy as np
import random

randomNum = []
npArray = np.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])

for i in range(10):
    randomNum.append(random.uniform(0.0,1.0))
print("Random Numbers: ")
print(randomNum)

npArray = np.sort(np.array(randomNum))

print("Mean:",npArray.mean())
print("Median:",(npArray[5]+npArray[6])/2)
print("Standard Deviation:",npArray.std())