import os
import shutil

def copy(f1, f2):
    if os.path.isfile(f1):
        shutil.copyfile(f1, f2)
        print('copied')
    else:
        print('file doesnt exists')
    
f1 = 'C:\Users\trarb\Desktop\6.lab\3.txt'
f2 = 'C:\Users\trarb\Desktop\6.lab\3.txt '
copy(f1, f2)