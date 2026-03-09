# mini project in Oops:

class chatbookk:
    
    __user_id =0

    def __init__(self):
        self.__name ="defualt name"
        self.id=chatbookk.__user_id
        chatbookk.__user_id +=1
        self.User_name=""
        self.password=""
        self.loggedin=False
        #self.menu()
        
        
      
    #Getter and Setter:  
    def get_name(self):
        return self.__name
    
    
    def set_name(self,value):
        self.__name= value
        
        
    
        
    def menu(self):
        user_input=input(""" Welcome to chatbook! how would u like to procceed
                         1.press 1 to signup
                         2.press 2 to signin
                         3.press 3 to write a post
                         4.press 4 to message a friend
                         5.press any other key to exit---->""")
        
        
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.send_message()
               
        else:
            exit()
            
    def signup(self):
        email=input("enter ur mail--->" )
        pswd=input("setup ur password here-->" )  
        self.User_name= email
        self.password=pswd
        print ("You have signedUp Successfully")
        print ("\n")
        self.menu()


    def signin(self):
        if self.User_name=="" and self.password=="" :
           print("Plz signup first by pressing 1")
           
        else:
           Uname =input("enter username here")
           Upswd =input("enter password here")
           if self.User_name==Uname and self.password==Upswd:
               print("yo have signed in successfully")
               self.loggedin =True
               
           else:
               print("enter correct credential")
        print("\n")
        self.menu()
        
       
    def my_post(self):
        if self.loggedin==True:
            txt=input("Enter ur message-->")
            print(f"your post has been saved-->{txt}")
            
        else:
            print("you need to sign first then u can post something")
        print("\n")
        self.menu()
        

    def send_message(self):
        if self.loggedin==True:
            txt=input("Enter ur message")
            friend=input("whom to send message-->")
            print(f"your message has been sent to--> {friend}")
            
        else:
            print("you need to sign first then u can post something")
        print("\n")
        self.menu()
        

#obj=chatbookk()

