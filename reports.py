import csv
import os
from datetime import datetime


def txt_raporu_kaydet(
    hedef,
    ip,
    acik_portlar,
    gecen_sure
):

    os.makedirs(
        "results",
        exist_ok=True
    )

    zaman = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    dosya_adi = (
        f"results/"
        f"scan_{zaman}.txt"
    )

    with open(
        dosya_adi,
        "w",
        encoding="utf-8"
    ) as dosya:

        dosya.write(
            "PYTHON PROFESSIONAL "
            "PORT SCANNER\n"
        )

        dosya.write(
            "=" * 50 + "\n"
        )

        dosya.write(
            f"Hedef: {hedef}\n"
        )

        dosya.write(
            f"IP: {ip}\n"
        )

        dosya.write(
            f"Tarama süresi: "
            f"{gecen_sure:.2f} saniye\n"
        )

        dosya.write(
            f"Açık port sayısı: "
            f"{len(acik_portlar)}\n"
        )

        dosya.write(
            "=" * 50 + "\n\n"
        )

        if not acik_portlar:

            dosya.write(
                "Açık port bulunamadı.\n"
            )

        else:

            for sonuc in acik_portlar:

                dosya.write(
                    f"Port: "
                    f"{sonuc['port']} | "
                    f"Durum: "
                    f"{sonuc['durum']} | "
                    f"Servis: "
                    f"{sonuc['servis']}\n"
                )

    return dosya_adi


def csv_raporu_kaydet(
    hedef,
    ip,
    acik_portlar
):

    os.makedirs(
        "results",
        exist_ok=True
    )

    zaman = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    dosya_adi = (
        f"results/"
        f"scan_{zaman}.csv"
    )

    with open(
        dosya_adi,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as dosya:

        yazici = csv.writer(
            dosya
        )

        yazici.writerow([
            "Hedef",
            "IP",
            "Port",
            "Durum",
            "Servis"
        ])

        for sonuc in acik_portlar:

            yazici.writerow([
                hedef,
                ip,
                sonuc["port"],
                sonuc["durum"],
                sonuc["servis"]
            ])

    return dosya_adi