class User:
    """
    Class generates new instances of the user
    """
    
    user_list = []
    def __init__(self, first_name, last_name, phone_number, email, user_name, pasword):
        
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.user_name = user_name
        self.pasword = pasword
        
        
    def save_user(self):
        """
        save_user saves contact objects to the user
        """
        
        User.user_list.append(self)    
        
      