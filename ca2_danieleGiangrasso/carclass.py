#compared with the file in moodle I did not add the general class Car(mileage,
#make, etc).
#in this  script I have defined the classes and separeted them from the other pieces of the code.

class ElectricCar():    
    def __init__(self):
        self.electric_cars = []

class PetrolCar():
    def __init__(self):
        self.petrol_cars = []
  
class DieselCar():
    def __init__(self):
        self.diesel_cars = []
        
class HybridCar():
    def __init__(self):
        self.hybrid_cars = []

class Dealership():
    
    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []
        self.petrol_cars_registerNum = []
        self.electric_cars_registerNum = []
        self.diesel_cars_registerNum = []
        self.hybrid_cars_registerNum = []            
    
    def create_current_stock(self):
        dataCarPark = open('carPark.csv').readlines()
        car_rented = []
        car_notrented = []
        for row in dataCarPark[1:41]:
            registerNum = row.strip().split(',')[0] 
            Type = row.strip().split(',')[3]
            rented = row.strip().split(',')[5]            
            if rented == 'No':
                car_rented.append(registerNum)
                if Type == 'Petrol':
                    self.petrol_cars.append(PetrolCar())
                    self.petrol_cars_registerNum.append(registerNum)                                    
                elif Type == 'Electric':
                    self.electric_cars.append(ElectricCar())
                    self.electric_cars_registerNum.append(registerNum)                    
                elif Type == 'Diesel':
                    self.diesel_cars.append(DieselCar())
                    self.diesel_cars_registerNum.append(registerNum)
                else:
                    self.hybrid_cars.append(HybridCar())
                    self.hybrid_cars_registerNum.append(registerNum)
            if rented == 'Yes':
                car_notrented.append(registerNum)
        #the below it is just for tests purposes       
        car_in_park = car_rented + car_notrented        
        return car_in_park        
                                               
    def process_rental(self):
        answer = input('would you like to rent a car? y/n : ')
        if answer == 'y':
            answer = input('what type would you like? p/e/d/h :')
            while answer not in ['p','d','e','h']:
                answer = input('what type would you like? p/e/d/h :') 
            amount = int(input('how many would you like? : '))
            if answer == 'p':
                self.rent(self.petrol_cars, self.petrol_cars_registerNum, amount)                
            elif answer == 'd':
                self.rent(self.diesel_cars,  self.diesel_cars_registerNum, amount)
            elif answer == 'e':
                self.rent(self.electric_cars, self.electric_cars_registerNum, amount)
            else:            
                self.rent(self.hybrid_cars, self.hybrid_cars_registerNum, amount)                
            self.stock_count()
        
        return answer

    def rent(self, car_list, register_num, amount):
        if len(car_list) < amount:
            print('Not enough cars in stock')
            return
        total = 0
        while total < amount:
            car_list.pop()
            register_num.pop()
            total = total + 1
        return car_list        
        
    def stock_count(self):
        print('petrol cars in stock ' + str(len(self.petrol_cars)))
        print('electric cars in stock ' + str(len(self.electric_cars)))
        print('diesel cars in stock ' + str(len(self.diesel_cars)))
        print('hybrid cars in stock ' + str(len(self.hybrid_cars)))





    
    

