import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
files = glob.glob(pattern)

# TODO: use os.path.getsize to find each file's size
for file in files:
    if os.path.isfile(file):  # Ensure it's a file (not a folder)
        size = os.path.getsize(file)  # Get the file size
        print(file, "->", size, "bytes")  # Print file path and size

# TODO: Add a test to only display files that are not zero length
for file in files:
    if os.path.isfile(file):  # Ensure it's a file
        size = os.path.getsize(file)
        if size > 0:  # Only process files with size > 0
            print(file, "->", size, "bytes")

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
for file in files:
    if os.path.isfile(file):  # Ensure it's a file
        size = os.path.getsize(file)
        if size > 0:  # Only process files with size > 0
            print(os.path.basename(file), "-", size, "bytes")  # Print only the filename


