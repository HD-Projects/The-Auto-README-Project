

MDString = "# "+input("Title\n")

print(MDString)
fileToOpen = open("README.md", "w")
fileToOpen.write(MDString)
fileToOpen.close()