from sklearn.ensemble import RandomForestRegressor

def train_soil(df):
    X = df[['soil_moisture', 'temperature']]
    y = df['yield']
    model = RandomForestRegressor()
    model.fit(X, y)
    print("Soil Model Trained ✅")
    return model
