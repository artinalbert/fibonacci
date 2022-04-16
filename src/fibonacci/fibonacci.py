def main():

   #print(fibonacci_loop(99))
   print(fibonacci_recursive(9,[0,1]))

def fibonacci_loop(n):
    fibonacci = [0,1]
    


    # while len(fibonacci) < n:
        

    #     i = fibonacci[-2] + fibonacci[-1]
    #     fibonacci.append(i)



    for i in range(n-2):
        # print(i)
        i = fibonacci[-1] + fibonacci[-2] 



        fibonacci.append(i)



    return fibonacci



def fibonacci_recursive(n, fibonacci):
    #  print(first_call)
    #  if first_call:
    #     fibonacci = [0,1]
    #  print(fibonacci)
    i = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(i)

    if n != 3:
        fibonacci_recursive(n-1, fibonacci)

    # if n != len(fibonacci):
    #     fibonacci_recursive(n, fibonacci)

    

    return fibonacci      


if __name__ == '__main__':
    main()
