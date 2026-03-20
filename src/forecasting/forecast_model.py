# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error

# def train_forecast_model(X_train, y_train):
#     model = RandomForestRegressor(random_state=42)
#     model.fit(X_train, y_train)
#     return model

# def evaluate_model(model, X_test, y_test):
#     preds = model.predict(X_test)
#     mae = mean_absolute_error(y_test, preds)
#     rmse = mean_squared_error(y_test, preds) ** 0.5

#     return {"MAE": mae, "RMSE": rmse}

# src/forecasting/forecast_model.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

def train_forecast_model(X_train, y_train):
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    rmse = mean_squared_error(y_test, preds) ** 0.5
    return {"MAE": mae, "RMSE": rmse}