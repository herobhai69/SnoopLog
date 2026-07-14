import pandas as pd
from sklearn.ensemble import IsolationForest

def run_anomaly_engine(csv_path="combined_logs.csv"):
    print("Loading optimized dataset and initializing AI engine...")
    
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: Could not find {csv_path}.")
        return []

    features = ['transfer_amount', 'data_downloaded_mb', 'login_speed_seconds']
    

    dynamic_contamination = (80 / len(df)) + 0.001 
    
    model = IsolationForest(contamination=dynamic_contamination, random_state=42) 
    df['anomaly_label'] = model.fit_predict(df[features]) 
    

    threats = df[df['anomaly_label'] == -1].copy()
    

    known_ips = ['192.168.1.10', '192.168.1.15', '10.0.0.5', '172.16.0.22']
    known_countries = ['USA', 'UK', 'Canada', 'India']
    
    alerts = []
    
    for _, row in threats.iterrows():
        risk_level = "Suspicious"
        reasons = []
        

        if row['ip_address'] not in known_ips:
            reasons.append("New IP Login")
            
        if row['country'] not in known_countries:
            reasons.append(f"Login from diff country ({row['country']})")
            
        if row['login_speed_seconds'] < 3.0:
            reasons.append(f"Quick Login / Bot Suspicion ({row['login_speed_seconds']}s)")

        if row['transfer_amount'] > 5000:
            reasons.append(f"Large Money Transfer (${row['transfer_amount']:,.2f})")
            risk_level = "High"
            
        if row['data_downloaded_mb'] > 150:
            reasons.append(f"Large Data Download ({row['data_downloaded_mb']} MB)")
            risk_level = "High" 
            
        if reasons:
            alerts.append({
                'ip': row['ip_address'],
                'country': row['country'],
                'device': row['device_type'],
                'risk': risk_level,
                'message': " | ".join(reasons)
            })
            
    alerts.sort(key=lambda x: x['risk'] == 'High', reverse=True)
    return alerts

if __name__ == "__main__":
    detected_alerts = run_anomaly_engine()
    print(f"\nEngine flagged {len(detected_alerts)} correlated anomalies.")