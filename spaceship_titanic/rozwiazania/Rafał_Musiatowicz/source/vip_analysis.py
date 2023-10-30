import pandas as pd

data = pd.read_csv(r"spaceship_titanic\dane.csv")

vip = data[data["VIP"] == True]
not_vip = data[data["VIP"] == False]

room_service_vip = vip["RoomService"].mean()
room_service_not_vip = not_vip["RoomService"].mean()

columns_of_interest = ["RoomService", "FoodCourt", "ShoppingMall", "Spa", "VRDeck"]

avg_vip = vip[columns_of_interest].mean()
avg_not_vip = not_vip[columns_of_interest].mean()
print()
print("Medium money spent by VIP:")
print(avg_vip, "\n")
print("Medium money spent by not VIP:")
print(avg_not_vip, "\n")

sum_vip1 = vip[columns_of_interest].sum(axis=1)
sum_not_vip1 = not_vip[columns_of_interest].sum(axis=1)

avg_sum_vip1 = sum_vip1.mean()
avg_sum_not_vip1 = sum_not_vip1.mean()

print("Sum of average expeses VIP: ", avg_sum_vip1)
print("Sum of average expeses not VIP: ",avg_sum_not_vip1, "\n")

print("Amount of VIP in cryosleep: ", len( (data[ (data["VIP"] == True) & (data["CryoSleep"] == True) ]) ))
print("Amount of not VIP in cryosleep: ", len( (data[ (data["VIP"] == True) & (data["CryoSleep"] == False) ]) ))
print("Amount of awaken VIPs: ", len( (data[ (data["VIP"] == False) & (data["CryoSleep"] == True) ]) ))
print("Amount of awaken not VIPs: ", len( (data[ (data["VIP"] == False) & (data["CryoSleep"] == False) ]) ))

print("Precentage of VIP sleeping: ", str(21/175*100) + "%")
print("Precentage of not VIP sleeping: ", str(2941/5143*100) + "%")

print()
print("Relationship between age and VIP:")
step = 5
sum = 0
for i in range (0, 80, step):
    age_filter = (vip["Age"] >= i) & (vip["Age"] < i+step)
    print("<" + str(i) + "," + str(i+step-1) + ">", len(vip[age_filter]) )
