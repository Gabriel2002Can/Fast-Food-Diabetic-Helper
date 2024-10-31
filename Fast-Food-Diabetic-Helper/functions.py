#not being used in the program
def string_format(word):
    return str.lower(word).replace("`","").replace("'","").replace(" ","")

#All of these are are used 
def insulin_calculator(carbo,ratio):
    return round(float(carbo)/ratio)

def percentage_calculator_part_of_total(carb_max,carb_total):
    return float((100*(carb_max/carb_total)))

def percentage_calculator_above_recommended(total):
    return float((100*(total/200))-100)