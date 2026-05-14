# Base Class
class MobilePhone:

    def __init__(self, screenType, networkType, dualSim,
                 frontCamera, rearCamera, ram, storage):

        self.screenType = screenType
        self.networkType = networkType
        self.dualSim = dualSim
        self.frontCamera = frontCamera
        self.rearCamera = rearCamera
        self.ram = ram
        self.storage = storage

    # Mobile functionalities
    def make_call(self):
        print("Calling...")

    def receive_call(self):
        print("Receiving Call...")

    def take_a_picture(self):
        print("Picture Captured!")

    def display_info(self):
        print("Screen Type:", self.screenType)
        print("Network Type:", self.networkType)
        print("Dual Sim:", self.dualSim)
        print("Front Camera:", self.frontCamera)
        print("Rear Camera:", self.rearCamera)
        print("RAM:", self.ram)
        print("Storage:", self.storage)


# Child Class : Apple
class Apple(MobilePhone):

    def __init__(self, screenType, networkType, dualSim,
                 frontCamera, rearCamera, ram, storage, model):

        # Calling parent constructor using super()
        super().__init__(screenType, networkType, dualSim,
                         frontCamera, rearCamera, ram, storage)

        self.model = model

    def apple_feature(self):
        print(self.model, "supports Face ID")


# Child Class : Samsung
class Samsung(MobilePhone):

    def __init__(self, screenType, networkType, dualSim,
                 frontCamera, rearCamera, ram, storage, model):

        # Calling parent constructor using super()
        super().__init__(screenType, networkType, dualSim,
                         frontCamera, rearCamera, ram, storage)

        self.model = model

    def samsung_feature(self):
        print(self.model, "supports S-Pen")


# Creating Apple objects
apple1 = Apple("Touch Screen", "5G", True,
               "12MP", "48MP", "4GB", "64GB", "iPhone 13")

apple2 = Apple("Touch Screen", "4G", False,
               "8MP", "32MP", "3GB", "32GB", "iPhone SE")


# Creating Samsung objects
samsung1 = Samsung("Touch Screen", "5G", True,
                   "16MP", "48MP", "4GB", "64GB", "Galaxy S23")

samsung2 = Samsung("Touch Screen", "4G", True,
                   "8MP", "16MP", "2GB", "32GB", "Galaxy A12")


# Using methods
print("----- Apple Phone -----")
apple1.display_info()
apple1.make_call()
apple1.take_a_picture()
apple1.apple_feature()

print("\n----- Samsung Phone -----")
samsung1.display_info()
samsung1.receive_call()
samsung1.take_a_picture()
samsung1.samsung_feature()