theString = ""

def link():
  global theString
  theLink = input("What is the http adress to the website you are linking\n")
  theString = theString+"\n["+input("title of link (user sees this)\n")+"]("+theLink+")"
def header():
  global theString
  theString = theString+"\n# "+input("Header\n")
def body():
  global theString
  theString = theString+"\n"+input("Body To put in link do [what you want the link to show as](the link) Bold text is **TEXT YOU WANT AT BOLD** italicied is *Text you want itacied*\n")
def bulletPoints():
  global theString
  theString = theString+"\n* "+input("First Bullet Point\n")
  doContinue = "y"
  while doContinue.lower() == "y":
    theString = theString+"\n* "+input("Next Bullet Point?\n")
    doContinue = input("Would you like to continue?(Y/N)\n")
def save():
  saveFile = open("README.md", "w")
  saveFile.write(theString)
  saveFile.close()
def choose():
  choice = input('What Would you like to add to the file,\nYou Can Add a header with "H"\nYou can add text with "T"\nYou could Add Bullet Points with "B"\nYou can add a link with "L"\n')
  if choice.lower() == "h":
    header()
    save()
    choose()
  elif choice.lower() == "t":
    body()
    save()
    choose()
  elif choice.lower() == "b":
    bulletPoints()
    save()
    choose()
  elif choice.lower() == "l":
    link()
    save()
    choose()
  else:
    saveFile = open("README.md", "w")
    saveFile.write(theString+"\n\nREADME.md made with [The Auto README project](https://github.com/ad101-lab/The-Auto-README-Project)")
    saveFile.close()