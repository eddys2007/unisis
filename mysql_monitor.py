import subprocess
from datetime import datetime

cmd1 = '/usr/sbin/service mariadb status'
cmd2 = '/usr/sbin/service mariadb start'  
# Using os.system() method
try:
    results = subprocess.check_output(cmd1,shell=True)
except:
    results = subprocess.run(cmd1,shell=True)

print(str(results)+"----------")
pos= str(results).find("active (running)")

if  pos>= 0:
    print ("Yes!"+str(pos) )
else:
    print ("No."+str(pos) )
    subprocess.call(cmd2,shell=True)    
        
    now = datetime.now()
    
    file = open("/home/eddys/testfile.txt","a")
    file.write("start mysql: "+str(now)+"\r\n")
    file.close() 
    #os.system(cmd2)
