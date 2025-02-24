import pandas as pd
import os
import matplotlib.pyplot as plt

# Klasor olusturma
ANALIZ_KLASORU = r"C:\Users\Hakan\Desktop\mindAI-Functions\analizler\musteri-bazli-satis-ve-kar"
os.makedirs(ANALIZ_KLASORU, exist_ok=True)


# Grafik dosya yolu
GRAFIK_DOSYA = os.path.join(ANALIZ_KLASORU, "musteri_bazli_satis_pie.png")

# Cikti dosyalari
TXT_DOSYA = os.path.join(ANALIZ_KLASORU, "musteri_analiz_sonucu.txt")

def musteri_bazli_satis_ve_kar(csv_dosya):
    # CSV dosyasini oku
    df = pd.read_csv(csv_dosya)

    # Musteri bazinda toplam satis ve kar hesapla
    musteri_veri = df.groupby("account").agg({
        "total_sale_value": "sum",
        "profit": "sum"
    }).reset_index()

    # En cok satis yapan ve en cok kar getiren musterileri belirle
    en_fazla_satis_yapan = musteri_veri.loc[musteri_veri["total_sale_value"].idxmax()]
    en_fazla_kar_getiren = musteri_veri.loc[musteri_veri["profit"].idxmax()]

    # İlk 5 müşteriyi al (çok fazla müşteri varsa hepsi gösterilmez)
    top_musteriler = musteri_veri.nlargest(5, "total_sale_value")

    # Pasta grafiği çiz
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(top_musteriler["total_sale_value"], labels=top_musteriler["account"], autopct="%1.1f%%", startangle=140, colors=plt.cm.Paired.colors)
    ax.set_title("Musteri Bazli Toplam Satis dagilimi (Ilk 5)")

    # Grafiği kaydet
    plt.savefig(GRAFIK_DOSYA)
    plt.close()


    # TXT dosyasina analiz sonuclarini yaz
    with open(TXT_DOSYA, "w") as f:
        f.write(f"Musteri Bazli Toplam Satis ve Kar Analizi\n")
        f.write(f"------------------------------------\n")
        f.write(f"En fazla satis yapan musteri: {en_fazla_satis_yapan['account']} (${en_fazla_satis_yapan['total_sale_value']:,.2f})\n")
        f.write(f"En fazla kar getiren musteri: {en_fazla_kar_getiren['account']} (${en_fazla_kar_getiren['profit']:,.2f})\n")

    print(f"Analiz tamamlandi. Sonuclar kaydedildi: {ANALIZ_KLASORU}")

# calistirma
if __name__ == "__main__":
    musteri_bazli_satis_ve_kar(r"C:\Users\Hakan\Desktop\mindAI-Functions\transactions.csv")
