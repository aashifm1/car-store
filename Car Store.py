import datetime
import getpass

print("\nCarBuy 360")
n = input("Do you want to buy a car? (Yes/No): ").lower()
car = {
    'bmw 5 series': 1340000,
    'audi a4': 17000000,
    'volvo xc90': 15200000,
    'porsche 911': 19900000
}

def carbuy():
    if n == 'yes':
        print("\nSure. Visit our showroom. We have 4 car models available.")
        while True:
            pick = input("Pick one (BMW 5 Series, Audi A4, Volvo XC90, Porsche 911): ").lower()
            if pick in car:
                price = car[pick]
                print(f"\nThe price of {pick.title()} is ₹{price:,}")
                conf = input("Are you sure you want to buy? (Yes/No): ").lower()
                if conf == 'yes':
                    print("Payment Process Started...\n")
                    payment_details = payment()  # Store the payment details
                    if payment_details: 
                        return pick, price, payment_details  # Return payment details as well
                    else:
                        return None, None, None
                else:
                    print("Okay. Thanks for visiting. Have a nice day.\n")
                    return None, None, None
            else:
                print("The car is not available here.\n")
    else:
        print("Okay. No problem.\n")
    return None, None, None

def payment():
    tran = input("Mode of Payment (Cash/Card): ").lower()
    if tran == 'card':
        pay = input("Enter your card number (12-Digits): ")
        cvv = getpass.getpass("Enter your CVV (3-Digits): ")
        if len(pay) == 12 and pay.isdigit() and len(cvv) == 3 and cvv.isdigit():
            pin = getpass.getpass("Enter your PIN (4-Digits): ")
            if len(pin) == 4 and pin.isdigit():
                print("Money deducted from your card.\n")
                return tran, pay
            else:
                print("Invalid PIN. Try again later.\n")
                return None
        else:
            print("Invalid card details. Try again later.\n")
            return None
    elif tran == 'cash':
        print("Money received. The car will be delivered to your address.\n")
        return tran, "Cash Payment"
    else:
        print("Invalid mode of payment. Try again later.\n")
        return None

def bill_gen(car_model, price, tran, payment_details):
    print("\n" + "=" * 40)
    print("CARBUY 360 BILL")
    print("=" * 40)
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Car Model: {car_model.title()}")
    print(f"Price: ₹{price:,}")
    print(f"Payment Method: {tran.capitalize()}")
    print(f"Payment Details: {payment_details}")
    print("=" * 40)
    print("Thank you for your purchase!")
    print("=" * 40)

car_model, price, payment_details = carbuy()
if car_model and price and payment_details:
    tran, payment_info = payment_details
    bill_gen(car_model, price, tran, payment_info)  
