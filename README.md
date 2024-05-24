# Information Gain and Gain Ratio Calculation

This repository contains Python functions for calculating entropy, information gain, and information gain ratio for a given dataset. These concepts are fundamental in fields like data science and machine learning, particularly in decision tree algorithms. I created it to use on an activity at college.

## Table of Contents

- [Introduction](#introduction)
- [Functions](#functions)
  - [entropy](#entropy)
  - [information_gain](#information_gain)
  - [information_gain_ratio](#information_gain_ratio)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Introduction

This project provides implementations of:

- **Entropy**: Measures the impurity or uncertainty in a dataset.
- **Information Gain**: Quantifies the reduction in entropy when a dataset is split on an attribute.
- **Information Gain Ratio**: Adjusts the information gain by taking into account the intrinsic information of a split, addressing the bias towards attributes with many distinct values.

## Functions

### `entropy(labels)`

Calculates the entropy of a dataset.

- **Parameters**:
  - `labels`: A list of labels (target values).

- **Returns**: 
  - A float representing the entropy.

### `information_gain(data, target_attr)`

Calculates the information gain of each attribute with respect to the target attribute.

- **Parameters**:
  - `data`: A list of dictionaries representing the dataset.
  - `target_attr`: The target attribute (string) for which to calculate the information gain.

- **Returns**: 
  - A dictionary where keys are attributes and values are the information gain for each attribute.

### `information_gain_ratio(data, target_attr)`

Calculates the information gain ratio of each attribute with respect to the target attribute.

- **Parameters**:
  - `data`: A list of dictionaries representing the dataset.
  - `target_attr`: The target attribute (string) for which to calculate the information gain ratio.

- **Returns**: 
  - A dictionary where keys are attributes and values are the information gain ratio for each attribute.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/information-gain.git
   cd information-gain
   ```

2. Use the functions in your Python code:
   ```python
   from entropy import entropy, information_gain, information_gain_ratio
   
   # Example data
   data = [
       {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Wind": "Weak", "Play": "No"},
       {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Wind": "Strong", "Play": "No"},
       # ... (other rows)
   ]
   
   # Calculate information gain
   gain = information_gain(data, "Play")
   print(gain)
   
   # Calculate information gain ratio
   gain_ratio = information_gain_ratio(data, "Play")
   print(gain_ratio)
   ```

3. Run the script to see the results:
   ```bash
   python your_script.py
   ```

## Examples

Below is an example of how to use the provided functions with a sample dataset:

```python
data = [
    {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Wind": "Weak", "Play": "No"},
    {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Wind": "Strong", "Play": "No"},
    {"Outlook": "Overcast", "Temperature": "Hot", "Humidity": "High", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "High", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "Play": "No"},
    {"Outlook": "Overcast", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "Play": "Yes"},
    {"Outlook": "Sunny", "Temperature": "Mild", "Humidity": "High", "Wind": "Weak", "Play": "No"},
    {"Outlook": "Sunny", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "Normal", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Sunny", "Temperature": "Mild", "Humidity": "Normal", "Wind": "Strong", "Play": "Yes"},
    {"Outlook": "Overcast", "Temperature": "Mild", "Humidity": "High", "Wind": "Strong", "Play": "Yes"},
    {"Outlook": "Overcast", "Temperature": "Hot", "Humidity": "Normal", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "High", "Wind": "Strong", "Play": "No"}
]

print("Calculo de ganho de informacao:")
gain = information_gain(data, "Play")
for attr, info_gain in gain.items():
    print(f"{attr}: {round(info_gain, 4)}")
    
print("\nCalculo de ganho de razao:")
gain_ratio = information_gain_ratio(data, "Play")
for attr, info_gain_ratio in gain_ratio.items():
    print(f"{attr}: {round(info_gain_ratio, 4)}")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to contribute to this project by submitting issues or pull requests. Happy coding!
