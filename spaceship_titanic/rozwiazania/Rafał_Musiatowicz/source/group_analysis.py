import pandas as pd

data = pd.read_csv(r"spaceship_titanic\dane.csv")

data["Group"] = data["PassengerId"].str.split('_').str[0]
data["Surname"] = data["Name"].str.split(' ').str[1]

i=0
multi_group_count = 0
multi_group_family_count = 0
same_src_count = 0
same_dst_count = 0
while i<8693:
    j=1
    surname = data["Surname"][i]
    from_one_family = True
    same_src = True
    same_dst = True
    while  i+j < 8693 and data["Group"][i] == data["Group"][i+j]:
        if data["Surname"][i+j] != surname:
            from_one_family = False
        if data["HomePlanet"][i] != data["HomePlanet"][i+j]:
            same_src = False
        if data["Destination"][i] != data["Destination"][i+j]:
            same_dst = False
        j += 1
    if j > 1:
        multi_group_count += 1
        if from_one_family:
            multi_group_family_count += 1
        if same_src:
            same_src_count += 1
        if same_dst:
            same_dst_count += 1
    i += j

print()
print("Ilość grup wieloosobowych:", multi_group_count)
print("Ilość grup wieloosobowych wyłącznie z członkami jednej rodziny:", multi_group_family_count)
print("Ilość grup wieloosobowych, gdzie wszyscy członkowie grupy startują z tej samej planety:", same_src_count)
print("Ilość grup wieloosobowych, gdzie członkowie grupy startują z innych planet:",same_dst_count)