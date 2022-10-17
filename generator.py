"""
Collection of the functions where they are being used to generate
the question and its answer to be served with the redered questions
"""

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

def first_ip(ip_addr):
    """
    Returns first avaliable ipv4 host address
    """
    net = ipaddress.ip_network(ip_addr, strict=False)
    return net[1]

def last_ip(ip_addr):
    """
    Returns  last avaliable ipv4 host address
    """
    net = ipaddress.ip_network(ip_addr, strict=False)
    return net[-2]

def number_subnet(ip_addr):
    """
    Returns number of avaliable subnets
    """
    net = ipaddress.ip_network(ip_addr, strict=False)
    return net(ip_addr).subnets()

def q_maker(question_kind, random_ip):
    """
    This is the main function for choosing the right answer for
    the questions. Depending on the question type, it selects the function.
    """
    if question_kind == 4:
        return first_ip(random_ip)
    if question_kind == 6:
        return f'{first_ip(random_ip)} - {last_ip(random_ip)}'
    if question_kind ==3:
        return last_ip(random_ip)
    if question_kind == 5:
        return number_subnet(random_ip)
