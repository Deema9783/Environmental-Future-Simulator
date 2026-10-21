import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

name = input("Enter your name: ")
print("Welcome", name, "to the Pollution and Afforestation Simulator!")
print("*" * 100)

trees = float(input("Enter the afforestation percentage: "))
pollution = float(input("Enter the pollution percentage: "))
renewable = float(input("Enter the renewable energy percentage: "))
print("*" * 100)

year = np.arange(2026, 2031)
environment = (trees * 0.9) + (renewable * 0.6) - (pollution * 0.7)
score = environment + (year - 2026) * 0.3

print("Year:", year)
print("Environment:", environment)
print("Score:", score)
print("*" * 100)

df = pd.DataFrame({
    "Year": year,
    "Score": score
})

print("\n⏳ Traveling to the future and analyzing data... ⏳\n")
time.sleep(2)

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="Year", y="Score", marker="o", linewidth=3, markersize=10)

plt.title(f"🌍 Future Prediction: {name} 🌍", fontsize=16, fontweight='bold')
plt.xlabel("Years (Future)", fontsize=14)
plt.ylabel("Environmental Health Index", fontsize=14)

plt.xticks(year)
plt.grid(True, linestyle='--')

plt.show()

print("\n")
print("-" * 65)
print("Reviewing the city path...")

final_val = score[-1]
time.sleep(1.5)

if final_val > 65:
    print(f"Hey {name}, your numbers are optimistic and your vision is responsible.")
    print("Your city is on a promising path and we look forward to seeing your impact.")
    print("Keep going, as conscious planning is the foundation for a healthy environment.")
elif final_val > 40:
    print(f"Hey {name}, the results are good but they need more work.")
    print("We need to balance our decisions as your steps today make a difference tomorrow.")
    print("There is still a chance to improve the indicators and develop performance.")
else:
    print(f"Hey {name}, the current path of the city needs an immediate review.")
    print("The environmental reality requires firmness to correct the path before it is too late.")
    print("Overcoming these challenges requires tougher and more serious decisions.")

print("-" * 65)
print("Our simulation for today has ended.")
print("Thank you for your time and your interest in the future of our environment.")
print("Remember that every decision you make today shapes our reality tomorrow.")
print("-" * 65)
