Nama : Aufa Nurcahyo
Kelas : PBP D
NPM : 2506656500


## Deskripsi Proyek

MyPortfolio merupakan website portofolio pribadi yang dikembangkan menggunakan Django sebagai bagian dari mata kuliah Pemrograman Berbasis Platform (PBP) Universitas Indonesia.

Website ini menampilkan profil pribadi, pengalaman organisasi dan kepanitiaan (Experience), serta riwayat pendidikan (Education). Pengguna dapat melakukan registrasi, login, memberikan star, dan mengakses fitur pengelolaan data sesuai hak akses masing-masing.

Pada **Individual Assignment 6**, fitur Education dikembangkan menggunakan Django REST Framework (DRF). Implementasinya mencakup serializer untuk validasi data, REST API untuk operasi CRUD, permission berdasarkan peran pengguna, serta integrasi Fetch API untuk melakukan pencarian dan pengelolaan data tanpa me-reload seluruh halaman.

Website juga menggunakan desain responsif dengan dukungan light mode, dark mode, serta animasi CSS.

## Teknologi yang Digunakan

- **Backend:** Python, Django, Django REST Framework
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (pengembangan lokal)
- **API:** REST API, Fetch API (AJAX)
- **Authentication:** Django SessionAuthentication
- **Testing:** Django TestCase dan DRF APITestCase

## Cara Menjalankan Proyek

**1. Buka direktori proyek**

Buka terminal pada folder yang berisi `manage.py`.

**2. Buat dan aktifkan virtual environment**

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

**3. Instal dependencies**

```powershell
pip install -r requirements.txt
```

**4. Jalankan migrasi database**

```powershell
python manage.py migrate
```

**5. Buat akun superuser (opsional)**

```powershell
python manage.py createsuperuser
```

**6. Jalankan server Django**

```powershell
python manage.py runserver
```

Website dapat diakses melalui `http://127.0.0.1:8000/`.

**7. Jalankan pengujian**

```powershell
python manage.py test main
```

## Endpoint Utama

- `/` — Halaman profil
- `/experience/` — Halaman pengalaman
- `/education/` — Halaman pendidikan
- `/admin/` — Django Admin
- `/api/v1/education/` — REST API Education
- `/api/v1/education/<uuid>/` — Detail, update, dan delete Education
- `/api/v1/education/<uuid>/star/` — Memberikan atau membatalkan star

## Perkembangan Proyek

Proyek dikembangkan secara bertahap melalui rangkaian tutorial dan tugas PBP. Pengembangan awal berfokus pada struktur HTML, styling CSS, Django MVT, model database, form, serta autentikasi.

Pengembangan berikutnya menambahkan interaktivitas menggunakan AJAX dan Fetch API. Pada Tugas 6, fitur Education diintegrasikan dengan Django REST Framework, lengkap dengan validasi serializer, permission, CSRF, dan pengujian API.

Tugas 1
1. Ya saya menerapkan elemen semantik HTML 5, khususnya penggunaan section dan article, section membantu membagi halaman menjadi lebih mudah dipahami seperti id="experience", sehingga langsung dapat masuk ke interface. Penggunaan article sendiri agar setiap daftar experience adalah informasi yang independen dan bisa terpisah dari halaman utamanya. Tetapi saya tidak menggunakan aside karena desain saya belum menggunakan sidebar dan semacamnya

2. Tantangan tata letak utama yang saya hadapi adalah menjaga konsistensi visual antara hero section bawaan template dengan section experience yang baru ditambahkan. Awalnya, kode CSS untuk section pengalaman ini saya hasilkan melalui bantuan AI dengan CSS Grid. Namun, saya tidak langsung menerimanya begitu saja. Saya melakukan eksplorasi mandiri terhadap cara kerja responsive layout tersebut dan membandingkannya dengan pendekatan bawaan template.

Dari eksplorasi tersebut, ada beberapa hal yang saya pelajari dan evaluasi:
- Eksplor CSS Grid: CSS yang disarakan AI yaitu memanfaatkan properti `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` Selanjutnya saat saya pelajari lebih lanjut, ternyata lebih fleksibel untuk masing masing ukuran layar device dan juga lebih efisiensi karena harus menuliskan banyak aturan-aturan terpisah untuk masing-masing device.

- Pading dan overflow: Saya sempat mencoba mengubah nilai padding dan ukuran gap antar kartu untuk melihat batas tampilan di layar kecil. Saya semisal ukuran padding luar tidak boleh bertabrakan dengan class `.container` bawaan template agar batas tepi tetap sejajar dari atas ke bawah.

- Prioritas Alur Baca di Mobile: Pada Experience, prioritasnya adalah kemudahan untuk baca kartu, di mana saya melihat bahwa kartu tidak boleh terlalu padat secara vertikal agar pengguna ponsel tetap nyaman melakukan scrolling.

3. Batasan yang paling terasa adalah semuanya harus hardcode. Saat menambahkan section baru, setiap data harus saya copas manual pada struktur tag. Jika experiencenya banyak maka dokumen HTMLnya akan semakin numpuk, rawan human error, dan tidak efisien untuk maintainance.

Penyelesaian dari hal tersebut adalah saya ingin persiapkan pada proyek selanjutnya saat materi database dan arsitektur MVT diperkenalkan meliputi kaya model pemisahan data dan tampilan ataupun pengelolaan konten yang terpusat.

AI DISCLOSURE
Tools : Gemini
- Bantuan Penuh AI: Styling CSS untuk section pengalaman baru `.experience-section`, layout grid `.experience-list`, serta kartu `article`.

- Konsultasi dengan AI: Panduan memilih kode hex warna kontras untuk elemen `<dt>` dan `<dd>`, penjelasan properti CSS positioning penggunaan icon.

- Pengerjaan Mandiri:Pembuatan markup HTML secara semantik (`<section>`, `<article>`, `<ul>`, `<li>`), serta penyesuaian variabel CSS agar menyatu dengan template.

Ringkasan log prompting : 
- Modifikasi Ikon Sosial Media: Meminta panduan untuk mengganti teks tautan GitHub, LinkedIn, dan Email menjadi logo interaktif menggunakan Font Awesome via CDN.

- Pemahaman CSS: Bertanya tentang perbedaan rem dan px, serta menanyakan format penulisan kode hex untuk warna transparan agar bisa diintegrasikan ke dalam variabel :root bawaan template.

- Struktur Semantik HTML5: Meminta penjelasan mengenai fungsi berbagai tag HTML seperti <div>, <dl>, <dt>, <dd>, <article>, <ul>, <li>, dan <span> untuk merancang section Experience yang sesuai standar semantik.

- Implementasi Layout: Berdiskusi tentang cara kerja navigasi otomatis menggunakan id atau class, serta meminta bantuan penyusunan struktur experience berbasis card layout.

- Responsivitas CSS Grid: Meminta bantuan menyusun kode CSS untuk kerangka HTML experience yang sudah dibuat, dilanjutkan dengan diskusi pendalaman secara kritis mengenai alasan dan fungsi penggunaan grid-template-columns: repeat(auto-fit, minmax()) dibandingkan dengan media query manual.

- Smooth scrolling

- Pembuatan navbar dan teks span rata kanan

Keterbatasan AI: 
- Awalnya AI membuat kode CSS yang menggunakan nilai warna hardcoded yang kemudian saya ganti dengan memasukkan warna tersebut ke dalam root dan diubah menajdi variabel

- AI menyuruh untuk membuat gridtemplate yang auto fit, namun setelah saya pertimbangkan hal ini ternyata membuat reader sulit untuk membaca karena ukuran cardnya terlalu kecil. Akhirnya saya ubah ukuran cardnya menjadi full width

Berikut adalah link chat AI nya : https://share.gemini.google/ZDLm3tnEJD9C



TUGAS 2
1.
- Client Request: Pengguna mengetik atau mengklik tautan halaman baru di browser, yang mengirimkan permintaan HTTP GET ke server web Django.
- `portofolio/urls.py` :Permintaan di acc oleh konfigurasi URL. Di sini, rute awal dicocokkan dengan menggunakan fungsi `include('main.urls')`, kemudian dilakukan pemrosesan rute yang tersisa ke tingkat aplikasi `main`.
- `main/urls.py`:Konfigurasi URL aplikasi spesifik (`'education/'`) dengan named route (`name='show_education'`) menuju fungsi control yang bersangkutan di `views.py`.
- `main/views.py`: `show_education` bertindak sebagai logika bisnis. View mengeksekusi kueri ORM ke basis data melalui model dan membungkus data tersebut
- `main/models.py`: Model `Education` merepresentasikan struktur tabel basis data di SQLite. Melalui Django ORM (`Education.objects.all()`), model mengeksekusi kueri SQL untuk mengambil seluruh baris data objek riwayat pendidikan dan mengembalikannya sebagai QuerySet.
- Template (`education.html`): View memanggil fungsi `render()` dengan memberikan data konteks ke berkas template HTML. kemudian django mengolah dengan melakukan iterasi data dengan `{% for %}`, mengecek kondisi kosong dengan `{% empty %}`, serta memasukkan variabel konteks.
- HTTP Response:Berkas HTML yang telah terisi data dinamis dikembalikan ke browser pengguna sebagai respons HTTP (status code 200 OK) untuk ditampilkan seutuhnya.

2.
- Memisahkan data dengan tampilan visual antarmuka secara bersih.
- Data dapat ditambah, diubah, atau dihapus langsung lewat Django Admin tanpa menyentuh kode HTML atau deploy ulang.
- Skema dan tipe data tervalidasi oleh model, serta data tersebut dapat digunakan ulang untuk kebutuhan rute lain (seperti API/JSON).

3.
- `makemigrations`: Mendeteksi perubahan pada `models.py` dan membuat berkas skrip migrasi baru.
- `migrate`: Menerapkan skrip migrasi tersebut ke basis data.
- Contoh: Menambahkan atribut baru `tes = models.FloatField()` pada class `Education` membutuhkan `makemigrations` untuk membuat berkas migrasinya, lalu `migrate` agar tabel di SQLite diperbarui.

AI Disclosure
- Tool: Gemini (Google).
- Menanyakan cara-cara untuk menginput data model langsung selain dari terminal.
- Mengubah struktur di `education.html` dan `experience.html`
- Membantu memberikan solusi terkait struktur HTML
Link AI: https://share.gemini.google/oB6Ks6rkewGH


TUGAS 3

Pertanyaan Reflektif
1.
   - Model form dapat menghemat waktu karena Django otomatis mengatur tipe field di database ke form HTML lengkap dengan validasi bawaan. Hal ini juga mencegah redudansi kode.
   - csrf_token ditambahkan untuk menghindari Cross-Site Request Forgery (CSRF). Token ini memastikan setiap request `POST` yang masuk adalah user sah dari aplikasi kita bukan pengguna dari third party yang menggunakan request palsu.

2. 
   - JSON lebih ringkas, tidak membutuhkan tag penutup berulang seperti XML, jadi ukuran datanya kecil dan transfer data ke jaringan bisa lebih cepat. Selain itu key-value JSON kompatibel dengan JavaScript dan mudah di terima oleh framework frontend baru.

3. 
   - Alur: Klien mengirim HTTP GET request ke endpoint API -> view memanggil model untuk query data dari database -> Objek `QuerySet` yang didapat diubah ke bentuk format teks JSON menggunakan serializer bawaan Django -> Data JSON dikembalikan dalam objek `HttpResponse` dengan header `application/json`.
   - Peran Serialization: Data dari database berupa objek Python sangat kompleks dan juga klien tidak mengerti tipe data internal Python. Serialization diperlukan untuk menerjemahkan objek tersebut menjadi format string standar agar bisa dipahami oleh berbagai platform.

AI Disclosure
Tools AI yang Digunakan: Gemini 
Bagian yang Dibantu:
  - Penyesuaian template di web pbp dengan model yang sudah saya buat
  - Penyesuaian ModelForm menggunakan parameter instance pada fungsi edit/update.
Perbaikan Manual:
  - Kode awal sempat mengalami error `TemplateSyntaxError` karena adanya komentar HTML sebelum tag `{% extends 'base.html' %}`. Perbaikan dilakukan secara manual dengan memastikan `{% extends %}` ditaruh persis di baris pertama file.
  -  Error lagi dimana `TemplateDoesNotExist` pada komponen modal hapus karena letak path yang belum sesuai. 

Tugas 4
AI Disclosure
Tools AI yang Digunakan: Gemini 
- toggle_star belum connect
- invalid block tag'empty pada education.html
- menanyakan cara mengganti color sebuah class


Tugas 5
- Debouncing adalah teknik untuk membatasi seberapa sering suatu fungsi dijalankan. Fungsi ini menunda eksekusi sampai pengguna berhenti melakukan aksi tertentu selama durasi waktu tertentu.
- Fungsi await adalah menahan eksekusi kode berikutnya sampai proses fetch() selesai menerima respon dari server. Jika tidak menggunakan await, variabel hanya akan berisi objek Promise berstatus pending (bukan data asli), sehingga kode yang mencoba mengolah data tersebut akan error.
- XSS adalah serangan dengan menyisipkan script berbahaya ke dalam data aplikasi agar dieksekusi oleh browser pengguna lain. AJAX/JavaScript lebih rentan karena tidak memiliki pengaman otomatis saat menyisipkan HTML (misal via innerHTML), sedangkan template Django secara default memiliki fitur Auto-escaping yang otomatis mengubah karakter berbahaya menjadi teks biasa.

AI Disclosure

Pada Tugas 5 ini, saya menggunakan Google Gemini sebagai asisten debugging.

- Strategi Prompting: Mengirimkan potongan kode modal, fetch, dan views untuk mengecek bug serta validasi keamanan.

- Bagian yang Dibantu: Validasi strip_tags pada forms.py, pengecekan ID form HTML, dan konfirmasi jaringan debouncing.

- Keterbatasan AI: AI sempat memberikan penempatan indentasi fungsi clean_field yang keliru (di dalam class Meta).

- Perbaikan Manual: Memperbaiki indentasi fungsi clean_field di luar class Meta, menghapus event listener ganda pada form, dan melakukan tes input script XSS manual.

Tugas 6
- REST adalah gaya arsitektur untuk membangun web API dengan menggunakan data sebagai resource yang dapat diakases melalui URL. Dalam REST, HTTP method digunakan untuk menentukan operasi terhadap resource,  GET, POST, PUT, PATCH, dan DELETE. Mengembalikan JSON saja belum cukup disebut RESTful karena JSON hanya format data, sedangkan REST juga memperhatikan struktur resource, penggunaan HTTP method, status response, dan prinsip stateless. PUT digunakan untuk mengganti representasi data secara keseluruhan, misalnya memperbarui seluruh informasi Education, sedangkan PATCH digunakan untuk mengubah sebagian field saja, seperti mengganti nama institusi tanpa mengubah informasi lainnya.

- Serializer pada Django REST Framework berfungsi mengubah objek model menjadi data yang dapat dikirim melalui API serta memvalidasi input sebelum disimpan ke database. Pada proyek saya, EducationSerializer digunakan untuk menentukan field Education yang ditampilkan, membersihkan input dengan strip_tags, serta menghitung informasi Star menggunakan SerializerMethodField. Dibandingkan membuat dictionary secara manual dengan JsonResponse seperti Tutorial 05, serializer membuat kode lebih ringkas, terstruktur, mudah dipelihara, dan memiliki validasi yang dapat digunakan kembali.

- Autentikasi merupakan proses mengenali identitas pengguna, sedangkan otorisasi menentukan tindakan yang boleh dilakukan pengguna tersebut. Pada proyek saya, SessionAuthentication digunakan untuk mengenali pengguna yang login, sedangkan IsPortfolioOwnerOrEditorOrReadOnly mengatur akses berdasarkan peran, seperti pengunjung, pengguna biasa, Editor, dan Superuser. Permission harus diperiksa di server karena menyembunyikan tombol pada template tidak mencegah pengguna mengakses endpoint API secara langsung. Dengan permission class, request tanpa izin dapat ditolak menggunakan HTTP 403.

- API yang menggunakan SessionAuthentication tetap memerlukan token CSRF untuk request seperti POST, PUT, PATCH, dan DELETE karena browser dapat mengirim cookie session secara otomatis sehingga berpotensi disalahgunakan melalui serangan CSRF. Pada proyek saya, token dikirim melalui header X-CSRFToken pada Fetch API. Pengujian force_authenticate() tidak cukup untuk membuktikan perlindungan CSRF karena melewati proses autentikasi session yang sebenarnya. Oleh karena itu, saya menggunakan APIClient(enforce_csrf_checks=True) dan client.login() untuk memastikan request tanpa token ditolak dengan HTTP 403, sedangkan request dengan token valid dapat diproses.

AI Disclosure – Tugas 6

Pada Tugas 6, saya menggunakan ChatGPT (OpenAI) sebagai asisten implementasi dan debugging Django REST Framework.

Strategi Prompting: Mengirimkan modul, potongan kode, dan hasil pengujian untuk mengevaluasi implementasi API.

Bagian yang Dibantu: Integrasi PATCH pada education_form.html, CSRF token, error handling, serta pemeriksaan serializer dan permission.

Keterbatasan AI: AI tidak selalu mengetahui kondisi terbaru proyek sehingga beberapa saran perlu disesuaikan.

Perbaikan Manual: Menyesuaikan kode dengan struktur Education, memeriksa hasil API, serta menjalankan pengujian Django secara mandiri