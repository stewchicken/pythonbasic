from os import rename, listdir
import glob

basedir='/home/yw/project/tutorial/pythonbasic/pythoncourse'
fnames = listdir(basedir)

for f in fnames:
    
    print (f)

#for filename in glob.iglob(basedir, recursive=True):
#    print(filename)

files = glob.glob(basedir + '/**/*.py', recursive=True)

for file in files:
    
    print (file)
