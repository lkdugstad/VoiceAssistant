#uese sets and unions for each category
#need global variables
greeting = {"begrüße": 1, "begrüße mein Freund":1, "Begrüße meine Freundin":1, "hallo":1}
stock = ["wie stehen meine Aktien", "aktiengewinne"]
#https://www.tutorialspoint.com/python/python_reg_expressions.htm

def findCategory(str):
    str = "begrüße xxx"
    if str in greeting:
        return "greeting"
    elif str in stock:
        return "stock"
    else:
        return"not.found"
