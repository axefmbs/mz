def table(number):
    return [[1, 1] + [0] * (number // 2 - 1)] * number

def f(table, x, y):
    def c(i):
        return table[x - i][min(x - i, i)] + c(i + 1) if i <= y else 0
    return c(1)

def dpRowOf(table, x):
    return table[x][0:2] + [f(table, x, y) 
        if y <= x and x + y <= len(table) 
        else table[x][y] for y in range(2, len(table[x]))]
    
def dp(table):
    def dp(t, x):
        return dp(t[0:x] + 
            [dpRowOf(t, x)] + t[x + 1:], x + 1) if x < len(t) else t
    return dp(table, 2)
    
def count(table):
    def j(i): return i if len(table) - i >= i else len(table) - i
    return sum([table[len(table) - i][j(i)] 
        for i in range(1, len(table) + 1)])

def numOfDecons(number):
    return count(dp(table(number)))

print("可拆解出 %d 组数字\n" % numOfDecons(10))
