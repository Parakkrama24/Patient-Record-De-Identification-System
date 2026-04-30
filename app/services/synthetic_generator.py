from faker import Faker

fake = Faker()

def generate_fake(entity_type: str):
    if entity_type == "NAME":
        return fake.name()
    elif entity_type == "PHONE":
        return fake.phone_number()
    elif entity_type == "EMAIL":
        return fake.email()
    elif entity_type == "LOCATION":
        return fake.city()
    elif entity_type == "DATE":
        return fake.date()
    else:
        return "[REDACTED]"