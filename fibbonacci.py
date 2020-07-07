def fibonacci(n, dictionary):
    if n not in dictionary.keys():
        if n==1:
            dictionary[n]= 0
        elif n==2:
            dictionary[n]= 1
        else:
            dictionary[n] = fibonacci(n-1, dictionary)+fibonacci(n-2, dictionary)
    else:
        return dictionary[n]
    # print(dictionary)
    return dictionary[n]

if __name__ == "__main__":
    
    n = int(input('Enter the value\n'))
    while n==0:
        n = int(input('wrong input, try again\n'))

    dictionary={}
    for i in range(1, n+1):
        print(fibonacci(i, dictionary), end=", ")