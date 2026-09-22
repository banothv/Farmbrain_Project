print("🚀 FarmBrain Major Project Started")

from utils.preprocessing import load_data
from models.soil.soil_model import train_soil

data = load_data()
model = train_soil(data)

print("✅ System Running Successfully")
