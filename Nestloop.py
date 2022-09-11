
matrix = [[1,2,3.4],[1,2,5.3],[1,2,-13]]

print(matrix)
#print(len(matrix[0]))
#print(len(matrix[2]))
#just to automatize

mina = -9e99 # set maxfinder to - infinity
#print(matrix[1][1])
for i in range(3):
 for j in range(3): # en(matrix[1])): #lengz):
       #print(matrix[i],[j])# just 2 see if t worx
       if (matrix[i][j] >  mina):
           mina = matrix[i][j]
print("maximum of natrix : ", mina)


#for elem in matrtix
