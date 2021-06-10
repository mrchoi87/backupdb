# backupdb

- python file create
home/pi/backupdb/backupdb.py

- script file create
home/pi/backupdb/script.sh
- file privilege
chmod +x script.sh

- scheduling program
crontab -e
*/60 * * * * /home/pi/backupdb/script.sh
- program restart
service crontab restart
systemctl restart cron.service

mkdir /home/pi/usb
fdisk -l
mount -t vfat /dev/sdb1 /home/pi/usb
