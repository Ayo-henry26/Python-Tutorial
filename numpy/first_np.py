import numpy as np
#NumPy (Numerical Python) is a library that works with arrays and this provides an object
#that is 50x faster than the traditional list. The object is called "ndarray"

arr = np.array([1, 2, 3, 4, 5])
#You can also pass a tuple but it will be convert to a list
arr2 = np.array((2, 4, 6, 8))
print(arr)
print(arr2)
# print(type(arr))
# print(np.__version__)

#DIMENSION IN ARRAYS
#NumPy provide the ndim attribute that returns an integer that tells you how many
#dimensions the array have.
#0-DIMENSIONAL / SCALERS ARRAYS
zero = np.array(26)
print(zero)
print(zero.ndim)

#1-DIMENSIONAL / UNI-DIMENSIONAL ARRAYS
one = np.array([5, 10, 15, 20, 25])
print(one)
print(one.ndim)

#2-DIMENSIONAL ARRAY / MATRIX
two = np.array([[0, 1, 2, 3, 4],
                 [5, 6, 7, 8, 9]]) # 2 x 5 matrix
print(two)
print(two.ndim)

#3-DIMENSIONAL ARRAY / MATRICES / MULTIPLE MATRIX
three = np.array([[[1, 2, 3], [4, 5, 6]],
                   [[7, 8, 9], [10, 11, 12]]])
print(three)
print(three.ndim)

#HIGHER DIMENSIONAL ARRAYS
higher = np.array([1, 2, 3, 4], ndmin=5)
print(higher)
print("No. of dimension: ", higher.ndim)

print()

#ACCESS ARRAY ELEMENTS
#1-DIMENSIONAL ARRAY
print(one[2])
print(one[4] - one[0] )

#2-DIMENSIONAL ARRAY
print(two[1, 2]) #two [row, column]
#You can also use negative indexing
print(two[0, -1])

#3-DIMENSIONAL ARRAY
print(three[1, 0, 2]) #three [matrix, row, column]

#ARRAY SLICING
#1-DIMENSIONAL ARRAY
sli = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(sli[2:8])
print(sli[:])#Slice throungh the whole array
print(sli[1:8:2])#Slice with step

#2-DIMENSIONAL ARRAY
sli2 = np.array([[10, 20, 30, 40],
                  [50, 60, 70, 80]])
print(sli2[1, 0:2]) #[slicing (through one row), indexing (multiple indexes)]
print(sli2[0:2, 1]) #[slicing (through both rows), indexing (one index)]
print(sli2[0:2, 2:4]) #[slicing (through both rows), indexing (multiple indexes)]


#DATA TYPES IN NUMPY
#NumPy arrays have a data type object (dtype) that provides information about the
#data types of the array elements.
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )
data = np.array([1, 2, 3, 4])
print(data.dtype)
data = np.array(['apple', 'banana', 'cherry'])
print(data.dtype)

#For i, u, f, S and U we can define size as well.
strings = np.array([2, 4, 6, 8], dtype = 'S')
print(strings)
print(strings.dtype)

integers = np.array([1, 2, 3, 4], dtype = 'i4')
print(integers)
print(integers.dtype)

#Converting Data Type on Existing Arrays
#valueError in NumPy
# error = np.array(['a', 3, 6], dtype='i')
# print(error)

#Using the astype()
#The astype() function creates a copy of the array, and allows you 
#to specify the data type as a parameter.
par = np.array([1.1, 2.1, 3.1])
new_par = par.astype('i') #You can use the datatype keyword (int)
print(new_par)
print(new_par.dtype)

par_bool = np.array([1, 0, 5])
new_par_bool = par_bool.astype(bool)
print(new_par_bool)
print(new_par_bool.dtype)

#COPY VS. VIEW
#The main difference between a copy and a view of an array is that
#a copy is a new array, and the view is just a view of the original array

#COPY: Changes in original doesn't affects the copy array
original = np.array([1, 2, 3, 4, 5])
copy_arr = original.copy()
original[0] = 38
print(original)
print(copy_arr)

#VIEW: Changes in both arrays affects both the original and view array
view_arr = original.view()
original[1] = 47
print(original)
print(view_arr)

#USING THE BASE ATTRIBUTE
#The base attribute returns None if the array owns the data.(copy array)
#And returns the original array if the array is a view of another array.
base = np.array([23, 54, 67, 82, 97])
base_copy = base.copy()
base_view = base.view()
print(base_copy.base) #None
print(base_view.base) #original array


#ARRAY SHAPE
#The shape of an array is the number of elements in each dimension.
#Dimensions are called axes in NumPy and dimension can be defined as 
#the number of indices needed to access an element in the array.
shape_arr = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8]])
print(shape_arr.shape)
shape_arr2 = np.array([1, 2, 3, 4, 5], ndmin=5)
print(shape_arr2.shape)

#ARRAY RESHAPE
#Reshaping means changing the shape of an array.

#Reshaping 1D array to 2D array
reshaped_2D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_reshaped_2D = reshaped_2D.reshape(3, 4) #3 rows and 4 columns
print(new_reshaped_2D)

#Reshaping 1D array to 3D array
reshaped_3D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_reshaped_3D = reshaped_3D.reshape(2, 3, 2) #2 matrices, 3 rows, and 2 columns
print(new_reshaped_3D)
#Yes, as long as the elements required for reshaping are equal in both shapes.
#We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array
#but we cannot reshape it into a 3 elements 3 rows 2D array as that
#would require 3x3 = 9 elements.

#Checking if the reshaped array returns copied or viewed
print(new_reshaped_3D.base)

#Unknown Dimension
#You are allowed to have one "unknown" dimension.
#Meaning that you do not have to specify an exact number for
#one of the dimensions in the reshape method.
#Pass -1 as the value, and NumPy will calculate this number for you.
#It is used for converting any array to a 1D array
unknown = np.array([[1, 2, 3],
                     [4, 5, 6]])
new_unknown = unknown.reshape(-1)
print(new_unknown)
# Note: There are a lot of functions for changing the shapes of arrays in numpy
# flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc.
# These fall under Intermediate to Advanced section of numpy.
print()

#Array Iterating
# Iterating means going through elements one by one.
# As we deal with multi-dimensional arrays in numpy, 
# we can do this using basic for loop of python.
#1-DIMENSIONAL ARRAY Looping
iter_arr_1D = np.array([10, 20, 30, 40, 50])
for i in iter_arr_1D:
    print(i)

#2-DIMENSIONAL ARRAY Looping
#It will go through a row when in 2D array
iter_arr_2D = np.array([[10, 20, 30],
                         [40, 50, 60]])
for j in iter_arr_2D:
    print(j)

#Iterating through each element in the 2D array (Scalar)
for j in iter_arr_2D:
    for k in j:
        print(k)

#3-DIMENSIONAL ARRAY Looping
iter_arr_3D = np.array([[[1, 2, 3], [4, 5, 6]],
                         [[7, 8, 9], [10, 11, 12]]])
for k in iter_arr_3D:
    print("K represents the 2D array: ")
    print(k)

#Iterating through each element in the 3D array (Scalar)
for k in iter_arr_3D:
    # print(k) prints of the Axis (0[slabs])
    for l in k:
        # print(l) prints of the Axis (1[rows])
        for m in l:
            print(m) # prints of the Axis (2[columns])

print()
#Using nditer()
#The nditer() function is a helping function that can be used from
#NumPy to iterate over multi-dimensional arrays.
#It provides a more efficient way to iterate through the elements
#of an array without the need for explicit loops.
nditer_arr = np.array([[[1, 2, 3], [4, 5, 6]],
                        [[7, 8, 9], [10, 11, 12]]])
for x in np.nditer(nditer_arr):
    print(x)

#Array With Different Data Types
#We can use op_dtypes argument and pass it the expected datatype
#to change the datatype of elements while iterating.
# NumPy does not change the data type of the element in-place 
# (where the element is in array) so it needs some other space to perform this action,
# that extra space is called buffer, and in order to enable it in nditer() 
# we pass flags=['buffered'].
dt_iter = np.array([1, 2, 3, 4])
for y in np.nditer(dt_iter, flags=['buffered'], op_dtypes=['S']):
    print(y)

#Iterating With Different Step Size
dif_arr = np.array([[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]])#Starts looping from 0 index of the 2 array
for x in np.nditer(dif_arr[:, ::2]):
    print(x)

#Enumerated Iteration Using ndenumerate()
#The ndenumerate() function is a helping function that can be used from
#NumPy to iterate over multi-dimensional arrays, providing both the index
#and the value of each element.
#You can use and dimesional array as well. (1D, 2D, 3D etc.)
enme_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
for index, val in np.ndenumerate(enme_arr):
    print(index, val)


#Joining NumPy Arrays
# Joining means putting contents of two or more arrays in a single array.
# In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
# We pass a sequence of arrays that we want to join to the concatenate() function, 
# along with the axis. If axis is not explicitly passed, it is taken as 0.

#1D ARRAY JOINING
conc_arr1 = np.array([1, 2, 3])
conc_arr2 = np.array([4, 5, 6])
new_conc = np.concatenate((conc_arr1, conc_arr2))
print(new_conc)

#2D ARRAY JOINING
#axis 0: Join along rows (vertically)
#axis 1: Join along columns (horizontally)
conc_2D_arr = np.array([[1, 2, 3], [4, 5, 6]])
conc_2D_arr2 = np.array([[7, 8, 9], [10, 11, 12]])
new_conc_2D_arr = np.concatenate((conc_2D_arr, conc_2D_arr2), axis=0)
print(new_conc_2D_arr)
new_conc_2D_arr = np.concatenate((conc_2D_arr, conc_2D_arr2), axis=1)
print(new_conc_2D_arr)

#Stacking Arrays
#Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

#1D ARRAY STACKING
stacked_1D = np.stack((conc_arr1, conc_arr2), axis=0)
print(stacked_1D)
stacked_1D = np.stack((conc_arr1, conc_arr2), axis=1)
print(stacked_1D)

#2D ARRAY STACKING
stacked_2D = np.stack((conc_2D_arr, conc_2D_arr2), axis=0)
print(stacked_2D)
stacked_2D = np.stack((conc_2D_arr, conc_2D_arr2), axis=1)
print(stacked_2D)

print()
#Stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows.
hstacked = np.hstack((conc_arr1, conc_arr2))
print(hstacked)

print()
#Stacking Along Columns
# NumPy provides a helper function: vstack() to stack along columns.
vstacked = np.vstack((conc_arr1, conc_arr2))
print(vstacked)

print()
#Depth Stacking
# NumPy provides a helper function: dstack() to stack along depth (third axis).
#1D Depth stacking
dstacked = np.dstack((conc_arr1, conc_arr2))
print(dstacked)
print(dstacked.shape)
#2D Depth stacking
dstacked_2D = np.dstack((conc_2D_arr, conc_2D_arr2))
print(dstacked_2D)
print(dstacked_2D.shape)


#Splitting NumPy Arrays
#Splitting is reverse operation of Joining.
#Joining merges multiple arrays into one, whereas splitting breaks one array into multiple sub-arrays.
#1D ARRAY SPLITTING
split_arr = np.array([1, 2, 3, 4, 5, 6])
new_split = np.array_split(split_arr, 3) #3 parts
print(new_split)
# Note: We also have the method split() available but it will not adjust the elements
# when elements are less in source array for splitting like in example above, array_split()
# worked properly but split() would fail.
#Accessing the splitted arrays
print(new_split[0])
print(new_split[1])
print(new_split[2])

#2D ARRAY SPLITTING using 2 elements in each block
split_arr_2D = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
new_split_2D = np.array_split(split_arr_2D, 3) #3 parts
print(new_split_2D)

#Using 3 elements
split_arr_2D_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_split_2D_2 = np.array_split(split_arr_2D_2, 3) #3 parts
print(new_split_2D_2)

#Splitting Along Columns
split_arr_2D_3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_split_2D_3 = np.array_split(split_arr_2D_3, 3, axis=1) #3 parts
print(new_split_2D_3)

#hSplit() function
hsplit_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_hsplit = np.hsplit(hsplit_arr, 3) #3 parts
print(new_hsplit)
#vSplit() function and dSplit() function also available for splitting along rows and depth respectively.

#Searching array
#You can search an array for a certain value, and return the indexes that
#contain that value using the where() function
#The where() function returns the indexes of the elements
search_arr = np.array([1, 2, 3, 4, 5, 4, 6, 7, 9, 8])
index = np.where(search_arr == 4)
print(index)

#Finding index of even numbers
num_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even = np.where(num_arr%2 == 0)
print(even)

#finding index of odd number
odd = np.where(num_arr%2 == 1)
print(odd)

#Search sorted array
#There is a method called searchsorted() which performs a binary search in the array,
#and returns the index where the specified value would be inserted to maintain the search order
sorted_arr = np.array([6, 7, 8, 8, 9, 10, 11])
x = np.searchsorted(sorted_arr, 8, side='right') #side can be 'left' (default) or 'right' 
print(x)

#Using multiple values
mul_sorted_arr = np.array([1, 3, 5, 7, 9])
sort = np.searchsorted(mul_sorted_arr, [2, 4, 6, 8])
print(sort)
#Note: The array must be sorted in ascending order before using the searchsorted() method.

#Sorting Arrays
#It means putting array in an ordered sequence. It can be ascending or descending.
#NumPy provides a method called sort() that will sort a specified array.
sort_arr = np.array([3, 6, 1, 8, 4, 2, 5, 7])
new_sort = np.sort(sort_arr)
print(new_sort)
#It returns a new array, leaving the original array unchanged.
#It can also be used on other data types, like strings
str_sort = np.array(['banana', 'date', 'apple', 'cherry'])
new_str_sort = np.sort(str_sort)
print(new_str_sort)
#And booleans
bool_sort = np.array([True, False, True, False])
new_bool_sort = np.sort(bool_sort)
print(new_bool_sort)

#Sorting 2D array
sort_2D_arr = np.array([[3, 7, 5], [8, 1, 4]])
new_sort_2D = np.sort(sort_2D_arr)
print(new_sort_2D)
#By default the sort() function sorts the array element along the last axis.

#Filtering Array
#Getting some elements out of an array and creating a new array out of them is called filtering.
#In NumPy we use boolean indexing to filter an array.
fil_arr = np.array([10, 15, 20, 25, 30, 35, 40])
fil = [True, False, True, False, True, False, True]
new_fil = fil_arr[fil]
print(new_fil)

#Creating a filter array using control structures
filter = np.array([30, 53, 45, 67, 89, 22, 96, 12])
filtered = []
for element in filter:
    if element > 50:
        filtered.append(True)
    else:
        filtered.append(False)
new_filter = filter[filtered]
print(filtered)
print(new_filter)

#Creating a filter directly from the array
even_filter = np.array([10, 23, 34, 45, 56, 67, 78, 89, 90])
show_filter = even_filter % 2 == 0
new_even_filter = even_filter[show_filter]
print(show_filter)
print(new_even_filter)



#Practicing the O(N) and O(log N) big O Notation
#O(N): Simple/linear search in an usorted array with calculating the all element
#in an array
def find_max(array):
    max = array[0]
    for element in array:
        if element > max:
            max = element
    return max


#SOME EXPLAINATION OF SECOND_NP

mult = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
mult2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])
print(mult * mult2)


#To retain a filtered array use the where()
age = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                [39, 22, 15, 99, 18, 19, 20, 21]])

adult = np.where(age >= 18, age, 0)
print(adult)


#How to generate random numbers in numpy
rng = np.random.default_rng(seed=1)#Seed used to reproduce the same result
print(rng.integers(low=1, high=101, size=3))#You can set the size to a 2D/ 3D array


#Random floating point numbers
np.random.seed(seed=1)
print(np.random.uniform(low=-1, high=1, size=(3, 2)))


#Shuffling an array
rng = np.random.default_rng(seed=1)
shuf = np.array([21, 17, 19, 20, 16, 30, 18, 65])
rng.shuffle(shuf)
print(shuf)

