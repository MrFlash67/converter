import flashConverter as fcv, myGetCh as gch, sys as s, time as t
print 'Welcome to...'
t.sleep(1)
print 'A unit calculator!'
print 'Type 1, 2 or 3 on your keyboard to select the type of conversions you want to make.'
print 'Press 1 to convert between 12 and 24 hour time, press 2 to convert between pounds and kilograms...' 
print '...and press 3 to convert between milliliters and liters'
choice1 = gch.getch()
if choice1 == '1':
    print 'Press 1 to convert from 12 to 24-hour time, and press 2 to convert from 12 to 24-hour time.'
    choicetime = gch.getch()
    if choicetime == '1':
        print 'What 12-hour PM time do you want to convert to 24-hour time? (It must be a 1 or 2 digit number that is between 1 and 12, inclusive)'
        outti1 = int(raw_input('>'))
        h12dh24 = str(fcv.h12h24(outti1))
        print 'Your output is ' + h12dh24 + '.'
        s.exit()
    elif choicetime == '2':
        print 'What 24-hour time do you want to convert to 12-hour PM time? (It must be a 2 digit number that is between 13 and 24, inclusive)'
        outti2 = int(raw_input('>'))
        h24dh12 = str(fcv.h24h12(outti2))
        print 'Your output is ' + h24dh12 + ' PM.'
        s.exit()
    else:
        print 'You did not follow the instructions.'
        t.sleep(1)
        print 'DIEEEEEEEEEE'
        s.exit()  
if choice1 == '2':
    print 'Press 1 to convert from pounds to kilograms, and press 2 to convert from kilograms to pounds.'
    choicewei = gch.getch()
    if choicewei == '1':
        print 'How many pounds do you want to convert to kilograms?'
        outwei1 = int(raw_input('>'))
        ibdkg = str(fcv.ib2kg(outwei1))
        print 'Your converted product is ' + ibdkg + ' KG.'
        s.exit()
    elif choicewei == '2':
        print 'How many kilograms do you want to convert to pounds?'
        outwei2 = int(raw_input('>'))
        kgdib = str(fcv.kg2ib(outwei2))
        print 'Your converted product is ' + kgdib + ' pounds.'
        s.exit()
    else:
        print 'You did not follow the instructions.'
        t.sleep(1)
        print 'DIEEEEEEEEEE'
        s.exit()  
elif choice1 == '3': #I really hate indentation
        print 'Press 1 to convert from milliliters to liters, and press 2 to convert from liters to milliliters.'
        choicelqd = gch.getch()
        if choicelqd == '1':
            print 'How many milliliters do you want to convert to liters?'
            outlqd1 = int(raw_input('>'))
            mldl = str(fcv.ml2l(outlqd1))
            print 'Your converted product is ' + mldl + ' liter(s).'
            s.exit()
        if choicelqd == '2':
            print 'How many liters do you want to convert to milliliters?'
            outlqd2 = int(raw_input('>'))
            ldml = str(fcv.l2ml(outlqd2))
            print 'Your converted product is ' + ldml + ' milliliters.'
            s.exit()
        else:
            print 'You did not follow the instructions.'
            t.sleep(1)
            print 'DIEEEEEEEEEE'
            s.exit()  
else:
        print 'You did not follow the instructions.'
        t.sleep(1)
        print 'DIEEEEEEEEEE'
        s.exit()