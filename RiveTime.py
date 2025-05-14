import socket
import requests
import whois
import pprint

def resolve_domain_to_ip(domain):
    try:
        ip_address = socket.getaddrinfo(domain, 80)[0][4][0]
        return ip_address
    except socket.gaierror as e:
        print(f"\n❌ Gagal resolve domain '{domain}': {e}")
        return None

def get_geolocation(ip_address):
    try:
        url = f"https://geolocation-db.com/json/{ip_address}&position=true"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"\n❌ Gagal mengambil data geolokasi. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"\n❌ Terjadi kesalahan saat mengakses API geolokasi: {e}")
        return None

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return {
            "Domain Name": w.domain_name,
            "Registrar": w.registrar,
            "Creation Date": w.creation_date,
            "Expiration Date": w.expiration_date,
            "Emails": w.emails,
            "Organization": w.org,
            "Name Servers": w.name_servers,
        }
    except Exception as e:
        return {"WHOIS Error": f"Gagal mengambil data WHOIS: {e}"}

def print_section(title, data):
    print(f"\n📌 {title}")
    print("-" * (len(title) + 4))
    if isinstance(data, dict):
        for k, v in data.items():
            pprint.pprint(f"{k}: {v}")
    else:
        print(data)

def main():
    print("🔍 Domain Info Checker (IP, Lokasi, WHOIS)")
    print("=" * 40)
    domain = input("Masukkan nama domain (contoh: google.com): ").strip()

    if not domain:
        print("❌ Domain tidak boleh kosong.")
        return

    ip_address = resolve_domain_to_ip(domain)
    if not ip_address:
        return

    print_section("Alamat IP", {"IP": ip_address})

    geo = get_geolocation(ip_address)
    if geo:
        print_section("Informasi Geolokasi", geo)

    whois_data = get_whois_info(domain)
    if whois_data:
        print_section("Informasi WHOIS", whois_data)

if __name__ == "__main__":
    main()
