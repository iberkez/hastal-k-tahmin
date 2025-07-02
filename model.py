import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import joblib  # Modeli kaydetmek için

# 1. Veriyi oku
df = pd.read_csv("veri.csv")

# 2. Giriş-çıkış ayrımı
X = df.drop("hastalik", axis=1).values
y = df["hastalik"]

# 3. Etiketleri sayıya çevir
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# 4. Eğitim ve test kümeleri
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# 5. Modeli kur
model = MLPClassifier(hidden_layer_sizes=(16, 12), max_iter=500, random_state=42)

# 6. Eğitimi başlat
model.fit(X_train, y_train)

# 7. Başarı oranı
tahminler = model.predict(X_test)
print("✅ Doğruluk oranı:", accuracy_score(y_test, tahminler))

# 8. Modeli kaydet
joblib.dump(model, "modelim.pkl")
joblib.dump(le, "label_encoder.pkl")
print("📦 Model ve etiketleyici kaydedildi.")
