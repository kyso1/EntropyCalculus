import math
from collections import Counter

def entropy(labels):
    """Calcula a entropia de um conjunto de dados."""
    n = len(labels)
    if n <= 1:
        return 0
    counts = Counter(labels)
    probs = [count / n for count in counts.values()]
    return -sum(p * math.log2(p) for p in probs)

def information_gain(data, target_attr):
    """Calcula o ganho de informação de cada atributo em relação ao atributo alvo."""
    # Calcula a entropia do atributo alvo
    target_labels = [row[target_attr] for row in data]
    target_entropy = entropy(target_labels)
    # Calcula a entropia de cada atributo
    attributes = data[0].keys()
    gains = {}
    for attr in attributes:
        if attr == target_attr:
            continue
        labels = [row[attr] for row in data]
        unique_labels = set(labels)
        attr_entropy = 0
        for label in unique_labels:
            subset = [row for row in data if row[attr] == label]
            subset_entropy = entropy([row[target_attr] for row in subset])
            attr_entropy += (len(subset) / len(data)) * subset_entropy
        gains[attr] = target_entropy - attr_entropy

    return gains

def information_gain_ratio(data, target_attr):
    """Calcula o ganho de informação de cada atributo em relação ao atributo alvo (Atributos Maiores)."""
    # Calcula a entropia do atributo alvo
    target_labels = [row[target_attr] for row in data]
    target_entropy = entropy(target_labels)
    # Calcula a entropia de cada atributo 
    attributes = data[0].keys()
    gains = {}
    for attr in attributes:
        if attr == target_attr:
            continue
        labels = [row[attr] for row in data]
        unique_labels = set(labels)
        attr_entropy = 0
        for label in unique_labels:
            subset = [row for row in data if row[attr] == label]
            subset_entropy = entropy([row[target_attr] for row in subset])
            attr_entropy += (len(subset) / len(data)) * subset_entropy
        # Calcula o ganho de informacao
        gain = target_entropy - attr_entropy
        # Calcula a divisao
        split_info = entropy(labels)
        # Calculate a razao do ganho de informação
        gain_ratio = gain / split_info
        gains[attr] = gain_ratio

    return gains

# data=[
#         {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High","Play": "No"},
#         {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Play": "No"},
#         {"Outlook": "Overcast", "Temperature": "Hot", "Humidity": "High","Play": "Yes"},
#         {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "High","Play": "Yes"},
#         {"Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal","Play": "Yes"},
#         {"Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal","Play": "No"},
#         {"Outlook": "Overcast", "Temperature": "Cool", "Humidity": "Normal","Play": "Yes"},
#         {"Outlook": "Sunny", "Temperature": "Mild", "Humidity": "High","Play": "No"},
#         {"Outlook": "Sunny", "Temperature": "Cool", "Humidity": "Normal","Play": "Yes"},
#         {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "Normal","Play": "Yes"},
#         {"Outlook": "Sunny", "Temperature": "Mild", "Humidity": "Normal","Play": "Yes"},
#         {"Outlook": "Overcast", "Temperature": "Mild", "Humidity": "High","Play": "Yes"},
#         {"Outlook": "Overcast", "Temperature": "Hot", "Humidity": "Normal","Play": "Yes"},
#         {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "High","Play": "No"}
#     ]


#dataset novo com wind
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
  
    
