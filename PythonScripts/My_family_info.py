fam = {
    "Appa" : "Siddhu",
    "Amma" : "Gayathri Padmagireesan",
    "Siddhu" : "Siddharth",
    "Sashu" : "Sashwati Narayanan"
}
inp = input("Enter a member: ")
if inp in fam :
    print(inp,":",fam[inp])
else:
    print("Who's that")    