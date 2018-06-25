import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Path of Data file
df = pd.read_excel('Data.xlsx')

number = int(input('Enter Number of Activities :'))

labels = []
# Enter  Name of activity
print("Now Enter the Name of Activites ")
for i in range(0, number):
    a = input("")
    labels.append(a)

ymax = 1
xmax = 1
work=0
plt.grid(True)
# a stores the data point as  (x,y)
choice=int(input("Use the data points in excel sheet (Press 1) or to use Duration pr gang per unit (Press2)"))

if choice ==1:
    a = np.array([])
    for i in range(1, ((3 * number) - 1), 3):
     b = df['X(Time)'][i]
     c = df['Y(Floors)'][i]
     d = df['X(Time)'][i + 1]
     e = df['Y(Floors)'][i + 1]
     a = np.append(a, b)
     a = np.append(a, c)
     a = np.append(a, d)
     a = np.append(a, e)

    print(a)


    ymax = np.maximum(1, a[1])
# n stores the rate of production


    n = np.array([])
    for l in range(2, ((3 * number)), 3):
        b = df['Rate of Production'][l]
        n = np.append(n, b)
    print(n)
    print("------n-----")
    n=np.reciprocal(n)
    print(n)



    print("To Display the Graph press 1 ")
    argument = int(input("To Check Number of Active Teams press 2 :  "))
    #switch statement
    while (argument != 9):
     if argument == 1:  # Plot
        plt.xlabel("Days / Weeks / Time")
        plt.ylabel("Floors/Units")
        plt.grid(True)
        for i in range(0, (4 * number), 4):
            plt.plot([a[i], a[i + 2]], [a[i + 1], a[i + 3]], label=labels[int(i / 4)], linewidth=2)

        leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
        leg.get_frame().set_alpha(0.5)
        plt.show()
        print("")
        print("To Display the Graph press 1")
        print("To Check Number of Active Teams press 2 ")
        argument = int(input("To change Any activity Duration press 3: TO EXIT PRESS 9 "))
     if argument == 2:
        count = 0
        yteam = int(input("Enter the day/week/ month to check for active teams:   "))
        for i in range(0, ((number - 1) * 4), 4):
            if (yteam > a[i]) & (yteam < a[i + 2]):
                count = count + 1
        print("The number of Teams Active : ")
        print(count)
        print("")
        print("To Display the Graph press 1")
        print("To Check Number of Active Teams press 2 ")
        argument = int(input("To change Any activity Duration press 3: TO EXIT PRESS 9 "))
     if argument == 3:
        c = int(input("Enter the activity number : "))
        print("Enter the X and Y coordinates of Staring point")
        a[(c - 1) * 4] = int(input("Enter the X coordinates of Staring point"))
        a[((c - 1) * 4) + 1] = int(input("Now the Y"))
        a[((c - 1) * 4) + 2] = int(input("Enter the X coordinates of Ending point"))
        a[((c - 1) * 4) + 3] = int(input("Now the Y"))
        print("")
        print("To Display the Graph press 1")
        print("To Check Number of Active Teams press 2 ")
        argument = int(input("To change Any activity Duration press 3: TO EXIT PRESS 9 "))

if choice==2:

# for unit wise calculations
 while work==0:
  n = np.array([])
  for l in range(2, ((3 * number)), 3):
    b = df['Duration per gang per unit'][l]
    n = np.append(n, b)
   #n duration  per floor per gang
  print(n)
  b = 0
  cp = np.array([])
  for l in range(1,n.size):
    b=b+n[l]
  print(b)
  a=b
  cp=np.append(cp,b)
  for l in range(1,n.size):
    b=b-n[l]
    print(b)
    cp=np.append(cp,b)
  print(cp)
  #Target completion graph
  setupp=int(input("Enter any setup period to be waited before the project commerces"))
  boxunits=int(input("Enter no of box units to be produced"))
  targettime=int(input("Enter the time of completion of all the units"))
  plt.xlabel("Days / Weeks / Time")
  plt.ylabel("Floors/Units")
  plt.grid(True)
  plt.plot([(a+setupp),targettime],[0,boxunits],linewidth=2,label="Target Completion Time Graph")
  leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
  leg.get_frame().set_alpha(0.5)
  plt.show()
  idealworkcheck=int(input("Enter the day to be examined :"))
  p=np.array([])
  for i in range(0,number):
     b=((idealworkcheck+cp[i]-(a+setupp))*(boxunits/(targettime-(a+setupp))))+1
     p=np.append(p,b)

  plt.xlabel("Activities")
  plt.ylabel("Floors/Units")
  plt.grid(True)
  N = len(p)
  x = range(N)
  width = 1/1.5
  plt.bar(x, p, width, color="blue")
  plt.show()
  # Gang graph
  m=np.array([])
  print("Enter number of gangs available per activity : ")
  for i in range(0,number):
    b=int(input(""))
    m=np.append(m,b)
  #m  stores number of gangn
  b=np.array([])

  for i in range(0,number):
    a= np.reciprocal(n[i])*m[i]
    b=np.append(b,a)
  print(b)#slope matrix
  print(b)
  n=np.reciprocal(b)#duration matrix
  print(n)
  plt.xlabel("Days / Weeks / Time")
  plt.ylabel("Floors/Units")
  plt.grid(True)
  y=0
  plt.plot([(setupp+n[0]),(setupp+(boxunits*n[0]))],[1,boxunits], label=labels[0], linewidth=2)
  x0=setupp+n[0]
  for l in range(1,number):
      if b[l-1]>b[l]:#fast to slow
        x0 = x0 + n[l]
        y=((boxunits-1)/(b[l]))+x0
        plt.plot([x0,y], [1, boxunits], label = labels[i], linewidth = 2)
      elif b[l-1]<b[l]:#slow to fast:
         x0=((y-x0)*(1-(b[l-1])/b[l]))+x0+n[l]
         y = ((boxunits - 1) / (b[l])) + x0
         plt.plot([x0, y], [1, boxunits], label = labels[i], linewidth = 2)
  leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
  leg.get_frame().set_alpha(0.5)
  plt.show()
 #for work to progress at same rate as act1
 # n = np.array([])
  for l in range(2, ((3 * number)), 3):
     b = df['Duration per gang per unit'][l]
     n = np.append(n, b)
     print(n)
  print(" ")
  print(" The Project Completes in " ,y ," Days ")
  work=int(input("     Enter 0 to change the number of gangs availble .press 1 to quit   "))