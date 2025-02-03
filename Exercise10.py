import sys, glob, os
from fileinput import filename

# the sys it to get system information
# the glob is used to find files using wild card patterns
# os is used to interact with the operating system such as paths and files sizes



# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
# os.path.join is a function that joins different parts of the file path in an os independent way
# the hdir part is the directory path where we are searching for the files
#  the above asteriks is a wild card. It is saying to match all the files within this folder
# essentially this string is telling python to look at all the files and folders inside the users home directory (C:\users\khris\ on my windows system
#
# TODO: Use the glob.glob() function to obtain the list of filenames
file_list = glob.glob(pattern)
# the glob.glob(pattern) looks for files and directories that match the wildcard pattern (*)
# Since pattern = os.path.join(hdir, '*'), it's searching inside C:\Users\khris\.
# glob.glob() returns a list of all matching files and folders

for file in file_list:
    print(file)
# the file_list = glob.glob is returning a list of all the files in my directory
#  the for in file_list is looping through my files, going through them one by one.

# TODO: use os.path.getsize to find each file's size
for file in file_list:
    file_size = os.path.getsize(file)
    print(f"file:{file}, size: {file_size}" )
# the above for in file statement is looking at the files in the files list
# we are putting the os.path.getsize(file) function into the file_size variable
# os.path.getsize finds the size of each of the files
# the "f" in this line of code is an f string that allows you to put variables inside of a string using the curly braces
# pyhon will replace what is in the curly brackets with the actual values of the variables

# TODO: Add a test to only display files that are not zero length
    if file_size > 0:
     print(f"file:{file}, size: {file_size}" )
# the above if statement is saying that if the file size is bigger than 0, then print the file and its size

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
# os.path.basename() extracts the basename of the file. the basename is the filename without the directory path
#first introduce a for loop for the files in file_list to make the script run through the files within the entire file list
for file in file_list:
    file_name =os.path.basename(file)
    #  we have put the os.path.basename(file) into the variable file_name
    print(f"file:{file_name}, size:{file_size}")
# this has allowed us to print just the filenames without the directory path, making this more user-friendly
#
