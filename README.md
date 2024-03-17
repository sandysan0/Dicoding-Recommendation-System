# Laporan Proyek *Machine Learning* - Sandy Susanto

## 1. *Project Overview*

Proyek ini membahas literasi digital dan kebutuhan teknologi literatur untuk mendukung akses informasi dalam literasi. 

![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/11936652-62e8-4c2a-8a60-d8618e4f1af4)
Gambar 1.1 Buku

Dalam konteks pendidikan dan kehidupan sehari-hari, literasi secara tradisional diakui sebagai kemampuan dasar membaca dan menulis yang menjadi fondasi pengetahuan masyarakat. Namun, di tengah perubahan zaman yang ditandai dengan digitalisasi, konsep literasi telah mengalami evolusi yang signifikan. Kini, literasi tidak hanya terbatas pada kemampuan literasi konvensional, melainkan juga mencakup keterampilan digital yang meliputi kolaborasi, komunikasi, kewarganegaraan digital, pemecahan masalah, berpikir kritis, dan kreativitas. Keterampilan-keterampilan ini dianggap vital dalam literatur terkini dan menjadi kompetensi esensial bagi tenaga kerja di era digital. Pengajaran keterampilan abad ke-21 ini kepada generasi muda menjadi penting, mengingat tidak semua individu secara otomatis mahir dalam menggunakan teknologi informasi dan komunikasi secara efektif meskipun mereka tumbuh di era digital [[3]](https://link.springer.com/article/10.1007/s10639-021-10451-0#Sec2). 

Peran media baru, khususnya Internet dan media sosial, dalam meningkatkan keterlibatan masyarakat dan pengaruhnya terhadap pemuda, telah menjadi fokus diskusi yang penting. Peningkatan penggunaan media sosial oleh remaja yang sering menggunakan perangkat mobile menunjukkan dampak yang signifikan terhadap prospek demokrasi di masa depan. Studi terkait menunjukkan adanya korelasi positif antara penggunaan media sosial dan tingkat partisipasi, di mana media sosial berperan dalam memfasilitasi keterlibatan melalui jaringan komunikasi dua arah. Penelitian ini mengeksplorasi berbagai dimensi literasi digital sebagai evolusi dari literasi media tradisional, yang dianggap sebagai kerangka kerja yang lebih relevan untuk penelitian tentang pemuda, khususnya dalam konteks pendidikan literasi yang ada di kelas [[1]](https://www.tandfonline.com/doi/full/10.1080/17482798.2020.1728700).

Literasi digital, yang pada awalnya hanya dianjurkan, kini telah menjadi komponen kunci dalam membentuk warga negara yang adaptif di era digital. Meskipun demikian, definisi dan ruang lingkup literasi digital belum distandarisasi dan terus berkembang seiring dengan kemajuan ilmu pengetahuan. Literasi digital kini diinterpretasikan sebagai serangkaian keterampilan yang saling terkait dan diperlukan untuk sukses di dunia digital, dengan penekanan khusus pada pentingnya pendekatan kritis yang berkembang melalui studi literasi media. [[2]](https://www.mdpi.com/2304-6775/8/4/48).

Pentingnya sistem rekomendasi buku digital terletak pada kemampuannya untuk memfasilitasi penemuan literatur baru dan sumber daya yang relevan, yang secara signifikan meningkatkan keterlibatan dan kepuasan pengguna. Hal ini berkontribusi pada peningkatan pengalaman pembelajaran secara keseluruhan. Lebih lanjut, sistem ini berperan dalam mengatasi penurunan minat baca, khususnya di kalangan generasi muda, dengan menyajikan rekomendasi yang tepat melalui perpustakaan, institusi pendidikan, dan *platform e-learning.* Di tengah berkembangnya ekonomi yang berbasis pengetahuan, literasi digital harus didefinisikan ulang sebagai kumpulan keterampilan dan kompetensi yang saling berkaitan, yang menjadi syarat esensial untuk mencapai kesuksesan di era digital saat ini. [[4]](https://link.springer.com/chapter/10.1007/978-981-99-6062-0_6#rightslink).

## 2. *Business Understanding*

### 2.1 *Problem Statements*

Dalam konteks sistem rekomendasi buku digital, masalah utama yang sering dihadapi adalah bagaimana cara mengidentifikasi dan merekomendasikan buku yang paling relevan dan menarik bagi pengguna individu. Dengan jumlah buku yang terus bertambah, tantangan ini menjadi semakin kompleks karena harus mempertimbangkan preferensi yang sangat personal dan dinamis dari setiap pengguna. Dari konteks yang telah disampaikan sebelumnya, teridentifikasi dua pertanyaan utama yang akan dijawab melalui proyek ini:
1. Bagaimana proses pembuatan model *machine learning* yang dapat merekomendasikan buku?
2. Apa langkah-langkah yang diperlukan dalam mempersiapkan data sebelum diaplikasikan dalam pengembangan model *machine learning*?

### 2.2 *Goals*

Dari permasalahan yang telah diuraikan, tujuan yang ingin dicapai melalui proyek ini adalah sebagai berikut:
1. Menjalankan proses persiapan data secara menyeluruh untuk memastikan data siap digunakan dalam model *machine learning*.
2. Mengembangkan model *machine learning* yang efektif untuk dijadikan sistem rekomendasi buku yang relevan dan realibitas.

### 2.3 *Solution Statements*

Dari uraian sebelumnya, beberapa langkah strategis telah diidentifikasi untuk mencapai target proyek, antara lain:
1. Proses pra-pemrosesan yang meliputi:
   - Menyesuaikan dan merenamakan kolom atau atribut untuk mempermudah proses pengambilan dataset dan atribut tertentu.
   - Mengkonsolidasikan data yang terpisah untuk mempersiapkannya untuk penggunaan di tahapan berikutnya.
2. Proses persiapan data akan meliputi:
   - Memeriksa kelogisan data yang terdapat dalam *dataset* dan menghilangkan nilai-nilai yang tidak masuk akal.
   - Memeriksa keberadaan nilai-nilai yang hilang atau *null* dalam *dataset* dan mengambil tindakan untuk mengeliminasi atau menggantinya dengan nilai yang sesuai.
   - Memastikan tidak ada entri data yang berulang untuk menjaga integritas model dan sistem yang dikembangkan.
3. Dalam fase pembuatan model *machine learning*, dua pendekatan yang berbeda akan diuji.
   - *Content-Based Recommendation*: Pendekatan ini akan menggunakan karakteristik buku seperti genre, penulis, dan deskripsi untuk merekomendasikan buku baru yang serupa dengan yang telah dibaca atau disukai oleh pengguna. Ini memungkinkan personalisasi yang kuat karena rekomendasi didasarkan pada preferensi pengguna yang spesifik.
   - *Collaborative Filtering Recommendation*: Pendekatan ini akan menganalisis pola dan preferensi membaca dari banyak pengguna untuk mengidentifikasi kesamaan antara pengguna dan merekomendasikan buku berdasarkan buku yang disukai oleh pengguna dengan preferensi serupa. Ini memanfaatkan ‘kecerdasan kolektif’ dari basis pengguna untuk memberikan rekomendasi yang lebih luas dan beragam.
   
## 3. *Data Understanding*

![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/9a75d57c-19d7-47de-8652-e4a62edc1ce0)
Gambar 3.1 *Dataset* proyek

*Dataset* yang digunakan adalah [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data) dalam bentuk `.csv` ([Comma-separated Values](https://en.wikipedia.org/wiki/Comma-separated_values)). Dalam *dataset* tersebut berisi tiga (3) berkas CSV, yaitu *`Books.csv`*, *`Ratings.csv`*, *`Users.csv`*.
- ***Books.csv***

  | No | Kolom | Jumlah Data Yang Tidak Kosong | Tipe data |
  |---|---|---|---|
  | 1 | *`ISBN`* | 271360 | *object* |
  | 2 | *`Book-Title`* | 271360 | *object* |
  | 3 | *`Book-Author`* | 271359 | *object* |
  | 4 | *`Year-Of-Publication`* | 271360 | *object* |
  | 5 | *`Publisher`* | 271358 | *object* |
  | 6 | *`Image-URL-S`* | 271360 | *object* |
  | 7 | *`Image-URL-M`* | 271360 | *object* |
  | 8 | *`Image-URL-L`* | 271357 | *object* |

  Tabel 3.1 Atribut *Books.csv*
   
     - *`ISBN`*: Kode unik yang diberikan untuk setiap buku yang memudahkan identifikasi dan standarisasi di seluruh dunia.
     - *`Book-Title`*: Nama resmi dari sebuah karya literatur.
     - *`Book-Author`*: Individu yang menciptakan konten buku.
     - *`Year-Of-Publication`*: Periode ketika buku tersebut pertama kali dirilis ke publik.
     - *`Publisher`*: Entitas yang mengatur proses penerbitan buku ke pasar.
     - *`Image-URL-S`*: Alamat web untuk gambar sampul buku yang berukuran kecil.
     - *`Image-URL-M`*: Alamat web untuk gambar sampul buku yang berukuran medium.
     - *`Image-URL-L`*: Alamat web untuk gambar sampul buku yang berukuran besar.

- ***Ratings.csv***

  | No | Kolom | Jumlah Data Yang Tidak Kosong | Tipe data |
  |---|---|---|---|
  | 1 | *`User-ID`* | 1149780 | *int64* |
  | 2 | *`ISBN`* | 1149780 | *object* |
  | 3 | *`Book-Rating`* | 1149780 | *int64* |

  Tabel 3.2 Atribut *Ratings.csv*
     
     - *`User-ID`*: Nomor yang diberikan secara khusus kepada setiap pengguna sebagai identifikasi yang membedakan satu pengguna dengan pengguna lainnya.
     - *`ISBN`*: Kode unik yang diberikan untuk setiap buku yang memudahkan identifikasi dan standarisasi di seluruh dunia.
     - *`Book-Rating`*: Skor yang diberikan oleh pengguna untuk menilai buku, biasanya mencerminkan kesukaan atau kualitas buku tersebut.

   Untuk mendapatkan gambaran statistik dari kolom `Book-Rating` dalam *dataframe* `Ratings`, kita akan menghitung dan menampilkan ukuran-ukuran statistik dasar. Ini termasuk menghitung rata-rata, standar deviasi, nilai minimum dan maksimum, serta nilai-nilai kuartil yang mencakup kuartil pertama, median, dan kuartil ketiga. Semua ini memberikan wawasan tentang distribusi nilai *rating* yang diberikan oleh pengguna pada buku.

  | Nilai | Total | 
  |---|---|
  | Jumlah data | 1149780 |
  | Rata-rata | 3 |
  | Standar Deviasi | 4 |
  | Minimal | 0 |
  | Kuartil 1 | 0 |
  | Kuartil 2 | 0 |
  | Kuartil 3 | 7 |
  | Maksimal | 10 |

  Tabel 3.3 Informasi statistik *Ratings.csv*

  Ini merupakan grafik histogram yang menampilkan distribusi frekuensi dari penilaian yang diberikan oleh pengguna untuk buku-buku yang telah mereka baca, dengan skala penilaian yang berkisar antara 1 sampai 10.

  ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/2e9f4875-ba55-4798-a230-d798f5f79970)
  Gambar 3.2 Histogram distribusi *rating*

  Dari grafik histogram "Jumlah Rating Buku" yang telah divisualisasikan, kita dapat melihat bahwa skor *rating* yang paling sering muncul adalah 0, dengan total sekitar 700.000 kali lebih. Karena *rating* 0 ini bisa menimbulkan bias dalam analisis data, ada baiknya kita mengeluarkan *rating* tersebut selama proses persiapan data untuk memastikan hasil analisis yang lebih akurat.

- ***Users.csv***

  | No | Kolom | Jumlah Data Yang Tidak Kosong | Tipe data |
  |---|---|---|---|
  | 1 | *`User-ID`* | 278858 | *int64* |
  | 2 | *`Location`* | 278858 | *object* |
  | 3 | *`Age`* | 168096 | *float64* |

  Tabel 3.4 Atribut *Users.csv*
     
     - *`User-ID`*: Nomor yang diberikan secara khusus kepada setiap pengguna sebagai identifikasi yang membedakan satu pengguna dengan pengguna lainnya.
     - *`Location`*: Tempat tinggal atau wilayah geografis di mana pengguna berada atau berasal.
     - *`Age`*: Tahun yang telah dilewati sejak kelahiran pengguna, biasanya digunakan untuk statistik demografis atau personalisasi konten.

  | Nilai | *`User-ID`* | *`Age`* |
  |---|---|---|
  | Jumlah data | 278858.00000 | 168096.000000 |
  | Rata-rata | 139429.50000 | 34.751434 |
  | Standar Deviasi | 80499.51502 | 14.428097 |
  | Minimal | 1.00000 | 0.000000 |
  | Kuartil 1 | 69715.25000 | 24.000000 |
  | Kuartil 2 | 139429.50000 | 32.000000 |
  | Kuartil 3 | 209143.75000 | 44.000000 |
  | Maksimal | 278858.00000 | 244.000000 |

  Tabel 3.5 Informasi statistik *Users.csv*

  Jika diperhatikan, nilai maksimal dari fitur *`Age`*  adalah 244, berarti ada pembaca buku yang berusia 244 tahun. Secara sekilas, ini tidak masuk akal, ada manusia modern yang berusia lebih dari 200 tahun. Untuk itu kita akan ekplorasi lebih jauh pada fitur *`Age`*  pada bagian *data preparation*.

## 4. *Data Preprocessing*

Proses pra-pemrosesan data, atau *data preprocessing*, adalah langkah penting yang harus diambil sebelum memulai pemodelan. Langkah ini melibatkan transformasi data asli menjadi format yang lebih terstruktur dan bersih, yang kemudian dapat digunakan dalam analisis lebih lanjut. Untuk kasus ini, *data preprocessing* mencakup penyesuaian nama-nama kolom di setiap *dataframe*, menggabungkan informasi ISBN, serta mengintegrasikan *users* untuk mendapatkan gambaran lengkap tentang *dataset*.

   4.1. **Penyesuaian Nama Kolom/Atribut**

   Menggunakan fungsi *`.assign()`* untuk mengubah nama kolom atau atribut dalam *dataframe* bertujuan agar proses referensi kolom atau atribut di langkah-langkah berikutnya menjadi lebih sederhana dan intuitif.
   
   4.2. **Menggabungkan Data Dengan Fitur ISBN**  
   
   Fungsi `.concatenate` dari *library* [*`numpy`*](https://numpy.org) digunakan untuk menggabungkan data ISBN yang terdapat di *dataframe* *`books`* untuk buku dan *`rating`* untuk *rating*. Proses ini menyatukan informasi ISBN dari kedua *dataframe* ke dalam satu kolom `isbn`.
   
   4.3. **Menggabungkan Data *User***  
   
   Fungsi *`.concatenate`* dari *library* [*`numpy`*](https://numpy.org) digunakan untuk menyatukan data *`user_id`* yang berasal dari *dataframe* *`rating`* dan *dataframe* *`users`*. Proses ini menggabungkan kedua set data berdasarkan kolom *`user_id`*.
   
## 5. *Data Preparation*

Proses persiapan data, atau *data preparation*, adalah langkah krusial yang mendahului fase pembuatan model *machine learning*. Langkah ini melibatkan modifikasi data ke format yang sesuai untuk pemodelan. Dalam konteks ini, *data preparation* mencakup penanganan nilai yang hilang, verifikasi keberadaan data ganda, serta integrasi data dari *dataframe* *`books`* dan *`rating`* untuk memastikan data siap digunakan.
   
   5.1. **Pengecekan *Missing Value***

   Untuk mengetahui jumlah total nilai yang tidak ada atau *missing* dalam sebuah *dataframe*, kita dapat memanfaatkan metode *`.isnull().sum()`*. Metode ini akan menghitung dan memberikan jumlah keseluruhan nilai yang hilang di seluruh kolom *dataframe*.

   - *Books*

     | Kolom | Jumlah Data Kosong |
     |---|---|
     | *`isbn`* | 0 |
     | *`book_title`* | 0 |
     | *`book-author`* | 1 |
     | *`pub_year`* | 0 |
     | *`publisher`* | 2 |
     | *`image_s_url`* | 0 |
     | *`image_m_url`* | 0 |
     | *`image_l_url`* | 3 |

     Tabel 5.1.1 *Missing Values* pada *dataframe books*

     Dari informasi yang diberikan, terlihat bahwa dalam *dataframe* *`books`*, ada beberapa entri yang kosong. Khususnya, kolom *`book_author`* kosong satu entri, *`publisher`* kosong dua entri, dan *`image_l_url`* kosong tiga entri. Oleh karena itu, entri yang tidak memiliki data atau *null* bisa dieliminasi dengan memanfaatkan metode *`.dropna()`*. Setelah proses ini, pemeriksaan ulang akan menunjukkan bahwa tidak ada lagi entri yang kosong atau *null* dalam *dataframe*.

   - *Rating*

     | Kolom | Jumlah Data Kosong |
     |---|---|
     | *`user_id `* | 0 |
     | *`isbn`* | 0 |
     | *`book_rating`* | 0 |

     Tabel 5.1.2 *Missing Values* pada *dataframe rating*

     Dari informasi yang diberikan Tabel 5.1.2, terlihat bahwa dalam *dataframe `rating`*, tidak ada entri yang kosong.

     Dari analisis eksploratif data univariat yang telah dilakukan, terungkap bahwa dalam histogram "Jumlah Rating Buku", mayoritas *rating* yang diberikan oleh pengguna adalah 0, dengan total mencapai lebih dari 700.000. Karena keberadaan *rating* 0 ini bisa mempengaruhi hasil analisis secara signifikan, menghapus data *rating* 0 dilakukan untuk mengurangi potensi bias.

     ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/391a523c-e500-4f31-8cbc-2a21b4eec7a2)

     Gambar 5.1.1 Histogram distribusi *rating* setelah menghilangkan *rating* 0

     Dari visualisasi histogram yang ditampilkan pada Gambar 5.1.1, dengan penghapusan *rating* 0, terlihat bahwa distribusi frekuensi menjadi lebih teratur dan mudah dipahami

   - *Users*

     Sebelum melakukan *missing value implementation*, ingat bahwa sebelumnya telah dibahas di bagian analisis eksploratif data univariat bahwa fitur `age` di dataframe users memiliki kejanggalan karena nilainya lebih dari 200 tahun. Data-data tersebut akan dihilangkan dari *dataset*. Setelah itu, kita melihat *missing value* dari users

     | Kolom | Jumlah Data Kosong |
     |---|---|
     | *`user_id `* | 0 |
     | *`location`* | 0 |
     | *`age`* | 110762 |

     Tabel 5.1.3 *Missing Values* pada *dataframe users*

     Dengan melihat Tabel 5.1.3, entri yang tidak terisi pada data *`age`* bisa diatasi dengan menggantinya menggunakan nilai yang paling banyak terjadi, atau modus, melalui penerapan fungsi *`.fillna()`* bersamaan dengan *`.mode()`*. Metode *`.mode()`* dipilih karena fitur *`age`* bernilai integer bilangan bulat, sehingga akan lebih cocok untuk mengisi *`NaN`* dengan data yang sering muncul pada fitur *`age`*.

     ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/5e374885-f0ae-458a-8a90-aa8b5eff9e56)

     Gambar 5.1.2 Histogram distribusi *users* setelah mengisi *`age`* yang bernilai 0

     Visualisasi histogram pada Gambar 5.1.2 di atas menunjukan bahwa usia para *users* didominasi di rentang usia 20-an


   5.2. ***Data Duplicate***  
   Untuk memeriksa keberadaan data yang duplikat dalam *dataframe*, kita dapat menggunakan perintah *`.duplicated().sum()`* yang akan menghitung jumlah data yang duplikat. Hasil penelusuran menunjukan bahwa tidak ada data duplikasi pada *dataframe* proyek ini.
    

   5.3. ***Merger Books and Rating***  
   *Dataframe `books`* dan *`rating`* memiliki fitur yang sama, yaitu `isbn`. Sehingga akan baik dilakukan *merger* untuk mendapatkan kesamaan dan korelasi antar dua *dataframe*.
    
## 6. *Modelling & Result*

Langkah berikutnya dalam proyek ini adalah fase *modeling*, di mana kita akan mengembangkan model *machine learning* untuk sistem rekomendasi. Model ini akan menyarankan buku-buku yang paling sesuai untuk pengguna berdasarkan algoritma rekomendasi yang dipilih. Dari analisis data awal, kita mengetahui bahwa kita memiliki jumlah data yang sangat besar untuk buku, *rating*, dan pengguna, yang berkisar dari ratusan ribu hingga jutaan entri. Ukuran data ini dapat menyebabkan tantangan dalam hal biaya komputasi, seperti waktu pemrosesan yang lama dan kebutuhan akan *RAM* atau *GPU* dengan kapasitas besar.

Mengingat keterbatasan ini, kita akan membatasi dataset yang digunakan dalam pemodelan *machine learning* ini. Kita akan menggunakan hanya 20.000 entri teratas dari data buku dan 10.000 entri teratas dari data *rating*. Langkah ini akan membantu mengurangi beban komputasi sambil tetap memungkinkan kita untuk melatih model yang efektif dan memberikan rekomendasi yang berkualitas.

### 6.1. *Content-based Recommendation*

*Content-based recommendations* adalah sistem rekomendasi yang menggunakan detail dan atribut dari item yang ada, seperti buku, film, atau produk lainnya, untuk memberikan saran yang sesuai dengan preferensi pengguna. Sistem ini menganalisis kata kunci dan atribut yang ditetapkan pada item dalam database untuk menghasilkan prediksi yang mungkin berguna bagi pengguna.

Dalam sistem ini, profil pengguna dibuat berdasarkan item-item yang mereka sukai atau interaksi yang mereka lakukan. Misalnya, jika seseorang sering menonton film bergenre komedi, sistem akan merekomendasikan film lain dengan genre yang sama atau yang memiliki karakteristik serupa.

- ***TF-IDF Vectorizer***  
   *Term Frequency Inverse Document Frequency Vectorizer*, atau *TF-IDF Vectorizer*, adalah sebuah metode untuk mengubah teks menjadi angka (vektor) yang dapat digunakan dalam pemrosesan data dan model *machine learning*. *TF-IDF* mengukur pentingnya sebuah kata dalam dokumen relatif terhadap kumpulan dokumen (korpus) [[5]](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html). 

   *TF-IDF* dihitung dengan formula berikut: 
$$idf_i = \log \left( \frac{n}{df_i} \right)$$
di mana $idf_i$ adalah nilai IDF untuk kata kunci $i$, $df_i$ adalah jumlah dokumen yang termasuk kata kunci $i$, dan $n$ adalah total jumlah dokumen. Nilai $df$ yang lebih tinggi untuk suatu kata kunci menghasilkan nilai $idf$ yang lebih rendah untuk kata kunci tersebut. Jika $df$ sama dengan $n$, yang berarti kata kunci muncul di setiap dokumen, maka $idf$ akan nol karena $\log(1) = 0$.

   Nilai *TF-IDF* sendiri adalah hasil kali dari frekuensi kata kunci dalam dokumen dengan nilai *IDF*-nya.
$$w_{i,j} = tf_{i,j} \times idf_i$$

  di mana $w_{i,j}$ adalah nilai TF-IDF untuk kata kunci $i$ di dokumen $j$, $tf_{i,j}$ adalah jumlah kemunculan kata kunci $i$ di dokumen $j$, dan $idf_i$ adalah nilai IDF untuk kata kunci $i$.
  
  | *book_title* | *narayan* | *kuswa* | *haas* | *estoril* | *las* | *hã* | *iain* | *ernaux* | *eade* | *gourevitch* | *shear* | *ladd* | *kemp* | *romain* | *heredia* | *troon* | *foucault* | *angley* | *kersh* | *alther* |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | *Women and Self-Esteem* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *Antonio S and the Mystery of Theodore Guzman (Little Ark Book)* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *Firebrand* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *Trauma Junkie: Memoirs of an Emergency Flight Nurse* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *Shipping News* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *The Girls' Guide to Hunting and Fishing* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *Making the Most of Your Money* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *It's Not About the Bike: My Journey Back to Life* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *Call back our yesterdays* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *Myrtle of Willendorf* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |


  Tabel 6.1.1 Hasil penerapan *TF-IDF Vectorizer*

   **Kelebihan dan Kekurangan Penggunaan *TF-IDF*** [[6]](https://www.capitalone.com/tech/machine-learning/understanding-tf-idf/)
  - Kelebihan Penggunaan *TF-IDF*

    Salah satu kelebihan terbesar dari *TF-IDF* adalah kemudahan dan kesederhanaannya dalam penggunaan. Perhitungannya mudah, tidak memerlukan banyak komputasi, dan menjadi titik awal yang baik untuk perhitungan kesamaan (melalui vektorisasi *TF-IDF* + *Cosine Similarity*).
    
  - Kekurangan Penggunaan *TF-IDF*

    Perlu diperhatikan bahwa *TF-IDF* tidak dapat menangkap makna semantik. Metode ini mempertimbangkan pentingnya kata berdasarkan bobotnya, namun tidak dapat menangkap konteks kata untuk memahami pentingnya dalam cara tersebut. Seperti yang telah disebutkan sebelumnya, *TF-IDF* mengabaikan urutan kata sehingga frasa seperti *"Queen of England"* tidak akan dianggap sebagai satu kesatuan. Hal ini juga berlaku pada situasi seperti negasi *"not pay the bill"* vs *"pay the bill"*, di mana urutan kata sangat mempengaruhi makna. Dalam kedua kasus tersebut, penggunaan alat *NER* dan garis bawah, seperti *"queen_of_england"* atau *"not_pay"*, dapat menjadi cara untuk menganggap frasa tersebut sebagai satu kesatuan.
    Kekurangan lainnya adalah *TF-IDF* dapat tidak efisien dalam penggunaan memori karena dapat mengalami masalah dimensi yang tinggi. Panjang vektor *TF-IDF* sama dengan ukuran kosakata. Dalam beberapa konteks klasifikasi ini mungkin tidak menjadi masalah, tetapi dalam konteks lain seperti pengelompokan, hal ini dapat menjadi tidak praktis seiring bertambahnya jumlah dokumen. 

- ***Cosine Similarity***

     *Cosine Similarity* adalah metrik matematika yang digunakan untuk mengukur kesamaan antara dua vektor dalam ruang multidimensi. Ini didefinisikan sebagai kosinus sudut antara vektor, yang merupakan hasil perkalian titik dari vektor dibagi dengan hasil kali panjang mereka. Metrik ini sangat berguna dalam analisis teks dan sistem rekomendasi, di mana teks diubah menjadi vektor kata dan kesamaan semantik antara dokumen dapat diukur berdasarkan arah vektor tersebut, bukan hanya berdasarkan magnitudo atau ukuran mereka. *Cosine Similarity* selalu berada dalam interval -1 hingga 1, di mana -1 berarti persis berlawanan, 0 menunjukkan ortogonal atau tidak berkorelasi, dan 1 berarti persis sama. Untuk menentukan seberapa mirip satu judul buku dengan yang lain, kita bisa menggunakan teknik *cosine similarity*. Fungsi *`cosine_similarity`* dari *library `sklearn`* memungkinkan kita untuk melakukan perhitungan ini [[7]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html).

  $$\text{similarity}(A,B) = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|} = \frac{\sum\limits_{i=1}^{n} A_i B_i}{\sqrt{\sum\limits_{i=1}^{n} A_i^2} \sqrt{\sum\limits_{i=1}^{n} B_i^2}}$$

  
  Di mana $A_i$ dan $B_i$ merupakan komponen dari masing-masing vektor A dan B.

  | *book_title* | *David Copperfield's Tales of the Impossible* | *Killing Floor* | *Almost blue (Stile libero)* | *Someday My Prince* | *From a Buick 8* | *A Murder, a Mystery and a Marriage: A Story* | *La ignorancia* | *Alice's Adventures in Wonderland and Through the Looking Glass* |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | *Our Man in Havana: An Entertainment (Twentieth Century Classics)* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *Out of the Shadows (Shadows Trilogy (Paperback))* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *Canadians on Everest* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *The Tulip* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *Chicken Soup for the Cat and Dog Lover's Soul - Celebrating Pets as Family with Stories About Cats, Dogs and Other Critters* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *Prime Witness* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *Allie's Crocodile (Young Puffin Confident Readers)* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
  | *The Iron Giant* | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

  Tabel 6.1.2 Hasil penerapan *Cosine Similarity*

  
  **Kelebihan dan Kekurangan Penggunaan *Cosine Similarity*** [[8]](https://www.geeksforgeeks.org/cosine-similarity/)
  - Kelebihan Penggunaan *Cosine Similarity*
       
       * Efektif dalam mengukur kesamaan antara dua objek, tidak terpengaruh oleh ukuran.
       * Cocok untuk data dengan banyak fitur yang jarang terisi.
       * Sering digunakan dalam analisis teks dan sistem rekomendasi karena invarian skala.
         
  - Kekurangan Penggunaan *Cosine Similarity*
 
       * Kurang optimal dalam ruang dimensi rendah.
       * Tidak menangkap makna semantik atau konteks kata.
       * Mengabaikan urutan kata, yang bisa penting dalam pemahaman makna.
       * Bisa tidak efisien memori dan menderita dari kutukan dimensionalitas, terutama dalam pengelompokan dokumen besar.

- ***Recommendation Testing***

Hasil pengujian sistem rekomendasi dengan pendekatan *Content-based Recommendation* adalah sebagai berikut.

| *isbn* | *book_title* | *book_author* | *pub_year* | *publisher* | *image_s_url* | *image_m_url* | *image_l_url* |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8005 | *Room for a Single Lady* | Clare Boylan | 0 | *Little Brown Company* | http://images.amazon.com/images/P/034910901X.0... | http://images.amazon.com/images/P/034910901X.0... | http://images.amazon.com/images/P/034910901X.0...	|

Tabel 6.1.3 Sampel buku pengujian

Di atas adalah tabel sampel buku yang akan dijadikan patokan rekomendasi. Rekomendasi yang diberikan dengan pendekatan *Content-based Recommendation* sebagai berikut

| No. | *book_title* | *book_author* |
| --- | --- | --- |
| 1 | *11 Edward Street* | Clare Boylan |
| 2 | *Dog Handling* | CLARE NAYLOR |
| 3 | *Love: A User's Guide* | CLARE NAYLOR |
| 4 | *Ratha's Challenge* | Clare Bell |
| 5 | *Catching Alice* | Clare Naylor |
| 6 | *She's Not There : A Life in Two Genders* | JENNIFER FINNEY BOYLAN |
| 7 | *Karma and Reincarnation: Transcending Your Past, Transforming Your Future* | Elizabeth Clare Prophet |
| 8 | *Creative Abundance: Keys to Spiritual and Material Prosperity* | Elizabeth Clare Prophet |
| 9 | *The Complete Book of Massage* | CLARE MAXWELL-HUDSON |
| 10 | *Business @ the Speed of Thought: Succeeding in the Digital Economy* | Bill Gates |

Tabel 6.1.4 *Top-n recommendation* menggunakan *Content-based Recommendation*

Terlihat bahwa sistem yang dikembangkan mampu memberikan saran beberapa buku berdasarkan masukan judul buku "*Room for a Single Lady*", dengan hasil yang didasarkan pada analisis algoritma sistem. Terlihat bahwa rekomendasi yang dihasilkan merujuk ke penulis buku yang ada nama Clare, dan menghasilkan satu rekomendasi dengan penulis buku yang sama dengan buku yang telah di baca, yaitu *11 Edward Street* oleh Clare Boylan.

### 6.2. *Collaborative Filtering Recommendation*
*Collaborative Filtering Recommendation* adalah teknik yang digunakan dalam sistem rekomendasi untuk memprediksi preferensi atau minat pengguna berdasarkan preferensi atau minat pengguna lain yang serupa. Teknik ini tidak mengandalkan konten item yang direkomendasikan, melainkan pada pola interaksi dan penilaian yang dilakukan oleh pengguna terhadap item-item tersebut [[9]](https://realpython.com/build-recommendation-engine-collaborative-filtering/#what-is-collaborative-filtering ).

![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/f940430f-d326-4202-bcc5-841705218bee)

Gambar 6.2.1 Visualisasi *Collaborative Filtering Recommendation* bekerja

- ***Data Preparation***

Dalam *data preparation*, fitur `user_id` dan `isbn` di *dataframe* `ratings` dikonversi menjadi indeks bilangan bulat. Setelah itu, fitur-fitur yang sudah dikonversi ini dipetakan kembali ke dalam *dataframe* `rating` masing-masing.

| *Description* | *Value* |
| --- | --- |
| *Number of User* | 2248 |
| *Number of Books* | 8791 |
| *Min Rating* | 1 |
| *Max Rating* | 10 |

Tabel 6.2.1 Hasil konversi menjadi integer

- ***Training Data and Validation Data Split***

Kemudian kita melakukan pembagian *dataset* dengan rasio 80:20, yaitu 80% untuk data latih (*training data*) dan 20% untuk data uji (*validation data*). Sebelum itu, kita harus menggabungkan *`user`* dan *`book`* menjadi satu nilai yang unik. Setelah itu, kita normalisasi nilai *`book_rating`* ke rentang 0 hingga 1 untuk mempermudah proses pelatihan.

- ***Model Development and Testing***

"*Highly Rated Books by user_id 695*"

| No. | *Book Title* | *Author* |
| --- | --- | --- |
| 1 | *Elements of Programming With Perl* | Andrew L. Johnson |
| 2 | *To Catch a Cat* | Marian Babson |
| 3 | *People of the Wolf (The First North Americans series, Book 1)* | W. Michael Gear |
| 4 | *The Door to December* | Dean R. Koontz |

Tabel 6.2.2 Buku-buku yang di-*rating* oleh *user_id* 695

*Top 10 Recommendations for user_id 695*

| No. | *Book Title* | *Author* |
| --- | --- | --- |
| 1 | *11 Edward Street* | Clare Boylan |
| 2 | *Dog Handling* | Clare Naylor |
| 3 | *Love: A User's Guide* | Clare Naylor |
| 4 | *Ratha's Challenge* | Clare Bell |
| 5 | *Catching Alice* | Clare Naylor |
| 6 | *She's Not There : A Life in Two Genders* | Jennifer Finney Boylan |
| 7 | *Karma and Reincarnation: Transcending Your Past, Transforming Your Future* | Elizabeth Clare Prophet |
| 8 | *Creative Abundance: Keys to Spiritual and Material Prosperity* | Elizabeth Clare Prophet |
| 9 | *The Complete Book of Massage* | Clare Maxwell-Hudson |
| 10 | *Business @ the Speed of Thought: Succeeding in the Digital Economy* | Bill Gates |

Tabel 6.2.3 *Top-n recommendation* menggunakan *Collaborative Filtering Recommendation*


Dari informasi yang diberikan, tampaknya sistem telah memilih secara acak seorang pengguna dengan *`user_id`* **695**. Sistem kemudian mencari buku-buku yang paling disukai oleh pengguna tersebut, yang meliputi:
*   ***Elements of Programming With Perl*** karya **Andrew L. Johnson**
*   ***To Catch a Cat*** karya **Marian Babson**
*   ***People of the Wolf (The First North Americans series, Book 1)*** karya **W. Michael Gear**
*   ***The Door to December*** karya **Dean R. Koontz**

Setelah itu, sistem akan membandingkan buku-buku dengan penilaian tertinggi dari pengguna ini dengan seluruh katalog buku, kecuali yang sudah dibaca, dan mengurutkan rekomendasi berdasarkan skor tertinggi. Terlihat ada 10 buku yang direkomendasikan oleh sistem. Rekomendasi yang diberikan benar-benar tidak ada kesamaan penulis buku dari buku yang sudah dibaca. Ini menunjukan bahwa rekomendasi dibentuk dari hasil kesamaan para *`users`* lainnya.

## 7. *Evaluation*

7.1. ***Content-based Recommendation***  
   Pada tahap evaluasi untuk model sistem rekomendasi dengan pendekatan berbasis konten (*content-based recommendation*), metrik akurasi dapat dihitung dengan membagi jumlah buku yang direkomendasikan dengan jumlah buku yang ditulis oleh penulis yang sama, kemudian dikalikan dengan 100.

   $$Accuracy=\frac{\displaystyle\sum_{i=1}^{n} RecommendedBooks_i}{\displaystyle\sum_{i=1}^{n} BooksWithSameAuthor_i} \times 100$$

   Menggunakan data pada tahap pemodelan sebelumnya, dengan penulis Clare Boylan, ditemukan bahwa ia menulis 2 buku. Jumlah rekomendasi buku yang dihasilkan, yaitu 1, lalu dibagi dengan 2, lalu dikalikan 100, menghasilkan akurasi 50,00%.

7.2. **Collaborative Filtering Recommendation**  
   Berdasarkan model machine learning yang dibangun menggunakan *embedding layer, Adam optimizer,* dan *binary crossentropy loss function,* metrik yang digunakan adalah *Root Mean Squared Error* (RMSE). RMSE dihitung dengan mengambil akar kuadrat dari jumlah kuadrat selisih antara nilai sebenarnya dan nilai prediksi, dibagi dengan jumlah data. Nilai RMSE yang rendah menunjukkan bahwa nilai prediksi mendekati nilai observasi. 

   $$RMSE=\sqrt{\sum^{n}_{i=1} \frac{y_i - y\\_pred_i}{n}}$$

   Di mana, nilai $n$ merupakan jumlah *dataset*, nilai $y_i$ adalah nilai sebenarnya, dan $y\\_pred$ yaitu nilai prediksinya terdahap $i$ sebagai urutan data dalam *dataset*.

   ![image](https://github.com/sandysan0/Dicoding-Recommendation-System/assets/144081667/f3b1e5df-4f56-476c-b9bc-7dbfdc052425)

   Gambar 7.2.1 Visualisasi hasil pelatihan dan validasi dari metrik *RMSE* serta *training* dan *validation loss*

   Gambar 7.2.1 menunjukkan dua metrik selama pelatihan model machine learning: *RMSE (Root Mean Squared Error)* dan *Loss*, diukur sepanjang 40 *epoch*.
   
   - *RMSE*: Nilai *RMSE* menurun dari awal yang tinggi hingga stabil pada nilai yang lebih rendah, baik untuk data pelatihan maupun validasi. Ini menandakan bahwa model tersebut menjadi lebih akurat dalam prediksinya seiring berjalannya waktu.
   - *Loss*: Sama seperti *RMSE*, nilai *loss* juga menurun seiring bertambahnya *epoch*, mengindikasikan peningkatan performa model. Penurunan yang tajam pada awal pelatihan menunjukkan pembelajaran yang cepat, yang kemudian melambat saat model mulai konvergen.
   
   Kedua grafik tersebut memberikan visualisasi yang jelas tentang bagaimana model *machine learning* memperbaiki dirinya seiring dengan pelatihan berulang, yang tercermin dalam penurunan nilai *RMSE* dan *loss*. Ini adalah indikator yang baik bahwa model sedang belajar dari data dan menjadi lebih baik dalam melakukan prediksi.

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
