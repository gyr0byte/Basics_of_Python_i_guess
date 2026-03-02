animes = ["One Piece", "Naruto", "Solo Leveling", "bleach", "Attack on Titan", "Demon Slayer"]
''' animescopy = animes[:]
animes.sort(key = str.lower)
print(animes)
print("\n")
print(animescopy) '''

print(sorted(animes, key=str.lower)) # sorted global function doesn't modify the original list unlike .sort
print()
print(animes)