#Alex Maximilian

overseas_airport_code = []
overseas_airport_name = []
distance_from_liverpool = []
distance_from_bourne =[]
uk_code = []
oversea_code = []
aircraft_type = []
first_class = []



#Reads relevant data files and process the read data 

with open('Airports.csv', 'r') as f:
    read_file = f.read()
    read_file_split = (read_file.split('\n'))
    for i in read_file_split:

        try:
            overseas_airport_code.append(i.split(',')[0])
            overseas_airport_name.append(i.split(',')[1])
            distance_from_liverpool.append(i.split(',')[2])
            distance_from_bourne.append(i.split(',')[3])
        except Exception:
            pass

#Main class with all the functions
class Airport:
    def __init__(self):
        self.medium_narrow_body = {"Type": "Medium narrow body", "Running Cost per seat per 100 km": 8, "Maximum flight range (km)": 2650,
                          "Capacity if all seats are standard-class": 180, "Minimum number of first class seats (if there are any)": 8}

        self.large_narrow_body = {"Type": "Large narrow body", "Running Cost per seat per 100 km": 7, "Maximum flight range (km)": 5600,
                          "Capacity if all seats are standard-class": 220, "Minimum number of first class seats (if there are any)": 10}

        self.medium_wide_body = {"Type": "Medium wide body", "Running Cost per seat per 100 km": 5, "Maximum flight range (km)": 4050,
                          "Capacity if all seats are standard-class": 406, "Minimum number of first class seats (if there are any)": 14}



    def number_of_standard_class_seats(self, all_seats, first_class_seats):
        return all_seats-(first_class_seats*2)

    def flight_cost_per_seat(self, cost_per_100, distance):
        return cost_per_100*(int(distance)/100)

    def flight_cost(self, flight_cost_perseat, first_class_seats, standard_seats):
        return float(flight_cost_perseat)*(int(first_class_seats)+int(standard_seats))

    def flight_income(self,first_class_seats, price_of_first_class_seat, standard_class_seat, price_of_standard_class_seat):
        return int(first_class_seats*price_of_first_class_seat)+int(standard_class_seat*price_of_standard_class_seat)

    def flight_profit(self, flight_income, flight_cost):
        return int(flight_income)-int(flight_cost)

    def clear_data(self):
        pass

    def airpot_input(self):
        code_input = str(input("Please enter the three-letter airport code in capital letters for the UK airport: "))
        while code_input in ["LPL", "BOH"]:
            uk_code.append(code_input)
            overseas_code_input = str(input("Please enter the three-letter airport code in capital letters for the Overseas airport: "))
            while overseas_code_input in overseas_airport_code:
                oversea_code.append(overseas_code_input)
                index = overseas_airport_code.index(overseas_code_input)
                print("\n{: <12} {: <12}\n".format("Airport Name: ", overseas_airport_name[index]))
                return [code_input, overseas_code_input]
            else:
                print("\nPlease enter a valid airport code")
                self.mainmenu()
                run()
        else:
            print("\nPlease enter a valid airport code")
            self.mainmenu()
            run()



    def aircrafttype(self):
        self.type_input = str(input("Please enter the type of aircraft: "))
        while self.type_input.lower() not in [self.medium_narrow_body["Type"].lower(),
                                         self.large_narrow_body["Type"].lower(), self.medium_wide_body["Type"].lower()]:
            print("Incorrect Input!")
            self.mainmenu()
            run()

        if self.type_input.lower() in [self.medium_narrow_body["Type"].lower(), self.large_narrow_body["Type"].lower(),
                                  self.medium_wide_body["Type"].lower()]:
            aircraft_type.append(self.type_input.lower())
            if self.type_input.lower() == self.medium_narrow_body["Type"].lower():
                print("\n")
                for k, v in self.medium_narrow_body.items():
                    print(f"{k}:  {v}")
                print("\n")

                self.first_class_seat_input = int(input("Enter first class seat on the aircraft: "))
                if self.first_class_seat_input > 0:
                    if self.first_class_seat_input < self.medium_narrow_body[
                        "Minimum number of first class seats (if there are any)"]:
                        print("First Class Seats are less than the condition! Please enter correct input!")
                        self.mainmenu()
                        run()

                    elif self.first_class_seat_input > (
                            self.medium_narrow_body["Capacity if all seats are standard-class"] / 2):
                        print("Number of seats are greater than the limit! Please enter correct input!")
                        self.mainmenu()
                        run()

                    else:
                        first_class.append(self.first_class_seat_input)
                        calculate_seats = self.number_of_standard_class_seats(
                            self.medium_narrow_body["Capacity if all seats are standard-class"],
                            self.first_class_seat_input)

                        print("\nNumber of standard class seats on the aircraft:  ", calculate_seats)

                        self.mainmenu()
                        run()

                else:
                    print("Incorrect Input!")
                    self.mainmenu()
                    run()


            elif self.type_input.lower() == self.large_narrow_body["Type"].lower():
                aircraft_type.append(self.type_input.lower())
                print("\n")
                for k, v in self.large_narrow_body.items():
                    print(f"{k}:  {v}")

                self.first_class_seat_input = int(input("Enter first class seat on the aircraft: "))
                if self.first_class_seat_input != 0:
                    if self.first_class_seat_input < self.large_narrow_body[
                        "Minimum number of first class seats (if there are any)"]:
                        print("First Class Seats are less than the condition! Please enter correct input!")
                        self.mainmenu()
                        run()

                    elif self.first_class_seat_input > (
                            self.large_narrow_body["Capacity if all seats are standard-class"] / 2):
                        print("Number of seats are greater than the limit! Please enter correct input!")
                        self.mainmenu()
                        run()

                    else:
                        first_class.append(self.first_class_seat_input)
                        calculate_seats = self.number_of_standard_class_seats(
                            self.large_narrow_body["Capacity if all seats are standard-class"],
                            self.first_class_seat_input)

                        print("\nNumber of standard class seats on the aircraft:  ", calculate_seats)

                        self.mainmenu()
                        run()

            elif self.type_input.lower() == self.medium_wide_body["Type"].lower():
                aircraft_type.append(self.type_input.lower())
                print("\n")
                for k, v in self.medium_wide_body.items():
                    print(f"{k}:  {v}")

                self.first_class_seat_input = int(input("Enter first class seat on the aircraft: "))
                if self.first_class_seat_input != 0:
                    if self.first_class_seat_input < self.medium_wide_body[
                        "Minimum number of first class seats (if there are any)"]:
                        print("First Class Seats are less than the condition! Please enter correct input!")
                        self.mainmenu()
                        run()

                    elif self.first_class_seat_input > (
                            self.medium_wide_body["Capacity if all seats are standard-class"] / 2):
                        print("Number of seats are greater than the limit! Please enter correct input!")
                        self.mainmenu()
                        run()

                    else:
                        first_class.append(self.first_class_seat_input)
                        calculate_seats = self.number_of_standard_class_seats(
                            self.medium_wide_body["Capacity if all seats are standard-class"],
                            self.first_class_seat_input)

                        print("\nNumber of standard class seats on the aircraft:  ", calculate_seats)

                        self.mainmenu()
                        run()



    def price_plan(self, uk_code, oversea_code):

        if oversea_code == None or uk_code == None:
            print("Please enter UK and Overseas Airport codes to proceed!")
            self.mainmenu()
            run()

        elif len(aircraft_type) < 1:
            print("Please enter aircraft type to proceed!")
            self.mainmenu()
            run()

        elif len(first_class) < 1:
            print("Please enter number of first class seats to proceed!")
            self.mainmenu()
            run()
        else:
            if uk_code == "LPL":
                index = overseas_airport_code.index(oversea_code)
                distance = distance_from_liverpool[index]
                print(f"Distance: {distance}")
                if self.type_input == "medium narrow body" and int(distance) <= self.medium_narrow_body["Maximum flight range (km)"]:
                    standard_price_input = int(input("Please enter price of standard-class seat: "))
                    first_price_input = int(input("Please enter price of first-class seat: "))

                    flightcostperseat = self.flight_cost_per_seat(self.medium_narrow_body["Running Cost per seat per 100 km"],
                                                             distance)
                    standardseats = self.number_of_standard_class_seats(
                        self.medium_narrow_body["Capacity if all seats are standard-class"], self.first_class_seat_input)

                    flightcost = self.flight_cost(flightcostperseat, self.first_class_seat_input, standardseats)

                    flightincome = self.flight_income(self.first_class_seat_input, first_price_input, standardseats,
                                                 standard_price_input)
                    flightprofit = self.flight_profit(flightincome, flightcost)

                    print("\n{} {}\n\n{} {}\n\n{} {}\n\n{} {}\n".format("Flight Cost Per Seat: ",
                                                                                 flightcostperseat,
                                                                                 "Flight Cost: ",
                                                                                 flightcost,
                                                                                 "Flight Income: ",
                                                                                 flightincome,
                                                                                 "Flight Profit",
                                                                                 flightprofit))

                    return ""


                elif self.type_input == "large narrow body" and int(distance) <= self.large_narrow_body["Maximum flight range (km)"]:
                    standard_price_input = int(input("Please enter price of standard-class seat: "))
                    first_price_input = int(input("Please enter price of first-class seat: "))

                    flightcostperseat = self.flight_cost_per_seat(
                        self.large_narrow_body["Running Cost per seat per 100 km"], distance)
                    standardseats = self.number_of_standard_class_seats(
                        self.large_narrow_body["Capacity if all seats are standard-class"],
                        self.first_class_seat_input)
                    flightcost = self.flight_cost(flightcostperseat, self.first_class_seat_input, standardseats)
                    flightincome = self.flight_income(self.first_class_seat_input, first_price_input,
                                                 standardseats, standard_price_input)
                    flightprofit = self.flight_profit(flightincome, flightcost)

                    print(
                        "\n{} {}\n\n{} {}\n\n{} {}\n\n{} {}\n".format("Flight Cost Per Seat: ",
                                                                               flightcostperseat,
                                                                               "Flight Cost: ",
                                                                               flightcost,
                                                                               "Flight Income: ",
                                                                               flightincome,
                                                                               "Flight Profit",
                                                                               flightprofit))
                    return ""


                elif self.type_input == "medium wide body" and int(distance) <= self.medium_wide_body["Maximum flight range (km)"]:
                    standard_price_input = int(input("Please enter price of standard-class seat: "))
                    first_price_input = int(input("Please enter price of first-class seat: "))

                    flightcostperseat = self.flight_cost_per_seat(
                        self.medium_wide_body["Running Cost per seat per 100 km"], distance)
                    standardseats = self.number_of_standard_class_seats(
                        self.medium_wide_body["Capacity if all seats are standard-class"],
                        self.first_class_seat_input)
                    flightcost = self.flight_cost(flightcostperseat, self.first_class_seat_input, standardseats)
                    flightincome = self.flight_income(self.first_class_seat_input, first_price_input,
                                                 standardseats, standard_price_input)
                    flightprofit = self.flight_profit(flightincome, flightcost)

                    print(
                        "\n{} {}\n\n{} {}\n\n{} {}\n\n{} {}\n".format("Flight Cost Per Seat: ",
                                                                               flightcostperseat,
                                                                               "Flight Cost: ",
                                                                               flightcost,
                                                                               "Flight Income: ",
                                                                               flightincome,
                                                                               "Flight Profit",
                                                                               flightprofit))
                    return ""

                else:
                    print("Distance exceeds aircraft total limit!")
                    self.mainmenu()
                    run()

            elif uk_code == "BOH":
                index = overseas_airport_code.index(oversea_code)
                distance = distance_from_bourne[index]
                if self.type_input == "medium narrow body" and int(distance) >= self.medium_narrow_body[
                    "Maximum flight range (km)"]:
                    standard_price_input = int(input("Please enter price of standard-class seat: "))
                    first_price_input = int(input("Please enter price of first-class seat: "))

                    flightcostperseat = self.flight_cost_per_seat(
                        self.medium_narrow_body["Running Cost per seat per 100 km"], distance)
                    standardseats = self.number_of_standard_class_seats(
                        self.medium_narrow_body["Capacity if all seats are standard-class"],
                        self.first_class_seat_input)
                    flightcost = self.flight_cost(flightcostperseat, self.first_class_seat_input, standardseats)
                    flightincome = self.flight_income(self.first_class_seat_input, first_price_input,
                                                 standardseats, standard_price_input)
                    flightprofit = self.flight_profit(flightincome, flightcost)

                    print(
                        "\n{} {}\n\n{} {}\n\n{} {}\n\n{} {}\n\n{} {}\n".format("Flight Cost Per Seat: ",
                                                                               flightcostperseat,
                                                                               "Flight Cost: ",
                                                                               flightcost,
                                                                               "Flight Income: ",
                                                                               flightincome,
                                                                               "Flight Profit",
                                                                               flightprofit))
                    return ""


                elif self.type_input == "large narrow body" and int(distance) >= self.large_narrow_body[
                    "Maximum flight range (km)"]:
                    standard_price_input = int(input("Please enter price of standard-class seat: "))
                    first_price_input = int(input("Please enter price of first-class seat: "))

                    flightcostperseat = self.flight_cost_per_seat(
                        self.large_narrow_body["Running Cost per seat per 100 km"], distance)
                    standardseats = self.number_of_standard_class_seats(
                        self.large_narrow_body["Capacity if all seats are standard-class"],
                        self.first_class_seat_input)
                    flightcost = self.flight_cost(flightcostperseat, self.first_class_seat_input, standardseats)
                    flightincome = self.flight_income(self.first_class_seat_input, first_price_input,
                                                 standardseats, standard_price_input)
                    flightprofit = self.flight_profit(flightincome, flightcost)

                    print(
                        "\n{} {}\n\n{} {}\n\n{} {}\n\n{} {}\n\n{} {}\n".format("Flight Cost Per Seat: ",
                                                                               flightcostperseat,
                                                                               "Flight Cost: ",
                                                                               flightcost,
                                                                               "Flight Income: ",
                                                                               flightincome,
                                                                               "Flight Profit",
                                                                               flightprofit))
                    return ""


                elif self.type_input == "medium wide body" and int(distance) >= self.medium_wide_body[
                    "Maximum flight range (km)"]:
                    standard_price_input = int(input("Please enter price of standard-class seat: "))
                    first_price_input = int(input("Please enter price of first-class seat: "))

                    flightcostperseat = self.flight_cost_per_seat(
                        self.medium_wide_body["Running Cost per seat per 100 km"], distance)
                    standardseats = self.number_of_standard_class_seats(
                        self.medium_wide_body["Capacity if all seats are standard-class"],
                        self.first_class_seat_input)
                    flightcost = self.flight_cost(flightcostperseat, self.first_class_seat_input, standardseats)
                    flightincome = self.flight_income(self.first_class_seat_input, first_price_input,
                                                 standardseats, standard_price_input)
                    flightprofit = self.flight_profit(flightincome, flightcost)

                    print(
                        "\n{} {}\n\n{} {}\n\n{} {}\n\n{} {}\n\n{} {}\n".format("Flight Cost Per Seat: ",
                                                                               flightcostperseat,
                                                                               "Flight Cost: ",
                                                                               flightcost,
                                                                               "Flight Income: ",
                                                                               flightincome,
                                                                               "Flight Profit",
                                                                               flightprofit))
                    return ""

                else:
                    print("Distance exceeds aircraft total limit!")
                    self.mainmenu()
                    run()


    def mainmenu(self):
        print("\n-- Welcome --\n")
        print("1. Enter airport details")
        print("2. Enter flight details")
        print("3. Enter price plan and calculate profit")
        print("4. Clear data")
        print("5. Quit")



#Main menu
if __name__ == '__main__':
    uk_airport_code_data = None
    oversea_code_data = None
    def run():
        global uk_airport_code_data
        global oversea_code_data
        user_input = str(input("Select: "))
        while user_input in ['1', '2', '3', '4', '5']:
            if user_input == '1':
                x = obj.airpot_input()
                uk_airport_code_data = x[0]
                oversea_code_data = x[1]
                print(uk_airport_code_data, oversea_code_data)
                obj.mainmenu()
                run()


            elif user_input == '2':
                obj.aircrafttype()

            elif user_input == "3":
                obj.price_plan(uk_airport_code_data, oversea_code_data)
                obj.mainmenu()
                run()


            elif user_input == "4":
                obj.clear_data()
                obj.mainmenu()
                run()

            elif user_input == "5":
                exit()

            else:
                print("Incorrect Input!")
                obj.mainmenu()
                run()
    obj = Airport()
    obj.mainmenu()
    run()









