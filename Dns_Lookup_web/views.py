from django.shortcuts import render
import socket


def welcome(request):
    return render(request, 'welcome.html')


def compute(request):
    url = request.POST.get('url')
    canonical = find_domain_name(url)
    address = find_listof_subdomain(url)
    classes = listof_class(address)
    class_with_subdomain = zip_lists(address, classes)
    return render(request, 'welcome.html',
                  {'canonical': canonical, 'url': url, 'class_with_subdomain': class_with_subdomain})


def zip_lists(address, classes):
    return zip(classes, address)


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
