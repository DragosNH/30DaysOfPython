import numpy as np

# print('numpy:', np.__version__)

# print(dir(np))

# --- Creating int numpy arrays ---

python_list = [1, 2, 3, 4, 5]

# print(f"Type: {type(python_list)}")

# print(python_list)

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

# print(two_dimensional_list)

numpy_array_from_list = np.array(python_list)
# print(type(numpy_array_from_list))
# print(numpy_array_from_list)

# --- Creating float numpy arrays ---

numpy_array_from_list2 = np.array(python_list, dtype=float)
# print(numpy_array_from_list2)

# --- Creating boolean numpy arrays ---

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype = bool)
# print(numpy_bool_array)

# --- Creating multidimensional array using numpy ---

numpy_two_dimensional_list = np.array(two_dimensional_list)
# print(type(numpy_two_dimensional_list))
# print(numpy_two_dimensional_list)

# --- Converting numpy array to list ---
np_to_list = numpy_array_from_list.tolist()
# print(type (np_to_list))
# print('one dimensional array:', np_to_list)
# print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# --- Creating numpy array from tuple ---

python_tuple = (1,2,3,4,5)
# print(type(python_tuple))
# print(f'python_tuple: {python_tuple}')

numpy_array_from_tuple = np.array(python_tuple)
# print(type(numpy_array_from_tuple))
# print(numpy_array_from_tuple)

nums = np.array([1, 2, 3, 4, 5])
# print(nums)
# print('shape of nums: ', nums.shape)
numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
# print(numpy_two_dimensional_list)
# print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3], [4,5,6,7], [8,9,10,11]])
# print(three_by_four_array)
# print('shape of three_by_four_array: ', three_by_four_array.shape)


nums = np.array([1, 2, 3, 4, 5])
# print(nums)
# print('shape of nums: ', nums.shape)
numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
# print(numpy_two_dimensional_list)
# print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
    [4,5,6,7],
    [8,9,10,11]])
# print(three_by_four_array)
# print('shape of three_by_four_array: ', three_by_four_array.shape)


int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

# print(int_array)
# print(int_array.dtype)
# print(float_array)
# print(float_array.dtype)

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

# print('The size:', numpy_array_from_list.size) # 5
# print('The size:', two_dimensional_list.size)  # 3

# Mathematical Operation
# Addition
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
# print(ten_plus_original)

# Subtraction
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list  - 10
# print(ten_minus_original)

# Multiplication
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
# print(ten_times_original)

# Division
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
# print(ten_times_original)

# Modulus; Finding the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
# print(ten_times_original)

# Floor division: the division result without the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
# print(ten_times_original)

# Exponential is finding some number the power of another:
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list  ** 2
# print(ten_times_original)

#Int,  Float numbers
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

# print(numpy_int_arr.dtype)
# print(numpy_float_arr.dtype)
# print(numpy_bool_arr.dtype)

# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
# print('First row:', first_row)
# print('Second row:', second_row)
# print('Third row: ', third_row)

first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
# print('First column:', first_column)
# print('Second column:', second_column)
# print('Third column: ', third_column)
# print(two_dimension_array)

two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
# print(first_two_rows_and_columns)