"""
Updated Load Data for IEEE 37-Node and 123-Node Distribution Systems
===================================================================

Reference:
    Modified from: C. Chen, J. Wang, F. Qiu et al., 
    "Resilient distribution system by microgrids formation after natural disasters", 
    IEEE Trans. Smart Grid, vol. 7, no. 2, pp. 958-966, 2016.

Modifications:
    - Time variation not considered
    - Uncertainty not considered
    - 37 nodes & 123 nodes

Author: Runze Han (thunderwizard0)
Date: June 2026
"""

# ==============================================================================
# 1. IEEE 37-Node System Load Data
# ==============================================================================

# Active Power Load (kW) for 37 nodes
PL37 = [
    30.4,  26.61, 38.79, 26.39, 20.58, 39.58, 16.09, 26.57, 30.08, 
    22.57, 45.23, 29.06, 37.61, 31.51, 18.89, 11.17, 12.36, 32.37, 
    18.82, 43.9,  25.18, 35.71, 43.98, 20.38, 38.5,  5.98,  7.69,  
    12.56, 35.12, 11.03, 46.24, 7.01,  42.55, 20.73, 25.04, 45.65, 5.27
]

# Reactive Power Load (kVar) for 37 nodes
QL37 = [
    5.09,  23.6,  26.48, 18.4,  11.3,  29.2,  5.76,  4.07,  8.82,  
    16.95, 28.64, 14.8,  7.71,  3.51,  7.45,  15.65, 12.72, 25.31, 
    4.8,   8.45,  19.28, 13.76, 12.74, 22.32, 7.13,  15.54, 22.34,   
    18.96, 21.79, 4.36,  21.26, 9.0,   7.5,   19.2,  25.36, 24.77, 0.0
]

TOTAL_ACTIVE_LOAD_37 = sum(PL37)    # 932.34 kW
TOTAL_REACTIVE_LOAD_37 = sum(QL37)  # 540.77 kVar


# ==============================================================================
# 2. IEEE 123-Node System Load Data
# ==============================================================================

# Active Power Load (kW) for 123 nodes
PL123 = [
    40, 20, 0, 40, 20, 40, 20, 0, 40, 20, 40, 20, 0, 0, 0, 40, 20, 0, 40, 40, 
    0, 40, 0, 40, 0, 0, 0, 40, 40, 40, 20, 20, 40, 40, 40, 0, 40, 20, 20, 0, 
    20, 20, 40, 0, 20, 20, 105, 210, 140, 40, 20, 40, 40, 0, 20, 20, 0, 20, 20, 
    20, 0, 40, 40, 75, 140, 75, 0, 20, 40, 20, 40, 0, 40, 40, 40, 245, 40, 0, 
    40, 40, 0, 40, 20, 20, 40, 20, 40, 40, 0, 40, 0, 40, 0, 40, 20, 20, 0, 40, 
    40, 40, 0, 20, 40, 40, 0, 40, 40, 0, 40, 0, 20, 20, 40, 20, 0, 0, 0, 0, 0, 
    0, 0, 0, 0
]

# Reactive Power Load (kVar) for 123 nodes
QL123 = [
    20, 10, 0, 20, 10, 20, 10, 0, 20, 10, 20, 10, 0, 0, 0, 20, 10, 0, 20, 20, 
    0, 20, 0, 20, 0, 0, 0, 20, 20, 20, 10, 10, 20, 20, 20, 0, 20, 10, 10, 0, 
    10, 10, 20, 0, 10, 10, 75, 150, 95, 20, 10, 20, 20, 0, 10, 10, 0, 10, 10, 
    10, 0, 20, 20, 35, 100, 35, 0, 10, 20, 10, 20, 0, 20, 20, 20, 180, 20, 0, 
    20, 20, 0, 20, 10, 10, 20, 10, 20, 20, 0, 20, 0, 20, 0, 20, 10, 10, 0, 20, 
    20, 20, 0, 10, 20, 20, 0, 20, 20, 0, 20, 0, 10, 10, 20, 10, 0, 0, 0, 0, 0, 
    0, 0, 0, 0
]

TOTAL_ACTIVE_LOAD_123 = sum(PL123)    # 3490 kW
TOTAL_REACTIVE_LOAD_123 = sum(QL123)  # 1910 kVar


if __name__ == "__main__":
    print("--- IEEE 37-Node System ---")
    print(f"Total Active Load: {TOTAL_ACTIVE_LOAD_37:.2f} kW")
    print(f"Total Reactive Load: {TOTAL_REACTIVE_LOAD_37:.2f} kVar")
    print(f"Number of Nodes: {len(PL37)}")
    print("\n--- IEEE 123-Node System ---")
    print(f"Total Active Load: {TOTAL_ACTIVE_LOAD_123:.2f} kW")
    print(f"Total Reactive Load: {TOTAL_REACTIVE_LOAD_123:.2f} kVar")
    print(f"Number of Nodes: {len(PL123)}")
