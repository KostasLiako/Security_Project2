import hashlib
import os
import subprocess

for year in range (2021,2022):
    for month in range (1,13):
        if month < 10:
            month = "0"+str(month)
        for day in range (1,32):    
            if day < 10:
                day = "0"+str(day)
            date=str(year)+"-"+str(month)+"-"+str(day)+" bigtent"
            print(date)
            key=hashlib.sha256(date.encode('utf-8'))
            key=str(key.hexdigest())
            cmd = "gpg -d --batch --passphrase "+ key +" signal.log.gpg"
            os.system(cmd)
