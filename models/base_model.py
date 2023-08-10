#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        # Check if any keyword arguments are provided during instance creation
        if kwargs:
            # Iterate through provided keyword arguments
            for key, value in kwargs.items():
                # Skip special '__class__' key
                if key != '__class__':
                    # Set the attribute using the provided value
                    setattr(self, key, value)
            
            # If 'id' is not provided, generate a unique ID using uuid.uuid4()
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            
            # If 'created_at' is not provided, set it to the current datetime
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            
            # If 'updated_at' is not provided, set it to the current datetime
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            # If no keyword arguments are provided, generate attributes as usual
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        # Return a formatted string representation of the object
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        # Update the 'updated_at' attribute with the current datetime
        self.updated_at = datetime.now()

    def to_dict(self):
        # Create a dictionary representation of the object
        obj_dict = self.__dict__.copy()
        
        # Add '__class__' key with the class name of the object
        obj_dict['__class__'] = self.__class__.__name__
        
        # Convert 'created_at' and 'updated_at' attributes to ISO format strings
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        
        return obj_dict
