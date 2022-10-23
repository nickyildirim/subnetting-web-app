
import ipaddress
import random


MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES 


def random_ipv4():
    """
    This function returns random IPv4 address
    which is only can be public or private.
    """
    random_ip = ipaddress.IPv4Address(random.randint(0, MAX_IPV4))
    while random_ip.is_reserved is True :
        random_ip = ipaddress.IPv4Address(random.randint(0, MAX_IPV4))
        continue
    return  f"{random_ip}/{random.randint(3, 29)}"


def max_host(ip_addr):
    """
    Returns number of avaliable subnets
    """
    return 2**(32 - int(random_ipv4().partition('/')[-1])) / 2 - 2


a = random_ipv4()
print(a)
print(str(a).partition('/')[-1])
print((32 - int(a.partition('/')[-1])))
print(max_host(ip_addr=random_ipv4))