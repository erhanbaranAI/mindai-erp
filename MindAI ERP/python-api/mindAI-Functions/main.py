import pandas as pd
import matplotlib.pyplot as plt
import os

# Klasor olusturma
ANALIZ_KLASORU = r"C:\Users\Hakan\Desktop\mindAI-Functions\analizler\aylik-toplam-satis-ve-kar"
os.makedirs(ANALIZ_KLASORU, exist_ok=True)

# cikti dosya yollari
TXT_DOSYA = os.path.join(ANALIZ_KLASORU, "analiz_sonucu.txt")
GRAFIK_DOSYA = os.path.join(ANALIZ_KLASORU, "satis_ve_kar_grafik.png")

def aylik_toplam_satis_ve_kar(csv_dosya):
    #  CSV dosyasini oku
    df = pd.read_csv(csv_dosya)
    
    #  Tarih formatini ayarla ve ay bazinda grupla
    df["inv_date"] = pd.to_datetime(df["inv_date"])
    df["Yil-Ay"] = df["inv_date"].dt.to_period("M")  # YYYY-MM formatina cevir
    
    #  Aylik toplam satis ve kar hesapla
    aylik_veri = df.groupby("Yil-Ay").agg({
        "total_sale_value": "sum",
        "profit": "sum"
    }).reset_index()

    #  Grafik ciz
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(aylik_veri["Yil-Ay"].astype(str), aylik_veri["total_sale_value"], marker="o", label="Toplam Satis", color="b")
    ax.plot(aylik_veri["Yil-Ay"].astype(str), aylik_veri["profit"], marker="s", label="Toplam Kar", color="g")

    #  X ekseni etiketlerini iyilestir
    ax.set_xticks(ax.get_xticks()[::3])  # X eksenindeki etiketleri 3 ayda bir goster
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=8)

    #  Genel ayarlamalar
    ax.set_xlabel("Aylar")
    ax.set_ylabel("Miktar ($)")
    ax.set_title("Aylik Toplam Satis ve Kar")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)
    
    # Grafigi kaydet
    plt.tight_layout()  # Kenar bosluklarini otomatik ayarla
    plt.savefig(GRAFIK_DOSYA)
    plt.close()

    # Analiz sonuclarini hesapla
    toplam_satis = aylik_veri["total_sale_value"].sum()
    toplam_kar = aylik_veri["profit"].sum()
    en_yuksek_ay = aylik_veri.loc[aylik_veri["total_sale_value"].idxmax(), "Yil-Ay"]
    en_dusuk_ay = aylik_veri.loc[aylik_veri["total_sale_value"].idxmin(), "Yil-Ay"]

    # TXT dosyasina analiz sonuclarini yaz
    with open(TXT_DOSYA, "w") as f:
        f.write(f"Aylik Toplam Satis ve Kar Analizi\n")
        f.write(f"------------------------------------\n")
        f.write(f"En yuksek satis yapilan ay: {en_yuksek_ay}\n")
        f.write(f"En dusuk satis yapilan ay: {en_dusuk_ay}\n")
        f.write(f"Toplam Satis: ${toplam_satis:,.2f}\n")
        f.write(f"Toplam Kar: ${toplam_kar:,.2f}\n")

    print(f"Analiz tamamlandi. Sonuclar kaydedildi: {ANALIZ_KLASORU}")

# calistirma
if __name__ == "__main__":
    aylik_toplam_satis_ve_kar(r"C:\Users\Hakan\Desktop\mindAI-Functions\transactions.csv")