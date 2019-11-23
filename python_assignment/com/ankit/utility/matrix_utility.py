def matrix_addition(mat1,mat2):
    aresult = []
    for i in range(len(mat1)):
        temp = []
        for j in range(len(mat1[0])):
            temp.append(mat1[i][j] + mat2[i][j])
        aresult.append(temp)
    return aresult

def matrix_multiplication(mat1,mat2):
    mresult = []
    for i in range(len(mat1)):
        temp = []
        for j in range(len(mat2[0])):
            sum= 0
            for k in range(len(mat2)):
                sum += mat1[i][k] * mat2[k][j]
            temp.append(sum)
        mresult.append(temp) 
    return mresult

def matrix_transpose(mat):
    tmatrix = []
    for i in range(len(mat)):
        temp = []
        for j in range(len(mat[0])):
            temp.append(mat[j][i])
        tmatrix.append(temp)
    return tmatrix


def get_matrix(rows,cols):
    matrix = []
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(int(input("Enter value[{0}][{1}]: ".format(i,j))))
        matrix.append(temp)
    return matrix