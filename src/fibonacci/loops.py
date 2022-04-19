def main():
    dic = {
        1:'a', 2:'b', 3:'c' , 4:'d', 5:'e', -1:'f', 7:'f'
        }
    dic2 = {}
    for i in dic.keys():
        # i = i + 1
        dic2[i+1] = dic[i]

        # dic2[1] = i
        # will make a new key if not already there (only if on left side of the assignment ioeratorgit !)
        # dic[-1] = i
    print (dic)
    print (dic2)

if __name__== "__main__":
    main() 