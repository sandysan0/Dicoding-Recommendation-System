# -*- coding: utf-8 -*-
"""Sandy Susanto - Dicoding - Machine Learning Terapan - Submission 2 : Rekomendasi Buku.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sbe5vsj919WGm2piR7UopRlRT_USrE2G

# **Proyek Akhir : Membuat Model Sistem Rekomendasi**

---

## Dicoding Submission
## Machine Learning Terapan

---

Kriteria submission:
- Project merupakan hasil pekerjaan sendiri.
- Project belum pernah digunakan untuk submission kelas Machine Learning di Dicoding dan belum pernah dipublikasikan di platform manapun.
- Dataset yang dipakai bebas, asal bisa digunakan untuk membuat sistem rekomendasi.
- Memberikan **dokumentasi** menggunakan **text cell** pada notebook (.ipynb) untuk menjelaskan **setiap tahapan proyek**.
- Menentukan solusi permasalahan dengan memilih pendekatan berikut:
    - Content-based Filtering
    - Collaborative Filtering
- Membuat draf laporan proyek machine learning yang menjelaskan alur proyek Anda dari mulai pemilihan domain permasalahan (problem domain), data understanding, data preparation, modeling, hingga tahap evaluasi. Ketentuan draf laporan proyek machine learning dapat Anda lihat pada sub modul berikutnya tentang **Detail Laporan**.

---

Saran:
- Menerapkan Rubrik/Kriteria Penilaian (Tambahan) untuk mendapatkan skala penilaian (bintang) yang lebih tinggi.


---


Tips:
- Menerapkan **Rubrik/Kriteria Penilaian (Tambahan)** untuk mendapatkan skala penilaian (bintang) yang lebih tinggi.
- Anda dapat memilih beberapa topik rekomendasi (namun tidak terbatas pada daftar) berikut:
  - Rekomendasi film
  - Rekomendasi buku
  - Rekomendasi musik
  - Rekomendasi video
  - Rekomendasi produk
  - Rekomendasi artikel
  - Rekomendasi berita
  - dsb.

- Untuk export project yang Anda kerjakan di Colaboratory sebagai berkas ipynb, klik tombol file yang berada di pojok kiri atas Colaboratory. Kemudian pilih **download .ipynb** dan **download .py**.
- Untuk melakukan training pada Colab dari data yang ada pada Drive, dapat Anda lihat caranya pada [tautan berikut](https://www.youtube.com/watch?v=Gvwuyx_F-28&t=384s).
---

Detail penilaian submission:
- **Bintang 1**: Semua ketentuan terpenuhi, tetapi terdapat indikasi plagiat dengan menggunakan proyek orang lain dan hanya mengubah kontennya saja.
- **Bintang 2**: Semua ketentuan terpenuhi, tetapi penulisan kode dan laporan berantakan.
- **Bintang 3**: Semua ketentuan terpenuhi, penulisan kode, dan laporan cukup baik.
- **Bintang 4**: Semua ketentuan terpenuhi, menerapkan minimal tiga (3) kriteria **Rubrik Penilaian Tambahan** pada laporan.
- **Bintang 5**: Semua ketentuan terpenuhi, menerapkan minimal **seluruh kriteria (6) Rubrik Penilaian Tambahan** pada laporan.

---

# Data Diri

- Nama: Sandy Susanto
- E-mail: susantosandy12@gmail.com
- Beasiswa : IDCamp2023

---
---

# **1. *Library Import***

*Library* [`os`](https://docs.python.org/3/library/os.html) untuk memproses *function* dari *operating system*. `os.environ` untuk membaca *username* dan *key* [Kaggle](https://kaggle.com).

*Library* [`numpy`](https://numpy.org) untuk melakukan pemrosesan matematis berupa himpunan, *array*, matriks multidimensi, dan vektorisasi.

*Library* [`pandas`](https://pandas.pydata.org) untuk melakukan pemrosesan, analisis dan manipulasi data.

*Library* [`tensorflow`](https://www.tensorflow.org) untuk melakukan pelatihan *machine learning* dan *neural networks*.

*Library* [`sklearn`](https://scikit-learn.org) untuk melakukan pemrosesan *machine learning* dan *data analysis*.

*Library* [`seaborn`](https://seaborn.pydata.org) untuk membuat visualisasi data yang berbasis `matplotlib`.

*Library* [`matplotlib`](https://matplotlib.org) untuk melakukan visualisasi menggunakan *plotting*.
"""

import os
import numpy as np
import pandas as pd
import tensorflow as tf
import zipfile
import seaborn as sns
import matplotlib.pyplot as plt

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.metrics import RootMeanSquaredError

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""# **2. *Data Loading***

## 2.1 *Kaggle Credential*

**Menghubungkan environtment** [`Colab`](https://colab.research.google.com/) dengan [Kaggle Dataset](https://kaggle.com/) menggunakan `Kaggle.json` yang didapatkan dari meng-*generate* [Kaggle API](https://www.kaggle.com/docs/api) token.

---
Gunakan `!python` untuk mengecek versi [`pyhton`](https://www.python.org/) di [`Colab`](https://colab.research.google.com/) dan memakai `!gdown` untuk men*download* `Kaggle.json` yang disimpan di [Google Drive](https://drive.google.com/)
"""

#Cek python dulu
!python --version

#Download Kaggle Credential
!pip install -q kaggle
!pip install --upgrade gdown
!gdown 1-78YSIrsevhJCtAsWGp2D6j189CdGP76
file = open("kaggle.json", "r")
data = file.read()
print(data)

"""Membuat *environtment* di `/root` dan mengetest *Kaggle API Command*"""

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod u=rw,g=,o= ~/.kaggle/kaggle.json
!ls ~/.kaggle
!kaggle datasets list

"""## 2.2 *Dataset Download*

Untuk proyek ini, *dataset* yang digunkan berjudul [*Book Recommendation Dataset*](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) dari Kaggle. *File* yang akan diunduh masih dalam format terkompresi dengan nama `book-recommendation-dataset.zip`.
"""

!kaggle datasets download -d arashnic/book-recommendation-dataset

"""Selanjutnya adalah menggunakan metode `extractall` dari modul `zipfile` untuk mengekstrak berkas `book-recommendation-dataset.zip`. Dengan menggunakan `zip.extractall`, adad didapatkan tiga berkas [`.csv`](https://en.wikipedia.org/wiki/Comma-separated_values 'Wikipedia - Comma-separated values'): `Books.csv`, `Ratings.csv`, dan `Users.csv`, yang akan digunakan dalam proyek rekomendasi buku ini."""

with zipfile.ZipFile('book-recommendation-dataset.zip','r') as zip:
  zip.extractall('/content/')

"""# **3. *Data Understanding***

## 3.1 Atribut Dasar dari *Dataset*

Gunakan *library* [Pandas](https://pandas.pydata.org 'Python Data Analysis Library') untuk memuat file `Books.csv`, `Ratings.csv`, `Users.csv` ke dalam *dataframe* yang akan disimpan dalam variabel `books`, `rating`, dan `users`. Ini akan mengubah data dari format `.csv` menjadi struktur *dataframe* yang dapat dikelola dengan Python.
"""

books = pd.read_csv('Books.csv')
rating = pd.read_csv('Ratings.csv')
users = pd.read_csv('Users.csv')

"""Untuk mengetahui berapa banyak nilai unik yang ada dalam setiap kolom dari *dataframe* dapat dengan memanfaatkan metode `.unique()`."""

# Mendefinisikan dictionary untuk menyimpan informasi yang ingin dicetak
info_buku = {
    'ISBN': ('Jumlah data ISBN', books),
    'Book-Title': ('Jumlah data Judul', books),
    'Book-Author': ('Jumlah data Penulis', books),
    'Publisher': ('Jumlah data Penerbit', books),
    'Year-Of-Publication': ('Jumlah data Tahun', books)
}

info_rating = {
    'User-ID': ('Jumlah data Pembaca', rating),
    'ISBN': ('Jumlah data Buku', rating)
}

# Fungsi untuk mencetak informasi
def cetak_info(info_dict):
    for kolom, (deskripsi, df) in info_dict.items():
        print(f'{deskripsi: <30}: {df[kolom].nunique()}')

# Mencetak informasi buku, rating, dan user
cetak_info(info_buku)
print('=====' * 9)
cetak_info(info_rating)
print(f'Jumlah data Rating yang diterima : {len(rating)}')
print('=====' * 9)
print(f'Jumlah data User : {len(users)}')

"""## 3.2 *Univariate Exploratory Data Analysis* (EDA)

*Exploratory Data Analysis* ([EDA](https://ankushmulkar.medium.com/complete-exploratory-data-analysis-step-by-step-guide-for-data-analyst-34a07156217a)) merupakan salah satu kegiatan kunci yang sering dijalankan ketika melakukan analisis Data. Kegiatan ini melibatkan penggalian dan pemeriksaan data untuk menemukan wawasan, menyingkap pola, serta menemukan hubungan dan ketidakteraturan yang tersembunyi dalam data.

Dalam EDA, kita menggunakan teknik visualisasi dan statistik deskriptif sebagai cara untuk memahami dan menginterpretasikan data. Sasaran utamanya adalah untuk memperoleh pemahaman yang lebih dalam terhadap data, menemukan pola, dan melakukan pengujian terhadap hipotesis yang akan menjadi panduan dalam analisis data yang lebih detail.

### 3.2.1 *Dataset* Books

*Exploratory Data Analysis* (EDA) untuk *dataframe* `Books`.
"""

books

books.info()

"""Semua fitur memiliki tipe data object

### 3.2.2 *Dataset* Rating

*Exploratory Data Analysis* (EDA) untuk *dataframe* `rating`.
"""

rating

rating.info()

rating.describe()

"""Untuk mendapatkan gambaran statistik dari kolom `Book-Rating` dalam *dataframe* `Ratings`, kita akan menghitung dan menampilkan ukuran-ukuran statistik dasar. Ini termasuk menghitung rata-rata, standar deviasi, nilai minimum dan maksimum, serta nilai-nilai kuartil yang mencakup kuartil pertama, median, dan kuartil ketiga. Semua ini memberikan wawasan tentang distribusi nilai *rating* yang diberikan oleh pengguna pada buku."""

rating['Book-Rating'].describe().apply(lambda x: '%.f' % x)

"""Untuk menampilkan distribusi frekuensi dari *rating* yang diberikan pengguna pada buku, kita akan membuat histogram. Grafik ini akan menggambarkan seberapa sering *rating* tertentu, dari 1 sampai 10, diberikan oleh pengguna untuk buku-buku yang telah mereka baca."""

colors = plt.cm.viridis(np.linspace(0, 1, 11))

# Membuat histogram frekuensi rating buku
plt.figure(figsize=(14, 5))
plt.barh(rating['Book-Rating'].value_counts().sort_index().index,
         rating['Book-Rating'].value_counts().sort_index().values,
         color=colors)
plt.title('Jumlah Rating Buku')
plt.xlabel('Jumlah')
plt.ylabel('Rating')
plt.xticks(np.arange(0, 720000, 50000))
plt.grid(axis='x', linestyle='-.', linewidth=0.5)
plt.show()

"""Dari grafik histogram "Jumlah Rating Buku" yang telah divisualisasikan, kita dapat melihat bahwa skor *rating* yang paling sering muncul adalah 0, dengan total sekitar 700.000 kali lebih. Karena *rating* 0 ini bisa menimbulkan bias dalam analisis data, ada baiknya kita mengeluarkan *rating* tersebut selama proses persiapan data untuk memastikan hasil analisis yang lebih akurat.

### 3.2.3 *Dataset* User

*Exploratory Data Analysis* (EDA) untuk *dataframe* `users`.
"""

users

"""Dari tabel *dataframe* `Users`, terlihat adanya nilai kosong atau `NaN` pada kolom `Age`. Nilai-nilai ini memerlukan penanganan khusus selama proses persiapan data untuk memastikan keakuratan analisis selanjutnya."""

users.info()

"""Untuk *dataframe* `Users`, kita akan melihat ukuran statistik yang mencakup total entri (`count`), nilai rata-rata (`mean`), variasi data (`std`), serta nilai-nilai ekstrem dan kuartil (`min`, `max`, `25%`, `50%`, `75%`) yang memberikan gambaran tentang distribusi usia pengguna."""

users.describe()

"""Jika diperhatikan, max dari fitur `age` adalah 244, berarti ada pembaca buku yang berusia 244 tahun. Secara sekilas, ini tidak masuk akal, ada manusia modern yang berusia lebih dari 200 tahun. Untuk itu kita akan ekplorasi lebih jauh pada fitur `age` pada bagian *data preparation*.

# **4. *Data Preprocessing***

Proses pra-pemrosesan data, atau *data preprocessing*, adalah langkah penting yang harus diambil sebelum memulai pemodelan. Langkah ini melibatkan transformasi data asli menjadi format yang lebih terstruktur dan bersih, yang kemudian dapat digunakan dalam analisis lebih lanjut. Untuk kasus ini, *data preprocessing* mencakup penyesuaian nama-nama kolom di setiap *dataframe*, menggabungkan informasi ISBN, serta mengintegrasikan *users* untuk mendapatkan gambaran lengkap tentang dataset.

## 4.1 Penyesuaian Nama Kolom/Atribut

Menggunakan fungsi `.assign()` untuk mengubah nama kolom atau atribut dalam *dataframe* bertujuan agar proses referensi kolom atau atribut di langkah-langkah berikutnya menjadi lebih sederhana dan intuitif.

### 4.1.1 Books
"""

new_columns = {
    'ISBN': 'isbn',
    'Book-Title': 'book_title',
    'Book-Author': 'book_author',
    'Year-Of-Publication': 'pub_year',
    'Publisher': 'publisher',
    'Image-URL-S': 'image_s_url',
    'Image-URL-M': 'image_m_url',
    'Image-URL-L': 'image_l_url'
}

books = books.assign(**{new_columns[old]: books[old] for old in new_columns}).drop(columns=new_columns.keys())

books

"""### 4.1.2 Ratings"""

new_columns = {
    'User-ID': 'user_id',
    'ISBN': 'isbn',
    'Book-Rating': 'book_rating'
}

rating = rating.assign(**{new_name: rating[old_name] for old_name, new_name in new_columns.items()}).drop(columns=new_columns.keys())

rating

"""### 4.1.3 Users"""

new_columns = {
    'User-ID'  : 'user_id',
    'Location' : 'location',
    'Age'      : 'age'
}

users = users.assign(**{new_name: users[old_name] for old_name, new_name in new_columns.items()}).drop(columns=new_columns.keys())

users

"""## 4.2 Menggabungkan Data Dengan Fitur ISBN

Fungsi `.concatenate` dari *library* [`numpy`](https://numpy.org) digunakan untuk menggabungkan data ISBN yang terdapat di *dataframe* `df_b` untuk buku dan `df_r` untuk *rating*. Proses ini menyatukan informasi ISBN dari kedua *dataframe* ke dalam satu kolom `isbn`.
"""

ISBNAll = np.unique(np.concatenate([books['isbn'].unique(), rating['isbn'].unique()]))
print('Jumlah Buku berdasarkan ISBN :', len(ISBNAll))

"""## 4.3 Menggabungkan Data *User*

Fungsi `.concatenate` dari *library* [`numpy`](https://numpy.org) digunakan untuk menyatukan data `user_id` yang berasal dari *dataframe* `rating` dan *dataframe* `users`. Proses ini menggabungkan kedua set data berdasarkan kolom `user_id`.
"""

USERAll = np.unique(np.concatenate([rating['user_id'].unique(), users['user_id'].unique()]))
print('Jumlah Buku berdasarkan ISBN :', len(USERAll))

"""# **5. *Data Preparation***

Proses persiapan data, atau *data preparation*, adalah langkah krusial yang mendahului fase pembuatan model *machine learning*. Langkah ini melibatkan modifikasi data ke format yang sesuai untuk pemodelan. Dalam konteks ini, *data preparation* mencakup penanganan nilai yang hilang, verifikasi keberadaan data ganda, serta integrasi data dari *dataframe* *`books`* dan *`rating`* untuk memastikan data siap digunakan.

## 5.1 *Pengecekan* *Missing Value*

Untuk mengetahui jumlah total nilai yang tidak ada atau *missing* dalam sebuah *dataframe*, kita dapat memanfaatkan metode `.isnull().sum()`. Metode ini akan menghitung dan memberikan jumlah keseluruhan nilai yang hilang di seluruh kolom *dataframe*.

### 5.1.1 Books
"""

books.isnull().sum()

"""Dari informasi yang diberikan, terlihat bahwa dalam *dataframe* `books`, ada beberapa entri yang kosong. Khususnya, kolom `book_author` kosong satu entri, `publisher` kosong dua entri, dan `image_l_url` kosong tiga entri.

Oleh karena itu, entri yang tidak memiliki data atau *null* bisa dieliminasi dengan memanfaatkan metode `.dropna()`. Setelah proses ini, pemeriksaan ulang akan menunjukkan bahwa tidak ada lagi entri yang kosong atau *null* dalam *dataframe*.
"""

books = books.dropna()
books.isnull().sum()

"""### 5.1.2 Ratings"""

rating.isnull().sum()

"""Dari informasi yang diberikan, terlihat bahwa dalam *dataframe* `rating`, tidak ada entri yang kosong.

Dari analisis eksploratif data univariat yang telah dilakukan, terungkap bahwa dalam histogram "Jumlah Rating Buku", mayoritas *rating* yang diberikan oleh pengguna adalah 0, dengan total mencapai lebih dari 700.000. Karena keberadaan *rating* 0 ini bisa mempengaruhi hasil analisis secara signifikan, menghapus data *rating* 0 dilakukan untuk mengurangi potensi bias.
"""

print(f'Total Rating 0 : {rating.book_rating.eq(0).sum()}')

rating = rating[rating.book_rating > 0]

"""Ternyata, terdapat 716.109 entri dengan *rating* 0. Entri tersebut akan dikecualikan dari *dataframe*, sehingga hanya *rating* antara 1 dan 10 yang akan dipertimbangkan dalam analisis data."""

colors = plt.cm.viridis(np.linspace(0, 1, 11))

# Membuat plot histogram untuk rating buku
plt.figure(figsize=(14, 5))
plt.barh(rating['book_rating'].value_counts().sort_index().index,
         rating['book_rating'].value_counts().sort_index().values,
         color=colors)
plt.title('Jumlah Rating Buku')
plt.xlabel('Jumlah')
plt.ylabel('Rating')
plt.xticks(np.arange(0, 110000, 7500))
plt.grid(axis='x', linestyle='-.', linewidth=0.5)
plt.show()

"""Dari visualisasi histogram yang ditampilkan, dengan penghapusan *rating* 0, terlihat bahwa distribusi frekuensi menjadi lebih teratur dan mudah dipahami

### 5.1.3 Users

Sebelum melakukan *missing value implementation*, ingat bahwa sebelumnya telah dibahas di bagian analisis eksploratif data univariat bahwa fitur `age` di dataframe users memiliki kejanggalan karena nilainya lebih dari 200 tahun.
"""

sorted_users = users.sort_values(by='age', ascending=False)
sorted_users

ab_users = (users['age'] > 120).sum()
print(f"Jumlah user yang usianya lebih dari 120 tahun adalah: {ab_users}")

"""Diketahui bahwa ada 78 data `users` memiliki usia lebih dari 120 tahun. Data-data tersebut akan dihilangkan dari *dataset*"""

users['age'] = pd.to_numeric(users['age'], errors='coerce')
del_users = users[users['age'] > 120].index
users.drop(del_users, inplace=True)

ab_users = (users['age'] > 120).sum()
print(f"Jumlah user yang usianya lebih dari 120 tahun adalah: {ab_users}")

users['age'] = users['age'].astype('object')

"""Mengembalikan tipe data `age` ke *object*"""

users.isnull().sum()

"""Dari informasi yang diberikan, terlihat bahwa dalam *dataframe* `users`, atribut `age` memiliki sejumlah 110.762 entri yang tidak terisi atau *null*.

Oleh karena itu, entri yang tidak terisi pada data `age` bisa diatasi dengan menggantinya menggunakan nilai yang paling banyak terjadi, atau modus, melalui penerapan fungsi `.fillna()` bersamaan dengan `.mode()`. Metode `.mode()` dipilih karena fitur `age` bernilai integer bilangan bulat, sehingga akan lebih cocok untuk mengisi *`NaN`* dengan data yang sering muncul pada fitur `age`.
"""

users.age = users.age.fillna(users.age.mode())
users.isnull().sum()

"""Fitur `age` sudah terisi penuh"""

users.age.hist(bins=100)

"""Visualisasi histogram di atas menunjukan bahwa usia para *users* didominasi di rentang usia 20-an

## 5.2 *Data Duplicate*

Untuk memeriksa keberadaan data yang duplikat dalam *dataframe*, kita dapat menggunakan perintah `.duplicated().sum()` yang akan menghitung jumlah data yang duplikat.
"""

def cetak_duplikat(df, nama_df):
    jumlah_duplikat = df.duplicated().sum()
    print(f'Jumlah data {nama_df} yang duplikat: {jumlah_duplikat}')

cetak_duplikat(books, 'books')
cetak_duplikat(rating, 'rating')
cetak_duplikat(users, 'users')

"""Hasil penelusuran menunjukan bahwa tidak ada data duplikasi pada *dataframe* proyek ini.

## 5.3 *Merger Books and Rating*

*Dataframe* `books` dan `rating` memiliki fitur yang sama, yaitu `isbn`. Sehingga akan baik dilakukan merger untuk mendapatkan kesamaan dan korelasi antar dua *dataframe*.
"""

books_rating = pd.merge(rating, books, on=['isbn'])
books_rating

"""# **6. *Model Development***

Langkah berikutnya dalam proyek ini adalah fase *modeling*, di mana kita akan mengembangkan model *machine learning* untuk sistem rekomendasi. Model ini akan menyarankan buku-buku yang paling sesuai untuk pengguna berdasarkan algoritma rekomendasi yang dipilih. Dari analisis data awal, kita mengetahui bahwa kita memiliki jumlah data yang sangat besar untuk buku, *rating*, dan pengguna, yang berkisar dari ratusan ribu hingga jutaan entri. Ukuran data ini dapat menyebabkan tantangan dalam hal biaya komputasi, seperti waktu pemrosesan yang lama dan kebutuhan akan RAM atau GPU dengan kapasitas besar.

Mengingat keterbatasan ini, kita akan membatasi dataset yang digunakan dalam pemodelan *machine learning* ini. Kita akan menggunakan hanya 20.000 entri teratas dari data buku dan 10.000 entri teratas dari data *rating*. Langkah ini akan membantu mengurangi beban komputasi sambil tetap memungkinkan kita untuk melatih model yang efektif dan memberikan rekomendasi yang berkualitas.
"""

books   = books[:20000]
rating = rating[:10000]

"""## 6.1 *Content-based Recommendation*

*Content-based recommendations* adalah sistem rekomendasi yang menggunakan detail dan atribut dari item yang ada, seperti buku, film, atau produk lainnya, untuk memberikan saran yang sesuai dengan preferensi pengguna. Sistem ini menganalisis kata kunci dan atribut yang ditetapkan pada item dalam database untuk menghasilkan prediksi yang mungkin berguna bagi pengguna.

Dalam sistem ini, profil pengguna dibuat berdasarkan item-item yang mereka sukai atau interaksi yang mereka lakukan. Misalnya, jika seseorang sering menonton film bergenre komedi, sistem akan merekomendasikan film lain dengan genre yang sama atau yang memiliki karakteristik serupa.

### 6.1.1 TF-IDF Vectorizer

*Term Frequency Inverse Document Frequency Vectorizer*, atau [TF-IDF Vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html 'TfidfVectorizer - scikit-learn Documentation'), adalah sebuah metode untuk mengubah teks menjadi angka (vektor) yang dapat digunakan dalam pemrosesan data dan model *machine learning*. TF-IDF mengukur pentingnya sebuah kata dalam dokumen relatif terhadap kumpulan dokumen (korpus).
"""

tf_idf = TfidfVectorizer()
tf_idf.fit(books.book_author)
tf_idf.get_feature_names_out()

"""Mengubah data buku yang memiliki kolom `book_author` menjadi format matriks bisa diwujudkan dengan memanfaatkan metode `.fit_transform()`."""

tf_idf_matrix = tf_idf.fit_transform(books.book_author)
tf_idf_matrix.shape

"""Hasil transformasi data tersebut menghasilkan sebuah matriks dengan dimensi yang terdiri dari 20.000 entri buku dan 8.877 entri penulis.

Hasil yang diperoleh dari *vectorizer* masih berupa vektor, dan untuk mengonversinya menjadi matriks, kita dapat menggunakan metode `.todense()`.
"""

tf_idf_matrix.todense()

"""Agar matriks TF-IDF dapat dilihat dengan jelas, kita perlu mengonversinya menjadi *dataframe* dimana kolom-kolomnya diwakili oleh nama-nama *author* dan setiap barisnya, atau *index*, diisi dengan judul-judul buku."""

pd.DataFrame(
    tf_idf_matrix.todense(),
    columns = tf_idf.get_feature_names_out(),
    index   = books.book_title
).sample(20, axis=1).sample(10, axis=0)

"""### 6.1.2 *Cosine Similarity*

*Cosine Similarity* adalah metrik matematika yang digunakan untuk mengukur kesamaan antara dua vektor dalam ruang multidimensi. Ini didefinisikan sebagai kosinus sudut antara vektor, yang merupakan hasil perkalian titik dari vektor dibagi dengan hasil kali panjang mereka. Metrik ini sangat berguna dalam analisis teks dan sistem rekomendasi, di mana teks diubah menjadi vektor kata dan kesamaan semantik antara dokumen dapat diukur berdasarkan arah vektor tersebut, bukan hanya berdasarkan magnitudo atau ukuran mereka. Cosine Similarity selalu berada dalam interval -1 hingga 1, di mana -1 berarti persis berlawanan, 0 menunjukkan ortogonal atau tidak berkorelasi, dan 1 berarti persis sama.

Untuk menentukan seberapa mirip satu judul buku dengan yang lain, kita bisa menggunakan teknik *cosine similarity*. Fungsi [`cosine_similarity`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html 'cosine_similarity - scikit-learn Documentation') dari perpustakaan `sklearn` memungkinkan kita untuk melakukan perhitungan ini.
"""

cosine_sim = cosine_similarity(tf_idf_matrix)
cosine_sim

"""Menggunakan metode yang serupa, kita dapat mengonversi *array* dari *cosine similarity* menjadi *dataframe* untuk memudahkan dalam melihat dan menganalisis datanya."""

cosine_sim_df = pd.DataFrame(
    cosine_sim,
    columns = books.book_title,
    index   = books.book_title
)

print(f'Cosine Similarity Shape : {cosine_sim_df.shape}')

cosine_sim_df.sample(8, axis=1).sample(8, axis=0)

"""### 6.1.3 Recommendation Testing

Membuat fungsi `author_recommendations` bertujuan untuk menunjukkan saran buku dari sistem algoritma yang telah dikembangkan, dengan menggunakan judul buku yang telah dibaca oleh pengguna sebagai parameter masukannya.
"""

def author_recommendations(book_title, similarity_data=cosine_sim_df, items=books[['book_title', 'book_author']], k=10):
    index = similarity_data.loc[:,book_title].to_numpy().argpartition(range(-1, -k, -1))
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    closest = closest.drop(book_title, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

readed_book_title = 'Room for a Single Lady'

"""Mengambil sample buku yang sudah dibaca"""

books[books.book_title.eq(readed_book_title)]

"""Dalam situasi tertentu, sistem rekomendasi mungkin menghasilkan saran buku yang sama lebih dari satu kali, yang mengharuskan kita untuk mengeliminasi judul-judul buku yang sama tersebut dari daftar rekomendasi."""

author_recommendations(readed_book_title).drop_duplicates()

"""Terlihat bahwa sistem yang dikembangkan mampu memberikan saran beberapa buku berdasarkan masukan judul buku "*Room for a Single Lady*", dengan hasil yang didasarkan pada analisis algoritma sistem. Terlihat bahwa rekomendasi yang dihasilkan merujuk ke penulisa buku yang ada nama Clare, dan menghasilkan satu rekomendasi dengan penulis buku yang sama dengan buku yang telah di baca, yaitu *11 Edward Street* oleh Clare Boylan.

## 6.2 *Collaborative Filtering Recommendation*

*Collaborative Filtering Recommendation* adalah teknik yang digunakan dalam sistem rekomendasi untuk memprediksi preferensi atau minat pengguna berdasarkan preferensi atau minat pengguna lain yang serupa. Teknik ini tidak mengandalkan konten item yang direkomendasikan, melainkan pada pola interaksi dan penilaian yang dilakukan oleh pengguna terhadap item-item tersebut.

### 6.2.1 *Data Preparation*

Sekarang kita berada di fase *preprocessing*. Di sini, kita harus mempersiapkan data dengan mengubah fitur `user_id` dan `isbn` menjadi indeks integer.

Melakukan penyandian (*encoding*) fitur `user_id` ke dalam indeks integer.
"""

user_ids = rating.user_id.unique().tolist()
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}

print(user_ids)
print(user_to_user_encoded)
print(user_encoded_to_user)

"""Melakukan penyandian (*encoding*) fitur `isbn` buku ke dalam indeks integer."""

book_ids = rating.isbn.unique().tolist()
book_to_book_encoded = {x: i for i, x in enumerate(book_ids)}
book_encoded_to_book = {i: x for i, x in enumerate(book_ids)}

print(book_ids)
print(book_to_book_encoded)
print(book_encoded_to_book)

"""Selanjutnya, kita akan menetapkan `user_id` dan `isbn` ke dataframe yang sesuai."""

rating['user'] = rating.user_id.map(user_to_user_encoded)
rating['book'] = rating.isbn.map(book_to_book_encoded)

"""Kita akan melakukan verifikasi terhadap total jumlah pengguna, total jumlah buku, serta nilai *rating* terendah dan tertinggi."""

num_users = len(user_encoded_to_user)
num_books = len(book_encoded_to_book)

min_rating = min(rating.book_rating)
max_rating = max(rating.book_rating)

print(num_users)
print(num_books)
print(f'Number of User: {num_users}, Number of Books: {num_books}, Min Rating: {min_rating}, Max Rating: {max_rating}')

"""### 6.2.2 *Training Data and Validation Data Split*

Kita akan mengaudit *dataframe* `ratings` untuk memastikan bahwa kolom tambahan `user` dan `book` telah terpetakan dengan benar. Kita juga akan mengacak urutan data menggunakan metode [`.sample(frac=1)`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html 'pandas.DataFrame.sample - Pandas Documentation').
"""

rating = rating.sample(frac=1, random_state=42)
rating

"""Melakukan pembagian *dataset* dengan rasio 80:20, yaitu 80% untuk data latih (*training data*) dan 20% untuk data uji (*validation data*).

Kemudian, kita akan membagi data menjadi set pelatihan dan validasi dengan perbandingan 80:20. Sebelum itu, kita harus menggabungkan `user` dan `book` menjadi satu nilai yang unik. Setelah itu, kita normalisasi nilai `book_rating` ke rentang 0 hingga 1 untuk mempermudah proses pelatihan.
"""

x = rating[['user', 'book']].values
y = rating['book_rating'].apply(lambda x: (x-min_rating) / (max_rating-min_rating)).values

train_indices = int(0.8 * rating.shape[0])

xTrain, xVal, yTrain, yVal = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""### 6.2.3 *Model Development and Training*

Di tahap ini, model akan mengevaluasi seberapa cocok pengguna dengan restoran menggunakan metode embedding. Pertama-tama, kita akan menerapkan proses `embedding` pada data `user` dan `book`. Kemudian, kita akan menghitung hasil perkalian *dot product* dari `embedding` `user` dan `book`. Kita juga bisa menambahkan bias untuk masing-masing `user` dan `book`. Nilai kecocokan akan diatur dalam rentang [0,1] menggunakan fungsi aktivasi `sigmoid`.

Pada tahap pembuatan model akan menggunakan kelas `RecommenderNet` dengan [*keras model class*](https://keras.io/api/models/model 'Model class - Keras Documentation').
"""

class RecommenderNet(tf.keras.Model):
    def __init__(self, num_users, num_books, embedding_size, **kwargs):
        super(RecommenderNet, self).__init__(**kwargs)
        self.num_users = num_users
        self.num_books = num_books
        self.embedding_size = embedding_size
        self.user_embedding = layers.Embedding(
            num_users,
            embedding_size,
            embeddings_initializer = 'he_normal',
            embeddings_regularizer = keras.regularizers.l2(1e-6)
        )
        self.user_bias      = layers.Embedding(num_users, 1)
        self.book_embedding = layers.Embedding(
            num_books,
            embedding_size,
            embeddings_initializer = 'he_normal',
            embeddings_regularizer = keras.regularizers.l2(1e-6)
        )
        self.book_bias = layers.Embedding(num_books, 1)

    def call(self, inputs):
        user_vector = self.user_embedding(inputs[:,0])
        user_bias   = self.user_bias(inputs[:, 0])
        book_vector = self.book_embedding(inputs[:, 1])
        book_bias   = self.book_bias(inputs[:, 1])

        dot_user_book = tf.tensordot(user_vector, book_vector, 2)

        x = dot_user_book + user_bias + book_bias

        return tf.nn.sigmoid(x)

"""Selanjutnya, dalam langkah *model compiling*, kita akan memilih [Adam optimizer](https://keras.io/api/optimizers/adam 'Adam - Keras Documentation'), [binary crossentropy loss function](https://keras.io/api/losses/probabilistic_losses/#binarycrossentropy-class 'BinaryCrossentropy - Keras Documentaion'), dan metrik [RMSE](https://keras.io/api/metrics/regression_metrics/#rootmeansquarederror-class 'RootMeanSquaredError - Keras Documentation') (Root Mean Squared Error) sebagai parameter."""

model = RecommenderNet(num_users, num_books, 50)

model.compile(
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    loss      = tf.keras.losses.BinaryCrossentropy(),
    metrics   = [tf.keras.metrics.RootMeanSquaredError()]
)

"""Untuk melatih model, kita akan menggunakan metode `.fit()`, menetapkan `batch_size` menjadi 20 dan jumlah `epochs` sebanyak 25."""

history = model.fit(
    x               = xTrain,
    y               = yTrain,
    batch_size      = 20,
    epochs          = 40,
    validation_data = (xVal, yVal),
)

"""Kita akan memvisualisasikan *error* dari hasil *training* dan validasi, serta *loss* dari *training* dan validasi, menggunakan grafik yang dibuat dengan *library* [`matplotlib`](https://matplotlib.org 'Matplotlib - Visualization with Python')."""

rmse_data = history.history['root_mean_squared_error']
val_rmse_data = history.history['val_root_mean_squared_error']
loss_data = history.history['loss']
val_loss_data = history.history['val_loss']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.plot(rmse_data, label='RMSE', color='blue')
ax1.plot(val_rmse_data, label='Validation RMSE', color='red')
ax1.set_title('Training and Validation RMSE')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Root Mean Squared Error')
ax1.legend(loc='lower right')

ax2.plot(loss_data, label='Training Loss', color='green')
ax2.plot(val_loss_data, label='Validation Loss', color='orange')
ax2.set_title('Training and Validation Loss')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()

"""## 6.2.4 *Get Recommendation Testing*

Melakukan pendefinisian ulang *dataset* *books* dan *ratings*.
"""

datasetBook   = books
datasetRating = rating

datasetBook.info()

"""Untuk menghasilkan saran buku dari sistem, kita memerlukan sampel data pengguna yang diambil secara acak. Kita juga perlu menentukan variabel untuk buku yang belum dibaca oleh pengguna (`notReadedBooks`), yang akan menjadi daftar rekomendasi. Kita bisa mendapatkan daftar ini dengan menerapkan operator bitwise NOT ([`~`](https://docs.python.org/3/reference/expressions.html#unary-arithmetic-and-bitwise-operations 'Unary Arithmetic and Bitwise Operations - Python Documentation')) pada variabel yang menyimpan buku yang sudah dibaca oleh pengguna (`readedBooks`)."""

userId      = datasetRating.user_id.sample(1).iloc[0]
readedBooks = datasetRating[datasetRating.user_id == userId]

notReadedBooks = datasetBook[~datasetBook['isbn'].isin(readedBooks.isbn.values)]['isbn']
notReadedBooks = list(
    set(notReadedBooks).intersection(set(book_to_book_encoded.keys()))
)

notReadedBooks = [[book_to_book_encoded.get(x)] for x in notReadedBooks]
userEncoder    = user_to_user_encoded.get(userId)
userBookArray = np.hstack(
    ([[userEncoder]] * len(notReadedBooks), notReadedBooks)
)

"""Untuk mendapatkan saran buku, kita dapat memanggil metode [`.predict()`](https://keras.io/api/models/model 'Model class - Keras Documentation') pada model yang telah dilatih dengan *library Keras*."""

ratings = model.predict(userBookArray).flatten()

topRatingsIndices   = ratings.argsort()[-10:][::-1]
recommendedBookIds = [
    book_encoded_to_book.get(notReadedBooks[x][0]) for x in topRatingsIndices
]

print('Showing recommendations for users: {}'.format(userId))
print('=====' * 8)
print('Book with high ratings from user')
print('-----' * 8)

topBookUser = (
    readedBooks.sort_values(
        by = 'book_rating',
        ascending=False
    )
    .head(5)
    .isbn.values
)

bookDfRows = datasetBook[datasetBook['isbn'].isin(topBookUser)]
for row in bookDfRows.itertuples():
    print(row.book_title, ':', row.book_author)

print('=====' * 8)
print('Top 10 Books Recommendation')
print('-----' * 8)

recommended_resto = datasetBook[datasetBook['isbn'].isin(recommendedBookIds)]
for row in recommended_resto.itertuples():
    print(row.book_title, ':', row.book_author)

"""Dari informasi yang diberikan, tampaknya sistem telah memilih secara acak seorang pengguna dengan `user_id` **695**. Sistem kemudian mencari buku-buku yang paling disukai oleh pengguna tersebut, yang meliputi:
*   **Elements of Programming With Perl** karya **Andrew L. Johnson**
*   **To Catch a Cat** karya **Marian Babson**
*   **People of the Wolf (The First North Americans series, Book 1)** karya **W. Michael Gear**
*   **The Door to December** karya **Dean R. Koontz**

Setelah itu, sistem akan membandingkan buku-buku dengan penilaian tertinggi dari pengguna ini dengan seluruh katalog buku, kecuali yang sudah dibaca, dan mengurutkan rekomendasi berdasarkan skor tertinggi. Terlihat ada 10 buku yang direkomendasikan oleh sistem. Rekomendasi yang diberikan benar-benar tidak ada kesamaan penulis buku dari buku yang sudah dibaca. Ini menunjukan bahwa rekomendasi dibentuk dari hasil kesamaan para `users` lainnya.

# **7. Kesimpulan**

Ringkasannya, model rekomendasi buku yang telah dikembangkan berhasil memenuhi kebutuhan pengguna dengan menggabungkan dua pendekatan: *Content-based Recommendation* dan *Collaborative Filtering Recommendation*. Dalam *Collaborative Filtering Recommendation*, penting untuk memiliki data peringkat dari pengguna untuk memahami dan memprediksi preferensi mereka. Sebaliknya, *Content-based Recommendation* tidak bergantung pada peringkat pengguna, tetapi lebih fokus pada analisis fitur-fitur spesifik dari buku itu sendiri.

Dengan memanfaatkan kedua teknik ini, model dapat memberikan saran yang sangat relevan dan personal, karena tidak hanya mempertimbangkan apa yang telah dinikmati oleh pengguna di masa lalu, tetapi juga menemukan pilihan baru yang serupa dengan minat mereka berdasarkan karakteristik buku. Ini menciptakan pengalaman yang kaya dan bervariasi, memungkinkan pengguna untuk menemukan karya-karya baru yang mungkin belum pernah mereka pertimbangkan sebelumnya, sambil tetap sejalan dengan selera pribadi mereka.
"""