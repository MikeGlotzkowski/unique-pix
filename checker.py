import os
# https://pypi.org/project/ImageHash/
from PIL import Image
import imagehash
import shutil


root_directory = "../data"

elements = {}
row = 0

# walk through pictures folder and 
# add every picture with its and hash to a dictionary
for root, dirs, files in os.walk(root_directory):
    for filename in files:
      full_file_path = "./" + root_directory + "/" + os.path.basename(filename)
      # TODO: get file extension
      file_extension = ".png"
      hash = imagehash.average_hash(Image.open(full_file_path))
      elements[row] = { }
      elements[row]['hash']= hash
      elements[row]['full_file_path'] = full_file_path
      row = row + 1

      # name pictures after their hash and move to target directory
      # if works, good, new picture
      # if fails, it's already there - also good
      # TODO: use real name
      dst_dir = "../reduced/" + os.path.basename(str(hash) + file_extension)
      print(dst_dir)
      shutil.copy(full_file_path, dst_dir)


set_1 = set()

# add hashes to a set to find how many unique pictures there are
for key, value in elements.items():
  set_1.add(value['hash'])

# name pictures after their hash and move to target directory
# if works, good, new picture
# if fails, it's already there - also good
some_name = str(set_1.pop())

# TODO: count number of files in target directory

# TODO compare
# compare to number of entries in set
# if it fits all ok
# if not - we fucked up


  
