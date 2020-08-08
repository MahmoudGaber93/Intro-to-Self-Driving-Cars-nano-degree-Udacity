import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)
    
#########################################################################################################
def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
#########################################################################################################
# I added the dotproduct function to help me in mul function
def dotproduct(vectora, vectorb):
    
    #creat a variablewhich hold the result of dot product operation on 2 vectors
    result = 0
    #loop on the vector elements
    for i in range(len(vectora)):
        #sum the multipication of 2 elements
        result += (vectora[i] * vectorb[i]) 
    #return the result    
    return result  


#########################################################################################################
#########################################################################################################

class Matrix(object):

    # Constructor
    def __init__(self,grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

#########################################################################################################
    # Primary matrix math methods
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        #check if the matrix 1x1 or 2x2
        det = 0
        if self.h ==1:
            #the det  is the only element in the matrix
            det = self.g[0][0]
            
        else:
            #calculate det in 2x2 matrix
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            det = (a*d) - (b*c)
            
        #return det    
        return det 
    
#########################################################################################################    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        else: 
            #create the variable that eill comtain the sum of diagonal
            diag_sum =0
            #creating a for loop to loop on the num of rows or col 
            #as the matrix is asquare matrix and we want to find the diagonal elemet which 
            #in it the row_ num = col_num
            for row in range(self.h):
                diag_sum +=  self.g[row][row]
        #return the sum of diagonal
        return diag_sum              

#########################################################################################################
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
            
        Inverse_matrix = []
        
        #check if the matrix 1x1 or 2x2
        if self.h == 1:
            Inverse_matrix= [[1/self.g[0][0]]]
        else:
            Det =0
            # 2x2 ,matrix
            #call det function to valvulate the determination
            Det = self.determinant()
            
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            
            #creat the inverse matrix
            Inverse_matrix = [[d ,-b],[-c ,a]]
            
            #nested for loop to multiplt each elemnt by the factor
            for i in range(len(Inverse_matrix)):
                for j in range(len(Inverse_matrix)):
                      Inverse_matrix[i][j] *= 1/Det
                        
        #return inverse matrix        
        return  Matrix(Inverse_matrix)             

#########################################################################################################
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        #creat the tran_matrix
        Transpose_Matrix =[]
        
        new_row =[]
        
        #nested loop to switch the cols with rows
        for col in range(self.w):  
            #reset the vector every loop
            new_row =[]
            
            for row in range(self.h):
                #convert the col to row in the new_row vector
                new_row.append(self.g[row][col])   
                
            #append the new row to the Transpose Matrix  
            Transpose_Matrix.append(new_row)
            
         #return the Transpose Matrix
        return Matrix(Transpose_Matrix)  

    def is_square(self):
        return self.h == self.w

#########################################################################################################
    # Begin Operator Overloading
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]
    
#########################################################################################################
    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

#########################################################################################################
    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
        #creat the addition matrix    
        Matrix_Addition = []  
        
        new_row = []
        #nested loop to add the elements that gad the same indices in both matrix
        for row in range(self.h):
            #reset the vector
            new_row = []
            for col in range(self.w):
                #added the to element ten append then sum in new_row vector
                new_row.append(self.g[row][col] + other.g[row][col])
                
            #append the new_row when complet
            Matrix_Addition.append(new_row)
            
        #return Matrix Addition    
        return Matrix(Matrix_Addition)
    
#########################################################################################################

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        Neg_Matrix= []
        new_row = []
        #nested loop to multiply the elements  by -1 
        for row in range(self.h):
            #reset the vector
            new_row = []
            for col in range(self.w):
                #multiply  the to element by -1  then append it in new_row vector
                new_row.append(self.g[row][col] *-1)
                
            #append the new_row when complet
            Neg_Matrix.append(new_row)
            
        #return Neg_Matrix     
        return Matrix(Neg_Matrix)
        
#########################################################################################################
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtract if the dimensions are the same")
        #creat the subtraction matrix    
        Matrix_subtraction = []  
        
        new_row = []
        #nested loop to subtract the elements that gad the same indices in both matrix
        for row in range(self.h):
            #reset the vector
            new_row = []
            for col in range(self.w):
                #added the to element ten append then subtraction in new_row vector
                new_row.append(self.g[row][col] - other.g[row][col])
                
            #append the new_row when complet
            Matrix_subtraction.append(new_row)
            
        #return Matrix subtraction    
        return  Matrix(Matrix_subtraction)

#########################################################################################################
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if self.w != other.h:
            raise(ValueError, "the num of column of the first matrix not equal the num of row of the second matrix")
            
        Transpose_other = other.T()
        
        new_row = []
        Multiplication_Matrix = []
        
        for i in range(self.h):
            new_row = []
            for j in range(other.w):
                new_row.append(dotproduct(self.g[i] ,Transpose_other[j]))
            Multiplication_Matrix.append(new_row)
            
        return  Matrix(Multiplication_Matrix)
        
###################################################################################
        
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
         
        Rmul_Matrix  = []
        new_row = []
        #nested loop to multiply the elements  by num
        for row in range(self.h):
            #reset the vector
            new_row = []
            for col in range(self.w):
                #multiply  the to element by number  then append it in new_row vector
                new_row.append(self.g[row][col] *other)
                
            #append the new_row when complet
            Rmul_Matrix.append(new_row)
            
        #return Rmul_Matrix     
        return  Matrix(Rmul_Matrix)

                         
 #########################################################################################################           