import sys
import typer
import json
import string
import random

from faker import Faker
from typing import List


fake = Faker()
app = typer.Typer()


# UTILS
def export_json(data_list, filename="data"):
    """
    Exports to JSON
    Arguements: data list, filename
    """

    with open(f"{filename}.json", "w") as exportfile:
        json.dump(data_list, exportfile, indent=4)



# Generate Data
@app.command()
def custom_data_list(iterations: int, args: List[str]):
    """
    Creates a list of custom data model and exports to JSON
    """

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
    typer.echo(f"Custom list created with: {len(data_list)} elements")


@app.command()
def user_list(iteration: int):
    """
    Creates a default list of users with attributes and exports to JSON
    """

    data_list = []
    for i in range(iteration):
        data = {}
        source = string.ascii_letters + string.digits
        data["first_name"]= fake.first_name()
        data["last_name"] = fake.first_name()
        data["email"] = fake.email()
        data["password"] = "".join([random.choice(source) for i in range(random.randint(8, 16))])
        data["date_of_birth"] = fake.date()
        data["company"] = fake.company()
        data["job"] = fake.job()
        data_list.append(data)
    export_json(data_list, "user")
    typer.echo(f"User list created with: {len(data_list)} elements")



if __name__ == "__main__":
    app()

