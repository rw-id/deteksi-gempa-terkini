"""
Aplikasi deteksi gempa terkini
Modularisasi dengan function
"""


def ekstraksi_data():
    """
    Tanggal: 5 Januari 2022
    Waktu: 03:34:28 WIB
    Magnitudo: 4.7
    Kedalaman: 12 km
    Lokasi: LS=7.01 LS  BT= 105.28 BT
    Pusat Gempa: Pusat gempa berada di laut 50 km Barat Daya Sumur
    Dirasakan: Dirasakan (Skala MMI): II Pandeglang, II Jiput, II Muncul
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '5 Januari 2022'
    hasil['waktu']  = '03:34:28 WIB'
    hasil['magnitudo']  = 4.7
    hasil['kedalaman']  = '12 km'
    hasil['lokasi']  = {'ls': 7.01, 'bt': 105.28}
    hasil['pusat']  = 'Pusat gempa berada di laut 50 km Barat Daya Sumur'
    hasil['dirasakan']  = 'Dirasakan (Skala MMI): II Pandeglang, II Jiput, II Muncul'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == "__main__":
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)