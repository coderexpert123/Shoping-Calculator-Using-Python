sum=0
while(True):
    userInput=input("Enter The Price : Or If You Want to Cancel Press Q  \n ")
    if(userInput!='q'):
        sum = sum + int(userInput)
        print(f"your total order so far is {sum}")

    else:
        print("")
        print(f"Your bill is {sum}.Thanks for Shoping with Nishant Kirana Store ")
        break

