#this is the application to run to make the files work.
# here it is present the process of update the csv and store it.

from carclass import Dealership

def still_available(dealership):
    petrol = dealership.petrol_cars_registerNum
    electric = dealership.electric_cars_registerNum
    diesel = dealership.diesel_cars_registerNum
    hybrid = dealership.hybrid_cars_registerNum    
    car_no_rented = petrol + diesel + electric + hybrid 
    return car_no_rented

    
def open_csv(car_no_rented):    
    carPark = open('carPark.csv').readlines()
    details = []
    for row in carPark[1:41]:
        details.append(row.strip().split(','))
    for i in range(40):
        if details[i][0] not in car_no_rented:
            details[i][5] = "Yes"
    return details
    
def save_csv(details):
    carPark = open('carPark.csv', 'w')
    carPark.write('RegisterNumber,Make,Mileage,Type,Colour,Rented\n')
    for detail in details:
       carPark.write('{0},{1},{2},{3},{4},{5}\n'.format(
               detail[0], detail[1], detail[2], detail[3], detail[4],
                detail[5]))
    carPark.close()


def main():
    dealership = Dealership()
    dealership.create_current_stock()
    proceed = 'y'
    while proceed == 'y':
        dealership.process_rental()
        proceed = input('continue? y/n : ')
    car_no_rented = still_available(dealership)
    details = open_csv(car_no_rented)
    save_csv(details)
    print("HI, please entere in the .csv to che check out that value are"+
          "updated with new cars avaibles for renting")
        
if __name__ == '__main__':
    main()



            
   

    

    




