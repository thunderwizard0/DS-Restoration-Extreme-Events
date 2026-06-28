"""
Subsequent Fault Scenario Sets for IEEE 123-Node System Restoration
==================================================================

This file contains 5 sets of subsequent fault scenarios with their respective 
probabilities and faulted lines, used for risk-mitigation evaluation.
"""

# Set 1 (10 Scenarios)
SET_1 = [
    {"scenario": 1, "probability": 0.1689, "faulted_lines": ["91-92"]},
    {"scenario": 2, "probability": 0.1553, "faulted_lines": ["86-87"]},
    {"scenario": 3, "probability": 0.1631, "faulted_lines": ["97-98"]},
    {"scenario": 4, "probability": 0.0097, "faulted_lines": ["93-94", "99-100"]},
    {"scenario": 5, "probability": 0.1689, "faulted_lines": ["100-123"]},
    {"scenario": 6, "probability": 0.1553, "faulted_lines": ["99-100"]},
    {"scenario": 7, "probability": 0.0097, "faulted_lines": ["91-93", "117-122"]},
    {"scenario": 8, "probability": 0.1534, "faulted_lines": ["98-99"]},
    {"scenario": 9, "probability": 0.0117, "faulted_lines": ["93-95", "95-96"]},
    {"scenario": 10, "probability": 0.0039, "faulted_lines": ["42-44", "93-94", "117-122"]}
]

# Set 2 (10 Scenarios)
SET_2 = [
    {"scenario": 1, "probability": 0.011, "faulted_lines": ["100-123", "117-122"]},
    {"scenario": 2, "probability": 0.004, "faulted_lines": ["78-79", "91-93", "109-110"]},
    {"scenario": 3, "probability": 0.158, "faulted_lines": ["87-89"]},
    {"scenario": 4, "probability": 0.160, "faulted_lines": ["91-92"]},
    {"scenario": 5, "probability": 0.154, "faulted_lines": ["93-94"]},
    {"scenario": 6, "probability": 0.1643, "faulted_lines": ["98-99"]},
    {"scenario": 7, "probability": 0.1563, "faulted_lines": ["86-87"]},
    {"scenario": 8, "probability": 0.1683, "faulted_lines": ["97-98"]},
    {"scenario": 9, "probability": 0.012, "faulted_lines": ["91-93", "98-99"]},
    {"scenario": 10, "probability": 0.012, "faulted_lines": ["60-61", "62-63"]}
]

# Set 3 (30 Scenarios)
SET_3 = [
    {"scenario": 1, "probability": 0.0075, "faulted_lines": ["91-92", "100-123"]},
    {"scenario": 2, "probability": 0.0733, "faulted_lines": ["93-95"]},
    {"scenario": 3, "probability": 0.0015, "faulted_lines": ["87-88", "91-93", "95-96"]},
    {"scenario": 4, "probability": 0.0748, "faulted_lines": ["99-100"]},
    {"scenario": 5, "probability": 0.0015, "faulted_lines": ["67-68", "93-94", "99-100"]},
    {"scenario": 6, "probability": 0.0718, "faulted_lines": ["89-90"]},
    {"scenario": 7, "probability": 0.0075, "faulted_lines": ["93-94", "98-99"]},
    {"scenario": 8, "probability": 0.009, "faulted_lines": ["93-95", "109-110"]},
    {"scenario": 9, "probability": 0.0075, "faulted_lines": ["91-92", "117-122"]},
    {"scenario": 10, "probability": 0.0075, "faulted_lines": ["99-100", "117-122"]},
    {"scenario": 11, "probability": 0.0696, "faulted_lines": ["86-87"]},
    {"scenario": 12, "probability": 0.0105, "faulted_lines": ["91-92", "109-110"]},
    {"scenario": 13, "probability": 0.0075, "faulted_lines": ["86-87", "87-89"]},
    {"scenario": 14, "probability": 0.0075, "faulted_lines": ["91-93", "93-94"]},
    {"scenario": 15, "probability": 0.0015, "faulted_lines": ["89-90", "98-99", "109-110"]},
    {"scenario": 16, "probability": 0.0703, "faulted_lines": ["109-110"]},
    {"scenario": 17, "probability": 0.0075, "faulted_lines": ["89-90", "99-100"]},
    {"scenario": 18, "probability": 0.0696, "faulted_lines": ["87-89"]},
    {"scenario": 19, "probability": 0.0082, "faulted_lines": ["86-87", "117-122"]},
    {"scenario": 20, "probability": 0.0711, "faulted_lines": ["117-122"]},
    {"scenario": 21, "probability": 0.0082, "faulted_lines": ["91-92", "95-96"]},
    {"scenario": 22, "probability": 0.0075, "faulted_lines": ["93-94", "97-98"]},
    {"scenario": 23, "probability": 0.0778, "faulted_lines": ["97-98"]},
    {"scenario": 24, "probability": 0.0778, "faulted_lines": ["91-93"]},
    {"scenario": 25, "probability": 0.0075, "faulted_lines": ["62-63", "97-98"]},
    {"scenario": 26, "probability": 0.009, "faulted_lines": ["91-93", "109-110"]},
    {"scenario": 27, "probability": 0.0778, "faulted_lines": ["91-92"]},
    {"scenario": 28, "probability": 0.0075, "faulted_lines": ["87-88", "89-90"]},
    {"scenario": 29, "probability": 0.0688, "faulted_lines": ["95-96"]},
    {"scenario": 30, "probability": 0.0733, "faulted_lines": ["87-88"]}
]

# Set 4 (30 Scenarios)
SET_4 = [
    {"scenario": 1, "probability": 0.0094, "faulted_lines": ["97-98", "98-99"]},
    {"scenario": 2, "probability": 0.0014, "faulted_lines": ["87-88", "95-96", "101-120"]},
    {"scenario": 3, "probability": 0.0664, "faulted_lines": ["60-61"]},
    {"scenario": 4, "probability": 0.0657, "faulted_lines": ["109-110"]},
    {"scenario": 5, "probability": 0.0094, "faulted_lines": ["87-89", "91-93"]},
    {"scenario": 6, "probability": 0.0072, "faulted_lines": ["87-88", "98-99"]},
    {"scenario": 7, "probability": 0.0715, "faulted_lines": ["89-91"]},
    {"scenario": 8, "probability": 0.0773, "faulted_lines": ["117-122"]},
    {"scenario": 9, "probability": 0.0065, "faulted_lines": ["97-98", "117-122"]},
    {"scenario": 10, "probability": 0.0079, "faulted_lines": ["62-63", "117-122"]},
    {"scenario": 11, "probability": 0.0729, "faulted_lines": ["95-96"]},
    {"scenario": 12, "probability": 0.0715, "faulted_lines": ["89-90"]},
    {"scenario": 13, "probability": 0.0065, "faulted_lines": ["100-123", "117-122"]},
    {"scenario": 14, "probability": 0.0072, "faulted_lines": ["98-99", "117-122"]},
    {"scenario": 15, "probability": 0.0079, "faulted_lines": ["91-92", "95-96"]},
    {"scenario": 16, "probability": 0.0072, "faulted_lines": ["91-93", "117-122"]},
    {"scenario": 17, "probability": 0.083, "faulted_lines": ["93-94"]},
    {"scenario": 18, "probability": 0.0751, "faulted_lines": ["87-89"]},
    {"scenario": 19, "probability": 0.0072, "faulted_lines": ["100-123", "109-110"]},
    {"scenario": 20, "probability": 0.0744, "faulted_lines": ["91-93"]},
    {"scenario": 21, "probability": 0.0079, "faulted_lines": ["97-98", "100-123"]},
    {"scenario": 22, "probability": 0.0809, "faulted_lines": ["100-123"]},
    {"scenario": 23, "probability": 0.0014, "faulted_lines": ["87-88", "91-92", "112-113"]},
    {"scenario": 24, "probability": 0.0671, "faulted_lines": ["93-95"]},
    {"scenario": 25, "probability": 0.0022, "faulted_lines": ["89-91", "97-98", "109-110"]},
    {"scenario": 26, "probability": 0.0072, "faulted_lines": ["95-96", "100-123"]},
    {"scenario": 27, "probability": 0.0079, "faulted_lines": ["86-87", "117-122"]},
    {"scenario": 28, "probability": 0.0072, "faulted_lines": ["67-68", "95-96"]},
    {"scenario": 29, "probability": 0.0072, "faulted_lines": ["89-90", "100-123"]},
    {"scenario": 30, "probability": 0.0751, "faulted_lines": ["86-87"]}
]

# Set 5 (50 Scenarios)
SET_5 = [
    {"scenario": 1, "probability": 0.0235, "faulted_lines": ["60-61", "98-99"]},
    {"scenario": 2, "probability": 0.0235, "faulted_lines": ["91-92", "99-100"]},
    {"scenario": 3, "probability": 0.0218, "faulted_lines": ["62-63", "112-113"]},
    {"scenario": 4, "probability": 0.0218, "faulted_lines": ["89-90", "117-122"]},
    {"scenario": 5, "probability": 0.0034, "faulted_lines": ["100-123", "103-104", "109-110"]},
    {"scenario": 6, "probability": 0.0286, "faulted_lines": ["89-90", "93-94"]},
    {"scenario": 7, "probability": 0.0235, "faulted_lines": ["62-63", "89-90"]},
    {"scenario": 8, "probability": 0.0218, "faulted_lines": ["86-87", "87-88"]},
    {"scenario": 9, "probability": 0.0235, "faulted_lines": ["89-91", "97-98"]},
    {"scenario": 10, "probability": 0.0202, "faulted_lines": ["100-123", "109-110"]},
    {"scenario": 11, "probability": 0.0218, "faulted_lines": ["89-91", "93-95"]},
    {"scenario": 12, "probability": 0.0252, "faulted_lines": ["91-92", "91-93"]},
    {"scenario": 13, "probability": 0.0235, "faulted_lines": ["87-89", "89-90"]},
    {"scenario": 14, "probability": 0.0235, "faulted_lines": ["87-89", "102-103"]},
    {"scenario": 15, "probability": 0.0303, "faulted_lines": ["86-87", "97-98"]},
    {"scenario": 16, "probability": 0.0218, "faulted_lines": ["99-100", "117-122"]},
    {"scenario": 17, "probability": 0.0034, "faulted_lines": ["89-90", "99-100", "109-110"]},
    {"scenario": 18, "probability": 0.0286, "faulted_lines": ["62-63", "87-89"]},
    {"scenario": 19, "probability": 0.0034, "faulted_lines": ["89-91", "110-112", "113-114"]},
    {"scenario": 20, "probability": 0.0218, "faulted_lines": ["91-93", "100-123"]},
    {"scenario": 21, "probability": 0.0235, "faulted_lines": ["91-93", "97-98"]},
    {"scenario": 22, "probability": 0.0252, "faulted_lines": ["60-61", "87-89"]},
    {"scenario": 23, "probability": 0.0252, "faulted_lines": ["87-89", "93-95"]},
    {"scenario": 24, "probability": 0.0286, "faulted_lines": ["100-123", "117-122"]},
    {"scenario": 25, "probability": 0.0034, "faulted_lines": ["95-96", "105-106", "117-122"]},
    {"scenario": 26, "probability": 0.0218, "faulted_lines": ["72-73", "117-122"]},
    {"scenario": 27, "probability": 0.0034, "faulted_lines": ["101-102", "102-103", "117-122"]},
    {"scenario": 28, "probability": 0.0252, "faulted_lines": ["93-95", "98-99"]},
    {"scenario": 29, "probability": 0.0034, "faulted_lines": ["97-98", "102-103", "109-110"]},
    {"scenario": 30, "probability": 0.0202, "faulted_lines": ["95-96", "98-99"]},
    {"scenario": 31, "probability": 0.0269, "faulted_lines": ["98-99", "99-100"]},
    {"scenario": 32, "probability": 0.0218, "faulted_lines": ["93-95", "95-96"]},
    {"scenario": 33, "probability": 0.0218, "faulted_lines": ["89-91", "91-93"]},
    {"scenario": 34, "probability": 0.0034, "faulted_lines": ["89-91", "95-96", "98-99"]},
    {"scenario": 35, "probability": 0.0218, "faulted_lines": ["87-89", "91-92"]},
    {"scenario": 36, "probability": 0.0235, "faulted_lines": ["60-61", "89-91"]},
    {"scenario": 37, "probability": 0.0252, "faulted_lines": ["86-87", "89-90"]},
    {"scenario": 38, "probability": 0.0269, "faulted_lines": ["60-61", "95-96"]},
    {"scenario": 39, "probability": 0.0252, "faulted_lines": ["99-100", "100-123"]},
    {"scenario": 40, "probability": 0.0034, "faulted_lines": ["89-91", "95-96", "101-102"]},
    {"scenario": 41, "probability": 0.0034, "faulted_lines": ["91-92", "100-123", "60-119"]},
    {"scenario": 42, "probability": 0.0235, "faulted_lines": ["91-92", "117-122"]},
    {"scenario": 43, "probability": 0.0218, "faulted_lines": ["60-61", "97-98"]},
    {"scenario": 44, "probability": 0.0218, "faulted_lines": ["60-61", "62-63"]},
    {"scenario": 45, "probability": 0.0286, "faulted_lines": ["89-91", "99-100"]},
    {"scenario": 46, "probability": 0.0269, "faulted_lines": ["97-98", "109-110"]},
    {"scenario": 47, "probability": 0.005, "faulted_lines": ["62-63", "99-100", "117-122"]},
    {"scenario": 48, "probability": 0.0218, "faulted_lines": ["62-63", "93-95"]},
    {"scenario": 49, "probability": 0.0218, "faulted_lines": ["87-89", "89-91"]},
    {"scenario": 50, "probability": 0.0303, "faulted_lines": ["89-91", "93-94"]}
]
