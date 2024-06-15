import subprocess
import time

while(True): 
    
    
# Run script1.py in a separate process
    subprocess.Popen(["python", "pythonscanner.py"]).wait()

    # Run script2.py in a separate process
    subprocess.Popen(["python", "creatinghtml.py"])
    
    time.sleep(5)