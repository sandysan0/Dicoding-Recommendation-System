# Laporan Proyek Machine Learning - Sandy Susanto

## Domain Proyek

Domain proyek ini akan membahas mengenai permasalahan dalam bidang ekonomi dan bisnis. Fokus pada proyek ini adalah untuk membuat prediksi harga mobil bekas pakai berdasarkan fitur-fitur dan dimiliki oleh kendaraan tersebut.

<img src="https://image.cnbcfm.com/api/v1/image/106961034-16342989482021-10-15t115305z_757712464_rc2baq9ww2kh_rtrmadp_0_usa-economy.jpeg?v=1671462564" alt="Car Market" title="Car Market Illustration" width="100%">

Pembelian kendaraan baru merupakan salah investasi finansial yang signifikan bagi sebagian besar institusi maupun individu. Dalam konteks ini, nilai jual kembali kendaraan, yang mencerminkan sebagian dari *return of investment*, menjadi faktor penting dalam proses pengambilan keputusan pembelian. Oleh karena itu, baik konsumen individu maupun perusahaan memiliki kepentingan dalam mengidentifikasi atribut-atribut kendaraan yang dapat mempertahankan nilai jualnya di pasar primer ataupun sekunder [[1]](https://link.springer.com/article/10.1057/jors.2016.16).

Menurut data yang dianalisis, ada beberapa hal penting yang sangat mempengaruhi berapa harga mobil bekas nantinya, seperti siapa produsen yang membuat mobilnya, tipe mobil, seberapa jauh mobil itu sudah berjalan, berapa umurnya, riwayat servisnya, bagaimana kondisi mobil secara fisik, seberapa banyak mobil itu terjual di pasaran, bagaimana layanan setelah mobil itu dibeli, dan bagaimana cara pemilik sebelumnya mengendarainya [[2]](https://www.semanticscholar.org/paper/New-Model-for-Residual-Value-Prediction-of-the-Used-Shen-Wang/af9ec65507e1f156d6c1817f92caa9547e5ba61a).

Reputasi yang baik dari penjual dapat sedikit meningkatkan harga yang ditawarkan dalam lelang *online* untuk mobil bekas, terutama jika sudah ada tawaran yang masuk dan peluang untuk terjual. Namun, pengaruhnya tidak sebesar faktor lain seperti kejelasan status kepemilikan atau waktu penutupan lelang. Menariknya, meskipun mobil dipajang dengan menarik dan banyak foto, hal tersebut tidak terlalu berpengaruh terhadap harga akhir atau kesempatan mobil tersebut untuk terjual. Ini cukup mengejutkan karena biasanya presentasi yang baik dianggap penting dalam penjualan *online*, terutama untuk barang yang beragam dan bernilai tinggi seperti mobil [[3]](https://link.springer.com/article/10.1007/s11293-006-9045-7).

Semua hal ini saling berkaitan dan bersama-sama menentukan harga jual kembali mobil. Jika kita tidak memperhatikan bagaimana semua hal ini saling berhubungan dan hanya menghitung pengaruhnya satu per satu, maka prediksi kita tentang harga mobil bekas tidak akan akurat.

Proyek ini akan melibatkan beberapa tahap, mulai dari pengumpulan dan pembersihan data, eksplorasi data untuk memahami fitur-fitur yang paling berpengaruh terhadap harga, pembangunan model prediksi, hingga evaluasi dan penyempurnaan model. Dengan pendekatan yang sistematis dan pemanfaatan teknologi terkini, proyek prediksi harga mobil ini berpotensi memberikan kontribusi terhadap efisiensi dan transparansi pasar mobil bekas.

# Business Understanding

## Problem Statements

Ketidakpastian harga jual kembali mobil bekas menyulitkan pembeli dan penjual dalam menentukan harga yang tepat. Faktor-faktor seperti merek, model, usia, jarak tempuh, riwayat servis, kondisi fisik, dan reputasi penjual mempengaruhi harga, tetapi sering kali sulit untuk mengintegrasikan faktor-faktor ini secara akurat. Dari konteks yang telah disampaikan sebelumnya, teridentifikasi dua pertanyaan utama yang akan dijawab melalui proyek ini:
1. Bagaimana proses pembuatan model *machine learning* yang dapat memprediksi harga jual mobil bekas?
2. Apa langkah-langkah yang diperlukan dalam mempersiapkan data sebelum diaplikasikan dalam pengembangan model *machine learning*?

## Goals

Dari permasalahan yang telah diuraikan, tujuan yang ingin dicapai melalui proyek ini adalah sebagai berikut:
1. Menjalankan proses persiapan data secara menyeluruh untuk memastikan data siap digunakan dalam model *machine learning*.
2. Mengembangkan model *machine learning* yang efektif untuk menganalisis dan memprediksi harga jual mobil bekas dengan tingkat *error* yang minimal.

## Solution Statements

Dari uraian sebelumnya, beberapa langkah strategis telah diidentifikasi untuk mencapai target proyek, antara lain:
1. Proses persiapan data akan meliputi teknik-teknik berikut:
   - One-hot-encoding untuk memtransformasikan fitur kategorikal menjadi fitur yang lebih detail dalam mempresentasikan kategori.
   - Pembagian dataset menjadi dua bagian, yaitu set pelatihan dan set pengujian dengan proporsi 90% untuk pelatihan dan 10% untuk pengujian, yang akan digunakan dalam pengembangan model *machine learning*.
   - Standardisasi nilai pada fitur numerik untuk menghindari deviasi yang signifikan pada data.
   - Reduksi dimensi untuk mengurangi jumlah variabel dalam data sambil memastikan informasi penting tetap terjaga.
2. Dalam fase pembuatan model *machine learning*, tiga model yang menggunakan algoritma yang berbeda akan diuji. Algoritma yang akan diaplikasikan meliputi Algoritma K-Nearest Neighbor, Algoritma Random Forest, dan Algoritma Adaptive Boosting. Setelah evaluasi kinerja masing-masing model, algoritma yang memberikan akurasi prediksi terbaik akan dipilih sebagai model utama.
3. Ketiga model ini akan diuji secara bersamaan dengan menggunakan set data yang sama. Performa mereka akan dievaluasi berdasarkan metrik ***Mean Squared Error (MSE)*** untuk menentukan algoritma yang paling efektif dalam memprediksi harga mobil bekas dengan akurat.
   
# Data Understanding

![Dataset](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/3aca9dff-0179-4bbc-b0bf-afe5570ec676)

*Dataset* yang digunakan adalah [Car Price Prediction Challenge](https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge) dalam bentuk `.csv` ([Comma-separated Values](https://en.wikipedia.org/wiki/Comma-separated_values)). 

*Dataset* tersebut masih perlu disesuaikan lagi sebelum digunakan. Berikut penyesuaian-penyesuaian yang dilakukan
- Menghapus kolom yang tidak akan digunakan karena tidak relevan, sama saja dengan kolom lain, dan tidak menjelaskan apapun, yaitu `ID`, `Levy`, `Manufacturer`, `Model`, dan `Prod. year`
  ```python
      car.drop('ID'          , inplace=True, axis=1)
      car.drop('Levy'        , inplace=True, axis=1)
      car.drop('Manufacturer', inplace=True, axis=1)
      car.drop('Model'       , inplace=True, axis=1)
      car.drop('Prod. year'  , inplace=True, axis=1)
   ```
- Menghilangkan tulisan 'km', tulisan 'Turbo', dan mengubah tipe data menjadi `int64` dan `float64` supaya lebih mudah untuk melakukan prediksi
  ```python
     car['Price'] = car['Price'].astype('float64')
     car['Engine volume'] = car['Engine volume'].str.replace(' Turbo', '').astype('float64')
     car['Mileage'] = car['Mileage'].str.replace(' km', '').astype('float64')
     car['Cylinders'] = car['Cylinders'].astype('int64')
  ```

Langkah selaunjutnya proses *Exploratory Data Analysis* (EDA). EDA adalah proses investigasi awal pada data untuk mengidentifikasi pola, menemukan anomali, menguji hipotesis, dan memeriksa asumsi dengan menggunakan statistik ringkasan dan representasi grafis.

1. **Deskripsi Variabel**  
   Melakukan pengecekan informasi dari *dataframe* `car`
   
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/d4402fb7-3c4e-4398-90fb-96aba87cb8a9)

   Dari *dataset* yang telah dibersihkan, terdapat 19.237 baris data dengan atribut sebanyak 13 kolom. Terdapat 2 atribut dengan tipe data `int64`, 3 atribut dengan tipe data `float64` dan 8 atribut dengan tipe data `object`. Berikut adalah keterangan untuk masing-masing variabel,
      - `Price` : Harga jual mobil dalam $
      - `Category` : Kategori mobil, seperti SUV, sedan, hatchback, dll
      - `Leather interior` : Menunjukkan apakah mobil memiliki interior kulit atau tidak.
      - `Fuel type` : Jenis bahan bakar yang digunakan mobil
      - `Engine volume` : Volume mesin mobil, diukur dalam liter
      - `Mileage` : Jarak tempuh mobil dalam KM
      - `Cylinders` : Jumlah silinder dalam mesin mobil.
      - `Gear box type` : Jenis kotak gigi/transmisi, seperti manual, otomatis, atau semi-otomatis.
      - `Drive wheels` : Jenis penggerak roda, seperti penggerak roda depan, belakang, atau semua roda.
      - `Doors` : Jumlah pintu pada mobil.
      - `Wheel` : Jenis roda yang digunakan, bisa juga merujuk pada *steering wheel* (kiri atau kanan).
      - `Color` : Warna eksterior mobil.
      - `Airbags` : Jumlah kantung udara keselamatan yang tersedia di mobil.
   
2. **Deskripsi Statistik**  
   
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/a997ee50-3f32-451f-97e3-916bd46959f2)

   Melihat deskripsi statistik dari *dataframe* `car` yaitu,
   -  `count` : Jumlah data
   -  `mean` : Rata-rata
   -  `std` : Standar deviasi/simpangan baku
   -  `min` : Nilai minimum
   -  `25%` : Kuartil bawah/Q1
   -  `50%` : Kuartil tengah/Q2/median
   -  `75%` : Kuartil atas/Q3
   -  `max` : Nilai maksimum
   
3. **Menangani Missing Value**  
   
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/7720f307-9d09-40d5-87f8-ed3119d23946)
   
   Ada **2405 kolom** *airbags*, **10 kolom** *engine volume*, dan **721 kolom** *mileage* yang tidak diketahui. Oleh karena itu, data-data yang tidak diketahui akan dihilangkan dari *dataset*.
   ```python
   car = car.loc[(car[['Engine volume', 'Mileage', 'Airbags']]!=0).all(axis=1)]
   ```
   
4. **Menangani Outliers**  
   Untuk memeriksa keberadaan data yang menyimpang atau *outliers* dalam *dataframe* `car` dapat menggunakan visualisasi data berupa [`boxplot`](https://seaborn.pydata.org/generated/seaborn.boxplot.html) yang dibantu oleh *library* [`seaborn`](https://seaborn.pydata.org/). *Outliers* adalah nilai-nilai yang sangat berbeda dari sebagian besar data dan bisa mempengaruhi hasil analisis secara keseluruhan. Visualisasi dengan `boxplot` memungkinkan kita untuk mengidentifikasi dan mengevaluasi *outliers* ini secara efektif.
   
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/7c9839f4-df1b-48f3-87b2-235553b3ea8f)
     
   Dari diagram boxplot yang ditampilkan, terlihat bahwa pada variabel numerik yang menunjukkan adanya nilai-nilai *outlier*, yaitu data yang jauh berbeda dari nilai-nilai lainnya dalam kumpulan data tersebut.

   Untuk mengidentifikasi dan menangani *outliers*, pendekatan yang digunakan adalah metode IQR, atau *Inter Quartile Range*.
   $$IQR=Q_3-Q_1$$
   
   Selanjutnya, batas bawah dan batas atas ditetapkan untuk mengelilingi *outliers*.
   
   $$BatasBawah=Q_1-1.5*IQR$$
   
   $$BatasAtas=Q_3-1.5*IQR$$

   Metode ini memungkinkan identifikasi nilai yang berada di luar jangkauan normal data.
   
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/27013af8-eae8-453c-af4f-c222b85c6e98)
   
   Setelah membersihkan *outliers* dengan metode IQR, atau *Inter Quartile Range*, terlihat bahwa jumlah *outliers* pada boxplot telah menurun. Walaupun masih terdapat *outliers* pada variabel `price`, `engine volume`, dan `mileage`, nilai-nilai tersebut masih berada dalam rentang yang dianggap aman.
   
5. **Univariate Analysis**  
   Melaksanakan analisis data *univariate* terhadap variabel-variabel. Proses analisis ini menggunakan bantuan visualisasi histogram.

   ***Categorical Features***

   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/84d8a4b8-c365-4feb-9598-979cc94ee71b)
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/a7a63af6-fecc-4e4a-b1f7-b853d5d90bb3)
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/f272404d-863c-4cb8-bed9-a141760d26c5)
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/e6686511-f998-4a46-b755-16ef62715ea8)
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/e17e4ea9-d744-45bb-9a15-91e14bf13d4a)
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/7b67f47b-21ec-453e-b859-a6faad0edff8)
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/d96fdbb9-5bb7-4a3f-b67e-7f8d6bab49f4)
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/0c1234dd-e0fd-4448-9f43-f093bfc028d4)

   Dari data beberapa histogram di atas diperoleh informasi, yaitu:
   - Mayoritas mobil yang ada di pasar bertipe sedan.
   - Lebih dari **50%** mobil memiliki interior terbuat dari kulit.
   - Mayoritas mobil berbahan bakar petrol.
   - Mobil matic lebih sering dijumpai di pasar.
   - Mobil dengan penggerak di depan lebih banyak.
   - Mobil dengan 4 pintu lebih banyak dibandingkan 2 pintu dan >5 pintu.
   - Lebih banyak mobil dengan posisi stir di kiri.
   - Warna putih, silver, dan hitam mendominasi warna mobil di pasar.

   ***Numerical Features***
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/56df933d-c99d-4e23-9767-9f8fa21b6268)

   Informasi yang dapat diketahui dari histogram di atas
   *   Harga pasaran mobil berada di **<$1000**
   *   Volume mesin kendaraan mobil umumnya 2 liter
   *   Kendaraan bekas pakai mendominasi pasar mobil
   *   Hampir semua mobil memiliki 4 silinder
   *   Mayoritas jumlah *airbags* dalam mobil adalah 4
   
6. **Multivariate Analysis**  
   Melaksanakan analisis data *multivariate* terhadap variabel-variabel.

   ***Categorical Features***
   
   Mengecek harga kendaraan terhadap masing-masing fitur
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/ed7edb20-444e-4c6f-9689-9b5c3d4f6f66)
   
   Informasi yang bisa didapatkan dari histogram di atas
   *   Mobil bertipe Jeep dan Universal memiliki harga yang tertinggi dibandingkan dengan mobil lainnya
   *   Mobil dengan interior kulit memiliki harga yang lebih mahal
   *   Mobil dengan bahan bakar Diesel dan *Plug-in Hybrid* memiliki harga tertinggi dan sangat jauh gap harganya dengan mobil berbahan bakar CNG
   *   Harga mobil yang *Gear box*-nya bertipe Tiptronic paling tinggi
   *   Tidak ada perbedaan harga mobil berdasarkan roda penggeraknya
   *   Mobil dengan pintu 2 memiliki harga yang jauh dangan pintu 4 dan pintu >5
   *   Mobil stri kiri memiliki harga yang lebih mahal dibandingkan mobil stir kanan
   *   Harga mobil berdasarkan warna memiliki banyak variasi. Mobil dengan warna *pink, purple*, dan *green* memiliki harga di bawah rata-rata

   ***Numerical Features***
   
   Menggambarkan distribusi data untuk variabel numerik dalam *dataframe* `epower` menggunakan visualisasi. Ini dilakukan dengan memanfaatkan fungsi `pairplot` dari *library*    `seaborn`, dengan menetapkan `diag_kind` ke `kde` untuk mengestimasi dan memvisualisasikan distribusi probabilitas dari setiap variabel numerik.
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/c35adee6-7572-4e95-b35e-1ec4c260ae94)

7. **Correlation Matrix with Heatmap**  
   Mengkaji hubungan antara variabel numerik dengan memvisualisasikan matriks korelasi melalui diagram *heatmap*.
   
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/d05feabc-aa06-42d1-822d-14bedaa52066)

   Diagram *heatmap* yang ditampilkan memiliki angka dari -0.25 hingga 1, yang mengindikasikan tingkat korelasi antara variabel numerik dengan cara berikut:
- Nilai yang mendekati 1 menandakan adanya korelasi positif yang kuat antara dua variabel, di mana keduanya cenderung meningkat secara bersamaan.
- Nilai yang mendekati 0 menunjukkan bahwa tidak ada korelasi yang signifikan antara dua variabel.
- Nilai yang mendekati -1 menunjukkan korelasi negatif yang kuat, di mana satu variabel cenderung meningkat sementara yang lainnya menurun.  

8. **Analisis Korelasi Antar Fitur**  
   Fitur `Price` memiliki korelasi yang cukup kuat dengan `Engine Volume`.

   Sehingga, fitur `Mileage`, `Cylinders`, dan `Airbags`yang memiliki korelasi rendah dapat dilakukan *drop* (menghapus) untuk menghilangkan fitur-fitur tersebut.

   ```python
   car.drop(['Mileage'],   inplace=True, axis=1)
   car.drop(['Cylinders'], inplace=True, axis=1)
   car.drop(['Airbags'],   inplace=True, axis=1)
   ```
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/7ea1d0f8-71fd-4263-ab41-a3efa55cc924)

# Data Preparation

Tahap persiapan data, yang sudah dijelaskan dalam bagian [Solution Statements](#solution-statements "Solution Statements"), merupakan langkah krusial untuk memastikan data siap digunakan dalam pelatihan model *machine learning*. Ada tiga langkah utama dalam persiapan data, yaitu:

1. **Encoding Fitur Kategori**

   Dalam proses pengkodean untuk variabel kategori, teknik yang sering digunakan adalah [*`one-hot-encoding`*](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html). Fungsi ini tersedia dalam library [*`scikit-learn`*](https://scikit-learn.org/), yang memungkinkan transformasi variabel kategori menjadi fitur-fitur baru yang dapat merepresentasikan informasi kategorikal dengan tepat.

    ```python
    #One-hot-encoding
   car = pd.concat([car, pd.get_dummies(car['Category'], prefix='Category')],axis=1)
   car = pd.concat([car, pd.get_dummies(car['Leather interior'], prefix='Leather interior')],axis=1)
   car = pd.concat([car, pd.get_dummies(car['Fuel type'], prefix='Fuel type')],axis=1)
   car = pd.concat([car, pd.get_dummies(car['Gear box type'], prefix='Gear box type')],axis=1)
   car = pd.concat([car, pd.get_dummies(car['Drive wheels'], prefix='Drive wheels')],axis=1)
   car = pd.concat([car, pd.get_dummies(car['Doors'], prefix='Doors')],axis=1)
   car = pd.concat([car, pd.get_dummies(car['Wheel'], prefix='Wheel')],axis=1)
   car = pd.concat([car, pd.get_dummies(car['Color'], prefix='Color')],axis=1)
   car.drop(['Category','Leather interior','Fuel type', 'Gear box type', 'Drive wheels', 'Doors', 'Wheel', 'Color'], axis=1, inplace=True)
    ```
    
2. **Split Data**  
   Proses pembagian data bertujuan untuk membagi kumpulan data menjadi dua segmen: segmen untuk pelatihan, yang disebut *data train*, dan segmen untuk pengujian, yang disebut *data test*. Pembagian ini menggunakan metode `train_test_split` dengan proporsi 90% data untuk pelatihan dan 10% sisanya untuk pengujian.
   
    ```python
       X = car.drop(["Price"],axis =1)
       y = car["Price"]
       X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 123)
    ```
    ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/c4761482-8a78-4cdf-ba17-3ad826fc091d)

3. **Standarisasi pada Fitur Numerik**  
   Melakukan standarisasi nilai pada fitur numerik dengan menggunakan `StandardScaler` dari *library* `scikit-learn`. Proses standarisasi ini bertujuan untuk mencegah terjadinya penyimpangan nilai data yang cukup besar.
   
    ```python
      numericalFeatures = ['Engine volume']
      scaler = StandardScaler()
      scaler.fit(X_train[numericalFeatures])
      X_train[numericalFeatures] = scaler.transform(X_train.loc[:, numericalFeatures])
      X_train[numericalFeatures].head()
    ```
   
   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/6aa0f8d7-d0ac-4c6f-abbe-4820161a7caa)

4. **Reduksi Dimensi**  
   Reduksi dimensi adalah metode yang digunakan untuk mengurangi jumlah variabel dalam data sambil memastikan informasi penting tetap terjaga. Salah satu metode reduksi dimensi yang sering digunakan adalah *Principal Component Analysis*, atau PCA. Teknik ini mengurangi dimensi data dengan mengubahnya dari ruang berdimensi n menjadi ruang berdimensi m yang lebih rendah, di mana m lebih kecil dari n, tanpa kehilangan esensi data tersebut.

   ```python
       sns.pairplot(car[['Price','Engine volume']], plot_kws={"s": 3});
   ```

   ![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/5075307b-324c-458b-a755-d9308a778a31)

   Aplikasikan [*`class PCA`*](https://scikit--learn-org.translate.goog/stable/modules/generated/sklearn.decomposition.PCA.html?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc) dari library *`scikit learn`*
 
    ```python
         pca = PCA(n_components=2, random_state=123)
         pca.fit(car[['Price','Engine volume']])
         princ_comp = pca.transform(car[['Price','Engine volume']])
    ```
    
# Model Development

Setelah dilakukannya tahap *data preparation*, selanjutnya adalah melakukan tahap persiapan model terlebih dahulu sebelum mengembangkan model menggunakan algoritma yang telah ditentukan.

Yang pertama dilakukan adalah menyiapkan *dataframe* untuk analisis model menggunakan `index` yang terdiri dari `train_mse` dan `test_mse`, serta `columns` yang mencakup algoritma prediksi seperti [`K-Nearest Neighbor (KNN)`](https://www.geeksforgeeks.org/k-nearest-neighbours/), [`Random Forest`](https://www.ibm.com/topics/random-forest#:~:text=Random%20forest%20is%20a%20commonly,Decision%20trees), dan [`Adaptive Boosting (AdaBoost)`](https://www.analyticsvidhya.com/blog/2021/09/adaboost-algorithm-a-complete-guide-for-beginners/#:~:text=AdaBoost%20algorithm%2C%20short%20for%20Adaptive,assigned%20to%20incorrectly%20classified%20instances.).

```python
models = pd.DataFrame(
    index   = ['train_mse', 'test_mse'],
    columns = ['KNN', 'RandomForest', 'Boosting']
)
```

Langkah selanjutnya adalah menerapkan ketiga algoritma ke dalam *dataframe*

1. **K-Nearest Neighbor (KNN) Algorithm**  
   ```python
   knn = KNeighborsRegressor(n_neighbors=10)
   knn.fit(X_train, y_train)
   models.loc['train_mse','knn'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)
   ```
   
   Algoritma KNN merupakan metode klasifikasi yang tidak bergantung pada parameter tertentu dan berada di bawah kategori pembelajaran dengan pengawasan. Algoritma ini       memanfaatkan jarak antar titik data untuk menentukan klasifikasi atau prediksi kelompok dari sebuah titik data. Algoritma ini termasuk metode yang populer dan mudah digunakan dalam *machine learning* untuk klasifikasi dan regresi. Walaupun algoritma KNN bisa digunakan untuk regresi maupun klasifikasi, umumnya lebih sering digunakan untuk klasifikasi. Algoritma ini beroperasi berdasarkan prinsip bahwa titik-titik data yang mirip biasanya berdekatan [[4]](https://www.ibm.com/topics/knn).
   Cara kerja algoritma K-Nearest Neighbor adalah sebagai berikut: [[5]](https://geospasialis.com/k-nearest-neighbor/)
     - Tentukan jumlah ( K ), yaitu tetangga terdekat yang akan digunakan untuk klasifikasi
     - Hitunglah jarak dari data yang akan diklasifikasikan ke semua titik dalam *dataset.*
     - Urutkan titik-titik tersebut berdasarkan jarak dari yang terkecil hingga terbesar dan pilih ( K ) titik dengan jarak terkecil.
     - Identifikasi kelas yang paling sering muncul di antara ( K ) titik tersebut.
     - Klasifikasikan data baru ke dalam kelas yang paling dominan berdasarkan tetangga terdekatnya.
       
      <br>
      <img src="https://user-images.githubusercontent.com/64983961/188507827-0f729ab6-61a5-4dbc-9be2-afa424f6c294.png" alt="Ilustrasi Algoritma K-Nearest Neighbor" title="Ilustrasi Algoritma K-Nearest Neighbor">
     
   Perhitungan jarak ke tetangga terdekat dapat dilakukan dengan menggunakan metrik sebagai berikut:
   
      - *Euclidean distance*
            $$d(x,y)=\sqrt{\sum_{i=1}^n (x_i-y_i)^2}$$
      - *Manhattan distance*
            $$d(x,y)=\sum_{i=1}^n |x_i-y_i|$$
      - *Hamming distance*
            $$d(x,y)=\frac{1}{n}\sum_{n=1}^{n=n} |x_i-y_i|$$
      - *Minkowski distance*
            $$d(x,y)=\left(\sum_{i=1}^n |x_i-y_i|^p\right)^\frac{1}{p}$$
     
   Kelebihan dari algoritma K-Nearest Neighbor adalah: 
     - Kesederhanaan dan mudah dipahami
     - Mudah diterapkan
     - Berlaku untuk klasifikasi dan regresi
     - Dapat digunakan pada jumlah kelas yang beragam
     - Tidak memerlukan proses training
     - Penambahan data baru yang mudah
     - Parameter minimal
     - Hasil pemodelan non-linear, cocok untuk data dengan batasan tidak linear
     
   Sedangkan kelemahan dari algoritma K-Nearest Neighbor adalah: 
     - Penentuan nilai \( K \) yang optimal diperlukan
     - Biaya komputasi yang besar
     - Proses yang lambat untuk dataset besar
     - Performa menurun pada data berdimensi tinggi
     - Sensitivitas terhadap data *noisy*, data yang hilang, dan *outlier*
     
2. **Random Forest Algorithm**  
   ```python
   RF = RandomForestRegressor(n_estimators=50, max_depth=16, random_state=55, n_jobs=-1)
   RF.fit(X_train, y_train)
   models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)
   ```
   
     *Random forest* memperluas metode *bagging* dengan menggabungkan teknik *bagging* dan pemilihan fitur secara acak, menciptakan kumpulan *decision tree* yang independen satu sama lain. Pemilihan fitur acak ini menciptakan subset fitur yang berbeda-beda, yang menjamin bahwa setiap *decision tree* memiliki sedikit kesamaan. Ini membedakan *random forest* dari *decision tree* biasa, yang biasanya mempertimbangkan semua fitur saat membagi data, sementara *random forest* hanya menggunakan sebagian dari fitur-fitur tersebut [[6]](https://www.ibm.com/topics/random-forest#:~:text=Random%20forest%20is%20a%20commonly,Decision%20trees).
     
     <img src="https://user-images.githubusercontent.com/64983961/188504775-b7e4aa9b-f1cd-41ef-8a70-a977db8f3d60.png" alt="Ilustrasi Algoritma Random Forest" title="Ilustrasi Algoritma Random Forest">
     
      Setelah dilakukan pelatihan, prediksi untuk sampel yang tidak terlihat ($x'$) dapat dibuat dengan menghitung rata-rata prediksi dari semua pohon setiap individu model pada $x'$ [[7]](https://en.wikipedia.org/wiki/Random_forest#Bagging 'Random Forest - Bagging').
     $$\hat{f}=\frac{1}{B}\sum_{b=1}^{B} f_b(x^{'})$$

      Kelebihan dari algoritma Random Forest adalah: 
     - Mengurangi risiko overfitting.
     - Fleksibilitas dalam menangani tugas regresi dan klasifikasi.
     - Kemudahan dalam mengevaluasi kepentingan fitur.
     
      Sedangkan kelemahan dari algoritma Random Forest adalah: 
     - Proses yang memakan waktu.
     - Membutuhkan lebih banyak sumber daya.
     - Lebih kompleks dalam interpretasi.
   
4. **Adaptive Boosting (AdaBoost) Algorithm**  
   ```python
   boosting = AdaBoostRegressor(learning_rate=0.05, random_state=55)
   boosting.fit(X_train, y_train)
   models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)
   ```
     
     AdaBoost, yang merupakan kependekan dari *Adaptive Boosting*, merupakan teknik ansambel dalam *machine learning* yang serbaguna, cocok untuk tugas-tugas klasifikasi dan regresi. Sebagai algoritma pembelajaran dengan pengawasan, AdaBoost menggabungkan sejumlah pembelajar dasar, seperti *decision tree*, untuk membentuk model yang lebih kuat. Cara kerja AdaBoost adalah dengan menyesuaikan bobot data latih sesuai dengan keakuratan klasifikasi yang telah dilakukan sebelumnya [[8]](https://www.almabetter.com/bytes/tutorials/data-science/adaboost-algorithm).
     
     <img src="https://user-images.githubusercontent.com/64983961/188507801-30224052-cac2-4e99-9c67-2aec18de8e59.png" alt="Ilustrasi Algoritma Adaptive Boosting" title="Ilustrasi Algoritma Adaptive Boosting">
     
     Algoritma AdaBoost mengacu kepada metode tertentu untuk melakukan pelatihan *classifier* yang di-*boosted*. Pengklasifikasian tersebut adalah pengklasifikasian dalam bentuk, [[9]](https://en.wikipedia.org/wiki/AdaBoost#Training 'AdaBoost - Training')
     $$F_T(x)=\sum_{t=q}^{T}f_t(x)$$
     di mana setiap $F_T$ adalah *learner* yang lemah yang mengambil objek $x$ sebagai input dan mengembalikan nilai yang menunjukkan kelas objek. Demikian juga pada pengklasifikasi $T$ merupakan nilai positif jika sampel berada dalam kelas positif, dan negatif jika sebaliknya.

      Kelebihan dari algoritma AdaBoost adalah: 
     - Meningkatkan akurasi prediktif.
     - Adaptif terhadap kasus sulit.
     - Cepat dan mudah diimplementasikan.
     - Efektif untuk klasifikasi biner dan multi-kelas.
     
      Sedangkan kelemahan dari algoritma AdaBoost adalah: 
     - Tidak cocok untuk data *noisy*.
     - Sensitif terhadap *outliers*.

Ketiga model yang telah dirancang —berdasarkan algoritma K-Nearest Neighbor, Random Forest, dan Adaptive Boosting— akan diuji untuk menentukan mana yang memiliki presisi prediksi paling akurat dan tingkat *error* paling minimal.

# Evaluation

Evaluasi model regresi pada dasarnya cukup mudah dipahami. Pada intinya, sebagian besar metrik evaluasi memiliki prinsip yang serupa. Performa model dianggap baik jika prediksi yang dihasilkan dekat dengan nilai aktual. Sebaliknya, dianggap kurang baik jika jauh dari nilai aktual. Perbedaan antara nilai yang diprediksi dan nilai aktual dikenal sebagai kesalahan prediksi. Oleh karena itu, tujuan utama dari semua metrik adalah untuk mengukur dan meminimalkan kesalahan prediksi tersebut.

```python
# Terapkan normalisasi pada data numerik dalam X_test agar nilai rata-ratanya menjadi nol dan variansnya satu
X_test.loc[:, numericalFeatures] = scaler.transform(X_test[numericalFeatures])
```

Evaluasi performa tiga model pembelajaran mesin: *K-Nearest Neighbor, Random Forest*, dan *AdaBoost*, pada set data pelatihan dan pengujian dengan mengukur tingkat kesalahan ketiga algoritma tersebut melalui *Mean Squared Error* (MSE).

$$MSE=\frac{1}{N}\sum_{i=1}^{N} (y_i-y\\_pred_i)^2$$

di mana, nilai $N$ adalah jumlah *dataset*, nilai $y_i$ merupakan nilai sebenarnya, dan $y\\_pred$ yaitu nilai prediksinya.

Metode metrik *Mean Squared Error* (MSE) menawarkan keuntungan karena proses perhitungannya yang mudah dan konsepnya yang tidak rumit. Namun, metrik ini memiliki kekurangan, seperti tidak mampu memberikan perbandingan langsung antara hasil prediksi dan situasi nyata, yang dapat mengakibatkan akurasi prediksi yang tidak optimal.

```python
mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])
model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting}
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3
```

![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/55a480ec-22a7-4981-bf16-14476edbe6fb)

Dari data tabel tersebut dapat divisualisasikan pada grafik batang berikut.

![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/badefcd8-dba2-4baf-b9a5-4cdc64af7dbc)

Berdasarkan diagram yang ditampilkan, dapat diketahui:
1.   Algoritma *Random Forest* menghasilkan nilai *error* terendah.
2.   Algoritma *K-Nearest Neighbor* menunjukkan tingkat *error* yang berada di tengah-tengah dibandingkan dengan dua algoritma lain.
3.   Algoritma *Adaptive Boosting* memiliki tingkat *error* tertinggi.

Tahap selanjutnya adalah melakukan pengujian prediksi dengan menggunakan harga (*price*) dari data uji (*testing*)

![image](https://github.com/sandysan0/Dicoding-Predictive-Analytics/assets/144081667/10cf7573-5889-4cc9-be1b-c22dbbda09ae)

Dapat dilihat prediksi pada model dengan algoritma *K-Nearest Neighbor* memberikan hasi yang paling mendekati dengan nilai `y_true` jika dibandingkan dengan algoritma model yang lainnya.

Nilai `y_true` sebesar **26594.0** dan nilai prediksi `*K-Nearest Neighbor*` sebesar **24513.1**.

Meskipun diagram `MSE` menunjukan *Random Forest* memiliki error paling kecil dibanding algoritma lainnya, ketika dilakukan pengujian justru *K-Nearest Neighbor* menghasilkan prediksi yang lebih mendekati `y_true`.

---

## Referensi

[1] Kihm, A., Vance, C. (2016). "The determinants of equity transmission between the new and used car markets: a hedonic analysis." *J Oper Res Soc* 67, 1250–1258 . https://doi.org/10.1057/jors.2016.16

[2] Shen Gongqi, Wang Yansong, & Zhu Qiang. (2011). "New Model for Residual Value Prediction of the Used Car Based on BP Neural Network and Nonlinear Curve Fit." *2011 Third International Conference on Measuring Technology and Mechatronics Automation.* doi:10.1109/icmtma.2011.455 

[3] Andrews, T., & Benzing, C. (2006). "The Determinants of Price in Internet Auctions of Used Cars." *Atlantic Economic Journal,* 35(1), 43–57. doi:10.1007/s11293-006-9045-7 

[4] *What is the K-nearest neighbors algorithm?*. IBM. https://www.ibm.com/topics/knn 

[5] Hussein, S. (2022, February 23). *Mengenal K-nearest neighbor: Algoritma Populer untuk machine learning.* GEOSPASIALIS. https://geospasialis.com/k-nearest-neighbor/ 

[6] *What is Random Forest?*. IBM. https://www.ibm.com/topics/random-forest#:~:text=Random%20forest%20is%20a%20commonly,Decision%20trees 

[7] Wikimedia Foundation. (2024, March 6). *Random Forest*. Wikipedia. https://en.wikipedia.org/wiki/Random_forest 

[8] *AdaBoost algorithm in Machine Learning*. AlmaBetter. https://www.almabetter.com/bytes/tutorials/data-science/adaboost-algorithm 

[9] Wikimedia Foundation. (2024, March 6). *Adaboost*. Wikipedia. https://en.wikipedia.org/wiki/AdaBoost 
