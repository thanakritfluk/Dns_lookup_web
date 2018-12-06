from django.shortcuts import render
import socket
import ipaddress


def welcome(request):
    return render(request, 'welcome.html')


def compute(request):
    url = request.POST.get('url')
    try:
        canonical = find_domain_name(url)
        ipv4_address = find_listof_subdomain(url)
        ipv6_address = convert_to_ipv6(ipv4_address)
        classes = listof_class(ipv4_address)
        class_with_subdomain = zip_lists(ipv4_address, classes, ipv6_address)
        return render(request, 'welcome.html',
                      {'canonical': canonical, 'url': url, 'class_with_subdomain': class_with_subdomain})
    except:
        error = 'The domain/hostname is invalid.'
        return render(request, 'welcome.html', {'error': error})


def zip_lists(ipv4_address, classes, ipv6_address):
    return zip(classes, ipv4_address, ipv6_address)


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


def listof_class(list):
    listclass = []
    for i in list:
        listclass.append(find_ip_class(i))
    return listclass


def convert_to_ipv6(ipv4):
    ipv6 = []
    for ip in ipv4:
        ipv6.append(ipaddress.IPv6Address('2002::' + ip).compressed)
    return ipv6


