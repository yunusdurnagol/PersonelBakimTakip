/*==============================================================
  Personel ve Bakım Yönetim Sistemi
  database_v2.sql
  Bölüm 1
  PostgreSQL 17
==============================================================*/

CREATE EXTENSION IF NOT EXISTS pgcrypto;

--==============================================================
-- UPDATED_AT TRIGGER
--==============================================================

CREATE OR REPLACE FUNCTION fn_update_timestamp()
RETURNS TRIGGER
LANGUAGE plpgsql
AS
$$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$;

--==============================================================
-- POZİSYONLAR
--==============================================================

CREATE TABLE pozisyonlar
(
    id              BIGSERIAL PRIMARY KEY,

    ad              VARCHAR(100) NOT NULL,

    aciklama        TEXT,

    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted      BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at      TIMESTAMP,

    CONSTRAINT uq_pozisyonlar_ad
        UNIQUE(ad)
);

CREATE TRIGGER trg_pozisyonlar_updated_at

BEFORE UPDATE

ON pozisyonlar

FOR EACH ROW

EXECUTE FUNCTION fn_update_timestamp();

--==============================================================
-- PERSONELLER
--==============================================================

CREATE TABLE personeller
(

    id BIGSERIAL PRIMARY KEY,

    sicil_no VARCHAR(20) NOT NULL,

    tc_kimlik_no VARCHAR(11),

    ad VARCHAR(100) NOT NULL,

    soyad VARCHAR(100) NOT NULL,

    dogum_tarihi DATE,

    dogum_yeri VARCHAR(100),

    cinsiyet VARCHAR(20),

    pozisyon_id BIGINT NOT NULL,

    egitim_durumu VARCHAR(100),

    medeni_durum VARCHAR(20),

    telefon VARCHAR(30),

    email VARCHAR(150),

    adres TEXT,

    fotograf VARCHAR(500),

    ise_giris_tarihi DATE NOT NULL,

    izin_hakki SMALLINT NOT NULL,

    kan_grubu VARCHAR(5),

    acil_durum_kisi VARCHAR(150),

    acil_durum_telefon VARCHAR(30),

    aktif_mi BOOLEAN NOT NULL DEFAULT TRUE,

    aciklama TEXT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at TIMESTAMP,

    CONSTRAINT uq_personeller_sicil_no
        UNIQUE(sicil_no),

    CONSTRAINT uq_personeller_tc
        UNIQUE(tc_kimlik_no),

    CONSTRAINT fk_personeller_pozisyon
        FOREIGN KEY (pozisyon_id)
        REFERENCES pozisyonlar(id),

    CONSTRAINT chk_personeller_cinsiyet
        CHECK
        (
            cinsiyet IS NULL
            OR
            cinsiyet IN ('Erkek','Kadın')
        ),

    CONSTRAINT chk_personeller_medeni_durum
        CHECK
        (
            medeni_durum IS NULL
            OR
            medeni_durum IN ('Bekar','Evli')
        ),

    CONSTRAINT chk_personeller_izin
        CHECK
        (
            izin_hakki IN (14,20)
        )

);

CREATE TRIGGER trg_personeller_updated_at

BEFORE UPDATE

ON personeller

FOR EACH ROW

EXECUTE FUNCTION fn_update_timestamp();

--==============================================================
-- PERSONEL EVRAKLARI
--==============================================================

CREATE TABLE personel_evraklari
(

    id BIGSERIAL PRIMARY KEY,

    personel_id BIGINT NOT NULL,

    evrak_adi VARCHAR(200) NOT NULL,

    evrak_tipi VARCHAR(20),

    dosya_adi VARCHAR(255),

    dosya_yolu VARCHAR(500),

    aciklama TEXT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at TIMESTAMP,

    CONSTRAINT fk_personel_evraklari_personel

        FOREIGN KEY(personel_id)

        REFERENCES personeller(id)

        ON DELETE CASCADE

);

CREATE TRIGGER trg_personel_evraklari_updated_at

BEFORE UPDATE

ON personel_evraklari

FOR EACH ROW

EXECUTE FUNCTION fn_update_timestamp();

--==============================================================
-- PERSONEL İZİNLERİ
--==============================================================

CREATE TABLE personel_izinleri
(

    id BIGSERIAL PRIMARY KEY,

    personel_id BIGINT NOT NULL,

    baslangic_tarihi DATE NOT NULL,

    bitis_tarihi DATE NOT NULL,

    gun_sayisi INTEGER NOT NULL,

    aciklama TEXT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at TIMESTAMP,

    CONSTRAINT fk_personel_izinleri_personel

        FOREIGN KEY(personel_id)

        REFERENCES personeller(id)

        ON DELETE CASCADE,

    CONSTRAINT chk_personel_izinleri_gun

        CHECK(gun_sayisi>0)

);

CREATE TRIGGER trg_personel_izinleri_updated_at

BEFORE UPDATE

ON personel_izinleri

FOR EACH ROW

EXECUTE FUNCTION fn_update_timestamp();
/*==============================================================
  database_v2.sql
  BÖLÜM 2
  Makine ve Parça Modülü
==============================================================*/

--==============================================================
-- MAKİNELER
--==============================================================

CREATE TABLE makineler
(
    id              BIGSERIAL PRIMARY KEY,

    kod             VARCHAR(30) NOT NULL,

    ad              VARCHAR(150) NOT NULL,

    aciklama        TEXT,

    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted      BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at      TIMESTAMP,

    CONSTRAINT uq_makineler_kod UNIQUE(kod),

    CONSTRAINT uq_makineler_ad UNIQUE(ad)
);

CREATE TRIGGER trg_makineler_updated_at
BEFORE UPDATE
ON makineler
FOR EACH ROW
EXECUTE FUNCTION fn_update_timestamp();

--==============================================================
-- MAKİNE BÖLÜMLERİ
--==============================================================

CREATE TABLE makine_bolumleri
(
    id              BIGSERIAL PRIMARY KEY,

    makine_id       BIGINT NOT NULL,

    ad              VARCHAR(150) NOT NULL,

    aciklama        TEXT,

    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted      BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at      TIMESTAMP,

    CONSTRAINT fk_makine_bolumleri_makine
        FOREIGN KEY(makine_id)
        REFERENCES makineler(id)
        ON DELETE CASCADE
);

CREATE TRIGGER trg_makine_bolumleri_updated_at
BEFORE UPDATE
ON makine_bolumleri
FOR EACH ROW
EXECUTE FUNCTION fn_update_timestamp();

--==============================================================
-- PARÇA KATEGORİLERİ
--==============================================================

CREATE TABLE parca_kategorileri
(
    id              BIGSERIAL PRIMARY KEY,

    ad              VARCHAR(100) NOT NULL,

    aciklama        TEXT,

    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted      BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at      TIMESTAMP,

    CONSTRAINT uq_parca_kategorileri_ad UNIQUE(ad)
);

CREATE TRIGGER trg_parca_kategorileri_updated_at
BEFORE UPDATE
ON parca_kategorileri
FOR EACH ROW
EXECUTE FUNCTION fn_update_timestamp();

--==============================================================
-- PARÇA MARKALARI
--==============================================================

CREATE TABLE parca_markalari
(
    id              BIGSERIAL PRIMARY KEY,

    ad              VARCHAR(100) NOT NULL,

    aciklama        TEXT,

    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted      BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at      TIMESTAMP,

    CONSTRAINT uq_parca_markalari_ad UNIQUE(ad)
);

CREATE TRIGGER trg_parca_markalari_updated_at
BEFORE UPDATE
ON parca_markalari
FOR EACH ROW
EXECUTE FUNCTION fn_update_timestamp();

--==============================================================
-- PARÇALAR
--==============================================================

CREATE TABLE parcalar
(
    id                  BIGSERIAL PRIMARY KEY,

    stok_kodu           VARCHAR(100) NOT NULL,

    orijinal_kod        VARCHAR(150),

    parca_adi           VARCHAR(250) NOT NULL,

    kategori_id         BIGINT NOT NULL,

    marka_id            BIGINT NOT NULL,

    model               VARCHAR(150),

    uretici             VARCHAR(150),

    birim               VARCHAR(20) NOT NULL,

    fotograf            VARCHAR(500),

    aciklama            TEXT,

    created_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted          BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at          TIMESTAMP,

    CONSTRAINT uq_parcalar_stok_kodu
        UNIQUE(stok_kodu),

    CONSTRAINT fk_parcalar_kategori
        FOREIGN KEY(kategori_id)
        REFERENCES parca_kategorileri(id),

    CONSTRAINT fk_parcalar_marka
        FOREIGN KEY(marka_id)
        REFERENCES parca_markalari(id),

    CONSTRAINT chk_parcalar_birim
        CHECK
        (
            birim IN
            (
                'Adet',
                'Kg',
                'Lt',
                'Metre',
                'Kutu',
                'Takım'
            )
        )
);

CREATE TRIGGER trg_parcalar_updated_at
BEFORE UPDATE
ON parcalar
FOR EACH ROW
EXECUTE FUNCTION fn_update_timestamp();

--==============================================================
-- TEDARİKÇİLER
--==============================================================

CREATE TABLE tedarikciler
(
    id                  BIGSERIAL PRIMARY KEY,

    firma_adi           VARCHAR(200) NOT NULL,

    yetkili             VARCHAR(150),

    telefon             VARCHAR(30),

    email               VARCHAR(150),

    web_sitesi          VARCHAR(250),

    adres               TEXT,

    vergi_dairesi       VARCHAR(150),

    vergi_no            VARCHAR(50),

    aciklama            TEXT,

    created_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted          BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at          TIMESTAMP,

    CONSTRAINT uq_tedarikciler_firma UNIQUE(firma_adi)
);

CREATE TRIGGER trg_tedarikciler_updated_at
BEFORE UPDATE
ON tedarikciler
FOR EACH ROW
EXECUTE FUNCTION fn_update_timestamp();

--==============================================================
-- PARÇA KULLANIM BÖLÜMLERİ
--==============================================================

CREATE TABLE parca_kullanim_bolumleri
(
    id                  BIGSERIAL PRIMARY KEY,

    parca_id            BIGINT NOT NULL,

    makine_bolumu_id    BIGINT NOT NULL,

    aciklama            TEXT,

    created_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted          BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at          TIMESTAMP,

    CONSTRAINT fk_pkb_parca
        FOREIGN KEY(parca_id)
        REFERENCES parcalar(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_pkb_bolum
        FOREIGN KEY(makine_bolumu_id)
        REFERENCES makine_bolumleri(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_parca_bolum
        UNIQUE(parca_id, makine_bolumu_id)
);

CREATE TRIGGER trg_parca_kullanim_bolumleri_updated_at
BEFORE UPDATE
ON parca_kullanim_bolumleri
FOR EACH ROW
EXECUTE FUNCTION fn_update_timestamp();
/*==============================================================
 database_v2.sql
 BÖLÜM 3
 Son Bölüm
 PostgreSQL 17
==============================================================*/

--==============================================================
-- PARÇA MUADİLLERİ
--==============================================================

CREATE TABLE parca_muadilleri
(
    id BIGSERIAL PRIMARY KEY,

    parca_id BIGINT NOT NULL,

    muadil_parca_id BIGINT NOT NULL,

    aciklama TEXT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at TIMESTAMP,

    CONSTRAINT fk_muadil_parca
        FOREIGN KEY (parca_id)
        REFERENCES parcalar(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_muadil_muadil
        FOREIGN KEY (muadil_parca_id)
        REFERENCES parcalar(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_muadil
        UNIQUE(parca_id, muadil_parca_id)
);

CREATE TRIGGER trg_parca_muadilleri_updated_at
BEFORE UPDATE
ON parca_muadilleri
FOR EACH ROW
EXECUTE FUNCTION fn_update_timestamp();

--==============================================================
-- PARÇA HAREKETLERİ
--==============================================================

CREATE TABLE parca_hareketleri
(
    id BIGSERIAL PRIMARY KEY,

    parca_id BIGINT NOT NULL,

    makine_bolumu_id BIGINT,

    tedarikci_id BIGINT NOT NULL,

    alis_tarihi DATE NOT NULL,

    adet NUMERIC(12,2) NOT NULL,

    birim_fiyat NUMERIC(12,2) NOT NULL,

    toplam_tutar NUMERIC(12,2) NOT NULL,

    para_birimi VARCHAR(3) NOT NULL DEFAULT 'TRY',

    fatura_no VARCHAR(100),

    fatura_tarihi DATE,

    fatura_dosyasi VARCHAR(500),

    tedarikci_urun_kodu VARCHAR(150),

    aciklama TEXT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,

    deleted_at TIMESTAMP,

    CONSTRAINT fk_hareket_parca
        FOREIGN KEY(parca_id)
        REFERENCES parcalar(id),

    CONSTRAINT fk_hareket_tedarikci
        FOREIGN KEY(tedarikci_id)
        REFERENCES tedarikciler(id),

    CONSTRAINT fk_hareket_bolum
        FOREIGN KEY(makine_bolumu_id)
        REFERENCES makine_bolumleri(id),

    CONSTRAINT chk_para_birimi
        CHECK
        (
            para_birimi IN
            (
                'TRY',
                'USD',
                'EUR',
                'GBP',
                'CHF',
                'JPY'
            )
        )
);

CREATE TRIGGER trg_parca_hareketleri_updated_at
BEFORE UPDATE
ON parca_hareketleri
FOR EACH ROW
EXECUTE FUNCTION fn_update_timestamp();

--==============================================================
-- AYARLAR
--==============================================================

CREATE TABLE ayarlar
(
    id BIGSERIAL PRIMARY KEY,

    firma_adi VARCHAR(200),

    logo VARCHAR(500),

    adres TEXT,

    telefon VARCHAR(30),

    email VARCHAR(150),

    vergi_dairesi VARCHAR(100),

    vergi_no VARCHAR(30),

    yetkili VARCHAR(150),

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER trg_ayarlar_updated_at
BEFORE UPDATE
ON ayarlar
FOR EACH ROW
EXECUTE FUNCTION fn_update_timestamp();

--==============================================================
-- INDEXLER
--==============================================================

CREATE INDEX idx_personeller_ad
ON personeller(ad);

CREATE INDEX idx_personeller_soyad
ON personeller(soyad);

CREATE INDEX idx_personeller_tc
ON personeller(tc_kimlik_no);

CREATE INDEX idx_personeller_sicil
ON personeller(sicil_no);

CREATE INDEX idx_parcalar_stok
ON parcalar(stok_kodu);

CREATE INDEX idx_parcalar_ad
ON parcalar(parca_adi);

CREATE INDEX idx_tedarikci
ON tedarikciler(firma_adi);

CREATE INDEX idx_hareket_tarih
ON parca_hareketleri(alis_tarihi);

CREATE INDEX idx_hareket_parca
ON parca_hareketleri(parca_id);

--==============================================================
-- DEFAULT POZİSYONLAR
--==============================================================

INSERT INTO pozisyonlar(ad)
VALUES
('Ram Operatörü'),
('Sanfor Operatörü'),
('Stenter Operatörü'),
('Boyahane Operatörü'),
('Planlama'),
('Muhasebe'),
('Satın Alma'),
('Depo'),
('Bakım'),
('Elektrik Bakım'),
('Kalite Kontrol'),
('İnsan Kaynakları');

--==============================================================
-- PARÇA KATEGORİLERİ
--==============================================================

INSERT INTO parca_kategorileri(ad)
VALUES
('Rulman'),
('Kayış'),
('Pnömatik'),
('Elektrik'),
('Motor'),
('Redüktör'),
('Sensör'),
('Yağ'),
('Keçe'),
('Conta'),
('Fan'),
('Zincir'),
('Kasnak'),
('Valf'),
('Pompa'),
('Filtre');

--==============================================================
-- MARKALAR
--==============================================================

INSERT INTO parca_markalari(ad)
VALUES
('SKF'),
('FAG'),
('INA'),
('NSK'),
('KOYO'),
('TIMKEN'),
('Mobil'),
('Shell'),
('Klüber'),
('Siemens'),
('Schneider'),
('Omron'),
('SMC'),
('Festo'),
('Contitech'),
('Optibelt');

--==============================================================
-- AYARLAR İLK KAYIT
--==============================================================

INSERT INTO ayarlar
(
    firma_adi
)
VALUES
(
    'Firma Adı'
);