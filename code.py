import numpy as np
import matplotlib.pyplot as plt

def analyze_kcl():
    print("--- Kirchhoff's Current Law (KCL) Analyzer ---")
    
    try:
        # Input Section
        total_i = float(input("Enter total source current (A): "))
        num_known_branches = int(input("How many branch currents do you already know? "))
        
        known_currents = []
        for i in range(num_known_branches):
            val = float(input(f"  Enter current for branch {i+1} (A): "))
            known_currents.append(val)
            
        # Calculation
        sum_known = sum(known_currents)
        remaining_i = total_i - sum_known
        
        # Result 
        print("\n--- Analysis Results ---")
        if remaining_i < 0:
            print(f"Warning: Known branch currents ({sum_known}A) exceed total current ({total_i}A).")
            print("Check for measurement errors or additional sources.")
        else:
            print(f"Calculated Current for unknown branch: {remaining_i:.3f} A")
            
        # Visualization
        labels = [f'Branch {i+1}' for i in range(num_known_branches)] + ['Unknown Branch']
        sizes = known_currents + [max(0, remaining_i)]
        
        plt.figure(figsize=(8, 5))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title(f"Current Distribution (Total: {total_i}A)")
        plt.show()

    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    analyze_kcl()
