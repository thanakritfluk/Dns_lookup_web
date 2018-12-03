from django.shortcuts import render
import socket


def welcome(request):
    return render(request, 'welcome.html')


def find_domain_name(url):
    data = socket.gethostbyname_ex(url)
    return str(repr(data[0]))


def find_listof_subdomain(url):
    data = socket.gethostbyname_ex(url)
    return data[2]


def find_ip_class(ip):
    first_octet = ip.split('.')
    print(first_octet[0])
    ip_check = int(first_octet[0])
    if 1 <= ip_check <= 126:
        return 'A'
    elif 128 <= ip_check <= 191:
        return 'B'
    elif 192 <= ip_check <= 223:
        return 'C'
    elif 224 <= ip_check <= 239:
        return 'D'
    else:
        return 'E'


# x = 'www.google.com'
#
# print("\nDomain Name is: " + find_domain_name(x))
# list_of_sub = find_listof_subdomain(x)
# for i in list_of_sub:
#     print(i)
#     print(type(i))
#     print("\nClass " + find_ip_class(i))
#     print('Sub domain is: ' + i)
