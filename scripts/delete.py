# Replace 779-OnePlan_Support-html5 with the output name from the .zip file generated by Paligo.
import os, glob

try:
    os.rmdir('../779-OnePlan_Support-html5/out')
    os.rmdir('../779-OnePlan_Support-html5')
    os.remove('../779-OnePlan_Support-html5_-Upload_to_GitHub.zip')
    print('Deleted unneeded sub-directories...')
    
except:
   print('[ERROR!] Unable to delete files.')

# Version 1 of unzip-util, see https://github.com/johnapaz/unzip-util for details.