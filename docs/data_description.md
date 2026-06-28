# Dataset Description (Updated for Revision)

This directory contains the updated load data and subsequent fault scenario sets used in the case studies for evaluating the distribution system restoration model.

---

## 1. System Load Data

### IEEE 37-Node System
- **Total Active Load**: 932.34 kW
- **Total Reactive Load**: 540.77 kVar
- **Modifications**: Time-variation and uncertainty are not considered (static and deterministic).

### IEEE 123-Node System (Newly Added)
- **Total Active Load**: 3490.00 kW
- **Total Reactive Load**: 1910.00 kVar
- **Modifications**: Time-variation and uncertainty are not considered.

---

## 2. Subsequent Fault Scenario Sets (IEEE 123-Node System)

To model the uncertainty of extreme events, **5 sets of subsequent fault scenarios** are provided. These scenarios represent additional line outages that could occur during the restoration process, along with their transition probabilities.

### Summary of Scenario Sets
| Scenario Set | Number of Scenarios | Key Characteristics / Purpose |
| :--- | :---: | :--- |
| **Set 1** | 10 | Low-cardinality baseline scenarios |
| **Set 2** | 10 | Alternative 10-scenario validation set |
| **Set 3** | 30 | Medium-cardinality scenario set |
| **Set 4** | 30 | Alternative 30-scenario validation set |
| **Set 5** | 50 | High-cardinality set for comprehensive risk evaluation |

---

## 💻 Usage Example

You can easily import both load data and scenario sets in Python:

```python
# Import system load
from data.load_data import PL37, QL37, PL123, QL123

# Import subsequent fault scenarios
from data.fault_scenarios import SET_1, SET_3, SET_5

# Example: Accessing Scenario Set 1
for item in SET_1[:3]:
    print(f"Scenario {item['scenario']} (Prob: {item['probability']}): Faulted Lines -> {item['faulted_lines']}")
