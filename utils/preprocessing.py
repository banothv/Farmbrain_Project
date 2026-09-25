import pandas as pd

def load_data():
    data = pd.DataFrame({
        'soil_moisture': [30, 40, 50],
        'temperature': [25, 30, 35],
        'yield': [2, 3, 4]
    })
    return data
