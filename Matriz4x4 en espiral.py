# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
     
    num=4
    value=0
   
matriz = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

vuelta=num/2
for k in range (vuelta):
    for j in range(num-2*k):
        fila=0+k
        columna=j+k
        value = value+1
        matriz[fila][columna] = value
        
    if k!=vuelta-1:            
        for i in range(num-1-k):
            fila=i+1
            columna=num-1
            value = value+1
            matriz[fila][columna] = value
                
    for j in range(num-1-k):
        fila=num-1-k
        columna=num-2-j
        value = value+1
        matriz[fila][columna] = value

    if k!=vuelta-1:
     for i in range(num-2):
        fila=num-2-i
        columna=0
        value = value+1
        matriz[fila][columna] = value
        

for a in range (num):
    print matriz[a]\n    
     