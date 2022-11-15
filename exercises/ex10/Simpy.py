"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730476042"


class Simpy:
    """Numpy like class."""
    values: list[float]

    def __init__(self, x: list[float]):
        """Create a list of floats."""
        self.values = x
    
    def __repr__(self) -> str:
        """Produce str representation of Simpy."""
        return f"Simpy({self.values})"
    
    def fill(self, value: float, amount: int) -> None:
        """Fills a Simpy's values with a specific number x amount of times."""
        i: int = 0
        self.values.clear()
        while i < amount:
            self.values.append(value)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill values attribute with range of values in terms of floats."""
        assert step != 0.0

        number: float = start
        i: int = 0
        
        if step > 0.0 and step.is_integer():
            while (i + step) < stop:
                self.values.append(number)
                number += step
                i += step
        elif step > 0.0:
            while (i) < stop:
                self.values.append(number)
                number += step
                i += step
        elif step < 0.0:
            while (i + step) > stop:
                self.values.append(number)
                number += step
                i += step
    
    def sum(self) -> float:
        """Sum all items in values attribute."""
        total: float = 0.0
        i: int = 0

        while i < len(self.values):
            total += self.values[i]
            i += 1
        return total
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add operator overload."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add operator overload."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce mask based on equality of values."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce maske based on greater than on values."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Use subscription operator with Simpy."""
        result: Simpy = ([])
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            for i in range(len(self.values)):
                if rhs[i] is True:
                    result.append(self.values[i])
        return result