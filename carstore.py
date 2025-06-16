import datetime
import getpass

def main():
    print("\nCar Store")
    response = input("Do you want to buy a car? (Yes/No): ").strip().lower()

    car_model, price, payment_details = carbuy(response)
    if car_model and price and payment_details:
        tran, payment_info = payment_details
        bill_gen(car_model, price, tran, payment_info)

# car datasets
car_catalog = {
    'bmw 5 series': 1340000,
    'audi a4': 17000000,
    'volvo xc90': 15200000,
    'porsche 911': 19900000
}

# car buying part
def carbuy(response):
    if response == 'yes':
        print("\nSure. Visit our showroom. We have 4 car models available.")
        while True:
            pick = input("Pick one (BMW 5 Series, Audi A4, Volvo XC90, Porsche 911): ").strip().lower()
            if pick in car_catalog:
                price = car_catalog[pick]
                print(f"\nThe price of {pick.title()} is ₹{price:,}")
                conf = input("Are you sure you want to buy? (Yes/No): ").strip().lower()
                if conf == 'yes':
                    print("Payment Process Started...\n")
                    for attempt in range(3):
                        payment_details = payment()
                        if payment_details:
                            return pick, price, payment_details
                        else:
                            print(f"Payment failed. Attempts left: {2 - attempt}\n")
                    print("Payment failed after multiple attempts. Please try again later.\n")
                    return None, None, None
                else:
                    retry = input("Would you like to choose a different model? (Yes/No): ").strip().lower()
                    if retry != 'yes':
                        print("Okay. Thanks for visiting. Have a nice day.\n")
                        return None, None, None
            else:
                print("The car is not available. Please choose from the listed models.\n")
    else:
        print("Okay. No problem.\n")
    return None, None, None

# payment gateway
def payment():
    tran = input("Mode of Payment (Cash/Card): ").strip().lower()
    if tran == 'card':
        pay = input("Enter your card number (12 digits): ").strip()
        cvv = getpass.getpass("Enter your CVV (3 digits): ").strip()
        if len(pay) == 12 and pay.isdigit() and len(cvv) == 3 and cvv.isdigit():
            pin = getpass.getpass("Enter your PIN (4 digits): ").strip()
            if len(pin) == 4 and pin.isdigit():
                print("Money deducted from your card.\n")
                return tran, f"Card ending with ****{pay[-4:]}"
            else:
                print("Invalid PIN.\n")
        else:
            print("Invalid card number or CVV.\n")
    elif tran == 'cash':
        print("Money received. The car will be delivered to your address.\n")
        return tran, "Cash Payment"
    else:
        print("Invalid mode of payment.\n")
    return None

# bill generation part
def bill_gen(car_model, price, tran, payment_info):
    print("\n" + "=" * 40)
    print("CAR STORE BILL")
    print("=" * 40)
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Car Model: {car_model.title()}")
    print(f"Price: ₹{price:,}")
    print(f"Payment Method: {tran.capitalize()}")
    print(f"Payment Details: {payment_info}")
    print("=" * 40)
    print("Thank you for your purchase!")
    print("=" * 40)

if __name__ == "__main__":
    main()
