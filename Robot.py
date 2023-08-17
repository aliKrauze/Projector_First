
class Robot:
    def __init__(self):
        self.orientation = 'up'
        self.position_x = 0
        self.position_y = 0

    def move(self, steps):
        if self.orientation == 'up':
            self.position_y += steps
        elif self.orientation == 'dawn':
            self.position_y -= steps
        elif self.orientation == 'left':
            self.position_x -= steps
        elif self.orientation == 'right':
            self.position_x += steps

    def turn(self, direction):
        if direction == 'left':
            if self.orientation == 'up':
                self.orientation = 'left'
            elif self.orientation == 'left':
                self.orientation = 'down'
            elif self.orientation == 'down':
                self.orientation = 'right'
            elif self.orientation == 'right':
                self.orientation = 'up'
        elif self.orientation == 'right':
            if self.orientation == 'up':
                self.orientation = 'right'
            elif self.orientation == 'right':
                self.orientation = 'down'
            elif self.orientation == 'down':
                self.orientation = 'left'
            elif self.orientation == 'left':
                self.orientation = 'up'

    def display_position(self):
        print(f"Robot Position is: ({self.position_x}, {self.position_y}), Orientation: {self.orientation}")


robot = Robot()
robot.move(3)
robot.turn('right')
robot.move(1)
robot.display_position()
