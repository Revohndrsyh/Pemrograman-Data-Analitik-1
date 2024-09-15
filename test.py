import requests
from bs4 import BeautifulSoup

def analitik_web(url):
    try:
        # Mengambil konten halaman
        response = requests.get(url)
        response.raise_for_status()  # Memastikan permintaan berhasil

        # Mem-parsing konten HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Mengambil judul halaman
        judul = soup.title.string if soup.title else 'Tidak ada judul'

        # Mengambil semua tautan
        tautan = [a['href'] for a in soup.find_all('a', href=True)]

        # Menampilkan hasil analitik
        print(f"Judul Halaman: {judul}")
        print(f"Jumlah Tautan: {len(tautan)}")
        print("Tautan:")
        for link in tautan:
            print(link)

    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan: {e}")

# Ganti URL berikut dengan URL yang ingin Anda analisis
url_web = 'https://www.example.com'
analitik_web(url_web)