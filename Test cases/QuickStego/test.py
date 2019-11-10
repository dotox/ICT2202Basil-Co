import subprocess
import os

#inputFile = raw_input("select file: ")
script_response = subprocess.check_output(["C:\/xampp\/php\/php.exe","test.php","imga.bmp"]) #args command,php script, file input
print script_response
