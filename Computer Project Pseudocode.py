import numpy as np
import math
#we will be using numpy extensively especially np.linalg
row=int(input("Enter the number of rows:"))
col=int(input("Enter the number of cols."))
if row!=col:
    print("Square Matrix Required! You have given a non-square matrix")
else:
    print("Enter the entries in a single line separated by a space")
    entries = list(map(int, input().split()))
    U=np.array(entries).reshape(m,n)
d=row=int(input("Enter the number of rows for matrix A:"))
col=col
A = np.zeros((d, col), dtype=float)
# Get each row of the matrix from the user
for i in range(d):
    for j in range(col):
        # Take input for each element in the row
        A[i, j] = float(input(f"Enter element at position ({i+1}, {j+1}): "))
'''Take R as a bunch of pre-processed matrices as done by Lee et al.'''
dimM=4*n+d
M=np.zeroes((dim,dim),dtype=float) #specifies an empty M matrix
for i in range(dim):
    for j in range(dim):
        # Take input for each element in the row
        M[i, j] = float(input(f"Enter element at position ({i+1}, {j+1}): "))
a=float(input("Enter the value of a in the interval (0,1):"))
b=float(input("Enter the value of b in the interval (0,1):"))
eps_mp=float(input("Enter the tolerance value in the interval (0,1):"))
def Ymatrix():
    # Get the dimensions of the matrix from the user
    rows = dimM
    cols = math.floor(n**b)
    # Initialize an empty matrix
    X = np.zeros((rows, cols), dtype=float)

    return Y
def Xmatrix():
    rows=dimM
    cols=math.floor(n**b)
    X=np.zeroes((rows,cols),dtype=float)
    return X
#The above two lines take input X and Y from the user
def Qmatrix():
    rows=math.floor(n**b)
    cols=math.floor(n**b)
    Q=np.zeroes((rows,cols),dtype=float)
    for i in range(rows):
        for j in range(cols):
        # Take input for each element in the row
            Q[i, j] = 1
    return Q
def Nmatrix():
    rows=cols=dimM
    N=np.zeroes((rows,cols),dtype='float')
    for i in range(rows):
        for j in range(cols):
        # Take input for each element in the row
            N[i, j] = float(input(f"Enter element at position ({i+1}, {j+1}): "))
    return N
#the above two lines takes the matrices Q and N as input from the user
def vectorv():
    rows=n
    cols=1
    v=np.zeroes((rows,cols),dtype=float)
    for i in range(rows):
        for j in range(cols):
        # Take input for each element in the row
            v[i, j] = float(input(f"Enter element at position ({i+1}, {j+1}): "))
    return v
def vectorvtilda():
    rows=n
    cols=1
    vtil=np.zeroes((rows,cols),dtype='float')
    for i in range(rows):
        for j in range(cols):
        # Take input for each element in the row
            vtil[i, j] = float(input(f"Enter element at position ({i+1}, {j+1}): "))
    return vtil
#the above two definitions take the vectors v and v-tilde as inputs from the user
l=int(input("Enter a natural number:"))
class MatrixAlgo:
    def INIT(self,N):
        def UMatrix():
            rows=n
            # Get user input for the values on the diagonal
            entries_str = input("Enter the values on the main diagonal separated by spaces: ")
            u0 = [float(x) for x in entries_str.split()]
            # Create a diagonal matrix with user-provided values
            U = np.diag(u0, k=0)
            return U
        '''specify M as the sketching matrix shown'''
        self.N_inverse=np.linalg.inv(N) #this inverts the matrix N and stores it in N_inverse
    #The above process takes time O(m^w) where 2.4<w<=3
        l=0
    #Fast Matrix Inversion Algorithms exist. See References 
    def UPDATE(self,delta,u_new):
        '''if np.count_nonzero(u_new==0)>n**b:
                raise Error
           else:
               intialize delta as given
           Let delta equal X times Y-transposed where X consists of non zero entries and Y is a column selection matrix'''
        Y_T=Y.T
        S=I+np.linalg.multidot([Y_T,N,X])
        Q=np.linalg.inv(S)
    def QUERY(self,I,j):
        '''returns M^(-1)[i,j] using the Matrix Woodburry Formula'''
        v_1=np.linalg.multidot([Y_T,N,e_j])
        #Here e_j is the jth canonical vector. It can be inputted as
        #def canonical_basis_vector(j, n):
            #basis_vector = np.zeros(n)
            #basis_vector[j] = 1
            #return basis_vector
        v_2=np.linalg.dot(Q,v_1)
        '''extract the Ith column of N.X and store it in L'''
        v_3=np.linalg.dot(L,v_2)
        v=N[I-1,j-1]-v_3
    def RESET(self,X,Y):
        '''requires k >=n**a'''
        '''returns M^(-1)[i,j] using the Matrix Woodburry Formula'''
        '''input X_new,Y_new as blank matrices of dim (4*n+d)*k'''
        Y_n_T=Y_new.T
        L_1=np.linalg.dot(Y_n_T,N)
        Q=np.linalg.inv(I+np.linalg.multidot([Y_n_T,np.linalg.inv(M),X_new]))
        L_2=np.linalg.dot(Q,L_1)
        L_3=np.linalg.multidot([N,X_new,L_2])
        L=N-L_3
        N=L
        M+=np.linalg.dot(X_new,Y_n_T)
        X=0
        Y=0
        Q=1



