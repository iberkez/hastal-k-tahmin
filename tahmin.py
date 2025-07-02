import pandas as pd
from sklearn.tree import DecisionTreeClassifier

veri = pd.read_csv("veri.csv")
X = veri.drop("hastalik", axis=1)
y = veri["hastalik"]

model = DecisionTreeClassifier()
model.fit(X, y)

print("Belirtileri gir (1: Evet, 0: Hayır)")
ates = int(input("Ateş: "))
oksuruk = int(input("Öksürük: "))
bas_agrisi = int(input("Baş ağrısı: "))
halsizlik = int(input("Halsizlik: "))

tahmin = model.predict([[ates, oksuruk, bas_agrisi, halsizlik]])
print(f"\n⚕️ Tahmini hastalık: {tahmin[0]}")
