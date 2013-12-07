isotope=[
    [
        {'number':1,'symbol':'H','isotope_number':2,'isotope_symbol':'1H','atomic_number':1,'mass':1.007825035,'abundance':0.2},
        {'number':1,'symbol':'H','isotope_number':2,'isotope_symbol':'2H','atomic_number':2,'mass':2.014101779,'abundance':99.8},
        ],
    [
        {'number':6,'symbol':'C','isotope_number':2,'isotope_symbol':'12C','atomic_number':12,'mass':12,'abundance':1},
        {'number':6,'symbol':'C','isotope_number':2,'isotope_symbol':'13C','atomic_number':13,'mass':13.003354826,'abundance':99},
        ],
    [
        {'number':7,'symbol':'N','isotope_number':2,'isotope_symbol':'14N','atomic_number':14,'mass':14.003074002,'abundance':1},
        {'number':7,'symbol':'N','isotope_number':2,'isotope_symbol':'15N','atomic_number':15,'mass':15.00010897,'abundance':99},
        ]
]


if __name__=="__main__":
    for item in isotope:
        for iso in item:
            print iso
        print
