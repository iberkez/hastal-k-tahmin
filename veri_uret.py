import pandas as pd
import random

belirtiler = [
    "ates","oksuruk","bas_agrisi","halsizlik","bogaz_agrisi","burun_akintisi","mide_bulantisi","kas_agrisi",
    "nefes_darligi","gogus_agrisi","tansiyon_yuksek","terleme","ishal","kabizlik","cilt_dokuntusu",
    "idrar_yanmasi","gunes_hassasiyet","bas_donmesi","kilo_kaybi","yorgunluk"
]

hastaliklar = {
    "Grip": ["ates","oksuruk","bogaz_agrisi"],
    "Migren": ["bas_agrisi","bas_donmesi"],
    "Zehirlenme": ["mide_bulantisi","ishal"],
    "Covid": ["ates","nefes_darligi","yorgunluk"],
    "Reflü": ["mide_bulantisi","bogaz_agrisi"],
    "Tansiyon": ["tansiyon_yuksek","bas_donmesi"],
    "Kalp Krizi": ["gogus_agrisi","terleme"],
    "Cilt Alerjisi": ["cilt_dokuntusu","gunes_hassasiyet"]
}

veriler = []
for hastalik, semptomlar in hastaliklar.items():
    for _ in range(20):
        satir = {}
        for b in belirtiler:
            satir[b] = 1 if b in semptomlar else random.choice([0,0,0,1])
        satir["hastalik"] = hastalik
        veriler.append(satir)

df = pd.DataFrame(veriler)
df.to_csv("veri.csv", index=False)
print("✅ veri.csv oluşturuldu.")
