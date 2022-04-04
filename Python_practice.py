counties=["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver':
    print(counties[1])

counties=["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")

for county in counties:
    print(county)  

numbers=[0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_tuples=("arapahoe","Denver","Jefferson")

for i in range(len(counties_tuples)):
    print(counties_tuples[i])

counties_dict={"Arapahoe":369237,"Denver":413229,"Jefferson":390222}
for county, voters in counties_dict.items():
    print(county+" county has "+str(voters)+" registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")



