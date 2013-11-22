def factorial(n):
    if n==0:
        return 1
    elif n==-1:
        return 0
    else:
        value=1
        for i in range(1,n):
            value*=(i+1)
        return value
def c(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def strC(par,n):
    array=[]
    for r in range(0,n+1):
        cab='['+str(c(n,r))+']'+par[0]+'('+str(n-r)+')'+par[1]+'('+str(r)+')'
        array.append(cab)
    return array

def stringC(par,n):
    items=strC(par,n)

    string=''
    for i in range(n):
        string+=items[i]+'+'
    string+=items[n]
    return string

def multiArray(arr1,arr2):
    array=[]
    n1,n2=len(arr1),len(arr2)
    for i in range(n1):
        for j in range(n2):
            array.append(arr1[i]+arr2[j])
    return array
    
if __name__=="__main__":
    par=('A','B')
    par2=('C','D','E')

    print stringC(par,10)
    print
    
    c1=multiArray(strC(par,4),strC(par2,4))
    c2=strC(par,3)
    print multiArray(c1,c2)
    
