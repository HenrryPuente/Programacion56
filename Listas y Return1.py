# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:08:48 2020

@author: PC
"""
#Henry Puente


def isYearLeap(year):
    if año % 4 != 0:
        return False
  elif año % 100 != 0:
     return True 
    elif año % 400 != 0:
     return False 
    else:
        return True
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")



