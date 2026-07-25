
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

---------------------
__all__ declares what should be exported when another file uses.

```python
# config is the file name
from config import *
```
if __name__ == "__main__"
It is a conditional block used to control the execution of code depending on how the Python file is launched.

When you execute a script from the terminal (e.g., python myscript.py), Python assigns the string "__main__" to the __name__ variable. The condition evaluates to True, and the code inside the block executes.

Importing as a Module: When you import the file into another script (e.g., import myscript), Python assigns the actual name of the file ("myscript") to the __name__ variable. The condition evaluates to False

------------------------
config.py centralizes the pipeline’s paths, forecast dates, model parameters, calibration values, and business rules. I used a dataclass to define a structured configuration object with defaults and type annotations. Mutable settings such as nested dictionaries use default_factory, ensuring each configuration instance receives its own dictionary. Calculated properties select values based on whether the run is quarterly or annual. The post-initialization method creates the required output directories, while validation methods check file availability and parameter logic. The module creates one shared configuration instance that the pipeline scripts import.
