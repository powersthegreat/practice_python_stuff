import pandas as pandas
from pandas import DataFrame

with open('names.txt', 'r') as open_file:
    all_text = open_file.read()

list_from_text = all_text.split("\n")

list_from_text_stripped = []

for links in list_from_text:
    stripped = links[3:]
    list_from_text_stripped.append(stripped)

catagories_all = []
catagories = []
catagories_counts = []
index_list = []

for i in range(0, len(catagories)):
    index_list.append(i)

for cats in list_from_text_stripped:
    index = cats.find("/")
    catagories_all.append(cats[0:int(index)])

for i in range(0,len(catagories_all),50):
    catagories.append(catagories_all[i])


for cats in catagories:
    count = all_text.count(str(cats))
    catagories_counts.append(count)

for i in range(0, len(catagories)):
    index_list.append(i)

cleaned = catagories_counts.pop(-1)
 
catagories_counts_dict = dict(zip(index_list, zip(catagories, catagories_counts)))

data_frame_dict = pandas.DataFrame(catagories_counts_dict)
data_frame_dict.to_csv("catagory_to_count_of_image.csv", index = False)

#godamn I'm getting good