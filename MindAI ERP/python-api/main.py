import pandas as pd
import matplotlib.pyplot as plt
import os

# 📂 Klasör oluşturma
ANALIZ_KLASORU = r"C:\Users\lerha\source\repos\MindAI ERP\MindAI ERP\analizler\aylik-toplam-satis-ve-kar"
os.makedirs(ANALIZ_KLASORU, exist_ok=True)

# 📂 Çıktı dosya yolları
TXT_DOSYA = os.path.join(ANALIZ_KLASORU, "analiz_sonucu.txt")
GRAFIK_DOSYA = os.path.join(ANALIZ_KLASORU, "satis_ve_kar_grafik.png")

def aylik_toplam_satis_ve_kar(csv_dosya):
    # 📌 CSV dosyasını oku
    df = pd.read_csv(csv_dosya)
    
    # 📌 Tarih formatını ayarla ve ay bazında grupla
    df["inv_date"] = pd.to_datetime(df["inv_date"])
    df["Yıl-Ay"] = df["inv_date"].dt.to_period("M")  # YYYY-MM formatına çevir
    
    # 📌 Aylık toplam satış ve kar hesapla
    aylik_veri = df.groupby("Yıl-Ay").agg({
        "total_sale_value": "sum",
        "profit": "sum"
    }).reset_index()

    # 📊 Grafik çiz
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(aylik_veri["Yıl-Ay"].astype(str), aylik_veri["total_sale_value"], marker="o", label="Toplam Satış", color="b")
    ax.plot(aylik_veri["Yıl-Ay"].astype(str), aylik_veri["profit"], marker="s", label="Toplam Kar", color="g")

    # 📌 X ekseni etiketlerini iyileştir
    ax.set_xticks(ax.get_xticks()[::3])  # X eksenindeki etiketleri 3 ayda bir göster
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=8)

    # 📌 Genel ayarlamalar
    ax.set_xlabel("Aylar")
    ax.set_ylabel("Miktar ($)")
    ax.set_title("Aylık Toplam Satış ve Kar")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)
    
    # 📂 Grafiği kaydet
    plt.tight_layout()  # Kenar boşluklarını otomatik ayarla
    plt.savefig(GRAFIK_DOSYA)
    plt.close()

    # 📊 Analiz sonuçlarını hesapla
    toplam_satis = aylik_veri["total_sale_value"].sum()
    toplam_kar = aylik_veri["profit"].sum()
    en_yuksek_ay = aylik_veri.loc[aylik_veri["total_sale_value"].idxmax(), "Yıl-Ay"]
    en_dusuk_ay = aylik_veri.loc[aylik_veri["total_sale_value"].idxmin(), "Yıl-Ay"]

    # 📝 TXT dosyasına analiz sonuçlarını yaz
    with open(TXT_DOSYA, "w") as f:
        f.write(f"Aylik Toplam Satis ve Kar Analizi\n")
        f.write(f"------------------------------------\n")
        f.write(f"En yuksek satis yapilan ay: {en_yuksek_ay}\n")
        f.write(f"En dusuk satis yapilan ay: {en_dusuk_ay}\n")
        f.write(f"Toplam Satis: ${toplam_satis:,.2f}\n")
        f.write(f"Toplam Kar: ${toplam_kar:,.2f}\n")
        f.write(f"Grafik Kaydedildi: {GRAFIK_DOSYA}\n")

    print(f"Analiz tamamlandı. Sonuçlar kaydedildi: {ANALIZ_KLASORU}")

# 🚀 Çalıştırma
if __name__ == "__main__":
    aylik_toplam_satis_ve_kar(r"C:\Users\lerha\source\repos\MindAI ERP\MindAI ERP\transactions.csv")
