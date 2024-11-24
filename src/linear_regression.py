import firebase_admin
from firebase_admin import credentials, firestore
import json
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime

# Conexão com o Firebase
cred = credentials.Certificate('firebase_key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection("Arduino").order_by("timestamp", direction="DESCENDING").limit(1)
docs = doc_ref.stream()

# Obter nível de água mais recente
water_level = None
for doc in docs:
    water_level = doc.to_dict().get("waterLevel")

if water_level is None:
    raise ValueError("Nenhum dado de nível de água encontrado no Firebase!")

with open('tabua_mare_2024.json', 'r') as file:
    data = json.load(file)

today = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M")
year_month = today[:7]
day_index = int(today[8:10]) - 1
today_tide_info = data[year_month][day_index]

closest_tide_level = None
closest_time_diff = float('inf')

for tide in today_tide_info.split('\n'):
    if 'm' in tide:
        if 'h' in tide:
            time, level = tide.split()[0], tide.split()[1]
            time = time.replace("h", "")
            tide_time = datetime.strptime(time, "%H:%M").time()

            tide_level = float(level[:-1])

            time_diff = abs(
                (datetime.combine(datetime.today(), tide_time) - datetime.now()).total_seconds()
            )

            if time_diff < closest_time_diff:
                closest_time_diff = time_diff
                closest_tide_level = tide_level

# Dados de exemplo para treinamento do modelo de regressão múltipla
level = np.array([
    [1800, 1.2],
    [1850, 1.4],
    [1900, 1.6],
    [1950, 1.8],
    [2000, 2.0],
    [2050, 2.2],
    [2100, 2.5]
])
risk = np.array([20, 30, 45, 55, 65, 75, 90])

# Treinar o modelo de regressão linear múltipla
model = LinearRegression()
model.fit(level, risk)

# Calcular o risco de enchente
new_level = np.array([[water_level, closest_tide_level]])
flood_risk = model.predict(new_level)[0]

print(f"Nível de água: {water_level}, Nível da maré mais próximo: {closest_tide_level}m")
print(f"Risco de enchente previsto: {flood_risk:.2f} %")
