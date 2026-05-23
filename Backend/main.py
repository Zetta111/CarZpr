
import pandas as pd

df=pd.read_csv("/Users/zetta/CarzPR/luxury_sedans_2024_2026.csv")
df.columns = df.columns.str.strip()





def power_to_wieght_ratio(hp,weight):
    res=(hp/weight)*1000
    return res

def horsepower_per_dollar(hp,price):
    res=(price/hp) 
    return res

def torque_to_weight_ratio(weight,torque):
    res=(torque/weight)
    return res




def car_spec():
    
    try:
        user_make = input("Please Enter car Make :").strip().title()
        user_model = input("Please Enter car Model: ").strip().title()
        user_year= int(input("Please Enter Car Year:").strip())
        
        result = df[
        (df["Make"]==user_make)&
        (df["Model"]==user_model)&
        (df["Year"]==(user_year))]

        car_price=result["MSRP (USD)"].values[0]
        torque_val=result["Torque (lb-ft)"].values[0]
        if result.empty:
            print("Car Not found")
        else:
            HP = result["Horsepower (hp)"].values[0]
            Weight=result["Curb Weight (lbs)"].values[0]
            pwtr=power_to_wieght_ratio(HP,Weight)
            hpd=horsepower_per_dollar(HP,car_price)
            ttw=torque_to_weight_ratio(HP,torque_val)
            print(f"Power to weight ration: {pwtr:.4f}")
            print(f"horsepower per dollar: {hpd:.4f}")
            print(f"Torque to weight ratio: {ttw:.4f}")

    except Exception:
        if user_make not in df["Make"].value:
            print("incorrect car make")
        elif user_model not in df["Model"].value:
            print("incorrect car model ")
        else :
            print("incorrect car year")




car_spec()



##power to weight ratio (HP/wieght) x 1000
## for any car from the csv file i want to caclaulte the pwoer to weight ratio and return it.


#horsepower rankings


