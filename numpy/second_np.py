from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#NUMPY RANDOM MODULE
#To generate random integers between 0 and 100
x = random.randint(100)
print(x)
#The randint() method takes a size parameter where you can specify the shape of an array.
#1-D array 
rand_int = random.randint(100, size=(4))
print(rand_int)
#2-D array
rand_int2 = random.randint(100, size=(3, 4))
print(rand_int2)

#To generate float number between 0 and 1
y = random.rand()
print(y)
#The rand() method also allows you to specify the shape of the array.
#1-D array
rand_float = random.rand(5)
print(rand_float)
#2-D array
rand_float2 = random.rand(3, 2)
print(rand_float2)
#Note: You can also randomize a 3-D array

#To generate a random number from an available array
rand_choice = random.choice([12, 45, 23, 97, 56])
print(rand_choice)

#You can also specify the size of the array
rand_choice2 = random.choice([12, 45, 23, 97, 56], size=(3, 4))
print(rand_choice2)

print()
#DATA DISTRIBUTIONS
#Data Distribution is a list of all possible values, and how often each value occurs.
#Such lists are important when working with statistics and data science.
#The random module offer methods that returns randomly generated data distributions.

#Random Distribution
#A random distribution is a set of random numbers that follow a certain probability density function.
#Probability Density Function: A function that describes a continuous probability. i.e. probability of
#all values in an array.
#We can generate random numbers based on defined probabilities using the choice() method of the random module.

#The choice() method allows us to specify the probability for each value.
#The probability (p) is set by a number between 0 and 1, where 0 means that the value 
#will never occur and 1 means that the value will always occur.
#1-D array with defined probabilities
prob = random.choice([1, 3, 5, 7, 9], p=[0.2, 0.3, 0.4, 0.1, 0.0], size=(20))
print(prob)
#2-D array with defined probabilities
prob2 = random.choice([2, 4, 6, 8], p=[0.1, 0.2, 0.3, 0.4], size=(3, 4))
print(prob2)

#Random Permutation
#A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
#The NumPy Random module provides two methods for this: shuffle() and permutation().

#Shuffling Array
#The shuffle() makes changes the original array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
# random.shuffle(arr)
# print(arr)

#Permutation of Array
#The permutation() method returns a re-arranged array (and leaves the original array un-changed).
print(random.permutation(arr))
print(arr)


#SEABORN LIBRARY WITH RANDOM DISTRIBUTION
#Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding
#to the distribution of points in the array.
# sns.distplot([0, 1, 2, 3, 4, 5])
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

#NORMAL (GUASSIAN) DISTRIBUTION





