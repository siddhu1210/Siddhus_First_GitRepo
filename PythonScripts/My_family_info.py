import sys
while True:
 fam = {
"Appa" : "Narayanan",
"Amma" : "Gayathri Padmagireesan",
"Siddhu" : "Siddharth",
"Sashu" : "Sashwati Narayanan",
"Rajam Paati" : "Rajalakshmi Subramanian"
}
 a = 
 inp = input("Enter a member or q to quit: ")
 if inp in fam :
    print(inp,":",fam[inp])
 elif inp == "q":
     print("bye bye...")
     sys.exit()
     
 else:
    print("Who's that")    
