# Load Data Description

## Overview
This dataset contains updated load data for the IEEE 37-node distribution system test case, used in the research on distribution system restoration considering risk mitigation in extreme events.

## Data Source
**Original Reference:**
> C. Chen, J. Wang, F. Qiu et al., "Resilient distribution system by microgrids formation after natural disasters", IEEE Trans. Smart Grid, vol. 7, no. 2, pp. 958-966, 2016.

## Modifications
The load data has been modified with the following assumptions:
- **Time variation**: Not considered (static load)
- **Uncertainty**: Not considered (deterministic values)
- **System size**: 37 nodes

## Data Format

### Active Power Load (PL37)
- **Unit**: kW (kilowatts)
- **Total**: 987.2 kW
- **Array length**: 37 elements

### Reactive Power Load (QL37)
- **Unit**: kVar (kilovolt-ampere reactive)
- **Total**: 540.77 kVar
- **Array length**: 37 elements

## File Formats Available
1. **Python** (`load_data.py`): Direct import for Python scripts
2. **CSV** (`load_data.csv`): Compatible with Excel, MATLAB, Python pandas
3. **JSON** (`load_data.json`): Universal format with metadata
4. **MATLAB** (`load_data.mat`): Native MATLAB format (optional)

## Usage Example

### Python
```python
from data.load_data import PL37, QL37
print(f"Node 1 Active Load: {PL37[0]} kW")
print(f"Node 1 Reactive Load: {QL37[0]} kVar")
