Nama : Aufa Nurcahyo

NPM : 2506656500

Kelas : PBP D

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