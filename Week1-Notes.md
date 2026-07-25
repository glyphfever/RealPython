
```python
# 1. import
from dataclasses import dataclass, field

# 2. decorator
@dataclass

# 3. define
# Use : after a variable name if including data type
class GlobalConfig:
  baseline_year: int = 2025
```
Becasuse it has standard __init__(), we don't need to write self defined functions.

--------------------------------------------

```python
'''
field with default_factory argument to create separate mutable default values for each instance
lambda: inline function returns the dictionary

A function that creates default value whenever a new GlobalConfig object is instantiated.
Otherwise, dataclasses reject mutable defaults such as dictionaries and lists because multiple instances could accidentally share the same object.
'''
tier_config: Dict = field(default_factory=lambda: {
        'PLT': {
            'n_tiers': 5,      # 5 tiers for PLT
            'cap_pct': 0.10    # Max 10% price increase
        },
        'Commercial': {
            'n_tiers': 5,      # 5 tiers for Commercial
            'cap_pct': 0.12    # Max 12% price increase
        },
        'Parts': {
            'n_tiers': 3,      # 3 tiers for Parts
            'cap_pct': 0.08    # Max 8% price increase
        }
    })
```
How to access?
```python
global_config.tier_config
global_config.tier_config['PLT']
global_config.tier_config['PLT'][n_tiers]
```
Put @property before a method in a class so we can access it like an ordinary attribute. Otherwise, call it with "()". <br>
global_config.forecast_horizon_end() <br>
global_config.forecast_horizon_end





