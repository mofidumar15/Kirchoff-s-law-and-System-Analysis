# Kirchoff-s-law-and-System-Analysis

## 📌 Overview
 This project implements **Kirchhoff’s Current Law (KCL)** and **Kirchhoff’s Voltage Law (KVL)** using Python to automate the conservation of charge and energy checks in a circuit.

## 🛠️ Features
- **Dynamic Branching:** Handles multiple parallel branches without hard-coded variables.
- **Automated KCL Validation:** Calculates the unknown "return" or "remaining" current in a junction.
- **Visual Analytics:** Uses `Matplotlib` to generate a distribution chart of how current splits across the network.
- **Robust Error Handling:** Validates user input to ensure physical laws (like non-negative total current) are respected.

## 💻 The Code
This repository contains a modular script designed for efficiency and scalability.

# Run the analyzer
python kcl_analyzer.py

## 🧠 Logic and Analysis

The core of this Day 04 project is transitioning from a "Calculator" to an "Analyzer." The script follows a structured logical flow to ensure electrical integrity.

### 1. The Mathematical Foundation
The script enforces **Kirchhoff’s Current Law (KCL)**, which states that the algebraic sum of currents entering a junction (node) is zero:
$$\sum_{k=1}^{n} I_k = 0$$

In our code, this is implemented as:
`Remaining_Current = Total_Source_Current - sum(Branch_Currents)`

### 2. Algorithmic Flow
The program follows this execution logic:
1.  **Input Acquisition:** Collects $I_{total}$ and $n$ known branch currents.
2.  **Validation Gate:** * Checks if $\sum I_{branches} > I_{total}$. 
    * *Analysis:* If true, the system flags a "Conservation of Charge" violation (potential measurement error or hidden source).
3.  **Residual Calculation:** Computes the current for the $n+1$ branch.
4.  **Data Representation:** Maps the numerical array to a `matplotlib` wedge to visualize the load distribution.

### 3. Efficiency Analysis
| Feature | Manual Method | Python (Day 04) Method |
| :--- | :--- | :--- |
| **Complexity** | $O(n)$ manual steps | $O(1)$ automated execution |
| **Error Margin** | High (Human calculation) | Low (Float precision) |
| **Scalability** | Fixed to 2-3 branches | Scalable to $n$ branches via NumPy arrays |

---

## 🛠️ Performance Metrics
By using `NumPy` for the current arrays, the memory overhead is minimized. This allows the logic to be exported into larger simulations (like Monte Carlo analysis for circuit reliability) in future steps of this 30-day challenge.
