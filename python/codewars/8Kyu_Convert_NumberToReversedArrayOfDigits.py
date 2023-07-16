# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# Example(Input => Output):
#   35231 => [1,3,2,5,3]
#   0 => [0]
def digitize(n):
    dic = []
    for i in str(n):
        dic.append(int(i))
    return(dic[::-1])

#   return map(int, str(n)[::-1]) --> Utiliza map para transformar un iterable en una cadena ordenándola de forma inversa