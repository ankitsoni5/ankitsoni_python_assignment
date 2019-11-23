from com.ankit.utility.matrix_utility import matrix_addition,matrix_multiplication,matrix_transpose,get_matrix

print("Please provide the input for Matrix :- ")
row1 = int(input("Enter rows for: "))
col1 = int(input("Enter columns: "))

print("1. Matrix additon.","2. Matrix Multiplication", "3. Matrix Transpose.",sep="\n")
choice = int(input("Enter your choice: "))

if choice >3 and choice < 1:
    print("Invalid option. Please try again.")
elif choice == 1:
    print("Please provide the input for second Matrix :- ")
    row2 = int(input("Enter rows : "))
    col2 = int(input("Enter columns: "))
    if row1 == row2 and col1 == col2:
        print("Enter data for first matrix:")
        amatrix1 = get_matrix(row1,col1)
        print("Enter data for second matrix:")
        amatrix2 = get_matrix(row2,col2)
        aresult = matrix_addition(amatrix1,amatrix2)
        print(aresult)
    else:
        print("For additon, number of rows and columns should be same.") 
elif choice == 2:
    print("Please provide the input for second Matrix :- ")
    row2 = int(input("Enter rows : "))
    col2 = int(input("Enter columns: "))
    if col1 == row2:
        print("Enter data for first matrix:")
        mmatrix1 = get_matrix(row1,col1)
        print(mmatrix1)
        print("Enter data for second matrix:")
        mmatrix2 = get_matrix(row2,col2)
        print(mmatrix2)
        mresult = matrix_multiplication(mmatrix1,mmatrix2)
        print(mresult)
    else:
        print("For multiplication, column of first matrix should be same as row of second matrix.") 
elif choice == 3:
    print("Enter data for matrix transpose:")
    matrix1 = get_matrix(row1,col1)
    transpose_result = matrix_transpose(matrix1)
    print(transpose_result)
else:
    print("Something went wrong. Please try again later.") 