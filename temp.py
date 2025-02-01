def get_temp():
    while True:
        temp = input("What's the temp right now? (or type 'exit' to quit) ").strip().lower()

        if temp == "exit":
            print("Roger, breaking the loop")
            break

        elif "c" in temp:
            temp = temp.replace("c", "").strip()  # Remove 'c' and clean up spaces
            try:
                con_temp = (9 / 5) * float(temp) + 32  # Convert Celsius to Fahrenheit
                print(f"{con_temp:.2f}°F")
            except ValueError:
                print("Invalid input! Please enter a valid number followed by 'C' or 'F'.")

        elif "f" in temp:
            temp = temp.replace("f", "").strip()  # Remove 'f' and clean up spaces
            try:
                con_temp = (5 / 9) * (float(temp) - 32)  # Convert Fahrenheit to Celsius
                print(f"{con_temp:.2f}°C")
            except ValueError:
                print("Invalid input! Please enter a valid number followed by 'C' or 'F'.")

        else:
            print("Invalid input! Please enter a number followed by 'C' or 'F'.")

if __name__ == "__main__":
    get_temp()