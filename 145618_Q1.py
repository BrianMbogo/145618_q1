def add_patient(patients):
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    illness = input("Enter patient's illness: ")
    patient = {'name': name, 'age': age, 'illness': illness}
    patients.append(patient)
    print(f"Patient {name} added successfully.")

def display_patients(patients):
    if not patients:
        print("No patients found.")
    else:
        for i, patient in enumerate(patients, 1):
            print(f"Patient {i}: Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

def search_patient(patients):
    name = input("Enter the name of the patient to search: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print(f"Patient found: Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            return
    print(f"No patient found with the name {name}.")

def remove_patient(patients):
    name = input("Enter the name of the patient to remove: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            patients.remove(patient)
            print(f"Patient {name} removed successfully.")
            return
    print(f"No patient found with the name {name}.")

def main():
    patients = []
    while True:
        print("\nHospital Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_patient(patients)
        elif choice == '2':
            display_patients(patients)
        elif choice == '3':
            search_patient(patients)
        elif choice == '4':
            remove_patient(patients)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if _name_ == "_main_":
    main()