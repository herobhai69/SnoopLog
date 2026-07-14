import pandas as pd
import numpy as np


np.random.seed(42)

num_normal = 20000

normal_ips = ['192.168.1.10', '192.168.1.15', '10.0.0.5', '172.16.0.22']
devices = ['Mobile', 'Desktop', 'Tablet']
normal_countries = ['USA', 'UK', 'Canada', 'India', 'Kenya', 'Niger']

df_normal = pd.DataFrame({
    'ip_address': np.random.choice(normal_ips, num_normal),
    'device_type': np.random.choice(devices, num_normal),
    'country': np.random.choice(normal_countries, num_normal),
    'login_speed_seconds': np.random.normal(12, 3, num_normal).clip(min=5.0).round(1), 
    'transfer_amount': np.random.normal(150, 50, num_normal).clip(min=5.0).round(2),
    'data_downloaded_mb': np.random.normal(15, 5, num_normal).clip(min=1.0).round(2),
    'is_threat': 0
})


anomaly_ips = [f'45.22.19.{i}' for i in range(10, 90)]
anomaly_countries = ['Pakistan', 'China', 'North Korea', 'Unknown Proxy']


num_suspicious = 54
df_suspicious = pd.DataFrame({
    'ip_address': np.random.choice(anomaly_ips, num_suspicious),
    'device_type': np.random.choice(devices, num_suspicious),
    'country': np.random.choice(anomaly_countries, num_suspicious),
    'login_speed_seconds': np.random.uniform(0.1, 2.5, num_suspicious).round(1),
    'transfer_amount': np.random.normal(150, 50, num_suspicious).clip(min=5.0).round(2),
    'data_downloaded_mb': np.random.normal(15, 5, num_suspicious).clip(min=1.0).round(2),
    'is_threat': 1
})


num_high_risk = 32
df_high_risk = pd.DataFrame({
    'ip_address': np.random.choice(anomaly_ips, num_high_risk),
    'device_type': np.random.choice(devices, num_high_risk),
    'country': np.random.choice(anomaly_countries, num_high_risk),
    'login_speed_seconds': np.random.uniform(0.1, 2.5, num_high_risk).round(1),
    'transfer_amount': np.random.normal(15000, 5000, num_high_risk).clip(min=5000).round(2),
    'data_downloaded_mb': np.random.normal(800, 200, num_high_risk).clip(min=150).round(2),
    'is_threat': 1
})


df_anomalies = pd.concat([df_suspicious, df_high_risk])


df_combined = pd.concat([df_normal, df_anomalies])

df_combined = df_combined.sample(frac=1, random_state=42).reset_index(drop=True)

csv_filename = 'combined_logs.csv'
df_combined.to_csv(csv_filename, index=False)

print(f"Success! Generated {len(df_combined)} total records.")
print(f"Injected {num_suspicious} Suspicious and {num_high_risk} High-Risk profiles.")
print(f"Saved optimized dataset to {csv_filename}")