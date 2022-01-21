from txt_to_dict_to_csv import catagories_counts_dict
import matplotlib
from matplotlib import pyplot as plt

imported_dict = catagories_counts_dict

def split_with_tuple(dict):
    return dict.keys(), tuple(dict.values())

keys_values_list = split_with_tuple(imported_dict)
index_list = keys_values_list[0]
values = keys_values_list[1]

catagories_list = []
counts_list = []
for items in values:
    catagories_list.append(items[0])
    counts_list.append(items[1])

plt.figure()
ax = plt.subplot(1, 1, 1)
plt.bar(index_list, counts_list)
plt.title("Pictures per Catagory")
plt.xlabel("Catagories")
plt.ylabel("Number of Pictures")
plt.savefig("matplotlib_practice.png")
