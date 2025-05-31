
import requests
from bs4 import BeautifulSoup
import csv

# --- Calculator Function ---
def calculator():
    print("\nSimple Calculator")
    print("Available operations: +, -, *, /")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator: ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operator.")

    except ValueError:
        print("Error: Invalid input. Please enter numbers.")

# --- Web Scraper Function ---
def web_scraper():
    print("\nWeb Scraper")
    url = input("Enter the website URL to scrape (e.g., https://example.com): ")
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        headlines = soup.find_all(['h1', 'h2', 'h3'])

        if not headlines:
            print("No headlines found.")
            return

        with open('headlines.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Tag', 'Text'])

            for tag in headlines:
                writer.writerow([tag.name, tag.text.strip()])

        print("Headlines saved to headlines.csv")

    except Exception as e:
        print("Error while scraping:", e)

# --- Main Menu ---
def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Use Calculator")
        print("2. Run Web Scraper")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            calculator()
        elif choice == '2':
            web_scraper()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# --- Run the program ---
if __name__ == "__main__":
    main()
