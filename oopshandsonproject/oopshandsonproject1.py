#creating a class car class

class Car:
    color = "Blue"
    max_speed = 120
    acceleration = "pressing"
    tyre_friction = "good"
    is_engine_started = "yes"
    current_speed = 80
    horn_sound = "Yes"

    '''def Old_methods(self,start_engine,stop_engine,
                    apply_breaks,sound_horn):
       self.start_engine = start_engine
       self.stop_engine = stop_engine
       self.apply_breaks = apply_breaks
       self.sound_horn = sound_horn'''

    def start_engine(self):
        self.is_engine_started = "Yes"
    def stop_engine(self):
        self.is_engine_started = "No"

    def apply_breaks(self):
        self.current_speed = 0

    def sound_horn(self):
        print("Car Honk Honk")

    def acceleration(self):
        print("the acceleration is pressing")

class Truck(Car):
    max_cargo_weight = 300
    vehicle_load = 0
    load = 0
   # is_engine_started = "no"
    current_speed = 0

    def sound_horn(self):
        #self.horn_sound = horn_sound
        if self.is_engine_started == "yes":
            print("honk ,honk ")
        else:
            print("car has not started yet")

    def load_cargo(self,cargo_weight):
        self.cargoweight = cargo_weight
        if self.is_engine_started == "No":
            print("load the truck")
            self.load += cargo_weight
            if (self.cargo_weight > self.max_cargoweight):
                print("you can not load the truck any more")
            else:
                print("you can load truck")
        else:
            print("Can not load the truck")

    def unload_cargo(self,cargo_weight=200):
        self.cargoweight = cargo_weight
        if (self.is_engine_started == "N0"):
            print("we can unload the truck ",self.cargo_weight)
        else:
            print("we cannot unload the truck")

#obj_car = Car()
objtruck = Truck()
objtruck.sound_horn()
objtruck.acceleration()
objtruck.stop_engine()
objtruck.load_cargo(100)
















