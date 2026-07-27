from scanner import portlari_tara
from validators import hedefi_coz, ip_gecerli_mi, port_araligi_gecerli_mi
from reports import txt_raporu_kaydet, csv_raporu_kaydet


def main():

    print("=" * 60)
    print("          PYTHON PROFESSIONAL PORT SCANNER")
    print("=" * 60)

    # Hedef bilgisi
    hedef = input("Hedef IP veya alan adı: ").strip()

    if not hedef:
        print("Hata: Hedef boş bırakılamaz.")
        return

    # IP adresini bul
    ip = hedefi_coz(hedef)

    if ip is None:
        print("Hata: Geçersiz IP veya alan adı.")
        return

    print(f"\nHedef IP: {ip}")

    # Port aralığı
    try:
        baslangic = int(
            input("Başlangıç portu: ")
        )

        bitis = int(
            input("Bitiş portu: ")
        )

    except ValueError:
        print("Hata: Port numarası sayı olmalıdır.")
        return

    # Port kontrolü
    if not port_araligi_gecerli_mi(
        baslangic,
        bitis
    ):
        print(
            "Hata: Geçersiz port aralığı."
        )
        print(
            "Portlar 1 ile 65535 arasında olmalıdır."
        )
        return

    # Timeout
    try:

        timeout_girdisi = input(
            "Timeout (saniye) "
            "[Varsayılan: 0.5]: "
        ).strip()

        if timeout_girdisi:
            timeout = float(
                timeout_girdisi
            )
        else:
            timeout = 0.5

        if timeout <= 0:
            print(
                "Hata: Timeout 0'dan büyük olmalıdır."
            )
            return

    except ValueError:

        print(
            "Hata: Timeout sayı olmalıdır."
        )
        return

    # Thread sayısı
    try:

        thread_girdisi = input(
            "Thread sayısı "
            "[Varsayılan: 100]: "
        ).strip()

        if thread_girdisi:
            thread_sayisi = int(
                thread_girdisi
            )
        else:
            thread_sayisi = 100

        if thread_sayisi <= 0:
            print(
                "Hata: Thread sayısı "
                "0'dan büyük olmalıdır."
            )
            return

    except ValueError:

        print(
            "Hata: Thread sayısı "
            "tam sayı olmalıdır."
        )
        return

    # Tarama başlat
    acik_portlar, gecen_sure = portlari_tara(
        ip,
        baslangic,
        bitis,
        timeout,
        thread_sayisi
    )

    # Sonuçları göster
    print("\n" + "=" * 60)
    print("TARAMA TAMAMLANDI")
    print("=" * 60)

    print(
        f"Açık port sayısı: "
        f"{len(acik_portlar)}"
    )

    print(
        f"Tarama süresi: "
        f"{gecen_sure:.2f} saniye"
    )

    # TXT raporu
    txt_dosyasi = txt_raporu_kaydet(
        hedef,
        ip,
        acik_portlar,
        gecen_sure
    )

    # CSV raporu
    csv_dosyasi = csv_raporu_kaydet(
        hedef,
        ip,
        acik_portlar
    )

    print("\nRaporlar oluşturuldu:")

    print(
        f"TXT: {txt_dosyasi}"
    )

    print(
        f"CSV: {csv_dosyasi}"
    )

    print("=" * 60)


if __name__ == "__main__":
    main()