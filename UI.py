from tkinter.tix import *
from tkinter import ttk
from tkinter import *
import main


# pass information to play3
class Information:
    def __init__(self, gridWidth, gridHeight, numberOfBalls, ballRadius, hitPoint, vx, vz):
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.numberOfBalls = numberOfBalls
        self.ballRadius = ballRadius
        self.hitPoint = hitPoint
        self.vx = vx
        self.vz = vz

    # get instance
    def get(self):
        return self.gridWidth, self.gridHeight, self.numberOfBalls, self.ballRadius, self.hitPoint, self.vx, self.vz

    # start Physics
    def StartBall(self):
        main.StartMain(self.gridWidth, self.gridHeight, self.numberOfBalls, self.ballRadius, self.hitPoint, self.vx, self.vz)


# GUI
class Gui:
    options = ['Top', 'Middle', 'Pure', 'Bottom']
    # define root
    info = Information(0, 0, 0, 0, 0, 0, 0)
    root = Tk(className='Balls')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # get full size
    root.geometry("%dx%d" % (screen_width, screen_height))
    # define image
    background_Image = PhotoImage(file="marbles.png")

    def __init__(self):
        self.my_canvas = Canvas(self.root, width=self.screen_width, height=self.screen_height)
        self.my_canvas.pack(fill="both", expand=True)

        # set image in canvas
        self.my_canvas.create_image(0, 0, image=self.background_Image, anchor="nw")

        # grid width & height
        self.grid_length_entry = Entry(self.root)
        self.my_canvas.create_text(300, 40, text="Enter Grid's Length :", fill='white', anchor="nw",
                                   font=('Arial Bold', 20))
        self.my_canvas.create_window(300, 80, anchor="nw", window=self.grid_length_entry, width=300, height=60)
        self.grid_width_entry = Entry(self.root)
        self.my_canvas.create_text(800, 40, text="Enter Grid's Width :", fill='white', anchor="nw",
                                   font=('Arial Bold', 20))
        self.my_canvas.create_window(800, 80, anchor="nw", window=self.grid_width_entry, width=300, height=60)

        # ball information
        self.radius_entry = Entry(self.root)
        self.my_canvas.create_text(300, 170, text="Enter Ball's Radius (cm):", fill='white', anchor="nw",
                                   font=('Arial Bold', 20))
        self.my_canvas.create_window(300, 210, anchor="nw", window=self.radius_entry, width=300, height=60)
        self.num_of_balls_entry = Entry(self.root)
        self.my_canvas.create_text(800, 170, text="Enter the Number of Balls :", fill='white', anchor="nw",
                                   font=('Arial Bold', 20))
        self.my_canvas.create_window(800, 210, anchor="nw", window=self.num_of_balls_entry, width=300, height=60)

        # velocity
        self.velocity_x_entry = Entry(self.root)
        self.my_canvas.create_text(300, 300, text="Enter Velocity On X (m/s):", fill='white', anchor="nw",
                                   font=('Arial Bold', 20))
        self.my_canvas.create_window(300, 340, anchor="nw", window=self.velocity_x_entry, width=300, height=60)
        self.velocity_z_entry = Entry(self.root)
        self.my_canvas.create_text(800, 300, text="Enter Velocity On Z (m/s):", fill='white', anchor="nw",
                                   font=('Arial Bold', 20))
        self.my_canvas.create_window(800, 340, anchor="nw", window=self.velocity_z_entry, width=300, height=60)

        self.my_canvas.create_text(560, 450, text="Enter Ball's Hit Point:", fill='white', anchor="nw",
                                   font=('Arial Bold', 20))
        self.drop = ttk.Combobox(self.root, values=self.options, font=('Arial ', 20))
        self.drop.current(0)
        self.my_canvas.create_window(600, 490, window=self.drop, anchor="nw", width=200, height=60)
        self.drop.bind("<<ComboboxSelected>>", self.selected)

        # Start Button
        self.start_button = Button(self.root, text="Start ", justify=CENTER, font=('Arial Bold', 35),
                                   command=lambda: [self.setValue(), self.root.destroy()])
        self.my_canvas.create_window(600, 600, anchor="nw", window=self.start_button, width=200, height=60)

        self.root.mainloop()

    def selected(self, event):
        pass

    def __del__(self):
        pass

    def setValue(self):
        invalidInput = False
        if float(self.num_of_balls_entry.get()) < 0:
            self.num_of_balls_entry.delete(0, 'end')
            invalidInput = True
        if float(self.radius_entry.get()) < 0:
            self.radius_entry.delete(0, 'end')
            invalidInput = True
        if float(self.grid_length_entry.get()) < 0:
            self.grid_length_entry.delete(0, 'end')
            invalidInput = True
        if float(self.grid_width_entry.get()) < 0:
            self.grid_width_entry.delete(0, 'end')
            invalidInput = True


        if not invalidInput:
            grid_width = self.grid_length_entry.get()
            grid_height = self.grid_width_entry.get()
            radius = self.radius_entry.get()
            number_of_balls = self.num_of_balls_entry.get()
            hit_point = self.drop.get()
            vx = self.velocity_x_entry.get()
            vz = self.velocity_z_entry.get()
            Information(grid_width, grid_height, number_of_balls, radius, hit_point, vx, vz).StartBall()
            self.__del__()
        else:
            Gui()

    def get(self):
        return self.info


Gui()
