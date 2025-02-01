# TODO: Add error handling


def is_even():


	try:
		# Ask the user for an integer, used to check parody (Even/Odd)
		user_input_number = int(input("Enter a number to check if even or odd: "))


		# Declare statement vars for each result
		even = f"{user_input_number} is even"
		odd = even.replace("even", "odd")

		# Final result execution
		print(even) if user_input_number % 2 == 0 else print(odd)

	except ValueError:
		print("Ah, that's not understood.")

if __name__ == "__main__":
		is_even()

