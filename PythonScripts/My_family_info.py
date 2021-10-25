
fam = {
    "Appa" : "Siddhu",
    "Amma" : "Gayathri Padmagireesan",
    "Siddhu" : "Siddharth",
    "Sashu" : "Sashwati Narayanan",
    "RajamPaati" : "Rajalakshmi Subramanian"
    
}
inp = input("Enter a member: ")
if inp in fam :
    print(inp,":",fam[inp])
else:
    print("Who's that")    
