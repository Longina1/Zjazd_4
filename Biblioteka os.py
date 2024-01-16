import os

import datetime
import time

ts1 = time.time()
print(os.getcwd())
os.chdir('C:\\Users\\longi\\Desktop\\')
#os.chdir(r'C:\Users\longi\Desktop\')
print(os.getcwd())
time.sleep(5)
os.mkdir('New_file')
time.sleep(5)
os.rename('New_file', 'Newer_folder')
time.sleep(5)
os.rmdir('Newer_folder')
time.sleep(5)
ts2 = time.time()
print(f'Duration {ts2 - ts1}')

print(os.environ)

os.system('cmd /c "ipconfig"')

