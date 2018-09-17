'''
This file handles the I/O of the script.

It is called from converdfer.py each time a set of lines is ready to be written,
so they can be cleared from memory.
'''
import re

# Regexes the file_name for a match
def find_name(target):
  try:
    # Build the regex - everything after the last '/'
    regex = re.search(r'([^/]+$)', target, re.I)

    # If not found
    if target.find('.cson') == -1:
      return regex.group()

    return regex.group().replace('.cson', '')

  except Exception as e:
    log_to_file('No match found for name!\r\n' + str(e))

# Concatenates the path and filename and writes content to it
def write_to_file(path, filename, content):
  try:
    full_path = '%s/%s.md' % (path, find_name(filename))
    with open(full_path, 'w') as new_file:
      new_file.write(content)

  except Exception as e:
    print('RIP HE, Wronk PAth >:(')
    print(path)

# Opens the file, extracts information and calls init func
def open_file(file_path):
  file_data = ''

  try:
    with open(file_path, 'r') as data:
      file_data = data.read()

  except IOError as e:
    log_to_file('No file found for path.\n\n' + str(e))

  finally:
    return file_data
