#!/usr/bin/python

class ModuleE:

    def __init__(self):
        pass

    @staticmethod
    def return_true():
        return True  # covered by pytest

    @staticmethod
    def return_false():
        return False # covered by unittest