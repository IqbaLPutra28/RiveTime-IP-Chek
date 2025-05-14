# RiveTime (Python Tool)

RiveTime adalah script Python sederhana yang berfungsi untuk mencari **alamat IP dari sebuah domain**, lalu mendapatkan **informasi lokasi geografis** berdasarkan IP tersebut.

Program Python untuk melakukan pengecekan informasi domain secara lengkap:
- 🔁 Resolusi domain ke alamat IP
- 🌍 Deteksi geolokasi berdasarkan IP
- 📄 Informasi WHOIS: email, organisasi, registrar, tanggal pendaftaran, dan lainnya

---

## ✨ Fitur

- ✅ Resolusi domain ke alamat IP menggunakan `socket`
- ✅ Deteksi lokasi geografis dari IP dengan API `geolocation-db.com`
- ✅ Ambil informasi WHOIS domain (jika tersedia)
- ✅ Output terformat rapi menggunakan `pprint`
- ✅ Penanganan error dan validasi input

---

## 🧰 Kebutuhan Sistem

- Python 3.6 atau lebih baru
- Koneksi internet

### 📦 Library yang Digunakan
- `requests`
- `python-whois`

Instalasi:
```bash
pip install requests python-whois

### 📦 Cara Menjalankan

```bash
python3 RiveTime.py
