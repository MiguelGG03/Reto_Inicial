def algoritmo_calculador(num):
    resultado = 3*(2*num)+4(2*num-1)+2(2*num-2)
    return resultado

def main():
        n=input('Cuantos movimientos desea usar: ')
        n=int(n)
        h=algoritmo_calculador(n)
        h=str(h)
        print(h)
        #print("{} movimientos tiene {} caminos".format(str(n),h))
      

if __name__=='__main__':
    main()

""" 

def algoritmo_calculador(num):
res=(20*num)+(6*(num-1))
return int(res)










sigue=True
while(sigue==True):
    print("Con "+str(n)+" movimientos, tenemos "+str(h)+" posibilidades.")
    pregunta=int(input('Desea seguir: 1=Si 0=No'))
    if(pregunta==0):
        sigue=False"""