import sys
import json
import string
import random
from faker import Faker


fake = Faker()

# Require the number of iterations
iterations = int(sys.argv[1])
# Require = the list of data_point
args = sys.argv[2:]


# Export data as JSON
def export_json(data_list, filename="data"):
    with open(f"{filename}.json", "w") as exportfile:
        json.dump(data_list, exportfile, indent=4)
    print(f"Completed {filename} list.")



# Generate Data
def custom_data(args, iterations):
    data_list = []
    for i in range(iterations):
        data = {}
        source = string.ascii_letters + string.digits
        data["password"] = "".join([random.choice(source) for i in range(random.randint(8, 16))])
        for arg in args:
            if hasattr(fake, arg):
                method = getattr(fake, arg)
                # Fix email
                data[arg] = method()
        data_list.append(data)
    export_json(data_list)


def user(iteration):
    data_list = []
    for i in range(iteration):
        data = {}
        source = string.ascii_letters + string.digits
        data["first_name"]= fake.first_name()
        data["last_name"] = fake.first_name()
        data["email"] = fake.email()
        data["password"] = "".join([random.choice(source) for i in range(random.randint(8, 16))])
        data["date_of_birth"] = fake.date()
        data["job"] = fake.job()
        data_list.append(data)
    export_json(data_list, "user")

