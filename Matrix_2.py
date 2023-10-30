class Matrix():
    def __init__(self,matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
    def print_matrix(self):
        for i in self.matrix:
            print('\t'.join(map(str, i)))
    def add_matrix(self,other):
        result = [[0 for j in range(self.columns)] for i in range(self.rows)]
        for indexrow, row in enumerate(self.matrix):
            for indexcol in range(len(row)):
                result[indexrow][indexcol] = other.matrix[indexrow][indexcol] + self.matrix[indexrow][indexcol]
        print(result)
    def multiply_matrix(self,other):
        if self.columns != other.rows:
            raise ArithmeticError('stupid')
        result = []
        b = []
        for j in range(0, len(other.matrix[0])):
            b.append(0)
        for i in range(0, len(self.matrix)):
            result.append(b)    
        for ii in range(len(self.matrix)):
            for jj in range(len(other.matrix[0])):
                for kk in range(len(other.matrix)):
                    result[ii][jj] += self.matrix[ii][kk] * other.matrix[kk][jj]
        print(result)
    def transpose_matrix(self):
        result = []
        b = []
        for j in range(0, self.columns):
            b.append(0)
        for i in range(0, self.rows):
            result.append(b)
        for ii in range(self.rows):
            for jj in range(self.columns):
                result[jj][ii] = self.matrix[ii][jj]
        return result
    def scalarTimesRow(self, scalar):
        result = [[0 for j in range(self.columns)] for i in range(self.rows)]
        for indexrow, row in enumerate(self.matrix):
            for indexcol in range(len(row)):
                result[indexrow][indexcol] = self.matrix[indexrow][indexcol] * scalar
        print(result)
    def rowreduce(self):
        for i in range(min(self.rows, self.columns)):
            for r in range(i, self.rows):
                # find the row with a non pivot entry
                zero_row = self.matrix[r][i] == 0
                if zero_row:
                    continue
                # swap rows to have the pivot at the top
                self.matrix[i], self.matrix[r] = self.matrix[r], self.matrix[i]
                first_row_first_col = self.matrix[i][i]
                for rr in range(i + 1, self.rows):
                    # take a subsequent entry in the proceeding rows of the matrix with an entry in the pivot column
                    this_row_first = self.matrix[rr][i]
                    # find the inverse of the leading pivot entry such that adding it with the pivot entry gives 1
                    scalarInverse = -1 * (this_row_first / first_row_first_col)
                    for cc in range(i, self.columns):
                        # add them together
                        self.matrix[rr][cc] += self.matrix[i][cc] * scalarInverse
                break
        return self.matrix
    def getMatrixDeternminant(self):
        if self.rows != self.columns:
            raise ArithmeticError
        if self.rows == 2:
            return self.matrix[0][0]*self.matrix[1][1]-self.matrix[0][1]*self.matrix[1][0]
        determinant = 0
        for c in range(self.rows):
            # Use matrix of minors to get determinant
            determinant += ((-1)**c)*self.matrix[0][c]*(self.getMatrixMinor(0,c)).getMatrixDeterminant()
        return determinant
    def inverse(self):
        # Check if the matrix is square
        if self.rows != self.columns:
            raise ValueError("Matrix must be square to find its inverse")

        # Check if the matrix is 2x2
        if self.rows == 2:
            determinant = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

            # Calculate the cofactors of the matrix
            cofactors = [[self.matrix[1][1], -self.matrix[0][1]], [-self.matrix[1][0], self.matrix[0][0]]]

            # Transpose the matrix of cofactors to obtain the adjugate
            adjugate = [[cofactors[0][0], cofactors[1][0]], [cofactors[0][1], cofactors[1][1]]]

            # Divide the adjugate by the determinant to obtain the inverse
            inverse = [[adjugate[0][0] / determinant, adjugate[0][1] / determinant], [adjugate[1][0] / determinant, adjugate[1][1] / determinant]]
            
            for i in range(self.rows):
                for j in range(self.columns): 
                    inverse[i][j] = round(inverse[i][j],3)

            return Matrix(inverse)

        # If the matrix is larger than 2x2, use recursion to find the inverse
        else:
            # Initialize a list to store the cofactors of each element
            cofactors = []

            # Iterate over the rows of the matrix
            for i in range(self.rows):
                # Initialize a list to store the cofactors for this row
                row_cofactors = []

                # Iterate over the columns of the matrix
                for j in range(self.columns):
                    # Find the minor of this element
                    minor = [[self.matrix[k][l] for l in range(self.columns) if l != j] for k in range(self.rows) if k != i]

                    # Calculate the determinant of the minor
                    minor_determinant = Matrix(minor).determinant()

                    # Calculate the cofactor for this element
                    cofactor = (-1) ** (i + j) * minor_determinant

                    # Add the cofactor to the list
                    row_cofactors.append(cofactor)

                # Add the row of cofactors to the list of cofactors
                cofactors.append(row_cofactors)

            # Transpose the matrix of cofactors to obtain the adjugate
            adjugate = [[cofactors[j][i] for j in range(self.rows)] for i in range(self.columns)]

            # Calculate the determinant of the original matrix
            determinant = self.determinant()

            if determinant == 0:
                raise ValueError("Matrix has no inverse (determinant is zero and matrix is singular)")

            # Divide the adjugate by the determinant to obtain the inverse
            inverse = [[adjugate[i][j] / determinant for j in range(self.columns)] for i in range(self.rows)]

            for i in range(self.rows):
                for j in range(self.columns): 
                    inverse[i][j] = round(inverse[i][j],3)

            return Matrix(inverse)

    def determinant(self):
        # Find the dimensions of the matrix
        rows = self.rows
        cols = self.columns

        # Check if the matrix is 2x2
        if rows == 2 and cols == 2:
            # Calculate the determinant of the 2x2 matrix
            determinant = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
            return determinant

        # If the matrix is larger than 2x2, use recursion to calculate the determinant
        else:
            # Initialize a variable to store the determinant
            determinant = 0

            # Iterate over the columns of the matrix
            for i in range(cols):
                # Find the minor of the first element in this column
                minor = [[self.matrix[k][l] for l in range(cols) if l != i] for k in range(1, rows)]

                # Calculate the determinant of the minor
                minor_determinant = Matrix(minor).determinant()

                # Add the product of the first element and the determinant of the minor to the determinant
                determinant += (-1) ** i * self.matrix[0][i] * minor_determinant

            return determinant






the_inp = input('type your matrix in this format [[a,b,c],[d,e,f]]: ')
matrix_the_inp = Matrix(the_inp)
operation_type = input('what operation would you like to do:')

if operation_type == 'Print':
    the_inp.print()
if operation_type == 'Add':
    the_inp2 = input('type your matrix in this format [[a,b,c],[d,e,f]]: ')
    the_inp.add_matrix(the_inp2)
if operation_type == 'Multiply':
    the_inp2 = input('type your matrix in this format [[a,b,c],[d,e,f]]: ')
    the_inp.multiply_matrix(the_inp2)
if operation_type == 'Transpose':
    the_inp.transpose_matrix()
if operation_type == 'Scalar Mult Row':
    scal = input('input scalar:')
    the_inp.scalarTimesRow(scal)
if operation_type == 'Row Reduce':
    print(the_inp.rowreduce())
if operation_type == 'Determinant':
    the_inp.getMatrixDeterminant()
if operation_type == 'Inverse':
    the_inp.inverse()








