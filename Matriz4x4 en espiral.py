# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
     
    num=4
    value=0
    aux=[]
   
matriz = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
print "Matriz inicial"
for a in range (num):
    print matriz[a]\n 
    
for i in range (num):
    for j in range (num):
        aux.append(matriz[i][j])
    

vuelta=num/2
for k in range (vuelta):
    for j in range(num-2*k):
        fila=0+k
        columna=j+k
        matriz[fila][columna] = aux[value]
        value = value+1
        
    if k!=vuelta-1:            
        for i in range(num-1-k):
            fila=i+1
            columna=num-1
            matriz[fila][columna] = aux[value]
            value = value+1
                
    for j in range(num-1-k):
        fila=num-1-k
        columna=num-2-j
        matriz[fila][columna] = aux[value]
        value = value+1

    if k!=vuelta-1:
     for i in range(num-2):
        fila=num-2-i
        columna=0
        matriz[fila][columna] = aux[value]
        value = value+1
        
print "Matriz Final"
for a in range (num):
    print matriz[a]\n    
     
