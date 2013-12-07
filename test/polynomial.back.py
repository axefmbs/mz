def isnumber(str):
    try:
        int(str)
        return True
    except:
        return False
    
def strSort(string):
    temp_string="*".join((lambda x:(x.sort(),x)[1])(string.split('*')))
    return temp_string
    '''
    temp_array=string.split('*')
    temp_array.sort()

    num_array=[]
    temp_string=""
    
    for item in temp_array:
        if len(item)==0:continue
        if isnumber(item)==True:
            num_array.append(int(item))
        else:
            temp_string+="*"+item

    temp_string=str(sum(num_array))+temp_string

    #print temp_string
    
    return temp_string
    '''

def arraySort(array):
    temp_array=[]
    
    for item in array:
        temp_array.append(strSort(item))

    return_array=[]
    for item in temp_array:
        #temp_item=strSort(item)
        #temp_array[temp_item]+=1
        #print temp_array[temp_item]
        temp_item=str(temp_array.count(item))+'*'+item
        if temp_item not in return_array:
            #查找相同的项的个数，并去除重复的项
            return_array.append(temp_item)
            #print ">>>",str(temp_array.count(item))+'*'+item

    return return_array
def arraySort1(array):
    #temp_array=[]
    
    #for item in array:
    #    temp_array.append(strSort(item))

    temp_array={}
    for item in array:
        temp_item=strSort(item)
        temp_array[temp_item]+=1
        print temp_array[temp_item]
        #temp_item=str(array.count(item))+'*'+item
        #if temp_item not in temp_array:
            #查找相同的项的个数，并去除重复的项
        #    temp_array.append(temp_item)
            #print ">>>",str(temp_array.count(item))+'*'+item

    return temp_array

def array_multiplication(array1,array2):
    #两个字符数组相乘
    temp_array=[]
    n1,n2=len(array1),len(array2)
    if n1==0:
        return array2
    elif n2==0:
        return array1
    
    for i in range(n1):
        for j in range(n2):
            temp_array.append(array1[i]+'*'+array2[j])
            
    return temp_array

def array_multi(*array):
    #n个字符数组相乘
    temp_array=[]
    for item in array:
        temp_array=array_multiplication(item,temp_array)
        
    return temp_array

def array_power(array,n):
    #字符数组的n次方
    temp_array=array
    for r in range(n-1):
        temp_array=array_multiplication(array,temp_array)
        
    return temp_array

def printStr(array):
    n=len(array)
    for i in range(n-1):
        print array[i],'+',
    print array[n-1]
def printr(array):
    for item in array:
        print item
    
if __name__=="__main__":
    '''
    [13C](4)[C](1)[H](5)[2H](3)[O](3)
    1. [13C] 4
    2. [C] 1
    3. [H] 5
    4. [2H] 3
    5. [O] 3
    '''
    arr1=['[13C-13C]','[13C-12C]']
    arr2=['[C-12C]','[C-13C]','[C-14C]']
    arr3=['[H-1H]','[H-2H]','[H-3H]']
    arr4=['[2H-2H]','[2H-1H]']
    arr5=['[O-16O]','[O-17O]','[O-18O]']

    par1=array_power(arr1,10)
    #par2=array_power(arr2,1)
    #par3=array_power(arr3,5)
    #par4=array_power(arr4,3)
    #par5=array_power(arr5,3)
    
    #par0=array_multi(par1,par2,par3,par4,par5)

    #printr(par1)
    print
    printr(arraySort(par1))
    #printr(par0)

    

    #printr(array_multiplication(par1,par1))
    #print
    #printr(array_power(par2,3))

    #print
    #printr(array_multi(par1,par2,par3))
    #print
    #printr(array_multi(par1,par1))
        
    
