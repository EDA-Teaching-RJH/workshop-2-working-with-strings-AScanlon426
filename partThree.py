import math

def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = (pounds * percent)
    print(f"Charge £{charge:.2f}")


def pounds_to_float(pounds):
    newpounds = float(pounds.replace('£',''))
    return newpounds

def percent_to_float(percent):
    newpercent = float(percent.replace('%',''))/100
    return newpercent

main()
