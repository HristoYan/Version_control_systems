# Again chatGPT it too lengthy and time-consuming. Sorry!
# Initialize database
tax_office_db = {}


# Function to add a new person to the database
def add_person(personal_id, name, city):
    if personal_id in tax_office_db:
        print(f"Person with ID {personal_id} already exists.")
    else:
        tax_office_db[personal_id] = {"name": name, "city": city, "penalties": []}
        print(f"Added new person: {name} with ID {personal_id}.")


# Function to add a penalty to an existing person
def add_penalty(personal_id, penalty_type, amount, date):
    if personal_id not in tax_office_db:
        print(f"Person with ID {personal_id} does not exist.")
    else:
        penalty = {"penalty_type": penalty_type, "amount": amount, "date": date}
        tax_office_db[personal_id]["penalties"].append(penalty)
        print(f"Added penalty to person with ID {personal_id}.")


# Function to delete a penalty
def delete_penalty(personal_id, penalty_type):
    if personal_id not in tax_office_db:
        print(f"Person with ID {personal_id} does not exist.")
    else:
        penalties = tax_office_db[personal_id]["penalties"]
        tax_office_db[personal_id]["penalties"] = [p for p in penalties if p["penalty_type"] != penalty_type]
        print(f"Deleted penalty {penalty_type} for person with ID {personal_id}.")


# Function to replace information about a person
def update_person(personal_id, new_name=None, new_city=None):
    if personal_id not in tax_office_db:
        print(f"Person with ID {personal_id} does not exist.")
    else:
        if new_name:
            tax_office_db[personal_id]["name"] = new_name
        if new_city:
            tax_office_db[personal_id]["city"] = new_city
        print(f"Updated information for person with ID {personal_id}.")


# Full hard copy of the database
def print_full_database():
    for personal_id, data in tax_office_db.items():
        print(f"ID: {personal_id}, Name: {data['name']}, City: {data['city']}, Penalties: {data['penalties']}")


# Hard copy of data by a specific code
def print_person_by_id(personal_id):
    if personal_id in tax_office_db:
        person = tax_office_db[personal_id]
        print(f"ID: {personal_id}, Name: {person['name']}, City: {person['city']}, Penalties: {person['penalties']}")
    else:
        print(f"No data found for ID {personal_id}.")


# Hard copy of data by a specific penalty type
def print_by_penalty_type(penalty_type):
    for personal_id, data in tax_office_db.items():
        penalties = [p for p in data["penalties"] if p["penalty_type"] == penalty_type]
        if penalties:
            print(f"ID: {personal_id}, Name: {data['name']}, Penalties: {penalties}")


# Hard copy of data by a specific city
def print_by_city(city):
    for personal_id, data in tax_office_db.items():
        if data["city"] == city:
            print(f"ID: {personal_id}, Name: {data['name']}, City: {city}, Penalties: {data['penalties']}")


# Example usage
add_person("123", "John Doe", "New York")
add_penalty("123", "Late Payment", 100, "2024-10-01")
add_penalty("123", "Fraud", 500, "2024-09-15")

add_person("456", "Jane Smith", "Los Angeles")
add_penalty("456", "Late Payment", 200, "2024-10-05")

print_full_database()
print_person_by_id("123")
print_by_penalty_type("Late Payment")
print_by_city("New York")

delete_penalty("123", "Fraud")
update_person("123", new_name="Johnathan Doe")
print_full_database()
