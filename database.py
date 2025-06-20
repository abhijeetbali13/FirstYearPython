import json
import os
from flask import session


class Database:

    def add_data(self,name,email,password):
        
        try:
            if os.path.exists("data_base.json") and os.path.getsize("data_base.json")>1:
                
                with open("data_base.json","r") as f:
                    data=json.load(f)
                    
                    if email in data:
                        return "Email already exist"
                    else:
                        data[email]=[name,password]
                        
                        with open("data_base.json","w") as f:
                            json.dump(data,f , indent=4)
                        
                        
                        return "Register Successfully"
        except json.JSONDecodeError :
            return "Error in file"
        
        
    def search_data(self,email,password):
        try:
            if os.path.exists("data_base.json") and os.path.getsize("data_base.json")>0:
                
                with open("data_base.json") as f:
                    data=json.load(f)
                    
                    if email in data:
                        if data[email][1]==password:
                            session["user_name"]=data[email][0]
                            return "Login succesful"
                        else:
                            return "Wrong password"
                    else:
                        return "Email does not exist"
        except json.JSONDecodeError:
            return "Error in file"
        
        