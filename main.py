## Input We Need From The User 
#Total Rent 
#Total food Ordered For Snacking 
#Electricity Units spend 
#charges per unit
#persons living in room / flat 

## output 
# total ammount you've to pay is 
while True: 
    print("------------your rent calaculator-------------")

    rent = int(input("enter your hostel / flat / room rent $ : "))
    food = int(input("enter the ammount of food your ordered $ : "))
    electricity_spend = int(input("enter the total electricity you spend $ : "))
    chargers_per_unit = float(input("enter the charges per unit (in decimal value) / unit : "))
    persons = int(input("enter the number of persons living in hostel / flat / room (numbers of members) : "))

    total_bill = electricity_spend * chargers_per_unit

    total_ammount =  (rent + food + total_bill)

    output = total_ammount // persons
    print("---------------------------------------------------")
    print(f"----- your total bill : {total_ammount} $-------")
    print(f"------each person wil pay : {output}$---------")
    print("---------------------------------------------------")

    with open("rent_data.text","a") as file:
        file.write("------new calculator------\n")
        file.write(f'rent : {rent} $\n')
        file.write(f'food : {food} $\n' )
        file.write(f'eletricity : {total_bill} $\n')
        file.write(f'total ammount : {total_ammount} $\n')
        file.write(f'each person pay : {output} $\n')
        file.write("--------------------------------\n\n")
    
    choice =  input("Do you want to calculate again? (yes/no): ").lower()
    if choice.lower() != 'yes':
        print("!!!!!!!thank you for using rent calculator!!!!!!!")
        break 
