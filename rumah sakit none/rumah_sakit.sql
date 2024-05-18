
CREATE TABLE `doctor` (
  `Id_Doctor` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Specialty` varchar(50) NOT NULL,
  `Jam` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `doctor` (`Id_Doctor`, `Name`, `Specialty`, `Jam`) VALUES
('ID003', 'dr.Ricky', 'umum', ' 08.00-12.'),
('ID006', 'dr.Kevin', 'umum', ' 08.00-12.'),
('ID009', 'dr.Ikhlas', 'poligigi', '08.00-12.0'),
('ID012', 'dr.Nur', 'penyakit dalam', '08.00-12.0'),
('ID015', 'dr.Erma', 'kandungan', ' 8.00-12.0');

CREATE TABLE `obat` (
  `id_product` varchar(50) NOT NULL,
  `nama_product` varchar(50) NOT NULL,
  `manfaat_obat` varchar(50) NOT NULL,
  `cara_penggunaan` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `obat` (`id_product`, `nama_product`, `manfaat_obat`, `cara_penggunaan`) VALUES
('12', 'Panadol', 'Test\n', 'Test\n'),
('48', 'Plossa', 'Press & Soothe Aromatics', 'Gosokkan pada bagian yang terasa pegal'),
('55', 'Dermatix', 'Sudah di edit', 'Diterapkan pada permukaan kulit bersih dua kali se');

CREATE TABLE `pasien` (
  `ID` varchar(10) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Age` varchar(10) NOT NULL,
  `Sex` varchar(10) NOT NULL,
  `Blood Type` varchar(30) NOT NULL,
  `Condition` varchar(30) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `pasien` (`ID`, `Name`, `Age`, `Sex`, `Blood Type`, `Condition`, `Status`) VALUES
('0001', 'Kevin', '19', 'Male', 'O', 'Fever', 'Belum Sembuh'),
('0002', 'James', '26', 'Male', 'B-', 'Hepatitis', 'Belum Sembuh'),
('0003', 'Natalie', '34', 'Female', 'A+', 'Pneumonia', 'Sudah Sembuh');

CREATE TABLE `ruangan` (
  `kode` varchar(50) NOT NULL,
  `Jenis` varchar(50) NOT NULL,
  `Kapasitas` varchar(50) NOT NULL,
  `Status` varchar(50) NOT NULL,
  `Biaya` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `ruangan` (`kode`, `Jenis`, `Kapasitas`, `Status`, `Biaya`) VALUES
('124', 'Poli Mata', '154', 'Penuh', '1000000');

ALTER TABLE `doctor`
  ADD PRIMARY KEY (`Id_Doctor`);

ALTER TABLE `obat`
  ADD PRIMARY KEY (`id_product`);

ALTER TABLE `pasien`
  ADD PRIMARY KEY (`ID`);

ALTER TABLE `ruangan`
  ADD PRIMARY KEY (`kode`);
COMMIT;


