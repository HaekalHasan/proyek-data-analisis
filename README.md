# Data Analysis Project - Bike Rental Dashboard 🚲

## Deskripsi Proyek
Proyek ini adalah analisis data penyewaan sepeda yang dibuat dengan menggunakan Streamlit untuk menampilkan dashboard interaktif. Data yang digunakan mencakup informasi tentang jumlah penyewaan sepeda per hari, cuaca, hari kerja vs akhir pekan, dan faktor lainnya.

## Persyaratan Sistem
Untuk menjalankan proyek ini, Anda perlu menginstal beberapa dependensi yang diperlukan. Silakan ikuti langkah-langkah berikut sesuai dengan lingkungan yang Anda pilih:

### Setup Lingkungan - Anaconda
Jika Anda menggunakan Anaconda, jalankan perintah berikut untuk membuat lingkungan baru dan menginstal dependensi:
```bash
conda create --name bike-rental-dashboard python=3.9
conda activate bike-rental-dashboard
pip install -r requirements.txt
```
```bash
mkdir bike_rental_dashboard
cd bike_rental_dashboard
pipenv install
pipenv shell
pip install -r requirements.txt
```
```bash
streamlit run dashboard.py
```
```bash
/bike_rental_dashboard
|-- dashboard.py            # Script Streamlit untuk dashboard
|-- data/                   # Folder yang berisi dataset
|   |-- bike_rental_data.csv
|-- requirements.txt        # Daftar dependensi Python
|-- README.md               # Panduan untuk menjalankan proyek
|-- .gitignore              # Daftar file dan folder yang diabaikan oleh Git
```