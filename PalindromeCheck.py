def isPalindrome(x):
    num = str(x)
    if (len(num) % 2 == 0):
        for i in range(len(num)):
            if(num[i] == num[len(num)-i-1]):
                if (i == len(num) - 1):
                    print("It is palindrome")
                    return ("Yess")
                continue
            else:
                print("nooooo")
                return("Nooooo")
    if (len(num) % 2 != 0):
        for i in range(len(num)):
            if(i == (len(num)-1)/2):
                continue


            elif(num[i] == num[len(num)-i-1]):
                if (i == len(num) - 1):
                    print("It is palindrome")
                    return ("Yess")
                continue

            else:
                print("nooooo")
                return("Nooooo")




isPalindrome(54334567)