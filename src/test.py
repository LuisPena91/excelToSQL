

def dictionary(list,dic):
    for j in range(len(list)):
        print('Add a number for: ', list[j])
        x = int(input())
        dic[list[j]] = x
    return dic

def main():
    list1=['a','b','c','d']
    dic1={}
    dic = dictionary(list1,dic1)

    print(dic)

if __name__=="__main__":
    main()