import pandas as pd
car_data = {
    'distance in (km)': [60,70,50,60,80,50,65,70,55,60],
    'time in (min)': [45,45,45,45,45,45,45,45,45,45]
}
myvar= pd.DataFrame(car_data, index = ["car1","car2","car3","car4","car5","car6","car7","car8","car9","car10"])
print (myvar)