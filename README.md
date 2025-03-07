# Data Analysis Project - Bike Rental Dashboard 🚲

## Deskripsi Proyek
Proyek ini adalah analisis data penyewaan sepeda yang dibuat dengan menggunakan Streamlit untuk menampilkan dashboard interaktif. Data yang digunakan mencakup informasi tentang jumlah penyewaan sepeda berdasarkan cuaca, hari kerja vs hari libur.
## Persyaratan Sistem
Untuk menjalankan proyek ini, Anda perlu menginstal beberapa dependensi yang diperlukan. Silakan ikuti langkah-langkah berikut sesuai dengan lingkungan yang Anda pilih:

### Setup Lingkungan - Anaconda
Jika Anda menggunakan Anaconda, jalankan perintah berikut untuk membuat lingkungan baru dan menginstal dependensi:
```bash
conda create --name submission python=3.9
conda activate submission
pip install -r requirements.txt
```
### Setup Lingkungan - Shell/Terminal
Jika Anda menggunakan terminal biasa (tanpa Anaconda), jalankan perintah berikut:
```bash
mkdir submission
cd submission
pipenv install
pipenv shell
pip install -r requirements.txt
```
## Menjalankan Streamlit App
Setelah instalasi selesai, jalankan aplikasi Streamlit dengan perintah berikut:
```bash
streamlit run dashboard.py
```
