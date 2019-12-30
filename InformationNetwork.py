import netifaces
if __name__ == '__main__':
	ntf = netifaces.interfaces()
	for i in ntf:
		ipaddr = netifaces.ifaddresses(i)
		if netifaces.AF_INET in ipaddr :
			dcip = ipaddr[netifaces.AF_INET]
			dcip = dcip[0]
			print("Giao gien mang {0}".format(i))
			print("IP address : {0}".format(dcip['addr']))
			print("Subnet mask : {0}".format(dcip['netmask']))
			gateway = netifaces.gateways()
			print("Defaunt gateways : ",gateway['defaunt'][netifaces.AF_INET[0]])


printf("Bao loi dong so 1")
printf("Bao loi khong import duoc thu vien netifaces")

printf("tao confielect")
