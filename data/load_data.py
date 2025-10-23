"""
Updated Load Data for IEEE 37-Node Distribution System
======================================================

Reference:
    Modified from: C. Chen, J. Wang, F. Qiu et al., 
    "Resilient distribution system by microgrids formation after natural disasters", 
    IEEE Trans. Smart Grid, vol. 7, no. 2, pp. 958-966, 2016.

Modifications:
    - Time variation not considered
    - Uncertainty not considered
    - 37 nodes

Author: [您的名字]
Date: [日期]
"""

# Active Power Load (kW) for 37 nodes
PL37 = [
    30.4, 18.61, 38.84, 26.39, 12.58, 29.58, 31.09, 22.57, 43.08,
    22.57, 48.23, 21.06, 37.61, 31.51, 18.89, 12.17, 15.36, 29.37,
    33.82, 43.9, 31.18, 35.71, 43.98, 24.38, 38.5, 5.98, 7.69, 12.56,
    35.12, 11.03, 46.24, 7.01, 42.55, 12.73, 19.04, 40.6, 5.27
]

# Reactive Power Load (kVar) for 37 nodes
QL37 = [
    5.09, 23.6, 26.48, 18.4, 11.3, 29.2, 5.76, 4.07, 8.82, 16.95,
    28.64, 14.8, 7.71, 3.51, 7.45, 15.65, 12.72, 25.31, 4.8, 8.45,
    19.28, 13.76, 12.74, 22.32, 7.13, 15.54, 22.34, 18.96, 21.79,
    4.36, 21.26, 9, 7.5, 19.2, 25.36, 24.77, 0
]

# Total system load
TOTAL_ACTIVE_LOAD = sum(PL37)  # 987.2 kW
TOTAL_REACTIVE_LOAD = sum(QL37)  # 540.77 kVar

if __name__ == "__main__":
    print(f"Total Active Load: {TOTAL_ACTIVE_LOAD} kW")
    print(f"Total Reactive Load: {TOTAL_REACTIVE_LOAD} kVar")
    print(f"Number of Nodes: {len(PL37)}")
