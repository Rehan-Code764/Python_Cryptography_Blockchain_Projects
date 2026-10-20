
vehicles = {}

def register_vehicle():
    print("\n--- Register Vehicle ---")

    number_plate = input("Enter Number Plate: ").strip().upper()

    if not number_plate:
        print("Error: Number plate cannot be empty!")
        return

    if number_plate in vehicles:
        print("Error: This number plate is already registered!")
        return

    owner = input("Enter Owner Name: ").strip()
    model = input("Enter Vehicle Model: ").strip()

    if not owner or not model:
        print("Error: Owner name and model cannot be empty!")
        return

    vehicles[number_plate] = {
        "owner": owner,
        "model": model
    }

    print("Vehicle registered successfully!")


def get_vehicle():
    print("\n--- Retrieve Vehicle ---")

    number_plate = input("Enter Number Plate: ").strip().upper()

    if number_plate in vehicles:
        vehicle = vehicles[number_plate]

        print("\nVehicle Details")
        print("Number Plate:", number_plate)
        print("Owner Name:", vehicle["owner"])
        print("Model:", vehicle["model"])
    else:
        print("Error: Vehicle not found!")


while True:
    print("\n===== VEHICLE REGISTRATION SYSTEM =====")
    print("1. Register Vehicle")
    print("2. Get Vehicle Details")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        register_vehicle()
    elif choice == "2":
        get_vehicle()
    elif choice == "3":
        print("Exiting Vehicle Registration System. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
