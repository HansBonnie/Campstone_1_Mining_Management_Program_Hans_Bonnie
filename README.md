# Mine Management Program

## Context

This project is a mine management program in Python. The program allows users to manage Sites, Heavy Equipment, and Workers. The aim of this program is to simplify the management of mining components into a single application.
The program is contain 

## Business Tasks
### Key Features
-	Displaying Mining Sites based on the type of coal (such as: Bituminous, Sub-Bituminous, Lignite)
-	Sorting Mining Sites based on the amount of coal reserves
-	Updating the status and specifications of Heavy Equipment
-	Adding and deleting heavy equipment
-	Updating the status and information of employees
-	Sorting and filtering the employees based on age and position
-	Adding and deleting employee data
## Objectives
Facilitating owners and stakeholders in managing supporting components of mining
Providing assistance to engineers in managing heavy equipment

## Stakeholders
1. End Users: Mining engineers and human resources personnel in organizing heavy equipment and employees.
2. Business Owners: Mining business owners in determining steps based on the existing mining sites and the available reserves.
3. Developers: The development team responsible for building, maintaining, and updating the program.
4. Investors : Deciding to invest based on the available reserves.

## Limitations
This project has several limitations to consider:
1. Limited Data: The program will use a dummy set of mining data.
2. No Automatic Updates: Business information will not be updated automatically.Manual updates are required.
3. No Production Simulation: Currently, the application does not support production simulation.

## Data Summary
The data used in this project includes:
Mining Site Data :
-	ID Siet
-	Site Name
-	Ore type
-	Volume Overburden
-	Ore Stock
Heavy Duty Vehicle Data :
-	Vehicle ID
-	Vehicle category
-	Vehicle Brand
-	Vehicle Type
-	Capacity 
-	Vehicle Status
Employee Data :
-	Employee ID
-	Employee Name
-	Position
-	Age
-	Status

## User Instructions
### Installation
To run this program, you need to install some dependencies. Use the following command:
pip install tabulate

### Running the Program
To run the program, use the following command:
python Capstone_1_MMP_HB.py
Follow the on-screen instructions to perform mining site, heavy duty vehicle and employee searches based on your desired category.

### License
This project has no license, since all the data in this project is dummy.
