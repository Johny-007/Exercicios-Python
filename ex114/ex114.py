import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except:
    print("\033[31m  -Deu erro, site não acessivél\033[m")
else:
    print("SITE FUNFANDO!!")