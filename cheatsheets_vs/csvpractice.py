import pandas 
from pandas import DataFrame

friends = [{"name": "Jon", "age": 37, "job": "student"}, 
            {"name": "Will", "age": 19, "job": "student"},
            {"name": "Matt", "age": 18, "job": "student"}]
names = {"First": ["William", "Matthew", "Brian", "Kathleen"], "Middle Initial": ["F", "N", "N", "C"]}

data_frame_friends = pandas.DataFrame(friends)
data_frame_names = pandas.DataFrame(names)
data_frame_friends.to_csv("friends.csv", header = True, index = True)
data_frame_names.to_csv("names.csv", header = True, index = False)