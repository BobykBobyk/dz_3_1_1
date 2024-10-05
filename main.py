x1 = float(input("X-cordinate of the point: "))
y1 = float(input("Y-cordinate of the point: "))

if x1>0 and y1>0:
    print('First quartal')

elif x1>0 and y1<0:
    print('Second quartal')

elif x1<0 and y1<0:
    print('Third quartal')

else:
    print('Fourth quartal')
