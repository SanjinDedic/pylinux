import os, shutil
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-create', '--create_file', help="Creates a file in current directory")
parser.add_argument('-delete', '--delete_file', help="Deletes a file in current directory")
parser.add_argument('-move', '--move_file', help="Moves a file from given path to current directory")

args = parser.parse_args()

if args.create_file:
	open(args.create_file, mode='x')
if args.delete_file:
        os.remove(args.delete_file)
if args.move_file:
        shutil.move(os.getcwd(), args.move_file)
