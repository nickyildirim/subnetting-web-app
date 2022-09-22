import ipaddress
import random

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES 

def random_ipv4():
    """
    This function returns random IPv4 address which is only public or private.
    """
    randomIp = ipaddress.IPv4Address(random.randint(0, MAX_IPV4))
    while randomIp.is_private is False and randomIp.is_global is False:
        randomIp = ipaddress.IPv4Address(random.randint(0, MAX_IPV4))
    return  f"{randomIp}/{random.randint(3, 29)}"

def firstIp(IP_Addr):
    """
    This is the Question 4's answer function. 
    It declares the net address and prints the first avaliable ipv4 host address
    """
    net = ipaddress.ip_network(IP_Addr, strict=False)
    return net[1]

def lastIp(IP_Addr):

    net = ipaddress.ip_network(IP_Addr, strict=False)
    return net[-2]

def numberSubnet(IP_Addr):
    net = ipaddress.ip_network(IP_Addr, strict=False)
    return net(IP_Addr).subnets()



def main(questionKind, random_ipv4):
    """
    This is the main function for choosing the write answer for the questions. 
    Depending on the question type, it selects the function.
    """
    if questionKind == 4:
        return firstIp(random_ipv4)
    elif questionKind == 6:
        return f'{firstIp(random_ipv4)} - {lastIp(random_ipv4)}'
    elif questionKind ==3:
        return lastIp(random_ipv4)
    elif questionKind == 5:
        return numberSubnet(random_ipv4)




if __name__ == '__main__':
    main(random_ipv4)





 

