import sys, os, shutil


if sys.argv[2] == '-create':
	open(sys.argv[1], mode='x')
if sys.argv[2] == '-delete':
        os.remove(sys.argv[1])
if sys.argv[2] == '-move':
        shutil.move(os.getcwd()+'/'+sys.argv[1], sys.argv[3])
if sys.argv[2] == '-help':
        print('HELP INSTRUCTIONS TO FOLLOW')