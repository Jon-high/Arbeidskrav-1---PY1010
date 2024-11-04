# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:11:32 2024
Arbeidskrav nr. 1
@author: Jon-k
"""
# Definerer funksjonen for å beregne årlige kostnader
def beregn_kostnader(km_per_aar, forsikring_bensinbil, forsikring_elbil, trafikkforsikringsavgift, drivstoff_elbil, 
drivstoffpris_bensinbil, drivstoffpris_elbil, bom_bensin, bom_elbil):

    # Beregner årlig kostnad for elbil
    kostnad_elbil = (forsikring_elbil + 
                 (trafikkforsikringsavgift * 365) + 
                 (drivstoff_elbil * drivstoffpris_elbil * km_per_aar) + 
                 (bom_elbil * km_per_aar))
      
    # Beregner årlig kostnad for bensinbil
    kostnad_bensinbil = (forsikring_bensinbil + 
                     (trafikkforsikringsavgift * 365) + 
                     (drivstoffpris_bensinbil * km_per_aar) + 
                     (bom_bensin * km_per_aar)) 

    #Beregn kostnadsdifferansen på elbil og bensinbil
    kostnadsdifferanse = kostnad_bensinbil - kostnad_elbil

    return kostnad_bensinbil, kostnad_elbil, kostnadsdifferanse

# Inputverdier
km_per_aar = 10000 # Pr. år
forsikring_bensinbil = 7500 # Pr. år
forsikring_elbil = 5000 # Pr. år
trafikkforsikringsavgift = 8.38 # Pr. dag
drivstoff_bensinbil = 1 # kr pr. km
drivstoff_elbil = 0.2 # drivstoff forbruk for elbil (kr/kWh)
drivstoffpris_elbil = 2 # Kr/kWh
bom_bensin = 0.3 # kr/km
bom_elbil = 0.1 #kr/km

# Beregn kostnadene
kostnad_bensinbil, kostnad_elbil, kostnadsdifferanse = beregn_kostnader (km_per_aar, forsikring_bensinbil, forsikring_elbil, trafikkforsikringsavgift, drivstoff_bensinbil,drivstoff_elbil, drivstoffpris_elbil, bom_elbil, bom_bensin)

# Presenterer resultatene
print(f"Årlige totalkostnader for elbil:{kostnad_elbil: .2f} kr")
print(f"Årlige totalkostnader for bensinbil:{kostnad_bensinbil: .2f} kr") 
print(f"Årlige kostnadsdifferanse:{kostnadsdifferanse: .2f} kr")          