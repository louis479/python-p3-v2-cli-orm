#!/usr/bin/env python3

import random
from classes.__init__ import CONN, CURSOR
from classes.department import Department
from classes.employee import Employee
from faker import Faker


def seed_database():
    Employee.drop_table()
    Department.drop_table()
    Department.create_table()
    Employee.create_table()

    # Create seed data
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    human_resources = Department.create(
        "Human Resources", "Building C, East Wing")
    Employee.create("Amir", "Accountant", payroll.id)
    Employee.create("Bola", "Manager", payroll.id)
    Employee.create("Charlie", "Manager", human_resources.id)
    Employee.create("Dani", "Benefits Coordinator", human_resources.id)
    Employee.create("Hao", "New Hires Coordinator", human_resources.id)


seed_database()
print("Seeded database")
