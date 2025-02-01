def main():
	players = str(input("Multiplayer/Singleplayer: ")).strip().lower()
	difficulty = str(input("Difficult/Easy:  ")).strip().lower()


	if difficulty == "difficult" and players == "multiplayer":
		print('We recommend playing poker')
	elif difficulty == "difficult" and players == "singleplayer":
		print('You should try playing Pacman! A classic!')


	if difficulty == "easy" and players == "multiplayer":
		print("You should play War")
	elif difficulty == "easy" and players == "singleplayer":
		print("Try playing mining tycoon!")


if __name__ == "__main__":
	main()


# If you use a dict instead:

"""def main():
    games = {
        ("difficult", "multiplayer"): "We recommend playing poker",
        ("difficult", "singleplayer"): "You should try playing Pacman! A classic!",
        ("easy", "multiplayer"): "You should play War",
        ("easy", "singleplayer"): "Try playing mining tycoon!"
    }
    print(games.get((input("Difficult/Easy: ").strip().lower(), input("Multiplayer/Singleplayer: ").strip().lower())))"""