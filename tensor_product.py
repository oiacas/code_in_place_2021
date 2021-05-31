# TENSOR PRODUCT AND MATRIX MULTIPLICATION WITHOUT USING NumPy

# This program is capable of asking if the user wants to perform a multiplication or an outer product (in this case, we can call it tensor product or Kronecker product as well) between two matrices and check if the operation is possible. After the desired result is shown, the user will be able to continue realizing new operations.

#The next step will be implementing operations with matrices whose elements can be complex numbers or other matrices. Then add the possibility of using the result from the last operation in the next one.



def desired_operation():
    #the function asks the user if the intended operation is a matrix multiplication or a tensor product
    #returns the desired operation

    operation = 0
    while operation != '1' and operation != '2' and operation != '': 
        operation = input('Type 1 for matrix multiplication, 2 for tensor product or just hit the enter key to end the program: ')
        if operation == '1':
            return '1'
        if operation == '2':
            return '2'
        if operation == '':
            break


def ask_matrices_size():
    #if performing a multiplication, asks the user for the sizes of the matrices and returns a list 
    #list[0]: number of rows of the first matrix
    #list[1]: number of columns of the first matrix
    #list[2]: number of rows of the second matrix
    #list[3]: number of columns of the second matrix

    matrix_a_rows = int(input('Enter the number of rows of the first matrix: '))
    matrix_a_columns = int(input('Enter the number of columns of the first matrix: '))
    matrix_b_rows = int(input('Enter the number of rows of the second matrix: '))
    matrix_b_columns = int(input('Enter the number of columns of the second matrix: '))
    dimensions = [matrix_a_rows, matrix_a_columns, matrix_b_rows, matrix_b_columns]

    return dimensions


def check_multiplication_possible(matrix_a_columns, matrix_b_rows):
    #this function checks if the multiplication between two matrices is possible.
    #first parameter: the quantity of columns of the first matrix
    #second parameter: the quantity of rows of the second matrix
    #The operation is possible only if the two parameters are equal
    #the function returns True if the operation is possible or False if not possible

    if matrix_a_columns == matrix_b_rows:
        print('\nThe two matrices can be multiplied.\n')
        return True
    else:
        print('\nThe two matrices can\'t be multiplied. Please enter possible values to their dimensions.\n')
        return False


def generate_blank_matrix_multiplication(matrix_a_rows, matrix_b_columns):
    #if the multiplication between the two matrices is possible, this function is called to generate an empty matrix with the correct dimensions for the result matrix
    #the function returns a blank matrix with height equal to the number of columns of the first matrix and width equal to the number of lines of the second matrix
    final_matrix = [ [ 0 for j in range(matrix_b_columns) ] for i in range(matrix_a_rows) ]
    return final_matrix


def generate_matrix(matrix_rows, matrix_columns):
    #this function first generates a blank matrix with the correct dimensions according to the parameters
    #first parameter: number of rows of the matrix
    #second parameter: number of columns of the matrix
    #then the user is aked to input the values of each element of the matrix
    #finally, the full matrix is returned

    matrix = [ [ 0 for j in range(matrix_columns) ] for i in range(matrix_rows) ] 

    for i in range(matrix_rows):
        for j in range(matrix_columns):
            matrix[i][j] = float(input(f'Enter the value (real) of the element ({i},{j}): '))

    print('MATRIX: ')
    for line in matrix:
        print(line)

    return matrix


def perform_multiplication(matrix_a, matrix_b):
    #this function takes as parameters the matrices that the user wants to multiply
    #a blank result matrix with the correct dimensions is generated using a previous helper function
    #then, the function iterates through the rows and columns of the two matrices, performing the necessary operations to conclude the multiplication
    #the elements of the result matrix receive the correct values, generating a final matrix that is printed and returned


    matrix_a_rows = len(matrix_a)
    matrix_b_columns = len(matrix_b[0])
    matrix_b_rows = len(matrix_b)
    final_matrix = generate_blank_matrix_multiplication(matrix_a_rows, matrix_b_columns)
    
    # iterate through rows of A:
    for i in range(matrix_a_rows):
        # iterate through columns of B:
        for j in range(matrix_b_columns):
            # iterate through rows of B:
            for k in range(matrix_b_rows):
                final_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

    print('MULTIPLICATION RESULT: ')
    for line in final_matrix:
        print(line)

    return final_matrix


def matrix_multiplication():
    #this function utilizes the previous helper functions in te correct order to perform a multiplication between two matrices
    print()
    print('So let\'s multiply two matrices!')
    print()
    possibility = False
    while possibility == False:
        dimensions = ask_matrices_size()
        #dimensions[matrix_a_rows, matrix_a_columns, matrix_b_rows, matrix_b_columns]
        matrix_a_rows = dimensions[0]
        matrix_a_columns = dimensions[1]
        matrix_b_rows = dimensions[2]
        matrix_b_columns = dimensions[3]
        possibility = check_multiplication_possible(matrix_a_columns, matrix_b_rows)
    print('Let\'s generate the first matrix: ')
    matrix_a = generate_matrix(matrix_a_rows, matrix_a_columns)
    print()
    print('Now let\'s generate the second matrix: ')
    matrix_b = generate_matrix(matrix_b_rows, matrix_b_columns)
    print()
    final_matrix = perform_multiplication(matrix_a, matrix_b)
    print()
    return final_matrix
    


#def generate_blank_matrix_tensor_product(matrix_rows, matrix_columns):
    #function utilized in a previous version of the program, discontinued due to not being necessary anymore
    #this function is called to generate an empty matrix with the correct dimensions for the result matrix of a tensor product
    #the parameters are the numbers of rows and columns of the final matrix 
    #the empty matrix is returned in the end


    #   final_matrix = [ [ 0 for j in range(matrix_columns) ] for i in range(matrix_rows) ]
    #   return final_matrix


def perform_tensor_product(matrix_a, matrix_b):
    #this function takes as parameters the matrices with wich the user wants to apply a tensor product (Kronecker Product)
    #a blank result matrix with the correct dimensions is generated using a previous helper function
    #then, the function iterates throug the rows and columns of the two matrices, performing the necessary operations to conclude the tensor product
    #the elements of the result matrix receive the correct values, generating a final matrix that is printed and returned

    
    #in the tensor product, each element of the final matrix is an element of the first matrix multiplied by a certain element of the second
    #EXAMPLE:  A = |a0,0  a0,1|     B = |b0,0|       A(tensorproduct)B = |(a0,0 * b0,0)  (a0,1 * b0,0)| = |ab0,0  ab0,1|
    #              |a1,0  a1,1|         |b1,0|                           |(a0,0 * b1,0)  (a0,1 * b1,0)|   |ab1,0  ab1,1|
    #                                                                    |(a1,0 * b0,0)  (a1,1 * b0,0)|   |ab2,0  ab2,1|
    #                                                                    |(a1,0 * b1,0)  (a1,1 * b1,0)|   |ab3,0  ab3,1|
    #
    #
    #          A_dimension: 2x2     B_dimension: 2x1             A(tensorproduct)B_dimension = 4x2


    # I decided to keep more verbose ways of calculating the Kronecker Product as a reference for how the writing of this program evolved. I utilized a series of iterations and a heper function to perform the calculation, as follows:


 #   VERSION 1:
 #   matrix_a_rows = len(matrix_a)
 #   matrix_a_columns = len(matrix_a[0])
 #   matrix_b_rows = len(matrix_b)
 #   matrix_b_columns = len(matrix_b[0])

 #   final_matrix_rows = matrix_a_rows * matrix_b_rows
 #   final_matrix_columns = matrix_a_columns * matrix_b_columns

    
    # final_matrix = generate_blank_matrix_tensor_product(final_matrix_rows, final_matrix_columns)  
   
 #   # i iterates through rows of A:
 #   for i in range(matrix_a_rows):
 #       # k iterates throughr rows of B:
 #     for k in range(matrix_b_rows):
 #           # j iterates through columns of A:
 #           for j in range(matrix_a_columns):
 #               # l iterates through columns of B:
 #               for l in range(matrix_b_columns):
 #                   # Each component of matrix A is multiplied by the matrix B
 #                   # The results are then assigned to the final_matrix
 #                   final_matrix[i + l + 1][j + k + 1] = matrix_a[i][j] * matrix_b[k][l]
 #                   #print(final_matrix[i + l + 1][j + k + 1]) 


 #--------
 # VERSION 2: 

 #   final_matrix = []
 #   aux_matrix = []

    #    count = len(matrix_b)
    
    #    for element_a in matrix_a:
    #        counter = 0
    #        check = 0
    #        while check < count:
    #            for num_a in element_a:
    #                for num_b in matrix_b[counter]:
    #                    aux_matrix.append(num_a * num_b)
    #            counter += 1
    #            final_matrix.append(aux_matrix)
    #            aux_matrix = []
    #            check +=1

    
    #FINAL VERSION, utilizing nested comprehensive lists:

    final_matrix = [[num_a * num_b for num_a in element_a for num_b in matrix_b[row]] for element_a in matrix_a for row in range(len(matrix_b))]
 
 
    

    print('\nTENSOR PRODUCT RESULT: \n')
    for line in final_matrix:
        print(line)
    print()

    return final_matrix



def tensor_product():
    #this fuction calls other helper functions to generate two matrices and realize a tensor product between the two of them

    print()
    dimensions = ask_matrices_size()
    #dimensions[matrix_a_rows, matrix_a_columns, matrix_b_rows, matrix_b_columns]
    matrix_a_rows = dimensions[0]
    matrix_a_columns = dimensions[1]
    matrix_b_rows = dimensions[2]
    matrix_b_columns = dimensions[3]
    print('\nSo let\'s calculate the tensor product between two matrices with real components!\n')
    print()
    print('Let\'s generate the first matrix: ')
    matrix_a = generate_matrix(matrix_a_rows, matrix_a_columns)
    print()
    print('Now let\'s generate the second matrix: ')
    matrix_b = generate_matrix(matrix_b_rows, matrix_b_columns)
    print()
    final_matrix = perform_tensor_product(matrix_a, matrix_b)
    return final_matrix



def main():
    print()
    print('Stanford University')
    print('CODE IN PLACE -- MAY 2021 -- FINAL PROJECT')
    print('MATRIX MULTIPLICATION and TENSOR PRODUCT CALCULATOR')
    print('----------------------------')
    print('Author: Caio Adriano Silvano')
    print('----------------------------')
    print()
    while True:
        print()
        operation = desired_operation()
        if operation == '1':
            result = matrix_multiplication()
        if operation == '2':
            result = tensor_product()
        more_operations = input('\nDo you want to perform another operation(y/n)? ')
        print()
        if more_operations != 'y' and more_operations != 'Y':
            break


if __name__ == '__main__':
    main()