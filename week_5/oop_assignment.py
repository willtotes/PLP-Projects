class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        
    def make_call(self):
        return "Calling..."

    def take_photo(self):
        return "Taking a photo..."
    
    def describe(self):
        return f"{self.brand} {self.model} ({self.storage}GB)"

print("Smartphone:")
phone = Smartphone("Iphone", "16 Plus", 256)
print(phone.describe())
print(phone.make_call())
print(phone.take_photo())