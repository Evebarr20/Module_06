#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 19:34:14 2026

@author: evebarr20
"""

class Date:
    """Represents a year, month, and day"""
    def __init__(self, year, month, day):
        """
        constructor method
        Initializes a Date object
        
        Parameters
        ----------
        year : int
            represents the year.
        month : int
            represents the month.
        day : int
            represents the day.

        Returns
        -------
        None.

        """
        self.year = year
        self.month = month
        self.day = day
    
    # I don't need make_date function because I used a constructor method instead
    def print_date(self):
        """
        prints Date object

        Returns
        -------
        None.

        """
        print(f"{self.year}-{self.month:02d}-{self.day:02d}")
    
    def date_to_tuple(self):
        """
        converts Date object into a tuple

        Returns
        -------
        tuple
            tuple that contains year, month, and day.

        """
        return (self.year, self.month, self.day)
        
    def is_after(self, other):
        """
        Takes two Date objects and returns True if the first comes after the second

        Parameters
        ----------
        other : Date Object
            Other date object.

        Returns
        -------
        bool
            True if first date comes after the second.

        """
        return self.date_to_tuple() > other.date_to_tuple()