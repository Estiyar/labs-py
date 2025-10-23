with open('"C:\Users\trarb\Desktop\6.lab\3.txt"',"a") as txt:
    a = list(input("Write list: ").split())
    for i in a:
        txt.write(i + " ")
    