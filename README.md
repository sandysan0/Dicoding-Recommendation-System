# Laporan Proyek Machine Learning - Sandy Susanto

## Project Overview

Proyek ini membahas literasi digital dan kebutuhan teknologi literatur untuk mendukung akses informasi dalam literasi. 

![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/11936652-62e8-4c2a-8a60-d8618e4f1af4)

Dalam konteks pendidikan dan kehidupan sehari-hari, literasi secara tradisional diakui sebagai kemampuan dasar membaca dan menulis yang menjadi fondasi pengetahuan masyarakat. Namun, di tengah perubahan zaman yang ditandai dengan digitalisasi, konsep literasi telah mengalami evolusi yang signifikan. Kini, literasi tidak hanya terbatas pada kemampuan literasi konvensional, melainkan juga mencakup keterampilan digital yang meliputi kolaborasi, komunikasi, kewarganegaraan digital, pemecahan masalah, berpikir kritis, dan kreativitas. Keterampilan-keterampilan ini dianggap vital dalam literatur terkini dan menjadi kompetensi esensial bagi tenaga kerja di era digital. Pengajaran keterampilan abad ke-21 ini kepada generasi muda menjadi penting, mengingat tidak semua individu secara otomatis mahir dalam menggunakan teknologi informasi dan komunikasi secara efektif meskipun mereka tumbuh di era digital [[3]](https://link.springer.com/article/10.1007/s10639-021-10451-0#Sec2). 

Peran media baru, khususnya Internet dan media sosial, dalam meningkatkan keterlibatan masyarakat dan pengaruhnya terhadap pemuda, telah menjadi fokus diskusi yang penting. Peningkatan penggunaan media sosial oleh remaja yang sering menggunakan perangkat mobile menunjukkan dampak yang signifikan terhadap prospek demokrasi di masa depan. Studi terkait menunjukkan adanya korelasi positif antara penggunaan media sosial dan tingkat partisipasi, di mana media sosial berperan dalam memfasilitasi keterlibatan melalui jaringan komunikasi dua arah. Penelitian ini mengeksplorasi berbagai dimensi literasi digital sebagai evolusi dari literasi media tradisional, yang dianggap sebagai kerangka kerja yang lebih relevan untuk penelitian tentang pemuda, khususnya dalam konteks pendidikan literasi yang ada di kelas [[1]](https://www.tandfonline.com/doi/full/10.1080/17482798.2020.1728700).

Literasi digital, yang pada awalnya hanya dianjurkan, kini telah menjadi komponen kunci dalam membentuk warga negara yang adaptif di era digital. Meskipun demikian, definisi dan ruang lingkup literasi digital belum distandarisasi dan terus berkembang seiring dengan kemajuan ilmu pengetahuan. Literasi digital kini diinterpretasikan sebagai serangkaian keterampilan yang saling terkait dan diperlukan untuk sukses di dunia digital, dengan penekanan khusus pada pentingnya pendekatan kritis yang berkembang melalui studi literasi media. [[2]](https://www.mdpi.com/2304-6775/8/4/48).

Pentingnya sistem rekomendasi buku digital terletak pada kemampuannya untuk memfasilitasi penemuan literatur baru dan sumber daya yang relevan, yang secara signifikan meningkatkan keterlibatan dan kepuasan pengguna. Hal ini berkontribusi pada peningkatan pengalaman pembelajaran secara keseluruhan. Lebih lanjut, sistem ini berperan dalam mengatasi penurunan minat baca, khususnya di kalangan generasi muda, dengan menyajikan rekomendasi yang tepat melalui perpustakaan, institusi pendidikan, dan *platform e-learning.* Di tengah berkembangnya ekonomi yang berbasis pengetahuan, literasi digital harus didefinisikan ulang sebagai kumpulan keterampilan dan kompetensi yang saling berkaitan, yang menjadi syarat esensial untuk mencapai kesuksesan di era digital saat ini. [[4]](https://link.springer.com/chapter/10.1007/978-981-99-6062-0_6#rightslink).

## Business Understanding

### Problem Statements

Dalam konteks sistem rekomendasi buku digital, masalah utama yang sering dihadapi adalah bagaimana cara mengidentifikasi dan merekomendasikan buku yang paling relevan dan menarik bagi pengguna individu. Dengan jumlah buku yang terus bertambah, tantangan ini menjadi semakin kompleks karena harus mempertimbangkan preferensi yang sangat personal dan dinamis dari setiap pengguna. Dari konteks yang telah disampaikan sebelumnya, teridentifikasi dua pertanyaan utama yang akan dijawab melalui proyek ini:
1. Bagaimana proses pembuatan model *machine learning* yang dapat merekomendasikan buku?
2. Apa langkah-langkah yang diperlukan dalam mempersiapkan data sebelum diaplikasikan dalam pengembangan model *machine learning*?

### Goals

Dari permasalahan yang telah diuraikan, tujuan yang ingin dicapai melalui proyek ini adalah sebagai berikut:
1. Menjalankan proses persiapan data secara menyeluruh untuk memastikan data siap digunakan dalam model *machine learning*.
2. Mengembangkan model *machine learning* yang efektif untuk dijadikan sistem rekomendasi buku yang relevan dan realibitas.

### Solution Statements

Dari uraian sebelumnya, beberapa langkah strategis telah diidentifikasi untuk mencapai target proyek, antara lain:
1. Proses pra-pemrosesan yang meliputi:
   - Menyesuaikan dan merenamakan kolom atau atribut untuk mempermudah proses pengambilan dataset dan atribut tertentu.
   - Mengkonsolidasikan data yang terpisah untuk mempersiapkannya untuk penggunaan di tahapan berikutnya.
2. Proses persiapan data akan meliputi:
   - Memeriksa kelogisan data yang terdapat dalam *dataset* dan menghilangkan nilai-nilai yang tidak masuk akal.
   - Memeriksa keberadaan nilai-nilai yang hilang atau null dalam *dataset* dan mengambil tindakan untuk mengeliminasi atau menggantinya dengan nilai yang sesuai.
   - Memastikan tidak ada entri data yang berulang untuk menjaga integritas model dan sistem yang dikembangkan.
3. Dalam fase pembuatan model *machine learning*, dua pendekatan yang berbeda akan diuji.
   - Content-Based Recommendation: Pendekatan ini akan menggunakan karakteristik buku seperti genre, penulis, dan deskripsi untuk merekomendasikan buku baru yang serupa dengan yang telah dibaca atau disukai oleh pengguna. Ini memungkinkan personalisasi yang kuat karena rekomendasi didasarkan pada preferensi pengguna yang spesifik.
   - Collaborative Filtering Recommendation: Pendekatan ini akan menganalisis pola dan preferensi membaca dari banyak pengguna untuk mengidentifikasi kesamaan antara pengguna dan merekomendasikan buku berdasarkan buku yang disukai oleh pengguna dengan preferensi serupa. Ini memanfaatkan ‘kecerdasan kolektif’ dari basis pengguna untuk memberikan rekomendasi yang lebih luas dan beragam.
   
## Data Understanding

![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/9a75d57c-19d7-47de-8652-e4a62edc1ce0)

*Dataset* yang digunakan adalah [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data) dalam bentuk `.csv` ([Comma-separated Values](https://en.wikipedia.org/wiki/Comma-separated_values)). 

Dalam *dataset* tersebut berisi tiga (3) berkas CSV, yaitu `Books.csv`, `Ratings.csv`, `Users.csv`.
- **Books.csv**

  ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/1bf780f9-f995-4f20-964a-590e60c27c83).     
     
     - ISBN: Kode unik yang diberikan untuk setiap buku yang memudahkan identifikasi dan standarisasi di seluruh dunia.
     - Book-Title: Nama resmi dari sebuah karya literatur.
     - Book-Author: Individu yang menciptakan konten buku.
     - Year-Of-Publication: Periode ketika buku tersebut pertama kali dirilis ke publik.
     - Publisher: Entitas yang mengatur proses penerbitan buku ke pasar.
     - Image-URL-S: Alamat web untuk gambar sampul buku yang berukuran kecil.
     - Image-URL-M: Alamat web untuk gambar sampul buku yang berukuran medium.
     - Image-URL-L: Alamat web untuk gambar sampul buku yang berukuran besar.

- **Ratings.csv**

  ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/6c63ab61-3c66-4019-a125-bd80669ea9bc).     
     
     - User-ID: Nomor yang diberikan secara khusus kepada setiap pengguna sebagai identifikasi yang membedakan satu pengguna dengan pengguna lainnya.
     - ISBN: Kode unik yang diberikan untuk setiap buku yang memudahkan identifikasi dan standarisasi di seluruh dunia.
     - Book-Rating: Skor yang diberikan oleh pengguna untuk menilai buku, biasanya mencerminkan kesukaan atau kualitas buku tersebut.

   Untuk mendapatkan gambaran statistik dari kolom `Book-Rating` dalam *dataframe* `Ratings`, kita akan menghitung dan menampilkan ukuran-ukuran statistik dasar. Ini termasuk menghitung rata-rata, standar deviasi, nilai minimum dan maksimum, serta nilai-nilai kuartil yang mencakup kuartil pertama, median, dan kuartil ketiga. Semua ini memberikan wawasan tentang distribusi nilai *rating* yang diberikan oleh pengguna pada buku.

   ```python
   rating['Book-Rating'].describe().apply(lambda x: '%.f' % x)
   ```

  ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/7c3e2946-153b-44cd-ac7e-25a33dbb275a)


  Ini merupakan grafik histogram yang menampilkan distribusi frekuensi dari penilaian yang diberikan oleh pengguna untuk buku-buku yang telah mereka baca, dengan skala penilaian yang berkisar antara 1 sampai 10.

  ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/2e9f4875-ba55-4798-a230-d798f5f79970)

  Dari grafik histogram "Jumlah Rating Buku" yang telah divisualisasikan, kita dapat melihat bahwa skor *rating* yang paling sering muncul adalah 0, dengan total sekitar 700.000 kali lebih. Karena *rating* 0 ini bisa menimbulkan bias dalam analisis data, ada baiknya kita mengeluarkan *rating* tersebut selama proses persiapan data untuk memastikan hasil analisis yang lebih akurat.

- **Users.csv**

  ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/7e2c2ba7-7f8f-4e59-8f0e-e4fe74073f3d)
     
     - User-ID: Nomor yang diberikan secara khusus kepada setiap pengguna sebagai identifikasi yang membedakan satu pengguna dengan pengguna lainnya.
     - Location: Tempat tinggal atau wilayah geografis di mana pengguna berada atau berasal.
     - Age: Tahun yang telah dilewati sejak kelahiran pengguna, biasanya digunakan untuk statistik demografis atau personalisasi konten.

   ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/9bdd0fab-da34-490c-bdc0-a20fac407bbb)

  Jika diperhatikan, max dari fitur `age` adalah 244, berarti ada pembaca buku yang berusia 244 tahun. Secara sekilas, ini tidak masuk akal, ada manusia modern yang berusia lebih dari 200 tahun. Untuk itu kita akan ekplorasi lebih jauh pada fitur `age` pada bagian *data preparation*.

## Data Preprocessing

Proses pra-pemrosesan data, atau *data preprocessing*, adalah langkah penting yang harus diambil sebelum memulai pemodelan. Langkah ini melibatkan transformasi data asli menjadi format yang lebih terstruktur dan bersih, yang kemudian dapat digunakan dalam analisis lebih lanjut. Untuk kasus ini, *data preprocessing* mencakup penyesuaian nama-nama kolom di setiap *dataframe*, menggabungkan informasi ISBN, serta mengintegrasikan *users* untuk mendapatkan gambaran lengkap tentang dataset.

1. **Penyesuaian Nama Kolom/Atribut**

   Menggunakan fungsi `.assign()` untuk mengubah nama kolom atau atribut dalam *dataframe* bertujuan agar proses referensi kolom atau atribut di langkah-langkah berikutnya menjadi lebih sederhana dan intuitif.

   - Books
   
   ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/af541c05-0fbc-444a-86f7-6758875bfd17)

   - Rating

   ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/9c72faae-32f4-4500-99aa-fcf8798c7d4e)

   - Users

   ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/82c55746-68ab-4091-a855-ccd3fa36e184)

    
2. **Menggabungkan Data Dengan Fitur ISBN**  
   Fungsi `.concatenate` dari *library* [`numpy`](https://numpy.org) digunakan untuk menggabungkan data ISBN yang terdapat di *dataframe* `df_b` untuk buku dan `df_r` untuk *rating*. Proses ini menyatukan informasi ISBN dari kedua *dataframe* ke dalam satu kolom `isbn`.
   
    ```python
       ISBNAll = np.unique(np.concatenate([books['isbn'].unique(), rating['isbn'].unique()]))
       print('Jumlah Buku berdasarkan ISBN :', len(ISBNAll))
    ```

3. **Menggabungkan Data *User***  
   Fungsi `.concatenate` dari *library* [`numpy`](https://numpy.org) digunakan untuk menyatukan data `user_id` yang berasal dari *dataframe* `rating` dan *dataframe* `users`. Proses ini menggabungkan kedua set data berdasarkan kolom `user_id`.
   
    ```python
      USERAll = np.unique(np.concatenate([rating['user_id'].unique(), users['user_id'].unique()]))
      print('Jumlah Buku berdasarkan ISBN :', len(USERAll))
    ```
   
## Data Preparation

Proses persiapan data, atau *data preparation*, adalah langkah krusial yang mendahului fase pembuatan model *machine learning*. Langkah ini melibatkan modifikasi data ke format yang sesuai untuk pemodelan. Dalam konteks ini, *data preparation* mencakup penanganan nilai yang hilang, verifikasi keberadaan data ganda, serta integrasi data dari *dataframe* *`books`* dan *`rating`* untuk memastikan data siap digunakan.

1. **Pengecekan Missing Value**

   Untuk mengetahui jumlah total nilai yang tidak ada atau *missing* dalam sebuah *dataframe*, kita dapat memanfaatkan metode `.isnull().sum()`. Metode ini akan menghitung dan memberikan jumlah keseluruhan nilai yang hilang di seluruh kolom *dataframe*.

   - Books

     ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/71694b91-4a14-4fbd-adab-ad1a92703e46)

     Dari informasi yang diberikan, terlihat bahwa dalam *dataframe* `books`, ada beberapa entri yang kosong. Khususnya, kolom `book_author` kosong satu entri, `publisher` kosong dua entri, dan `image_l_url` kosong tiga entri. Oleh karena itu, entri yang tidak memiliki data atau *null* bisa dieliminasi dengan memanfaatkan metode `.dropna()`. Setelah proses ini, pemeriksaan ulang akan menunjukkan bahwa tidak ada lagi entri yang kosong atau *null* dalam *dataframe*.
     ```python
     books = books.dropna()
     books.isnull().sum()
     ``` 

   - Rating

     ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/2183e891-136d-4628-9d0f-4a87ac0a2df5)

     Dari informasi yang diberikan, terlihat bahwa dalam *dataframe* `rating`, tidak ada entri yang kosong.

     Dari analisis eksploratif data univariat yang telah dilakukan, terungkap bahwa dalam histogram "Jumlah Rating Buku", mayoritas *rating* yang diberikan oleh pengguna adalah 0, dengan total mencapai lebih dari 700.000. Karena keberadaan *rating* 0 ini bisa mempengaruhi hasil analisis secara signifikan, menghapus data *rating* 0 dilakukan untuk mengurangi potensi bias.

     ```python
     rating = rating[rating.book_rating > 0]
     ```

     ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/391a523c-e500-4f31-8cbc-2a21b4eec7a2)

     Dari visualisasi histogram yang ditampilkan, dengan penghapusan *rating* 0, terlihat bahwa distribusi frekuensi menjadi lebih teratur dan mudah dipahami

   - Users

     Sebelum melakukan *missing value implementation*, ingat bahwa sebelumnya telah dibahas di bagian analisis eksploratif data univariat bahwa fitur `age` di dataframe users memiliki kejanggalan karena nilainya lebih dari 200 tahun.

     ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/93abfc2a-6abf-42d6-b3f1-d84ab7dfef40)

     Data-data tersebut akan dihilangkan dari *dataset*

     ```python
     users['age'] = pd.to_numeric(users['age'], errors='coerce')
     del_users = users[users['age'] > 120].index
     users.drop(del_users, inplace=True)
     ```

     Setelah itu, kita melihat *missing value* dari users

     ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/94ee9d20-b40e-47a3-9bf5-66668f0c0a18)

     Oleh karena itu, entri yang tidak terisi pada data `age` bisa diatasi dengan menggantinya menggunakan nilai yang paling banyak terjadi, atau modus, melalui penerapan fungsi `.fillna()` bersamaan dengan `.mode()`. Metode `.mode()` dipilih karena fitur `age` bernilai integer bilangan bulat, sehingga akan lebih cocok untuk mengisi *`NaN`* dengan data yang sering muncul pada fitur `age`.

     ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/5e374885-f0ae-458a-8a90-aa8b5eff9e56)

     Visualisasi histogram di atas menunjukan bahwa usia para *users* didominasi di rentang usia 20-an


2. **Data Duplicate**  
   Untuk memeriksa keberadaan data yang duplikat dalam *dataframe*, kita dapat menggunakan perintah `.duplicated().sum()` yang akan menghitung jumlah data yang duplikat.
   
   ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/e3dcd57a-b554-4f64-867a-6a9524af92c8)

   Hasil penelusuran menunjukan bahwa tidak ada data duplikasi pada *dataframe* proyek ini.
    

3. **Merger Books and Rating**  
   *Dataframe* `books` dan `rating` memiliki fitur yang sama, yaitu `isbn`. Sehingga akan baik dilakukan merger untuk mendapatkan kesamaan dan korelasi antar dua *dataframe*.
   
    ```python
      books_rating = pd.merge(rating, books, on=['isbn'])
    ```
    
## Modelling & Result

Langkah berikutnya dalam proyek ini adalah fase *modeling*, di mana kita akan mengembangkan model *machine learning* untuk sistem rekomendasi. Model ini akan menyarankan buku-buku yang paling sesuai untuk pengguna berdasarkan algoritma rekomendasi yang dipilih. Dari analisis data awal, kita mengetahui bahwa kita memiliki jumlah data yang sangat besar untuk buku, *rating*, dan pengguna, yang berkisar dari ratusan ribu hingga jutaan entri. Ukuran data ini dapat menyebabkan tantangan dalam hal biaya komputasi, seperti waktu pemrosesan yang lama dan kebutuhan akan RAM atau GPU dengan kapasitas besar.

Mengingat keterbatasan ini, kita akan membatasi dataset yang digunakan dalam pemodelan *machine learning* ini. Kita akan menggunakan hanya 20.000 entri teratas dari data buku dan 10.000 entri teratas dari data *rating*. Langkah ini akan membantu mengurangi beban komputasi sambil tetap memungkinkan kita untuk melatih model yang efektif dan memberikan rekomendasi yang berkualitas.

```python
   books   = books[:20000]
   rating = rating[:10000]
```

### 1. Content-based Recommendation

*Content-based recommendations* adalah sistem rekomendasi yang menggunakan detail dan atribut dari item yang ada, seperti buku, film, atau produk lainnya, untuk memberikan saran yang sesuai dengan preferensi pengguna. Sistem ini menganalisis kata kunci dan atribut yang ditetapkan pada item dalam database untuk menghasilkan prediksi yang mungkin berguna bagi pengguna.

Dalam sistem ini, profil pengguna dibuat berdasarkan item-item yang mereka sukai atau interaksi yang mereka lakukan. Misalnya, jika seseorang sering menonton film bergenre komedi, sistem akan merekomendasikan film lain dengan genre yang sama atau yang memiliki karakteristik serupa.

- **TF-IDF Vectorizer**  
   *Term Frequency Inverse Document Frequency Vectorizer*, atau TF-IDF Vectorizer, adalah sebuah metode untuk mengubah teks menjadi angka (vektor) yang dapat digunakan dalam pemrosesan data dan model *machine learning*. TF-IDF mengukur pentingnya sebuah kata dalam dokumen relatif terhadap kumpulan dokumen (korpus) [[5]](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html). 

   TF-IDF dihitung dengan formula berikut: 
$$idf_i = \log \left( \frac{n}{df_i} \right)$$
di mana $idf_i$ adalah nilai IDF untuk kata kunci $i$, $df_i$ adalah jumlah dokumen yang termasuk kata kunci $i$, dan $n$ adalah total jumlah dokumen. Nilai $df$ yang lebih tinggi untuk suatu kata kunci menghasilkan nilai $idf$ yang lebih rendah untuk kata kunci tersebut. Jika $df$ sama dengan $n$, yang berarti kata kunci muncul di setiap dokumen, maka $idf$ akan nol karena $\log(1) = 0$.

   Nilai TF-IDF sendiri adalah hasil kali dari frekuensi kata kunci dalam dokumen dengan nilai IDF-nya.
$$w_{i,j} = tf_{i,j} \times idf_i$$

  di mana $w_{i,j}$ adalah nilai TF-IDF untuk kata kunci $i$ di dokumen $j$, $tf_{i,j}$ adalah jumlah kemunculan kata kunci $i$ di dokumen $j$, dan $idf_i$ adalah nilai IDF untuk kata kunci $i$.

   Hasil penerapan TF-IDF Vectorizer
  
  ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/15803f3c-b352-4f97-8f7e-92e5d734767e)

   Kelebihan dan Kekurangan Penggunaan TF-IDF [[6]](https://www.capitalone.com/tech/machine-learning/understanding-tf-idf/)
  - Kelebihan Penggunaan TF-IDF

    Salah satu kelebihan terbesar dari TF-IDF adalah kemudahan dan kesederhanaannya dalam penggunaan. Perhitungannya mudah, tidak memerlukan banyak komputasi, dan menjadi titik awal yang baik untuk perhitungan kesamaan (melalui vektorisasi TF-IDF + Cosine Similarity).
    
  - Kekurangan Penggunaan TF-IDF

    Perlu diperhatikan bahwa TF-IDF tidak dapat menangkap makna semantik. Metode ini mempertimbangkan pentingnya kata berdasarkan bobotnya, namun tidak dapat menangkap konteks kata untuk memahami pentingnya dalam cara tersebut. Seperti yang telah disebutkan sebelumnya, TF-IDF mengabaikan urutan kata sehingga frasa seperti "Queen of England" tidak akan dianggap sebagai satu kesatuan. Hal ini juga berlaku pada situasi seperti negasi "not pay the bill" vs "pay the bill", di mana urutan kata sangat mempengaruhi makna. Dalam kedua kasus tersebut, penggunaan alat NER dan garis bawah, seperti "queen_of_england" atau "not_pay", dapat menjadi cara untuk menganggap frasa tersebut sebagai satu kesatuan.
    Kekurangan lainnya adalah TF-IDF dapat tidak efisien dalam penggunaan memori karena dapat mengalami masalah dimensi yang tinggi. Panjang vektor TF-IDF sama dengan ukuran kosakata. Dalam beberapa konteks klasifikasi ini mungkin tidak menjadi masalah, tetapi dalam konteks lain seperti pengelompokan, hal ini dapat menjadi tidak praktis seiring bertambahnya jumlah dokumen. 

- **Cosine Similarity**

     *Cosine Similarity* adalah metrik matematika yang digunakan untuk mengukur kesamaan antara dua vektor dalam ruang multidimensi. Ini didefinisikan sebagai kosinus sudut antara vektor, yang merupakan hasil perkalian titik dari vektor dibagi dengan hasil kali panjang mereka. Metrik ini sangat berguna dalam analisis teks dan sistem rekomendasi, di mana teks diubah menjadi vektor kata dan kesamaan semantik antara dokumen dapat diukur berdasarkan arah vektor tersebut, bukan hanya berdasarkan magnitudo atau ukuran mereka. Cosine Similarity selalu berada dalam interval -1 hingga 1, di mana -1 berarti persis berlawanan, 0 menunjukkan ortogonal atau tidak berkorelasi, dan 1 berarti persis sama. Untuk menentukan seberapa mirip satu judul buku dengan yang lain, kita bisa menggunakan teknik *cosine similarity*. Fungsi `cosine_similarity` dari *library* `sklearn` memungkinkan kita untuk melakukan perhitungan ini [[7]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html).

  ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/020973bc-9602-4cc3-83b3-215817c8d9a5)

  Di mana $A_i$ dan $B_i$ merupakan komponen dari masing-masing vektor A dan B.

  Hasil penerapan Cosine Similarity.

  ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/d80fe713-ac6d-47c5-8730-83cf84d8c1a3)

  Kelebihan dan Kekurangan Penggunaan Cosine Similarity [[8]](https://www.geeksforgeeks.org/cosine-similarity/)
  - Kelebihan Penggunaan Cosine Similarity
       
       * Efektif dalam mengukur kesamaan antara dua objek, tidak terpengaruh oleh ukuran.
       * Cocok untuk data dengan banyak fitur yang jarang terisi.
       * Sering digunakan dalam analisis teks dan sistem rekomendasi karena invarian skala.
         
  - Kekurangan Penggunaan Cosine Similarity
 
       * Kurang optimal dalam ruang dimensi rendah.
       * Tidak menangkap makna semantik atau konteks kata.
       * Mengabaikan urutan kata, yang bisa penting dalam pemahaman makna.
       * Bisa tidak efisien memori dan menderita dari kutukan dimensionalitas, terutama dalam pengelompokan dokumen besar.

**Recommendation Testing**

Hasil pengujian sistem rekomendasi dengan pendekatan *Content-based Recommendation* adalah sebagai berikut.

![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/60470a17-5d4d-4619-87b3-83e9c3dd38cd)

Di atas adalah gambar sample buku yang akan dijadikan patokan rekomendasi. Rekomendasi yang diberikan dengan pendekatan **Content-based Recommendation** sebagai berikut

![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/d89a23ad-b57a-4e9d-aeb0-3967975f8635)

Terlihat bahwa sistem yang dikembangkan mampu memberikan saran beberapa buku berdasarkan masukan judul buku "*Room for a Single Lady*", dengan hasil yang didasarkan pada analisis algoritma sistem. Terlihat bahwa rekomendasi yang dihasilkan merujuk ke penulisa buku yang ada nama Clare, dan menghasilkan satu rekomendasi dengan penulis buku yang sama dengan buku yang telah di baca, yaitu *11 Edward Street* oleh Clare Boylan.

### 2. Collaborative Filtering Recommendation
*Collaborative Filtering Recommendation* adalah teknik yang digunakan dalam sistem rekomendasi untuk memprediksi preferensi atau minat pengguna berdasarkan preferensi atau minat pengguna lain yang serupa. Teknik ini tidak mengandalkan konten item yang direkomendasikan, melainkan pada pola interaksi dan penilaian yang dilakukan oleh pengguna terhadap item-item tersebut [[9]](https://realpython.com/build-recommendation-engine-collaborative-filtering/#what-is-collaborative-filtering ).

![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/f940430f-d326-4202-bcc5-841705218bee)

- **Data Preparation**

Dalam *data preparation*, fitur `user_id` dan `isbn` di *dataframe* `ratings` dikonversi menjadi indeks bilangan bulat. Setelah itu, fitur-fitur yang sudah dikonversi ini dipetakan kembali ke dalam *dataframe* `rating` masing-masing.

![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/bf5424ce-eaac-4009-bc8b-ed1d0c0bc350)

- **Training Data and Validation Data Split**

Kemudian kita melakukan pembagian *dataset* dengan rasio 80:20, yaitu 80% untuk data latih (*training data*) dan 20% untuk data uji (*validation data*).

![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/7a223708-52ef-45f8-b046-f072ac2059b9)

- **Model Development and Testing**

Hasil pengujian sistem rekomendasi dengan pendekatan *Collaborative Filtering Recommendation* adalah sebagai berikut.

![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/8e2c4a59-d4ed-4359-b2f9-65e4a89ca594)

Dari informasi yang diberikan, tampaknya sistem telah memilih secara acak seorang pengguna dengan `user_id` **695**. Sistem kemudian mencari buku-buku yang paling disukai oleh pengguna tersebut, yang meliputi:
*   **Elements of Programming With Perl** karya **Andrew L. Johnson**
*   **To Catch a Cat** karya **Marian Babson**
*   **People of the Wolf (The First North Americans series, Book 1)** karya **W. Michael Gear**
*   **The Door to December** karya **Dean R. Koontz**

Setelah itu, sistem akan membandingkan buku-buku dengan penilaian tertinggi dari pengguna ini dengan seluruh katalog buku, kecuali yang sudah dibaca, dan mengurutkan rekomendasi berdasarkan skor tertinggi. Terlihat ada 10 buku yang direkomendasikan oleh sistem. Rekomendasi yang diberikan benar-benar tidak ada kesamaan penulis buku dari buku yang sudah dibaca. Ini menunjukan bahwa rekomendasi dibentuk dari hasil kesamaan para `users` lainnya.

## Evaluation

1. **Content-based Recommendation**  
   Pada tahap evaluasi untuk model sistem rekomendasi dengan pendekatan berbasis konten (content-based recommendation), metrik akurasi dapat dihitung dengan membagi jumlah buku yang direkomendasikan dengan jumlah buku yang ditulis oleh penulis yang sama, kemudian dikalikan dengan 100.

   $$Accuracy=\frac{\displaystyle\sum_{i=1}^{n} RecommendedBooks_i}{\displaystyle\sum_{i=1}^{n} BooksWithSameAuthor_i} \times 100$$

   ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/747ecd8a-8cf6-4845-ac74-32c09b20817b)

   Menggunakan data pada tahap pemodelan sebelumnya, dengan penulis Clare Boylan, ditemukan bahwa ia menulis 2 buku. Jumlah rekomendasi buku yang dihasilkan, yaitu 1, lalu dibagi dengan 2, lalu dikalikan 100, menghasilkan akurasi 50,00%.

2. **Collaborative Filtering Recommendation**  
   Berdasarkan model machine learning yang dibangun menggunakan *embedding layer, Adam optimizer,* dan *binary crossentropy loss function,* metrik yang digunakan adalah *Root Mean Squared Error* (RMSE). RMSE dihitung dengan mengambil akar kuadrat dari jumlah kuadrat selisih antara nilai sebenarnya dan nilai prediksi, dibagi dengan jumlah data. Nilai RMSE yang rendah menunjukkan bahwa nilai prediksi mendekati nilai observasi. 

   $$RMSE=\sqrt{\sum^{n}_{i=1} \frac{y_i - y\\_pred_i}{n}}$$

   Di mana, nilai $n$ merupakan jumlah *dataset*, nilai $y_i$ adalah nilai sebenarnya, dan $y\\_pred$ yaitu nilai prediksinya terdahap $i$ sebagai urutan data dalam *dataset*.

   Visualisasi hasil pelatihan dan validasi dari metrik RMSE serta training dan validation loss ditampilkan dalam bentuk grafik plot.

   ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/f3b1e5df-4f56-476c-b9bc-7dbfdc052425)

## Kesimpulan

Ringkasannya, model rekomendasi buku yang telah dikembangkan berhasil memenuhi kebutuhan pengguna dengan menggabungkan dua pendekatan: *Content-based Recommendation* dan *Collaborative Filtering Recommendation*. Dalam *Collaborative Filtering Recommendation*, penting untuk memiliki data peringkat dari pengguna untuk memahami dan memprediksi preferensi mereka. Sebaliknya, *Content-based Recommendation* tidak bergantung pada peringkat pengguna, tetapi lebih fokus pada analisis fitur-fitur spesifik dari buku itu sendiri.

Dengan memanfaatkan kedua teknik ini, model dapat memberikan saran yang sangat relevan dan personal, karena tidak hanya mempertimbangkan apa yang telah dinikmati oleh pengguna di masa lalu, tetapi juga menemukan pilihan baru yang serupa dengan minat mereka berdasarkan karakteristik buku. Ini menciptakan pengalaman yang kaya dan bervariasi, memungkinkan pengguna untuk menemukan karya-karya baru yang mungkin belum pernah mereka pertimbangkan sebelumnya, sambil tetap sejalan dengan selera pribadi mereka.

---
---

## Referensi

[1] Moon, S. J., & Bai, S. Y. (2020). "Components of digital literacy as predictors of youth civic engagement and the role of social media news attention: the case of Korea." *Journal of Children and Media,* 1–17. doi:10.1080/17482798.2020.1728700 

[2] Tejedor, S., Cervi, L., Pérez-Escoda, A., & Jumbo, F. T. (2020). "Digital Literacy and Higher Education during COVID-19 Lockdown: Spain, Italy, and Ecuador." *Publications,* 8(4), 48. doi:10.3390/publications8040048 

[3] Nikou, S., Aavakare, M. (2021). "An assessment of the interplay between literacy and digital Technology in Higher Education." *Educ Inf Technol 26,* 3893–3915. https://doi.org/10.1007/s10639-021-10451-0 

[4] Dogan, O., Tokumaci, S., Hiziroglu, O.A. (2024). "Web-Based Intelligent Book Recommendation System Under Smart Campus Applications." *In: Şen, Z., Uygun, Ö., Erden, C. (eds) Advances in Intelligent Manufacturing and Service System Informatics.* IMSS 2023. Lecture Notes in Mechanical Engineering. Springer, Singapore. https://doi.org/10.1007/978-981-99-6062-0_6

[5] org,  scikit-learn. "Sklearn.feature_extraction.text.TfidfVectorizer". scikit. https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

[6] capitalone. (2021, October 6). "Understanding TF-IDF for Machine Learning." Capital One. https://www.capitalone.com/tech/machine-learning/understanding-tf-idf/ 

[7] org,  scikit-learn. "Sklearn.metrics.pairwise.cosine_similarity". scikit. https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

[8] GfG. (2023, July 15). "Cosine similarity." GeeksforGeeks. https://www.geeksforgeeks.org/cosine-similarity/ 

[9] Real Python. (2022, August 18). "Build a recommendation engine with collaborative filtering." https://realpython.com/build-recommendation-engine-collaborative-filtering/#what-is-collaborative-filtering 
