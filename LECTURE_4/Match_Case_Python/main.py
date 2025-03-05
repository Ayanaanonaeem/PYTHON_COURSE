x=8
match x:
    case 0:
        print("x is zero")

    case 1:
        print("x is one")

    case 7:
        print("x is seven")

    case _:
        print("x is nothing")

y=5

match y:
    case 2:
        print("ye two hai")
    case 4 if y % 2 == 0:
        print("the case is 4")
    case _ if y < 10:
        print("y is less than 10")

        