import random
from math import sin, cos
from matplotlib import pyplot as plt

## Represent a cannonball, tracking its position and velocity.
#
class PrintInterface:
    def plot(self, x, y):
        print("The ball is at (%.1f, %.1f)" % (x, y))
        plt.scatter(x, y)
        plt.pause(.01)

class Cannonball:
    ## Create a new cannonball at the provided x position.
    #  @param x the x position of the ball
    #
    def __init__(self, x):
        self._x = x
        self._y = 0
        self._vx = 0
        self._vy = 0

    ## Move the cannon ball, using its current velocities.
    #  @param sec the amount of time that has elapsed.
    #
    def move(self, sec, g):
        dx = self._vx * sec
        dy = self._vy * sec

        self._vy = self._vy - g * sec

        self._x = self._x + dx
        self._y = self._y + dy

    ## Get the current x position of the ball.
    #  @return the x position of the ball
    #
    def getX(self):
        return self._x

    ## Get the current y position of the ball.
    #  @return the y position of the ball
    #
    def getY(self):
        return self._y

    ## Shoot the canon ball.
    #  @param angle the angle of the cannon
    #  @param velocity the initial velocity of the ball
    #
    def shoot(self, angle, velocity, user_grav, printW):
        self._vx = velocity * cos(angle)
        self._vy = velocity * sin(angle)
        self.move(0.1, user_grav)

        # Compares the Y value to the lowest it can be.
        # As long as it is above a threshold, the coordinates are plotted
        # the move() method is called to advance the position of the "projectile."
        while self.getY() > 1e-14:
            printW.plot(self.getX(), self.getY())
            plt.scatter(self.getX(), self.getY())
            self.move(0.1, user_grav)

# class Crazyball is a class that inherits from Cannonball.
# it starts the x and y position at a random position,
# then uses a randomly generated gravity to plot a wonky trajectory.
class Crazyball(Cannonball):
    # Builds on the information initialized from Cannonball.
    # Adds new initialized values for x and y.
    def __init__(self, x, y):
        super().__init__(x)
        super().__init__(y)

        self.x = random.randrange(0, 10)
        self.y = random.randrange(0, 10)

    # Carries out the incrementing of the x and y values to similuate the
    # "projectile" moving in the plot.
    def move(self, sec, g):
        super().move(sec, g)

        if self.getX() < 400:
            self._vx += random.uniform(-1, 1)
            self._vy += random.uniform(-1, 1)

        if self.getX() > 400:
            self._vx -= random.uniform(-1, 1)
            self._vy -= random.uniform(-1, 1)


# class Main that creates a menu of options for the user.
class Main:
    # constructor that specifically creates a list of options that are available to the user.
    def __init__(self):
        self._options = ["Earth's Gravity", "Moon Gravity", "Crazy Trajectory", "Quit"]

    # displayMenu() method that uses a while loop to allow the user to make multiple selections,
    # a for loop to display the options for each selection made,
    # and if statements to get the correct inputs for whatever selection is made.
    def displayMenu(self):
        printW = PrintInterface()
        done = False
        while not done:
            for i in range(len(self._options)):
                print("%d %s" % (i + 1, self._options[i]))

            userChoice = int(input())
            if userChoice < 1 or userChoice > len(self._options):
                print('Enter a 1-4 only')
                continue
            if userChoice == 1:
                c1 = Cannonball(0)
                angle = float(input("Enter starting angle:"))
                v = float(input("Enter initial velocity:"))

                c1.shoot(angle, v, 9.81, printW)
            if userChoice == 2:
                c2 = Cannonball(0)
                angle = float(input("Enter starting angle:"))
                v = float(input("Enter initial velocity:"))

                c2.shoot(angle, v, 1.625, printW)

            if userChoice == 3:
                c3 = Crazyball(0, 0)
                angle = float(input("Enter starting angle:"))
                v = float(input("Enter initial velocity:"))

                g = random.randrange(0, 10)

                c3.shoot(angle, v, g, printW)

            if userChoice == 4:
                print("Quitting here")
                done = True
                quit()

# if statement to check if the file name is main.
# if so, run the following commands.
if __name__ == '__main__':
    menu1 = Main()

    menu1.displayMenu()
