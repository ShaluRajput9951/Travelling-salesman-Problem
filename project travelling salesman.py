import tkinter
from tkinter import *
import numpy as np
from sys import maxsize 
from tkinter import messagebox
from PIL import Image, ImageTk


root = Tk()

#window
root.title('The Travelling Salesman')
root.geometry('845x650')
root.configure(bg='lightblue')



#photo=PhotoImage(file="img.gif")
#label=Label(root,image=photo)
#label.place(x=0,y=0)





#text on main page
Label(root, text='The Travelling Salesman',fg='Red',bg='pink', font=("arial black", 28)).place(x=165, y=210)
Label(root, text='Hello Traveller',fg='green',bg='lightgreen', font=("arial black", 22)).place(x=295, y=270)
Label(root, text='Welcome To the World of Best Solutions!!',fg='blue',bg='skyblue', font=("arial black", 15)).place(x=185, y=320)

frame = Frame(root).pack()



#various functions


def graph_1():
    canvas_width = 650
    canvas_height = 500

    master = Tk()

    w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
    w.pack()

    la = w.create_line(100, 300, 192, 142, fill='black',
                   arrow=LAST, activefill='red', width=2)
    lb = w.create_line(200, 140, 391, 140, fill='black',
                   arrow=LAST, activefill='green', width=2)
    lc = w.create_line(400, 140, 551, 236, fill='black',
                   arrow=LAST, activefill='blue', width=2)
    ld = w.create_line(560, 240, 358, 322, fill='black',
                   arrow=LAST, activefill='brown', width=2)
    le = w.create_line(350, 320, 110, 300, fill='black',
                   arrow=LAST, activefill='yellow', width=2)
    a = w.create_oval(93, 293, 107, 307, fill='black')
    b = w.create_oval(193, 133, 207, 147, fill='black')
    c = w.create_oval(393, 133, 407, 147, fill='black')
    d = w.create_oval(553, 233, 567, 247, fill='black')
    e = w.create_oval(343, 313, 357, 327, fill='black')
    na = w.create_text(93, 320, font=('arial black', 12), text='Chandigarh')
    nb = w.create_text(193, 120, font=('arial black', 12), text='Ludhiana')
    nc = w.create_text(393, 120, font=('arial black', 12), text='Patiala')
    nd = w.create_text(590, 220, font=('arial black', 12), text='Amritsar')
    ne = w.create_text(343, 340, font=('arial black', 12), text='Jalandhar')
    master.mainloop()


def about_us():
    ab = Toplevel()
    ab.title('About US')
    ab.geometry('525x300')
    ab.configure(bg='orange')
    Label(ab, text="We Provide You with the best and optimal \nsolutions to your problems\n and path to your destination.",bg='lightgreen', fg='black', font=("arial black", 13)).place(x=50,y=110)
    back_button = Button(ab, text='Back',bg='red', fg='black', width=8, height=1, font=("arial black",10), command=ab.destroy).place(x=220,y=200)
    
    
    
    
    
def get_started():
    global e3
    cin=Toplevel()
    cin.title("Getting Started")
    cin.geometry('525x525')
    cin.configure(bg='lightgreen')
    Label(cin, text="Welcome",bg='gold',fg='green' ,font=("arial black", 30)).place(x=160,y=20)

    Label(cin, text='Name',bg='pink',fg='red' ,font=("arial black", 12)).place(x=120,y=120)
    Label(cin, text='Gender',bg='skyblue',fg='blue' ,font=("arial black", 12)).place(x=120,y=160)
    Label(cin, text='Enter Unique ID',bg='yellow2',fg='gold4' ,font=("arial black", 12)).place(x=120,y=260)
   

    
    var1 = IntVar()
    Checkbutton(cin, text="Male", variable=var1).place(x=300,y=160)
    var2 = IntVar()
    Checkbutton(cin, text="Female", variable=var2).place(x=300,y=190)
    var3 = IntVar()
    Checkbutton(cin, text="Other", variable=var3).place(x=300,y=220)
    
    enter_button = Button(cin, text='Enter',bg='green', fg='black', width=8, height=1, font=("arial black",12), command=enter_cities).place(x=330,y=320)

    e1 = Entry(cin)
    e2 = Entry(cin)
    e1.place(x=300,y=120)
    e2.place(x=300,y=265)

    back_button = Button(cin, text='Back',bg='red', fg='black', width=8, height=1, font=("arial black",12), command=cin.destroy).place(x=120,y=320)

    cin.mainloop()
    

    
def enter_cities():
    
    cit=Toplevel()
    cit.title("Enter Cities")
    cit.geometry('500x510')
    cit.configure(bg='gold2')
    Label(cit, text="Hey There!",bg='pink',fg='red', font=("arial black", 25)).place(x=150,y=10)

    Label(cit, text='Hello Sir/Mam ! We understand that you need to go\n to 5 cities exatly only once and return to the same city using the shortest path.\n The Given Cities are \n1.Ludhiana\n2.Jalandhar\n3.Amritsar\n4.Amritsar\n5.Patiala',bg='skyblue',fg='blue', font=("arial black", 8)).place(x=8,y=80)
    Label(cit, text="City     Ludhiana   Jalandhar   Amritsar   Chandigarh  Patiala", font=("arial black", 10)).place(x=42,y=220)
    Label(cit, text="Ludhiana         0             61           140           106           93          ", font=("arial black", 10)).place(x=42,y=244)
    Label(cit, text="Jalandhar        61             0           80           149             154       ",font=("arial black", 10)).place(x=42,y=268)
    Label(cit, text="Amritsar         140             80           0           229          235         ",font=("arial black", 10)).place(x=42,y=288)
    Label(cit, text="Chandigarh    106             149           229           0          75         ", font=("arial black", 10)).place(x=42,y=310)
    Label(cit, text="Patiala              93             154           235           75          0          ",font=("arial black", 10)).place(x=42,y=332)
    shortest_button = Button(cit, text='Click here to Find Shortest Distance',bg='lightgreen', fg='black', width=30, height=1, font=("arial black",12), command=funct).place(x=90,y=360)
    show_graph_button = Button(cit, text='Show The Graph of Shortest Path',bg='seagreen', fg='black', width=30, height=1, font=("arial black",12), command=cit.graph_1).place(x=90,y=410)
    back_button = Button(cit, text='Back',bg='red', fg='black', width=8, height=1, font=("arial black",12), command=cit.destroy).place(x=200,y=460)

    cit.mainloop()
    
V=5
# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 

    # store all vertex apart from source vertex 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 

    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 

    while True: 

        # store current Path weight(distance) 
        current_pathweight = 0

        # compute current path weight 
        k = s 
        for i in range(len(vertex)): 
            current_pathweight += graph[k][vertex[i]] 
            k = vertex[i] 
        current_pathweight += graph[k][s] 

        # update minimum 
        min_path = min(min_path, current_pathweight) 

        if not next_permutation(vertex): 
            break

    return min_path 

# next_permutation implementation 
def next_permutation(L): 

    n = len(L) 

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]: 
        i -= 1

    if i == -1: 
        return False

    j = i + 1
    while j < n and L[j] > L[i]: 
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i] 

    left = i + 1
    right = n - 1

    while left < right: 
        L[left], L[right] = L[right], L[left] 
        left += 1
        right -= 1

    return True

# Driver Code 
def funct():

    # matrix representation of graph 
    graph = [[0,61,140,106,93], [61,0,80,149,154], 
            [140,80,0,229,235], [106,149,229,0,75], [93,154,235,75,0]] 
    s = 0
    xyz=travellingSalesmanProblem(graph, s)
    abc = Toplevel()
    abc.title('The Shortest Path')
    abc.geometry('300x300')
    abc.configure(bg='lightgreen')
    Label(abc, text=xyz,bg='pink', fg='red', font=("arial black", 20)).pack(pady=20)
    Label(abc, text='This is the least Distance that the\nSalesman needs to cover', bg='skyblue',fg='blue', font=("arial black", 10)).pack(pady=10)
    back_button = Button(abc, text='Back',bg='red', fg='black', width=8, height=1, font=("arial black",12), command=abc.destroy).pack(pady=20)


    

start_button = Button(frame, text='Get Started',bg='green', fg='black', width=10, height=1, font=("arial black",12), command=get_started).place(x=360, y=400)
about_button = Button(frame, text='About Us',bg='orange', fg='black', width=10, height=1, font=("arial black",12), command=about_us).place(x=360, y=450)
back_button = Button(frame, text='Exit',bg='red', fg='black', width=10, height=1, font=("arial black",12), command=root.destroy).place(x=360,y=500)
root.mainloop()
