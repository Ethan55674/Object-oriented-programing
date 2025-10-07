from math import sin, cos, radians
from matplotlib import pyplot as plt
import random as random
## Represent a cannonball, tracking its position and velocity.
#
class Print_Iface:
    def display(self, x, y):
        print(f"The ball is at ({x:.1f}, {y:.1f})")
        plt.scatter(x, y)
        plt.pause(0.01)
class Cannonball:
## Create a new cannonball at the provided x position.
# @param x the x position of the ball
#
    def __init__(self, x):
        self._x = x
        self._y = 0
        self._vx = 0
        self._vy = 0
## Move the cannon ball, using its current velocities.
# @param sec the amount of time that has elapsed.
#
    def move(self, sec, grav=9.81):
        dx = self._vx * sec
        dy = self._vy * sec
        self._vy = self._vy - grav * sec
        self._x = self._x + dx
        self._y = self._y + dy
        if self.getX() < 400:
            self.rand_q = random.randrange(0,10)
## Get the current x position of the ball.
# @return the x position of the ball
#
    def getX(self):
        return self._x
## Get the current y position of the ball.
# @return the y position of the ball
#
    def getY(self):
        return self._y
## Shoot the canon ball.
# @param angle the angle of the cannon
# @param velocity the initial velocity of the ball
#
    def shoot(self, angle, velocity, user_grav):
        self._vx = velocity * cos(angle)
        self._vy = velocity * sin(angle)
        self.move(0.1, user_grav)
        while self.getY() > 1e-14:
            print("The ball is at (%.1f, %.1f)" % (self.getX(), self.getY()))
            plt.scatter(self.getX(), self.getY())
            plt.pause(.01)
            self.move(0.1, user_grav)
        

class Crazyball(Cannonball):
    def move(self, sec, grav=9.81):
        dx = self._vx * sec
        dy = self._vy * sec
        self._vy -= grav * sec

        if self.getX() < 400:
            rand_q = random.randrange(-10, 10)
            self._vx += random.uniform(-0.2, 0.2)
            self._vy += random.uniform(-0.2, 0.2)
            print(f" Random time.  Adjusting velocity by {rand_q} at x={self.getX():.1f}")

        self._x += dx
        self._y += dy

def main():
    plt.ion()

    while True:
        print("\n--- Cannonball Launcher ---")
        print("1. Earth Gravity")
        print("2. Moon Gravity")
        print("3. Crazy Trajectory")
        print("4. Quit")

        choice = input("Enter your choice 1-4: ")

        if choice == '4':
            print("Exiting program.")
            break

        if choice not in ['1', '2', '3']:
            print("Please enter 1, 2, 3, or 4.")
            continue

        angle_deg = float(input("Enter starting angle in degrees: "))
        v = float(input("Enter initial velocity: "))

        # convert to radians
        angle = radians(angle_deg)

        # set gravity based on choice
        if choice == '1':
            grav = 9.81
            ball = Cannonball(0)
        elif choice == '2':
            grav = 1.62  # Moon gravity
            ball = Cannonball(0)
        elif choice == '3':
            grav = 9.81
            ball = Crazyball(0)

        # simulate
        plt.figure()
        ball.shoot(angle, v, grav)
        plt.title("Cannonball Trajectory")
        plt.xlabel("X position (m)")
        plt.ylabel("Y position (m)")
        plt.show(block=False)

        input("Press Enter to continue")

if __name__ == '__main__':
    main()