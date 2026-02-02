import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

np.random.seed(42)

time = np.arange(0,20)
ture_signal = 25 + 0.05 * time
noise = np.random.normal(0, 1.5, size=len(time))
sensor_value = ture_signal + noise

df = pd.DataFrame({
    "time": time,
    "sensor_value": sensor_value
})
df.loc[::20, "sensor_value"] = np.nan
df.loc[::33, "sensor_value"] += 10

df.to_csv("data/sensor_data.csv", index=False)

plt.figure()
plt.plot(df["time"], df["sensor_value"])
plt.xlabel("Time")
plt.ylabel("sensor_value")
plt.title("Raw Sensor Data")
plt.show()

df_clean = df.copy()
df_clean["sensor_value"] = df_clean["sensor_value"].interpolate()

mean = df_clean["sensor_value"].mean()
std = df_clean["sensor_value"].std()

outliers = abs(df_clean["sensor_value"] - mean)> 3 * std
df_clean.loc[outliers, "sensor_value"] = mean

plt.figure()
plt.plot(df["time"], df["sensor_value"], label="Raw", alpha=0.5)
plt.plot(df_clean["time"], df_clean["sensor_value"], label="Cleaned")
plt.legend()
plt.title("Raw vs Cleaned Sensor Data")
plt.show()

df_clean["model"] = df_clean["sensor_value"].rolling(window=10).mean()

plt.figure()
plt.plot(df_clean["time"], df_clean["sensor_value"],label="Cleaned Data")
plt.plot(df_clean["time"], df_clean["sensor_value"],label="Model")
plt.legend()
plt.title("Time-Dependent Modelling")
plt.show()

df_eval = df_clean.dropna()
rmse = np.sqrt(np.mean((df_eval["sensor_value"] - df_eval["model"])**2))

print(f"Model RMSE: {rmse:.2f}")