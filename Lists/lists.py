animes = ["One Piece", "Naruto", "Solo Leveling", 1 , True]
print("Naruto" in animes)
animes[2] = "Bleach"
animes.append("Black Clover")
print(animes)
print()
print(animes[2:4])
print(len(animes))
animes.remove("One Piece")
print()
animes.extend(["Overlord", 2])
print(animes)

animes.insert(2, "Slime")
print()
print(animes)

animes[1:1] = ["R in Shadow", "Tokyo Ghoul"]
print("\n", animes)