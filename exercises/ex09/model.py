"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730476042"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, second: Point) -> float:
        """Find the distance between two cells and return a new Point."""
        x: float = (second.x - self.x) ** 2
        y: float = (second.y - self.y) ** 2
        distance: float = sqrt(x + y)
        return distance

    
class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    
    def __init__(self, location: Point, direction: Point, sickness: int = constants.VULNERABLE):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
        self.sickness = sickness

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Update the cells location by adding direction."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return color of cell depending on sickness."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red" 
        elif self.is_immune():
            return "blue"
    
    def contract_disease(self) -> None:
        """Assign infected to sickness attribute."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Return True is sickness is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Return True if sickness is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def contact_with(self, cell: Cell) -> None:
        """Infected cell will make an vulnerable cell infected with contact."""
        if self.is_infected() and cell.is_vulnerable():
            cell.contract_disease()
        elif self.is_vulnerable() and cell.is_infected():
            self.contract_disease()

    def immunize(self) -> None:
        """Assign immune to sickness attribute of Cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns True if cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False
    

class Model:
    """The state of the simulation."""
    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with infected, random locations, directions, and immunity."""
        self.population = []
        if (infected + immune) >= cells or infected <= 0 or immune >= (cells):
            raise ValueError("# of infected and/or immune cells exceeds # of cells in model.")
        
        for i in range(cells - (infected + immune)):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            sick: int = constants.VULNERABLE
            cell: Cell = Cell(start_location, start_direction, sick) 
            self.population.append(cell)
        
        for i in range(infected):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            sick: int = constants.INFECTED
            cell: Cell = Cell(start_location, start_direction, sick)
            self.population.append(cell)
        
        for i in range(immune):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            sick: int = constants.IMMUNE
            cell: Cell = Cell(start_location, start_direction, sick)
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_X
            cell.direction.y *= -1.0
            
    def check_contacts(self) -> None:
        """Compare distance between Cells to check for contact."""
        # infected_cells: list[Cell] = []
        # for cell in self.population:
        #     if cell.is_infected():
        #         infected_cells.append(cell)
        
        for cell in range(len(self.population)):
            for cells in range(cell + 1, len(self.population)):
                disance: float = self.population[cell].location.distance(self.population[cells].location)
                if disance < constants.CELL_RADIUS:
                    self.population[cell].contact_with(self.population[cells])

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True
