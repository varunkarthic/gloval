import ctypes
import json
import os

# gloval.py
class Gloval:
    def __init__(self):
        self.user_variables = {}

    def set(self, key, value):
        self.user_variables[key] = value

    def get(self, key):
        return self.user_variables.get(key)

    def info(self):
        return("Gloval: A Global Variable Management Package by Varun Karthic. Facilitates cross-file communication and resource sharing among Python scripts within the same directory. Stay tuned for multi-directory support in the future.")

    def new(self, var_type, var_name, var_value):
        if var_type == "str":
            self.user_variables[var_name] = (ctypes.c_char_p(var_value.encode("utf-8")), var_type)
        elif var_type == "int":
            self.user_variables[var_name] = (ctypes.c_int(var_value), var_type)
        elif var_type == "float":
                self.user_variables[var_name] = (ctypes.c_float(var_value), var_type)

    def edit(self, var_name, new_value):
        if var_name in self.user_variables:
            var_type = self.user_variables[var_name][1]
            if var_type == "string":
                self.user_variables[var_name] = (ctypes.c_char_p(new_value.encode("utf-8")), var_type)
            elif var_type == "int":
                    self.user_variables[var_name] = (ctypes.c_int(new_value), var_type)
            elif var_type == "float":
                self.user_variables[var_name] = (ctypes.c_float(new_value), var_type)
            else:
                print(f"[Error] Variable '{var_name}' not found.")
    
    def load(self, var_name):
        if var_name in self.user_variables:
            var, var_type = self.user_variables[var_name]
            if var_type == "str":
                return var.value.decode("utf-8")
            else:
                return var.value
        else:
            return(f"[Error] Variable '{var_name}' not found.")

    def clear(self, var_name):
        if var_name in self.user_variables:
            del self.user_variables[var_name]
        else:
            print(f"[Error] Variable '{var_name}' not found.")

    def path(self, var_name):
        if var_name in self.user_variables:
            var = self.user_variables[var_name]
            return(ctypes.addressof(var))
        else:
            return(f"[Error] Variable '{var_name}' not found.")
        
    def global_init(self, json_path):
       data = {
    "default": "This is a default variable created by Golval. Feel free to delete it."
        }
       with open(json_path, "w") as f:
            json.dump(data, f, indent=4)
        
    def new_global(self, var_name, json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
        data[var_name] = ""
        with open(json_path, "w") as f:
            json.dump(data, f)
    
    def load_global(self, var_name, json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
        if var_name in data:
            return data[var_name]
        else:
            return f"[Error] Variable '{var_name}' not found."
    
    def clear_global(self, var_name, json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
        if var_name in data:
            del data[var_name]
        else:
            print(f"[Error] Variable '{var_name}' not found.")
        with open(json_path, "w") as f:
            json.dump(data, f)
            
    def edit_global(self, var_name, new_value, json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
        if var_name in data:
            data[var_name] = new_value
        else:
            print(f"[Error] Variable '{var_name}' not found.")
        with open(json_path, "w") as f:
            json.dump(data, f)
    
    def clear_global_object(self, path):
        if os.path.exists(path):
            os.remove(path)
        else:
            print(f"[Error] Object '{path}' not found.")
        

# Create a Gloval instance
gloval = Gloval()
