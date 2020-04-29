"""
Project Skyforce -- Aaron Ma & Rohan Fernandes
@NOTE(aaronhma): AARON should we add any of our modules to pypi
Copyright 2020 - Present Rohan Fernandes & Aaron Ma

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from collections import Sequence, Iterator
from math import ceil
import random as rand          # Random library
import datetime as timing       # Datetime library
import time as current_time    # Time library
import math                    # Math library
import turtle                  # Turtle library
import decimal                 # Decimal library
import requests  # Requests library
import colorama  # Colorama library
import flask  # Flask library
# Functions


def user(msg):
    """
    Get the user's name.
    - input:
        - message to display
    """
    user = input("What is your name? ")
    print("Hello {}! {}".format(user, msg))


def timer(time):
    """
    A timer function.
    - input:
        - time of counting down
    """
    timer = int(timer)         # convert timer to an integer
    for i in range(timer):     # for loop
        print(timer)           # print
        current_time.sleep(1)  # wait
        timer -= 1             # countdown


def random(min_num, max_num):
    """
    Use a random number generator 
        - give a & b
    prints a random number
    """
    min_num = int(input("What is the minumum? "))  # min number
    max_num = int(input("What is the maximum? "))  # maximum number
    # select a random number between min - max
    num = rand.randint(min_num, max_num)
    print(num)  # print the random #


def floor(num):
    """
    Give a decimal and it will return the number floored
    """
    new_num = math.floor(num)
    print("rf", new_num)
    return new_num


def round(flt):
    """
    Rounds number up or down, depending ONLY on LAST digit
    """
    strflt = str(flt)
    newstrflt = strflt[-1:]
    intstrflt = int(newstrflt)
    if (intstrflt >= 5):
        newflt = floor(flt)
        newflt = newflt + 1
    else:
        newflt = floor(flt)
    print(newflt)


def calculator(a, operator, b):
    """
    A calculator function for basic  2 number calculations
    """
    if (operator == "*" or "multiply"):
        num = a*b
        print(num)
    elif (operator == "/" or "divide"):
        num = a/b
        print(num)
    elif (operator == "-" or "subract"):
        num = a - b
        print(num)
    elif (operator == "+" or "add"):
        num = a + b
        print(num)
    else:
        print("invalid")

# Xrange


class xrange(Sequence):
    """Pure-Python implementation of an ``xrange`` (aka ``range``
    in Python 3) object.
    """

    def __init__(self, *args):
        if len(args) == 1:
            start, stop, step = 0, args[0], 1
        elif len(args) == 2:
            start, stop, step = args[0], args[1], 1
        elif len(args) == 3:
            start, stop, step = args
        else:
            raise TypeError('xrange() requires 1-3 int arguments')

        try:
            start, stop, step = int(start), int(stop), int(step)
        except ValueError:
            raise TypeError('an integer is required')

        if step == 0:
            raise ValueError('xrange() arg 3 must not be zero')
        elif step < 0:
            stop = min(stop, start)
        else:
            stop = max(stop, start)

        self._start = start
        self._stop = stop
        self._step = step
        self._len = (stop - start) // step + bool((stop - start) % step)

    def __repr__(self):
        if self._start == 0 and self._step == 1:
            return 'xrange(%d)' % self._stop
        elif self._step == 1:
            return 'xrange(%d, %d)' % (self._start, self._stop)
        return 'xrange(%d, %d, %d)' % (self._start, self._stop, self._step)

    def __eq__(self, other):
        return isinstance(other, xrange) and \
            self._start == other._start and \
            self._stop == other._stop and \
            self._step == other._step

    def __len__(self):
        return self._len

    def index(self, value):
        """Return the 0-based position of integer `value` in
        the sequence this xrange represents."""
        diff = value - self._start
        quotient, remainder = divmod(diff, self._step)
        if remainder == 0 and 0 <= quotient < self._len:
            return abs(quotient)
        raise ValueError('%r is not in range' % value)

    def count(self, value):
        """Return the number of ocurrences of integer `value`
        in the sequence this xrange represents."""
        # a value can occur exactly zero or one times
        return int(value in self)

    def __contains__(self, value):
        """Return ``True`` if the integer `value` occurs in
        the sequence this xrange represents."""
        try:
            self.index(value)
            return True
        except ValueError:
            return False

    def __reversed__(self):
        """Return an xrange which represents a sequence whose
        contents are the same as the sequence this xrange
        represents, but in the opposite order."""
        sign = self._step / abs(self._step)
        last = self._start + ((self._len - 1) * self._step)
        return xrange(last, self._start - sign, -1 * self._step)

    def __getitem__(self, index):
        """Return the element at position ``index`` in the sequence
        this xrange represents, or raise :class:`IndexError` if the
        position is out of range."""
        if isinstance(index, slice):
            return self.__getitem_slice(index)
        if index < 0:
            # negative indexes access from the end
            index = self._len + index
        if index < 0 or index >= self._len:
            raise IndexError('xrange object index out of range')
        return self._start + index * self._step

    def __getitem_slice(self, slce):
        """Return an xrange which represents the requested slce
        of the sequence represented by this xrange.
        """
        start, stop, step = slce.start, slce.stop, slce.step
        if step == 0:
            raise ValueError('slice step cannot be 0')

        start = start or self._start
        stop = stop or self._stop
        if start < 0:
            start = max(0, start + self._len)
        if stop < 0:
            stop = max(start, stop + self._len)

        if step is None or step > 0:
            return xrange(start, stop, step or 1)
        else:
            rv = reversed(self)
            rv._step = step
            return rv

    def __iter__(self):
        """Return an iterator which enumerates the elements of the
        sequence this xrange represents."""
        return xrangeiterator(self)


class xrangeiterator(Iterator):
    """An iterator for an :class:`xrange`.
    """

    def __init__(self, xrangeobj):
        self._xrange = xrangeobj

        # Initialize the "last outputted value" to the value
        # just before the first value; this simplifies next()
        self._last = self._xrange._start - self._xrange._step
        self._count = 0

    def __iter__(self):
        """An iterator is already an iterator, so return ``self``.
        """
        return self

    def next(self):
        """Return the next element in the sequence represented
        by the xrange we are iterating, or raise StopIteration
        if we have passed the end of the sequence."""
        self._last += self._xrange._step
        self._count += 1
        if self._count > self._xrange._len:
            raise StopIteration()
        return self._last

# Progress Bar


def progress_bar(t):
    """Prints a progress bar that take t seconds to complete loading."""

    from time import sleep

    for i in range(1, 101):
        print("\r{:>6}% |{:<30}|".format(
            i, u"\u2588" * round(i // 3.333)), end='', flush=True)
        sleep(t/100)

    sleep(0.1)
    print("\n")


def pyrange(n):
    """
    Pure Python Implementation and Use to Understand Range and using it. Alternative to XRange but does not allow action in the for loop 
    """
    zen = 0
    while zen < 0:
        zen = zen + 1
        #Do Stuff
    print("finished")
    
def err_raise(error,notes):
    if err_raise == "ValueError":
        raise ValueError(notes)
    elif err_raise == "TypeError":
        raise TypeError(notes)
    elif err_raise == "NoneTypeError":
        raise NoneTypeError(Notes)

class Human():
    def __init__(self,f_name,l_name,age,status):
        self.f_name = f_name
        self.l_name = l_name
        self.status = status
        self.age = age
    
    def intro(self):
        print("Found person: {} {} who is {} years old and works as {} onboard.".format(f_name, l_name, age, status))
    
    def find_birth_year(self):
        year = timing.datetime.now().year
        print(year - (self.age))
    
    def talk(self, expression):
        pass

    def status_check(self):
        if self.status == "administrator":
            pass
        elif self.status == "mission control":
            pass
        elif self.status == "commander":
            pass
        elif self.status == "astronaut":
            pass
        else:
            print("[ALERT] I've never seen anything like that before!")

    def change_access(self, new_status):
        old_status = self.status
        self.status = new_status
        print("Successfully changed permissions from {} to {}".format(old_status, self.status))
    
# RESOLVED - @TODO(aaronhma,rohan): find a way to funnel use class Human in server for enabling privleges based on status
# do this for each astronaut/person who uses this as a record keeper
aaron = Human("Aaron","Ma",11,"administrator")
rohan = Human("Rohan","Fernandes",11,"administrator")

aaron.intro()
rohan.intro()
