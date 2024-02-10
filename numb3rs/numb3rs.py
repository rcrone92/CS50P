#libraries
import sys, re

def main():
    in_ip = input("IPv4 Address: ").strip()
    print(validate(in_ip))



def validate(ip):
    if re.search(r"^(([0-9]|[0-9][0-9]|[01][0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9][0-9]|[01][0-9][0-9]|2[0-4][0-9]|25[0-5])$", ip):
        return True
    else:
        return False
    # print("validate")



if __name__=="__main__":
    main()

