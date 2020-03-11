import sys
import django


print('python-version =')
print(sys.version)


print('\nDjango version =')
print(django.get_version())


'''
op:
python-version =
3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609]

Django version =
2.2.6

'''