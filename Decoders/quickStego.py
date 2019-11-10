import subprocess
import os
#inputFile = input("Enter: ")
def quickStego(inputFile):
    #filename = os.path.basename(inputFile)
	script_response = subprocess.check_output(["php","test.php",inputFile])
	print(script_response)
	return script_response
	

