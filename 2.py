import os

path = 'C:\Users\trarb\Desktop\6.lab\2.py'

print("Current Path:", path)

print("Existence: ")
if os.access(path, os.F_OK):
    print("Yes")
    
print("Readability: ")
if os.access(path, os.R_OK):
    print("Yes")
    
print("Writability: ")
if os.access(path, os.W_OK):
    print("Yes")
    
print("Executability: ")
if os.access(path, os.X_OK):
    print("Yes")