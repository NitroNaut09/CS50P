def emoticon():
	user = str(input("Say some things mate: "))
	user.replace(":)", "🙂")
	user.replace(":(", "🙁")
	print(user)
emoticon()


mass = int(input("Enter the mass of the object: "))
velocity = 300000000
joules = mass * velocity
print(joules)


def main():
    dollars = dollars_to_float(input("meal? "))
    percent = percent_to_float(input("What percentage tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d[1:])

def percent_to_float(p):
    return float(p[:-1]) / 100

main()



