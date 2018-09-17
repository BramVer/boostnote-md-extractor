import os
import glob
import sys
import re

import io_handler as io

def main():
  arguments = sys.argv

  notes_dir = '/home/darm/Nextcloud/Boostnote/notes'
  output_dir = '/home/darm/Nextcloud/Joplin'

  current_dir = os.getcwd()

  files = glob.glob('%s/*.cson' % notes_dir)

  for i, file in enumerate(files):
    file_data = io.open_file(file)

    regex = r"(content: '''\n*)(.*\n)(''')"
    matches = re.finditer(regex, file_data, re.DOTALL | re.MULTILINE)

    for match in matches:
      content = match.groups()[1]
      io.write_to_file(output_dir, file, content)

  print('All found files were processed.')

if __name__ == '__main__':
  main()
