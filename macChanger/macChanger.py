import re
import subprocess
from random import choice, randint

print("press")
print("1 for manual changing of MAC address")
print("2 for random MAC address")

inp= input()
interface = input("Enter your network interface:").strip()

def Mac_random():
    cisco = ["00", "40", "96"]
    dell = ["00", "14", "22"]
    mac_address = choice([cisco, dell])
    for i in range(3):
        one= choice(str(randint(0,9)))
        two= choice(str(randint(0,9)))
        three= (str(one + two))
        mac_address.append(three)
    return ":".join(mac_address)
def Change_mac(interface, new_mac):
    subprocess.call(["ifconfig "+ str(interface)+ "down"], shell=True)
    subprocess.call(["ifconfig "+ str(interface)+ "hw ether "+ str(new_mac)+ " "], shell=True)
    subprocess.call(["ifconfig "+ str(interface)+ "up"], shell=True)

def CurrentMac():
    output = subprocess.check_output(["ifconfig " + "eth0"], shell=True)
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    print("Old mac address is {}".format(current_mac))

def main():
    if inp =="1":
        new_mac = input("Enter the new mac address you want to change:").strip()
        Change_mac(interface, new_mac)
    elif inp == "2":
         random = Mac_random()
         print(random)
         Change_mac(interface, random)


if __name__ == "__main__":
    main()

