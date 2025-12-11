class ChatBook:
    def __init__(self):
        self.__name = "default name" # private attribute(encapsulation)
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menue()
        
    def get_name(self):     # getter 
        return self.__name
    
    def set_name(self, new_name):  # setter
        self.__name = new_name
        
    def menue(self):
        user_input = input("""Welcome to the ChatBook! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other button to exit 
                           
                            -> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_msg()
        else:
            exit()
            
    def signup(self):
        email = input("Enter your Email here: ")
        pwd = input("Setup your password here: ")
        self.username = email
        self.password = pwd
        print("Congratulations! Your have successfully signed up.")
        print("\n")
        self.menue()
        
    def signin(self):
        if self.username == "" and self.password == "":
            print("Please signup first by pressing 1 in the main menue.")
        else:
            username = input("Enter your username here: ")
            password = input("Enter your password here: ")
            if self.username == username and self.password == password:
                print("You have signed in successfully.")
                self.loggedin = True
            else:
                print("You have put the wrong credentials, try again.....")
        print("\n")
        self.menue()
        
    def my_post(self):
        if self.loggedin == True:
            text = input("Write your post here: ")
            print(f"Following content has been posted -> {text}")
        else:
            print("you need to singin first to post anything....")
        print("\n")
        self.menue()
        
    def send_msg(self):
        if self.loggedin == True:
            frnd = input("Whom to send message -> ")
            msg = input("Write your message here -> ")
            print(f"The following message has been sent to {frnd} -> {msg}")
        else:
            print("You need to singin first to send any messages.....")
        print("\n")
        self.menue()
        

obj_1 = ChatBook()