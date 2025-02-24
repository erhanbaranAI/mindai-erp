import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import BayesianRidge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import zscore

# 📁 Çıktı Klasörünü Oluştur
ANALIZ_KLASORU = r"C:\Users\Hakan\Desktop\mindAI-Functions\analizler\kar-tahmini"
os.makedirs(ANALIZ_KLASORU, exist_ok=True)

# 📂 CSV Dosyasını Parça Parça Oku
csv_dosya = r"C:\Users\Hakan\Desktop\mindAI-Functions\transactions.csv"

chunk_size = 10000  # 10.000 satırlık bloklar halinde oku
df_list = []
for chunk in pd.read_csv(csv_dosya, chunksize=chunk_size):
    chunk.fillna(chunk.median(numeric_only=True), inplace=True)  # Eksik verileri doldur
    df_list.append(chunk)

df = pd.concat(df_list, ignore_index=True)

# 🕵️ Veri Önizleme
print("🔍 Veri Önizleme:")
print(df.head())

# 📊 Eksik Veri Analizi
print("🔎 Eksik Veri Sayıları:")
print(df.isnull().sum())

# 📉 Aykırı Değerleri Temizleme (Z-Score Kullanarak)
z_scores = df.select_dtypes(include=["number"]).apply(zscore)

df = df[(np.abs(z_scores) < 3).all(axis=1)]  # Z skoru 3’ten büyük olanları kaldır

# 📊 Kategorik Değişkenleri Kontrol Et
categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

# 🏷️ Yüksek kategorik değişkenleri azalt
MAX_CATEGORIES = 50
for col in categorical_cols:
    if df[col].nunique() > MAX_CATEGORIES:
        top_categories = df[col].value_counts().nlargest(MAX_CATEGORIES).index
        df[col] = df[col].apply(lambda x: x if x in top_categories else "Other")

# 🔄 Bellek Dostu One-Hot Encoding (Sadece İlk 50 Kategoriyi Koru)
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True, dtype=np.float32)

# 🏗️ Bellek Optimizasyonu: float64 → float32, int64 → int32
for col in df.select_dtypes(include=["float64"]).columns:
    df[col] = df[col].astype(np.float32)

for col in df.select_dtypes(include=["int64"]).columns:
    df[col] = df[col].astype(np.int32)

# 🎯 Giriş ve Çıkış Değişkenlerini Seç
X = df.drop(columns=["profit"])  # Hedef değişken hariç tüm değişkenler
y = df["profit"]

# 📏 Ölçeklendirme (MinMaxScaler)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 📊 Veri Setini Eğitim ve Test Olarak Ayır
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 📈 Bayesian Ridge Regression Modelini Eğitme
model = BayesianRidge()
model.fit(X_train, y_train)

# 📊 Tahmin Yapma
y_pred = model.predict(X_test)

# 🎯 Model Performans Metrikleri
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# 📈 Gerçek ve Tahmin Edilen Değerleri Karşılaştırma Grafiği
GRAFIK_DOSYA = os.path.join(ANALIZ_KLASORU, "kar_tahmin_grafik.png")

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5, color="blue", label="Gerçek vs Tahmin")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle="--", color="red", label="Mükemmel Doğrusal")
plt.xlabel("Gerçek Kar ($)")
plt.ylabel("Tahmin Edilen Kar ($)")
plt.title("Kar Tahmini: Bayesian Regression")
plt.legend()
plt.grid(True)
plt.savefig(GRAFIK_DOSYA)
plt.close()

# 📜 TXT Dosyasına Model Başarısı ve Katsayıları Yaz
TXT_DOSYA = os.path.join(ANALIZ_KLASORU, "kar_tahmin_analiz.txt")

with open(TXT_DOSYA, "w") as f:
    f.write("Kar Tahmini - Bayesian Ridge Regression Modeli\n")
    f.write("--------------------------------------------\n")
    f.write(f"R2 Skoru: {r2:.4f}\n")
    f.write(f"MAE (Ortalama Mutlak Hata): {mae:.2f}\n")
    f.write(f"RMSE (Karekok Ortalama Kare Hata): {rmse:.2f}\n")
    f.write("\nModel Katsayıları:\n")
    for col, coef in zip(X.columns, model.coef_):
        f.write(f"{col}: {coef:.4f}\n")

# 🏆 Modelin Başarı Raporunu Yazdır
print(f"✅ Geliştirilmiş Regresyon Analizi Tamamlandı! Sonuçlar Kaydedildi: {TXT_DOSYA}")
