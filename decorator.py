#over here you will see how else is working after completing its all iteration but if it does not
#completing its iteration then it does not execute the else part of the code
def decor_result(result_funtion):
    def distinction(marks):
        for i in marks:
            if i>75:
                print("extinction")
        result_funtion(marks)
    return distinction

@decor_result
def fun(marks):
    for m in marks:
        if m>33:
            pass
        else:
            print("bro you got fail")
            break
    else:
        print("bro don't worry you will pass")
fun([60,94,94,92])