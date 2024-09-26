--* soal 4 a
SELECT *
FROM barang
WHERE harga > 10000
ORDER BY harga ASC;
--* soal 4 b
SELECT *
FROM pelanggan
WHERE nama LIKE '%g%'
    AND alamat = 'BANDUNG';
--* soal 4 c
SELECT t.kode AS KODE,
    t.tanggal AS TANGGAL,
    p.nama AS NAMA_PELANGGAN,
    b.nama AS NAMA_BARANG,
    t.jumlah_barang AS JUMLAH,
    b.harga AS HARGA_SATUAN,
    t.jumlah_barang * b.harga AS TOTAL
FROM transaksi t
    INNER JOIN pelanggan p ON t.kode_pelanggan = p.kode
    INNER JOIN barang b ON t.kode_barang = b.kode
ORDER BY p.nama,
    b.nama;
--* soal 4 d
SELECT p.nama AS NAMA_PELANGGAN,
    SUM(t.jumlah_barang) AS JUMLAH,
    SUM(t.jumlah_barang * b.harga) AS TOTAL_HARGA
FROM transaksi t
    INNER JOIN pelanggan p ON t.kode_pelanggan = p.kode
    INNER JOIN barang b ON t.kode_barang = b.kode
GROUP BY p.nama;