try:
    numerator=10
    denominator=0
    result=numerator/denominator
    print(result)

except IndexError:
    print("Index out of bound")
except ZeroDivisionError:
    print("Error: Denominator cannot be 0.")
finally:
    print("this is final block")

