def isnumber(str):
    try:
        int(str)
        return True
    except:
        return False
def parse_key(string):
    temp_array=string.split('*')
    temp_array.sort()

    key_times=1
    key_string=''

    for item in temp_array:
        if len(item)==0:continue;
        if isnumber(item)==True:
            key_times*=int(item)
        else:
            key_string+='*'+item
            
    return_array=[]
    return_array.append(key_string)
    return_array.append(key_times)
    
    return return_array

def array_multiplication(array1,array2):
    #两个字符数组相乘
    temp_dict={}
    
    n1,n2=len(array1),len(array2)
    #如果有一个数组长度为0，则直接返回另一个数组
    if n1==0:
        return array2
    elif n2==0:
        return array1

    #两数组中各项分别相乘
    for i in range(n1):
        for j in range(n2):
            #此为该算法的关键，字符串相乘得到的结果是两个字符串用×连接，×用于后面的分割使用
            string=array1[i]+'*'+array2[j]

            #此为合并同类项
            #str=1*[13C-13C]*[13C-13C]*[13C-13C]*[13C-13C]
            #将str中的系数1和字符串[13C-13C]*[13C-13C]*[13C-13C]*[13C-13C]分开
            #其中的key=temp[0]为字符串，而times=temp[1]则为该字符串的系数
            temp=parse_key(string)
            key=temp[0]
            times=temp[1]
            
            try:
                #用字典表示可以自动去除重复项，如有重复的想直接将其系数相加即可
                temp_dict[key]+=times
            except:
                #第一次出现
                temp_dict[key]=times

    temp_array=[]
    for key in temp_dict.keys():
        temp_array.append(str(temp_dict[key])+key)
    return temp_array

def array_multi(array):
    #n个字符数组相乘
    #print type(array)
    temp_array=[]
    for item in array:
        temp_array=array_multiplication(item,temp_array)
        
    return temp_array

def array_power(array,n):
    #字符数组的n次方
    temp_array=array
    for i in range(n-1):
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
    arr0=['8O-16O','8O-17O','8O-18O']
    arr1=['C','D','E']

    print len(array_power(arr0,3))
    #arr=[array_power(arr0,5),arr0]

    #printr(array_multi(arr))
    #print
    #printr(array_power(arr0,6))
           
    '''
    arr1=['[13C-13C]','[13C-12C]']
    arr2=['[C-12C]','[C-13C]']
    arr3=['[H-1H]','[H-2H]']
    arr4=['[2H-2H]','[2H-1H]']
    arr5=['[O-16O]','[O-18O]']


    par1=array_power(arr1,5)
    par2=array_power(arr2,1)
    par3=array_power(arr3,5)
    par4=array_power(arr4,3)
    par5=array_power(arr5,3)

    arr=[par1,par2,par3,par4,par5]
    par0=array_multi(arr)
    #par00=array_multi(par1,par2,par3,par4,par5)

    printr(par0)
    print
    #printr(par2)
    print
    #printr(par3)
    print
    #printr(par4)
    print
    #printr(par5)
    
    #printr(par0)
    '''
        
    
