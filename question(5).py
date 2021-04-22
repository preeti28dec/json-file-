# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?
import json
def complex_num(objct):
    if '__complex__' in objct:
        return complex(objct['real'], objct['img'])
    return objct

com_o =json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook = complex_num)
simple_object =json.loads('{"real": 4, "img": 3}', object_hook = complex_num)
print("Complex_object: ",com_o)
print("Without complex object: ",simple_object)