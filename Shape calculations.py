def calculatepna():
    print("1. Calculate Perimeter")
    print("2. Calculate Area")

repeat = True

while repeat == True:
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Square")
    print("5. Trapezoid")
    print("6. Sphere")
    Input = int(input("What shape would you like to calculate?"))
    print("")

#Calculator Determinor
    if Input == 1:
        calculatepna()
        rectInput = int(input("What would you like to calculate?"))
        print("")
    #Rectangle calculations
        #Perimeter
        if rectInput == 1:
            a = float(input("Enter rectangle length"))
            b = float(input("Enter rectangle width"))
            print("The perimeter of the rectangle is", 2 * (a+b), "units")
            print("")
        #Area
        elif rectInput == 2:
            a = float(input("Enter rectangle length"))
            b = float(input("Enter rectangle width"))
            print("The area of the rectangle is", a * b, "units")
            print("")

    elif Input == 2:
        calculatepna()
        triInput = int(input("What would you like to calculate?"))
        print("")
    #Triangle Calculations
        #Perimeter
        if triInput == 1:
            a = float(input("Enter triangle side 1"))
            b = float(input("Enter triangle side 2"))
            c = float(input("Enter triangle side 3"))
            print("The perimeter of the triangle is", a + b + c, "units")
            print("")
        #Area
        elif triInput == 2:
            a = float(input("Enter triangle height"))
            b = float(input("Enter traingle base"))
            print("The area of the triangle is", 0.5 * (a * b), "units")
            print("")

    elif Input == 3:
        print("1. Calculate Circumference")
        print("2. Calculate Area")
        circInput = int(input("What would you like to calculate?"))
        print("")
    #Circle Claculations
        #Circumference
        if circInput == 1:
            print("1. Diameter calculation")
            print("2. Radius calculation")
            diamraInput = int(input("Enter value available"))
            print("")
        #Valule Determinor
            if diamraInput ==  1:
                a = float(input("Enter circle diameter"))
                pi = 3.14159265359
                print("The circumference of the circle is", pi * a, "units")
                print("")
            elif diamraInput == 2:
                b = float(input("Enter circle radius"))
                pi = 3.14159265359
                print("The circumference of the circle is", 2 * (pi * b), "units")
                print("")
        #Area
        elif circInput == 2:
            a = float(input("Enter circle radius"))
            pi = 3.14159265359
            print("The area of the circle is", pi * (a * a), "units")
            print("")

    elif Input == 4:
        calculatepna()
        squaInput = int(input("What would you like to calculate?"))
        print("")
    #Square Calculations
        #Perimeter
        if squaInput == 1:
            a = float(input("Enter square height"))
            print("The perimeter of the square is", 4 * a, "units")
            print("")
        #Area
        elif squaInput == 2:
            a = float(input("Enter square height"))
            print("The area of the square is", a * a, "units")
            print("")

    elif Input == 5:
        calculatepna()
        trapInput = int(input("What would you like to calculate?"))
        print("")
    #Trapezoid Calculations
        #Perimeter
        if trapInput == 1:
            a = float(input("Enter trapezoid side one"))
            b = float(input("Enter trapezoid side two"))
            c = float(input("Enter base side one"))
            d = float(input("Enter base side two"))
            print("The perimeter of the trapezoid is", a + c + b + d, "units")
            print("")
        #Area
        elif trapInput == 2:
            a = float(input("Enter trapezoid height"))
            b = float(input("Enter trapezoid base one"))
            c = float(input("Enter trapezoid base two"))
            print("The area of the trapezoid is", (0.5 * a) * (b + c), "units")
            print("")

    elif Input == 6:
        print("1. Calculate Surface Area")
        print("2. Calculate Volume")
        sphInput = int(input("What would you like to calculate?"))
        print("")
    #Sphere Calculations
        #Surface Area
        if sphInput == 1:
            a = float(input("Enter sphere radius"))
            pi = 3.14159265359
            print("The surface area of the sphere is", 4 * pi * (a * a), "units")
            print("")
        #Volume
        elif sphInput == 2:
            a = float(input("Enter sphere radius"))
            pi = 3.14159265359
            print("The volume of the sphere is", ((4/3) * pi) * (a ** 3), "units")
            print("")
        repeat == False
