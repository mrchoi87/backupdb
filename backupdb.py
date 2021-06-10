import os
from datetime import datetime
userid = "farmos"
passwd = "farmosv2@"
database = "farmos"
enc = "utf8"
def dumpdb():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    command = []
    command.append("mysqldump")
    command.append("-u%s" % userid)
    command.append("-p%s" % passwd)
    command.append("--default-character-set=%s" % enc)
    command.append("--no-tablespaces=TRUE")
    command.append("--extended-insert=FALSE")
    command.append("%s > ~/backupdb/%s_%s.sql" % (database, database, timestamp))
    command = " ".join(command)
    os.system(command)
    os.system("cp ~/backupdb/%s_%s.sql /media/pi/F1C6-E30D/" % (database, timestamp))
if __name__=="__main__":
    dumpdb()
