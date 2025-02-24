import matplotlib.pyplot as plt
import pandas as pd
import os

# Klasor olusturma
ANALIZ_KLASORU = r"C:\Users\Hakan\Desktop\mindAI-Functions\analizler\urun-bazli-satis-ve-kar"
os.makedirs(ANALIZ_KLASORU, exist_ok=True)

csv_dosya = r"C:\Users\Hakan\Desktop\mindAI-Functions\transactions.csv"
df = pd.read_csv(csv_dosya)


# Grafik dosya yolları
GRAFIK_SATIS_DOSYA = os.path.join(ANALIZ_KLASORU, "urun_bazli_satis_bar.png")
GRAFIK_KAR_DOSYA = os.path.join(ANALIZ_KLASORU, "urun_bazli_kar_bar.png")

# En çok satılan 10 ürünü belirle
top_urunler_satis = df.groupby("part_number")["qty"].sum().nlargest(10)

# En fazla kâr getiren 10 ürünü belirle
top_urunler_kar = df.groupby("part_number")["profit"].sum().nlargest(10)

# 📊 Satış miktarı grafiği
fig, ax = plt.subplots(figsize=(10, 6))
top_urunler_satis.plot(kind="bar", color="b", ax=ax)
ax.set_title("En Çok Satılan Ürünler (Adet Bazında)")
ax.set_xlabel("Ürün Kodu")
ax.set_ylabel("Toplam Satış Miktarı")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(GRAFIK_SATIS_DOSYA)
plt.close()

# 📊 Kâr miktarı grafiği
fig, ax = plt.subplots(figsize=(10, 6))
top_urunler_kar.plot(kind="bar", color="g", ax=ax)
ax.set_title("En Fazla Kâr Getiren Ürünler")
ax.set_xlabel("Ürün Kodu")
ax.set_ylabel("Toplam Kâr ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(GRAFIK_KAR_DOSYA)
plt.close()

# TXT dosya yolu
TXT_DOSYA = os.path.join(ANALIZ_KLASORU, "urun_bazli_analiz_sonucu.txt")

# TXT dosyasina analiz sonuclarini yaz
with open(TXT_DOSYA, "w") as f:
    f.write("Urun Bazli Satis ve Kar Analizi\n")
    f.write("------------------------------------\n")
    
    f.write("\nEn Cok Satilan Urunler (Adet Bazinda)\n")
    for idx, (urun, adet) in enumerate(top_urunler_satis.items(), 1):
        f.write(f"{idx}. Urun Kodu: {urun} - Toplam Satis: {adet} adet\n")

    f.write("\nEn Fazla Kar Getiren Urunler\n")
    for idx, (urun, kar) in enumerate(top_urunler_kar.items(), 1):
        f.write(f"{idx}. Urun Kodu: {urun} - Toplam Kar: ${kar:,.2f}\n")

print(f"Analiz tamamlandi. Sonuclar kaydedildi: {TXT_DOSYA}")


