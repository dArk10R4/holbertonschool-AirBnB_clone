from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel."""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializer for User class."""
        super().__init__(*args, **kwargs)
        if kwargs:
            self.email = kwargs['email']
            self.password = kwargs['password']
            self.first_name = kwargs['first_name']
            self.last_name = kwargs['last_name']