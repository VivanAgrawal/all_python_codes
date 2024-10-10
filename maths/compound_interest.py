try:
    principle=int(input("Give your principle for compound intrest: ₹"))
    rate_of_intrest=float(input("Give your rate of interst for compound interst:%"))
    time=int(input("How much time you want:-\n1:yearly\n2:half yearly\n3:quarterly\n4:according your choice\nyour choice:-"))
    if time==1:
        a1=principle*(1+rate_of_intrest/100)**1
        print(f"The Compound Intrest for your Yearly is: {a1}")
    elif time==2:
        a2=principle*(1+rate_of_intrest/200)**0.5
        print(f"The Compound Intrest for half yearly is: {a2}")
    elif time==3:
        a3=principle*(1+rate_of_intrest/400)**0.25
        print(f"The Compound Interst for quaterly is: {a3}")
    elif time==4:
        time1=int(input("Enter time you want:-"))
        a4=principle*(1+rate_of_intrest/100)**time
        print(f"The Compound Interst for quaterly is: {a4}")
    else:
       print("Invalid choice")
except:
    ValueError:print("Value Error Rasied ,please enter proper value!")