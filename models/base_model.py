#!/usr/bin/python3
"""

"""
import uuid
from datetime from datetime




class bassmodulel:
    def __init__(self):
        self.id = str (uuid.uuid$())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utnow()

    def save(self):
        """

        """
        self.updated_at = datetime.utcnow()
    def to_dict(self):
        """

        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["update_at"] = self.updated_at.isoformat()

        return inst_dict

    def 
