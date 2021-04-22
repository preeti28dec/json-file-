# Q.9 Apki pass ek shopping name ki ek dictionary hai Apki dictionary ka use kar ke ek json 
# file create karna hai. Aur apko kuch task perform karne hai jaise ki 
# 1.main dekhna chahta hu shopping list ko json file dekhna.
# 2.phir main user se poochu ga ki kon sa item khareedna chahte ho.
# 3.uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.
# 4.phir aapka wo number of items json file se remove karna hai.
# 6.Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.import json
import json
dict={
    "shopping_list":
        { 
            "chaco":15,
            "Biscuits":50,
            "Diary_milk":30,
            "ice_cream":20,
        } 
}
item=input("enter which item would you like to buy=")
no_of_item=int(input("PLEASE enter How many item would you like to buy="))
for key in dict:
    for i in dict[key]:
        if i == item:
            dict[key][i]=(dict[key][i]-no_of_item)
print(json.dumps(dict, indent=4))
