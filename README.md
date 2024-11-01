Fake Data Generator
This project is a Python-based application designed to generate realistic mock data, ideal for use in testing and development environments. It leverages the Faker library to create synthetic user information and outputs the data into a structured CSV file. The project includes two main scripts:

main.py: This script uses Faker to generate individual fake transactions, with each entry including randomized payment methods (PayPal or Bitcoin) and masked email addresses for privacy.

GenerateFakeInfo.py: This module generates a dataset that contains columns for dates, names, emails, and transaction amounts. Dates are generated within a specified range, names and emails are dynamically created, and transaction amounts are assigned random values within a range.

The output is saved as a CSV file (out.csv), which is useful for testing data pipelines, database integrations, and analytics workflows.

Project Details
Technologies: Python, Faker, Pandas
Features:
Generates fake names, emails, and transaction amounts.
Randomly selects payment methods for each transaction.
Masks email addresses for enhanced data privacy.
Saves data to a CSV file for easy access and analysis.
