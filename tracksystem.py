import socket
import os


host_name=socket.gethostname()
host_ip=socket.gethostbyname(host_name)
print("host ip=", host_ip)
print("hostname=",host_name)


from getmac import get_mac_address as gma
print("macaddress is=",gma())


import uuid
# printing the value of unique MAC
# address using uuid and getnode() function
print (hex(uuid.getnode()))


username =os.getlogin()
print("UserName: ",username)
