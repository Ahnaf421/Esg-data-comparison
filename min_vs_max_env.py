import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Ensure the environment_score column is numeric
if df['environment_score'].dtype != 'int64' and df['environment_score'].dtype != 'float64':
    df['environment_score'] = pd.to_numeric(df['environment_score'], errors='coerce')

max_row = df.loc[df['environment_score'].idxmax()]
min_row = df.loc[df['environment_score'].idxmin()]
names = [min_row['name'], max_row['name']]
scores = [min_row['environment_score'], max_row['environment_score']]
colors = ['red', 'green']

plt.figure(figsize=(8,6))
bars = plt.bar(names, scores, color=colors)
plt.title('Comparison of Least vs Most Environmental Company', fontsize=16)
plt.ylabel('Environmental Score', fontsize=14)
plt.xlabel('Company', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('min_vs_max_env.png')
plt.close() 