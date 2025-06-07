import os
import json
import configparser

class logger:
    def __init__(self):
        self.colors = {
            "yellow": "\033[01;33m",
            "white": "\033[01;37m",
            "green": "\033[01;32m",
            "blue": "\033[01;34m",
            "cyan": "\033[36m",
            "red": "\033[1;31m",
            "reset": "\033[0m",
        }

    def info(self, message: str):
        print(f"[{self.colors['blue']}*{self.colors['reset']}]{message}") 

    def success(self, message: str):
        print(f"[{self.colors['green']}+{self.colors['reset']}]{message}") 

    def error(self, message: str):
        print(f"[{self.colors['red']}-{self.colors['reset']}]{message}") 

    def found(self, message: str):
        print(f"[{self.colors['red']}!{self.colors['reset']}]{message}") 

    def type(self, message: str):
        print(f"\n{self.colors['yellow']}>> {self.colors['reset']}{message}") 


    def debug(self, message: str):
        print(f"[{self.colors['yellow']}DEBUG{self.colors['reset']}]{message}") # TODO Check config if logging.debug is set or not
