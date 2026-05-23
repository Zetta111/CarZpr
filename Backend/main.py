import csv
import io
import pandas as pd

df=pd.read_csv("/Users/zetta/CarzPR/luxury_sedans_2024_2026.csv")
df.columns = df.columns.str.strip()

UserMake = input("Please Enter car Make :").strip().title()
UserModel = input("Please Enter car Model: ").strip().title()
UserYear= int(input("Please Enter Car Year:").strip())

result = df[
    (df["Make"]==UserMake)&
    (df["Model"]==UserModel)&
    (df["Year"]==(UserYear))
]




def PTWR(hp,weight):
    res=(hp/weight)*1000
    print(f"Power TO Weight Ratio:{res:.4f}")

HP = result["Horsepower (hp)"].values[0]
Weight=result["Curb Weight (lbs)"].values[0]
PTWR(HP,Weight)


##power to weight ratio (HP/wieght) x 1000
## for any car from the csv file i want to caclaulte the pwoer to weight ratio and return it.


#horsepower rankings


