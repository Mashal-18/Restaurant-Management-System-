import json

def load_data():
    try:
        with open("Menu.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"appetizer": [], "main course": [], "dessert": []}

def save_data(Dishes):
    with open("Menu.txt", "w") as file:
        json.dump(Dishes, file)

def list_all_Dishes(Dishes):
    for category, dishes in Dishes.items():
        print(f"\n{category.capitalize()}s:")
        print("*" * 70)
        for index, Dish in enumerate(dishes, start=1):
            print(f"{index}. {Dish['name']}, Description: {Dish['Description']}, Price: {Dish['Price']}")
            print("*" * 70)

def add_Dish(Dishes):
    name = input("Enter the name of the Dish or type 'exit' to cancel: ")
    if name.lower() == 'exit':
        print("Exiting Menu.")
        return
    
    Description = input("Enter the Description of the Dish or type 'exit' to cancel: ")
    if Description.lower() == 'exit':
        print("Exiting Menu.")
        return
    
    Price = input("Enter the Price of the Dish or type 'exit' to cancel: ")
    if Price.lower() == 'exit':
        print("Exiting Menu.")
        return
    
    Category = input("Enter the Category of the Dish (appetizer, main course, dessert) or type 'exit' to cancel: ").lower()
    if Category == 'exit':
        print("Exiting Menu.")
        return
    
    if Category not in Dishes:
        print("Invalid category. Please try again.")
        return
    
    Dishes[Category].append({"name": name, "Description": Description, "Price": Price})
    print("Dish successfully added.")
    save_data(Dishes)

def update_Dish(Dishes):
    list_all_Dishes(Dishes)
    Category = input("Enter the Category of the Dish you want to update (appetizer, main course, dessert) or type 'exit' to cancel: ").lower()
    if Category == 'exit':
        print("Exiting Menu.")
        return
    
    if Category not in Dishes:
        print("Invalid category. Please try again.")
        return
    
    index = input("Enter the index of the Dish you want to update or type 'exit' to cancel: ")
    if index.lower() == 'exit':
        print("Exiting Menu.")
        return
    
    try:
        index = int(index)
    except ValueError:
        print("Invalid input. Please enter a number or type 'exit' to cancel.")
        return

    if 1 <= index <= len(Dishes[Category]):
        name = input("Enter the new Dish name or type 'exit' to cancel: ")
        if name.lower() == 'exit':
            print("Exiting Menu.")
            return
        
        Description = input("Enter the new Dish Description or type 'exit' to cancel: ")
        if Description.lower() == 'exit':
            print("Exiting Menu.")
            return
        
        Price = input("Enter the new Dish Price or type 'exit' to cancel: ")
        if Price.lower() == 'exit':
            print("Exiting Menu.")
            return
        
        Dishes[Category][index-1] = {"name": name, "Description": Description, "Price": Price}
        print("Dish successfully updated.")
        save_data(Dishes)
    else:
        print("Invalid index. Please try again.")

def delete_Dish(Dishes):
    list_all_Dishes(Dishes)
    Category = input("Enter the Category of the Dish you want to delete (appetizer, main course, dessert) or type 'exit' to cancel: ").lower()
    if Category == 'exit':
        print("Exiting Menu.")
        return
    
    if Category not in Dishes:
        print("Invalid category. Please try again.")
        return
    
    index = input("Enter the index of the Dish you want to delete or type 'exit' to cancel: ")
    if index.lower() == 'exit':
        print("Exiting Menu.")
        return
    
    try:
        index = int(index)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 1 <= index <= len(Dishes[Category]):
        del Dishes[Category][index-1]
        print("Dish successfully deleted.")
        save_data(Dishes)
    else:
        print("Invalid index. Please try again.")

def main():
    Dishes = load_data()

    while True:
        print("\n")
        print("Restaurant Management System")
        print("1. List all Dishes")
        print("2. Add a new Dish")
        print("3. Update a Dish")
        print("4. Delete a Dish")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_Dishes(Dishes)
            case "2":
                add_Dish(Dishes)
            case "3":
                update_Dish(Dishes)
            case "4":
                delete_Dish(Dishes)
            case "5":
                break
            case _:
                print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()