import socket
import requests
import pprint

def resolve_domain_to_ip(domain):
    try:
        # Menggunakan getaddrinfo sebagai alternatif gethostbyname
        ip_address = socket.getaddrinfo(domain, 80)[0][4][0]
        return ip_address
    except socket.gaierror as e:
        print(f"\n❌ Gagal resolve domain '{domain}': {e}")
        return None

def get_geolocation(ip_address):
    try:
        url = f'https://geolocation-db.com/json/{ip_address}'
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"\n❌ Gagal mengambil data geolokasi. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"\n❌ Terjadi kesalahan saat mengakses API geolokasi: {e}")
        return None

def main():
    domain = input("Masukkan nama domain (contoh: google.com): ").strip()

    if not domain:
        print("❌ Domain tidak boleh kosong.")
        return

    ip_address = resolve_domain_to_ip(domain)
    if not ip_address:
        return

    print(f"\n🔎 Alamat IP untuk {domain} adalah: {ip_address}")

    geolocation = get_geolocation(ip_address)
    if not geolocation:
        return

    print("\n📍 Informasi Geolokasi:")
    for k, v in geolocation.items():
        pprint.pprint(f"{k} : {v}")

if __name__ == "__main__":
    main()
import socket 
import requests 
import pprint 
import json 

hostname = input('Enter a domain name: ') 
ip_address = socket.gethostbyname (hostname) 

request_url = 'https://geolocation-db.com/jsonp/' + ip_address 
response = requests.get(request_url) 
geolocation = response.content.decode() 
geolocation = geolocation.split("(")[1].strip(")") 
geolocation = json.loads(geolocation) 
for k,v in geolocation.items(): 
        pprint.pprint(str(k) + ' ' + str(v))

import socket 
import requests 
import pprint 
import json 

hostname = input('Enter a domain name: ') 
ip_address = socket.gethostbyname (hostname) 

request_url = 'https://geolocation-db.com/jsonp/' + ip_address 
response = requests.get(request_url) 
geolocation = response.content.decode() 
geolocation = geolocation.split("(")[1].strip(")") 
geolocation = json.loads(geolocation) 
for k,v in geolocation.items(): 
        pprint.pprint(str(k) + ' ' + str(v))


