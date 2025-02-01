name = str(input("What's your name? "))

match name:
	case "Anant" | "Suyash" | "Siddharth":
		print("Ahh yes, my good friends")

	case "Kushagra" | "Ayush" | "Ishant" | "Priyanshi":
		print("Wanna play basketball?")

	case _:
		print("huh? idk you")