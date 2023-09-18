from Prac_09.taxi import Taxi

def main():
    prius_1 = Taxi(100, "Prius 1")
    # 2. Drive the taxi 40 km
    prius_1.drive(40)
    # 3. Print the taxi's details and the current fare
    print(prius_1)
    # 4. Restart the meter (start a new fare) and then drive the car 100 km
    prius_1.start_fare()
    prius_1.drive(100)
    # 5. Print the details and the current fare
    print(prius_1)


main()