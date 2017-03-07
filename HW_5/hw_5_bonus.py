# task 5_bonus

def chek_str_int(data):
    if type(data) == str:
        return(True)
    elif type(data) == int:
        return(False)
    else:
        return("Wrong data! Input pleas string or integer.")
print(chek_str_int(26))
