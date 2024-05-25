print("\033[35m A demo project of security system using PYTHON🐍 \033[0m")
print()
print(" Use any one of these credentials to login🔰")
print("""
        Name : David    Password: PyTh0nR*cks
        Name : Becky  Password: Repl!t4evEr
        Name : Bill   Password: SmashTHEb*gs!
        """)
print("========== Secure Login ==========")
username = input("What is your username?")
password = input("What is your password?")

if username == "David" and password == "PyTh0nR*cks":
  print("\033[34m Welcome, David! You are looking nice today! \033[0m")
  print("Thank you once again for joining us! We hope you have an enjoyable and fulfilling experience using our services.")
  
elif username == "Becky" and password == "Repl!t4evEr":
  print("\033[33mHi Becky! Love your hair today!\033[0m")
  print("Thank you once again for joining us! We hope you have an enjoyable and fulfilling experience using our services.")
  
elif username == "Bill" and password == "SmashTHEb*gs!":
  print(" \033[32mYo! Bill! What up?! \033[0m")
  print("Thank you once again for joining us! We hope you have an enjoyable and fulfilling experience using our services.")
  
else:
  print("\033[31m You do not have access. Go away!⚔️ \033[0m ")
