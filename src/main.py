Antal_motorer = int(input("How many motors are carrying the packages? "))
Kg_pakker = int(input("How many kg of packages do we expect? "))
if Kg_pakker/ Antal_motorer <= 12:
    print("Yes! The conveyor belt can carry the packages.")
else:
    print("No. The conveyor belt cannot carry the packages.")
