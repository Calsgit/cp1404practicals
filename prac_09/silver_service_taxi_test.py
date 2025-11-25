from silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi("Silver Boy", 100, 1.5)
print(silver_taxi)
silver_taxi.drive(1)
print(silver_taxi.get_fare())