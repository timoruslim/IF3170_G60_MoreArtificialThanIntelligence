# **Tujuan** {#tujuan}

Tugas Besar I pada kuliah IF3170 Intelegensi Buatan bertujuan agar peserta kuliah mendapatkan wawasan tentang bagaimana cara mengimplementasikan dan mengevaluasi algoritma-algoritma *local search* untuk menyelesaikan permasalahan berupa studi kasus yang relevan terhadap industri.

Pada tugas ini peserta akan merancang representasi solusi, mengimplementasikan beberapa varian algoritma *local search*, melakukan eksperimen, dan menganalisis hasilnya.

# 

# **Aturan** {#aturan}

Terdapat beberapa hal yang perlu diperhatikan dalam pengerjaan tugas ini:

1. Tugas besar dilaksanakan **secara berkelompok**. Pembagian kelompok ditentukan sendiri oleh mahasiswa dengan mengisi sheet kelompok [berikut ini](https://docs.google.com/spreadsheets/d/1wjVL9iONdI6qzymbOryo65dYNKeE_LCCH3-EJcOEPyw/edit?usp=sharing) dengan 1 kelompok terdiri dari **3 mahasiswa** yang dapat berasal dari lintas kelas. Batas waktu pengisian kelompok adalah **Jumat, 25 September 2026 pukul 23.59 WIB**. Silakan lihat instruksi lebih lanjut di *sheets* kelompok di atas.

2. **Utamakan implementasi yang mengacu pada salindia kuliah**. Apabila menggunakan atau mengadaptasi metode dari sumber di Internet, **sumber tersebut wajib dicantumkan** dalam bentuk komentar pada program serta referensinya pada laporan.

3. Jika terdapat hal yang kurang dipahami, peserta dapat mengajukan pertanyaan kepada asisten melalui **komentar pada Unggahan Tugas Besar di Teams**. Pertanyaan yang diajukan secara personal kepada asisten tidak akan dijawab untuk menghindari perbedaan informasi yang diterima.

4. Dilarang melakukan plagiarisme, meminta atau memberikan kode dan/atau laporan kepada kelompok lain, dan alasan penggunaan LLM tidak dapat diterima. Pelanggaran terhadap aturan ini akan mengakibatkan **pemberian nilai E** kepada seluruh anggota kelompok yang terlibat.

# ***Deliverables*** {#deliverables}

Berikut *deliverables* dalam pengerjaan tugas ini:

1. Untuk tugas ini, setiap kelompok diwajibkan menggunakan *version control system* Git dengan membuat *repository* pada GitHub (akun pribadi). Format penamaan *repository* adalah **IF3170\_GXX\_NamaKelompok**, dengan XX merupakan nomor kelompok yang terdapat pada [sheet kelompok](https://docs.google.com/spreadsheets/d/1wjVL9iONdI6qzymbOryo65dYNKeE_LCCH3-EJcOEPyw/edit?usp=sharing). *Repository* dapat bersifat *private* selama masa pengerjaan dan **wajib diubah menjadi *public*** sebelum pengumpulan agar dapat diakses oleh asisten.

2. Meskipun *commit* dan *development* tidak dinilai secara langsung, setiap kelompok diharapkan melakukan *commit* dan *branching* yang mengikuti *best practice*. Disarankan menggunakan [*semantic commit*](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716) agar kontribusi tiap anggota dapat terlihat dengan jelas.

3. *Repository* harus memiliki struktur sebagai berikut:  
- Folder **src**, digunakan untuk menyimpan *source code*.

- Folder **docs,** digunakan untuk menyimpan laporan dalam bentuk **.pdf** yang terdiri atas komponen berikut:

  * **Cover**  
  * **Deskripsi Persoalan**  
  * **Pembahasan** yang berisi penjelasan implementasi algoritma *local search* (berisi deskripsi fungsi/kelas beserta *source code*), hasil dan analisis eksperimen (disertai dengan visualisasi dari program yang telah dibuat)  
  * **Kesimpulan dan Saran**  
  * **Pembagian tugas** tiap anggota kelompok  
  * **Referensi**  
  * **Lampiran Form Penggunaan Generative AI** yang diisi dengan sejujur-jujurnya (Halaman 19 pada [Panduan AI ITB](https://drive.google.com/file/d/1sKEun1xTuK5UW8ktrkuZtVTU-1YRE-_n/view?usp=sharing)). Apabila terdapat indikasi kecurangan atau ketidakjujuran, maka akan **ditindaklanjuti sesuai hukum yang berlaku**.  
  * **Lampiran Lainnya** (bila ada)

- Folder **output**, digunakan untuk menyimpan hasil *run* algoritma.

- **README.md**, yang berisi deskripsi singkat *repository*, cara *setup* dan *run program*, dan pembagian tugas tiap anggota kelompok.

4. Pengumpulan dilakukan dengan membuat *release* dengan *tag* **vX.Y** pada *repository* yang telah dibuat sebelum *deadline*, dengan **X adalah nomor *milestone*** dan **Y adalah angka revisi** yang dimulai dari 0 untuk versi awal. Pastikan format *tag* sesuai ketentuan. Pengumpulan yang melewati *deadline* akan dikenakan **pengurangan nilai**.

# ***Timeline*** {#timeline}

# 

| No | Waktu | Kegiatan |
| :---: | ----- | ----- |
| 1 | Senin, 21 September 2026 | Rilis Tugas Besar I IF3170|
| 2 | Jumat, 25 September 2026 | Batas pengisian daftar kelompok. |
| 3 | Senin, 19 Oktober 2026 | Pengumpulan *final deliverables* tugas besar pada platform Edunex. |
| 4 | \[Menyusul\] | Batas pengisian jadwal demo tugas besar. |
| 5 | \[Menyusul\] | Pelaksanaan demo tugas besar. |

# 

# **Deskripsi** {#deskripsi}

![][image1]

Gambar 1\. Special Week, driver truk handal (Sumber: [真夏の银堡垒🐴C108土曜日 東地区 ホ-10a on X](https://x.com/Drift_in_/status/1381525587844460545))

Keluarga **Mejiro** sedang berencana mengekspansi bisnisnya ke bidang logistik darat dan ingin melakukan uji coba berskala kecil terlebih dahulu untuk torasen. Sebagai teman yang baik, **Mejiro McQueen** menawarkan posisi driver truk ujicoba kepada **Special Week**, karena sudah sering menyetir truk di kampung halamannya di Hokkaido. Usaha baru ini bernama **Mejiro Express** dengan slogan “Lebih kilat dari Umamusume”.

Karena **Special Week** sibuk berlatih untuk memenangkan lomba-lombanya, dia tidak bisa membuang waktu berlama-lama untuk menentukan pengaturan pengiriman yang optimal. Oleh karena itu, dia meminta kalian, toreena-toreena yang pintar dalam keinformatikawan, untuk membuat suatu program yang cerdas untuk menolongnya.

# **Spesifikasi**  {#spesifikasi}

Tugas ini bertujuan untuk membuat konfigurasi pengisian paket paling optimal untuk sebuah truk peti kemas. Optimal disini berarti **memaksimalkan** fungsi objektif.

## **Daftar Variabel Permasalahan** {#daftar-variabel-permasalahan}

| Entitas | Atribut | Contoh | Keterangan |
| :---- | :---- | :---- | :---- |
| Package | id | “RusdiPackage” | *Identifier* |
|  | Dimensions | {w:3, l:4, h:1} | Ukuran sebuah paket, yaitu *width*, *length*, dan *height* |
|  | Orientation | {w:x, l:y, h:z} | Sumbu yang sejajar dengan setiap sisi paket. Terdapat enam kemungkinan orientasi, misalnya {w:y, l:x, h:z} setelah rotasi 90° terhadap sumbu *z*. |
|  | Value | 60 | Nilai harga sebuah paket (satuan unit) |
|  | Weight | 5 | Berat paket (satuan unit berat) |
|  | IsFragile | False | Benda pecah-belah |
|  | ETA | 3 | [Estimated Time of Arrival](https://www.shippeo.com/resources/explore/blog-newsletter/eta-meaning-in-business-a-critical-metric-for-supply-chain-success), perkiraan waktu kedatangan paket (dalam sisa hari) |
| Truck | Dimensions | {w:10, l:20, h:5} | Ukuran sebuah peti kemas pada truk, yaitu *width*, *length*, dan *height* |
|  | MaxCapacity | 500 | Kapasitas angkut maksimum pada suatu peti kemas (satuan unit berat) |

### 

## **Ketentuan Representasi** {#ketentuan-representasi}

Berikut prosedur bagaimana dalam merepresentasikan permasalahan ini:

* Paket hanya berbentuk kubus / balok. Paket dapat berbeda ukuran satu sama lain dan tidak semua harus dimasukkan ke dalam peti kemas pada truk sehingga suatu paket dapat berada di luar **(seluruh bagian paket di luar)**

* Koordinat berupa bilangan bulat. Cara representasi koordinat dibebaskan.

* Struktur data yang digunakan untuk representasi dibebaskan. Misalnya menggunakan *key-value* seperti JSON.

* Inisialisasi (***initial state***) random.

* Langkah neighbor (***move***) yang diperbolehkan tiap iterasi:

1. Menukar dua paket, baik di dalam maupun di luar truk  
2. Memindahkan sebuah paket ke suatu koordinat yang berbeda  
3. Merotasi paket 90° terhadap sumbu *x*, *y*, atau *z*

* Representasi solusi (***final state***) adalah pemetaan semua paket yang ada dan juga pemetaan semua koordinat dalam peti kemas pada truk. Secara detail yang harus dapat ditunjukkan oleh state dan visualisasi adalah:

  1. Bagaimana keadaan semua paket yang di dalam maupun yang di luar  
  2. Bagaimana keadaan peti kemas pada truk  
  3. *Value* pada *state* tersebut

## **Objective Function & Constraints** {#objective-function-&-constraints}

Agar permasalahan ini tidak menjadi kompleks, berikut arahan yang diberikan

* **Objective function**   
  Permasalahan ini bertujuan untuk memaksimalkan *value* peti kemas pada truk.

* **Kardus tidak bisa melayang dan menembus dinding peti kemas**  
  Melayang disini didefinisikan dengan misalkan paket $i$ setelah orientasi tertentu memiliki posisi sudut kiri-bawah-belakang  

  $({x}_{i}\ ,{y}_{i}\ ,{z}_{i})$ 

  dan dimensi

   $({w}_{i}\ ,{d}_{i}\ ,{h}_{i})$

  sehingga alas paket $i$ adalah

  ${B}_{i}\ =\ \{(x,y,{z}_{i})\ |\ {x}_{i}\ \leq \ x\ <\ {x}_{i}+{w}_{i},\ {y}_{i}\ \leq \ y\ <\ {y}_{i}+{d}_{i}\ \}){\ }$

	Sebuah titik di alas memiliki *support* apabila:

1. ${Z}_{i\ =\ 0}$, artinya di alas truk, atau  
2. Terdapat paket lain $j$ yang mempunyai bagian atas tepat di bawah titik tersebut

   Maka melayang adalah kondisi tidak ada satupun titik alas yang memiliki support.

* **Barang pecah-belah tidak boleh di bawah paket lain**

  Barang pecah-belah tidak boleh menjadi *support*

* **Truk tidak boleh mengangkut melebihi kapasitasnya**

# **Cakupan** {#cakupan}

Anda akan diminta untuk mengimplementasikan rencana yang telah Anda buat pada Tugas Besar 1\. Berikut merupakan hal-hal yang perlu dilakukan oleh setiap kelompok.

Implementasikan 3 algoritma *local search* dengan rincian sebagai berikut:

1. Salah satu algoritma Hill-climbing  
2. Simulated Annealing  
3. Genetic Algorithm

Jalankan setiap algoritma (selain Genetic Algorithm) sebanyak **3 kali**, kemudian catat beberapa hal berikut:

1. Berlaku untuk semua algoritma  
   1. *State* awal dan akhir  
   2. Nilai *objective function* akhir yang dicapai  
   3. Plot nilai *objective function* terhadap banyak iterasi yang telah dilewati  
   4. Durasi proses pencarian

2. Berlaku hanya untuk Steepest Ascent Hill-Climbing dan Stochastic Hill-climbing  
   1. Banyak iterasi hingga proses pencarian berhenti

3. Berlaku hanya untuk Hill-Climbing with Sideways Move  
   1. Banyak iterasi hingga proses pencarian berhenti  
   2. Tambahkan parameter ***maximum sideways move***, dimana ketika banyak *sideways move* yang dilakukan sudah mencapai maksimum, pencarian dihentikan

4. Berlaku hanya untuk Random Restart Hill-climbing  
   1. Banyak *restart*  
   2. Banyak iterasi per *restart*  
   3. Tambahkan parameter ***maximum restart***, dimana ketika banyak *restart* sudah mencapai maksimum, pencarian dihentikan.

5. Berlaku hanya untuk Simulated Annealing  
   1. Plot ${e}^{\frac{\Delta E}{T}}$ terhadap banyak iterasi yang telah dilewati  
   2. Frekuensi ‘*stuck*’ di *local optima*

Khusus untuk Genetic Algorithm, lakukan beberapa hal berikut:

1. Terdapat 2 parameter yang dapat diubah, yaitu **jumlah populasi** dan **banyak iterasi.**

2. Jadikan jumlah populasi sebagai kontrol, kemudian pilih **3 variasi** banyak iterasi yang berbeda. Jalankan program sebanyak masing-masing **3 kali** untuk setiap konfigurasi parameter.

3. Jadikan banyak iterasi sebagai kontrol, kemudian pilih **3 variasi** jumlah populasi yang berbeda. Jalankan program sebanyak masing-masing **3 kali** untuk setiap konfigurasi parameter.

4. Untuk setiap eksperimen, catat beberapa hal berikut:  
   1. *State* awal dan akhir  
   2. Nilai *objective function* akhir yang dicapai  
   3. Plot nilai *objective function* terhadap banyak iterasi yang telah dilewati (Cukup plot nilai *objective function* maksimum dan rata-rata dari populasi terhadap banyak iterasi yang telah dilewati.) 
   4. Jumlah populasi  
   5. Banyak iterasi  
   6. Durasi proses pencarian

Lakukan analisis terhadap hasil eksperimen, berikut merupakan beberapa pertanyaan yang dapat menjadi acuan untuk analisis yang Anda lakukan:

1. Seberapa dekat tiap-tiap algoritma bisa mendekati *global optima* dan mengapa hasilnya demikian? 

2. Bagaimana perbandingan hasil pencarian tiap-tiap algoritma dengan algoritma *local search* yang lain?

3. Bagaimana perbandingan durasi proses pencarian tiap algoritma relatif terhadap algoritma lainnya?

4. Seberapa konsisten hasil akhir yang didapatkan dari tiap-tiap eksperimen yang dilakukan?

5. Bagaimana pengaruh banyak iterasi dan jumlah populasi terhadap hasil akhir pencarian pada Genetic Algorithm?

6. dst…

Anda boleh mengganti dan/atau menambahkan beberapa pertanyaan jika dirasa perlu untuk memudahkan penjelasan.

Program yang dibuat harus bisa **memvisualisasikan** *initial state*, *final state* dan juga hasil eksperimennya (sesuaikan informasi hasil eksperimen yang ditampilkan dengan ketentuan yang telah dijelaskan di poin sebelum ini).

Gunakan bahasa **Python dalam implementasi *local search*.** Semua bahasa dan *library* boleh digunakan untuk **visualisasi** (misalnya ingin *web based*). Cara visualisasi tidak memengaruhi penilaian dan dibebaskan kepada masing-masing kelompok sedemikian rupa untuk memudahkan penjelasan saat demo nanti.

Diperbolehkan untuk menggunakan heuristik yang Anda buat sendiri atau dari referensi lain untuk optimasi pencarian solusi, asalkan masih dalam lingkup *local search*. Jelaskan *heuristik* yang Anda pakai di laporan.

# 

# **Bonus** {#bonus}

Hanya kerjakan spesifikasi ini jika Anda sudah menyelesaikan seluruh spesifikasi wajib. Berikut merupakan beberapa spesifikasi bonus yang dapat Anda kerjakan:

1. Buatlah ***objective function*** selain yang telah didefinisikan, **tanpa menambah variabel yang ada**. (3 poin)

2. Buatlah implementasi untuk **seluruh algoritma Hill-climbing** yang ada.  
   (7 poin)

3. **Multi-truk**. Program dapat menerima jumlah truk lebih dari satu dan memaksimalkan *value* **total** yang diangkut armada. (10 poin)