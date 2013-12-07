import pybel
import element as el

def parse_molfile(file_name):
    mol=pybel.readfile('mol',file_name).next()
    mol.addh()
    
    temp_array=[]
    for atom in mol.atoms:
        #if atom.isotope==0:            
        #    symbel=el.get_isotope_info(atom.atomicnum,atom.isotope,'isotope_symbol')
        #else:
        #    symbel=el.get_isotope_info(atom.atomicnum,atom.isotope,'isotope_symbol')
            
        symbel=el.get_isotope_info(atom.atomicnum,atom.isotope,'isotope_symbol')
        temp_array.append([symbel,1,atom.atomicnum,atom.isotope])

    #消除重复项
    return_array=[]
    stack=[]
    for item in temp_array:
        if item not in stack:
            stack.append(item)
            return_array.append([item[0],temp_array.count(item),item[2],item[3]])
            
    '''
    ['12C', 9, 6, 0L]
    ['15N', 1, 7, 15L]
    ['16O', 2, 8, 0L]
    ['35Cl', 1, 17, 0L]
    ['1H', 10, 1, 0L]
    [0]:同位素元素符号
    [1]:该元素的个数
    [2]:原子序数
    [3]:同位素序数，0表示是天然丰度的
    '''
    return return_array

def print_molfile(file_name):
    print 
    print 'file name:',file_name
    print '='*30
    mol=pybel.readfile('mol',file_name).next()
    
    mol.addh()    
    for atom in mol.atoms:
        #if atom.isotope==0:            
        #    symbel=el.get_isotope_info(atom.atomicnum,atom.isotope,'isotope_symbol')
        #else:
        #    symbel=el.get_isotope_info(atom.atomicnum,atom.isotope,'isotope_symbol')
        
        symbel=el.get_isotope_info(atom.atomicnum,atom.isotope,'isotope_symbol')
        print "%5s%4d%5d%15.10f" % (symbel,atom.atomicnum,atom.isotope,atom.atomicmass)
            
if __name__=='__main__':
    file_name='mol1.mol'
    moll=parse_molfile(file_name)
    
    for item in moll:
        print item
    
    #print_molfile(file_name)
    
