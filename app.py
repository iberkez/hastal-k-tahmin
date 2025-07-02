from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# 🔹 Veriyi oku
veri = pd.read_csv("veri.csv")
belirtiler = list(veri.columns[:-1])  # hastalik hariç
etiketleyici = LabelEncoder()
veri["hastalik_kod"] = etiketleyici.fit_transform(veri["hastalik"])
etiketler = etiketleyici.classes_

# 🔹 Ek sütunlar
veri["yas"] = np.random.randint(18, 70, size=len(veri))
veri["sure"] = np.random.randint(1, 10, size=len(veri))
veri["cinsiyet_kod"] = np.random.randint(0, 2, size=len(veri))

# 🔹 Model eğitimi
X = veri[belirtiler + ["yas", "sure", "cinsiyet_kod"]]
y = veri["hastalik_kod"]
model = MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=500, random_state=42)
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def form():
    sonuc = None
    nedenler = []
    if request.method == "POST":
        secimler = [int(request.form.get(b, 0)) for b in belirtiler]
        yas = int(request.form.get("yas", 0))
        sure = int(request.form.get("sure", 0))
        cinsiyet = 1 if request.form.get("cinsiyet") == "erkek" else 0
        girdi = np.array([secimler + [yas, sure, cinsiyet]])
        tahmin_kod = model.predict(girdi)[0]
        sonuc = etiketler[tahmin_kod]
        nedenler = [b.replace("_", " ").capitalize() for i, b in enumerate(belirtiler) if secimler[i] == 1]
        nedenler += [f"Yaş: {yas}", f"Süre: {sure} gün", f"Cinsiyet: {'Erkek' if cinsiyet == 1 else 'Kadın'}"]

    return render_template("form.html", sonuc=sonuc, nedenler=nedenler, belirt_listesi=belirtiler)

if __name__ == "__main__":
    app.run(debug=True)
