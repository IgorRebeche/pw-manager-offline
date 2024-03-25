# Import the necessary packages
import os
from time import sleep
from typing import Any, Callable, List

class Item:
    def __init__(self, title, command, alias, function: Callable[..., Any]) -> None:
        self.title = title
        self.command = command
        self.alias = alias
        self.function  = function


class TerminalViewService:
    def __init__(self) -> None:
        self.menu_itens: List[Item] = []
        pass
    
    def add_menu_item(self, item: Item):
        self.menu_itens.append(item)
    
    def run_main_loop(self):
        self.add_default_commands()
        
        print("You can start typing /help")
        while True:
            command_input = input("Digite um comando: ")
            
            if command_input.startswith('/'):
                parts = command_input.split()
                command = parts[0]
                args = parts[1:]
                
                found = False
                for i in self.menu_itens:
                    if i.command == command[1:] or i.alias == command[1:]:
                        try:
                            i.function(*args)
                        except Exception as e:
                            print("Something went wrong!", e)
                        found = True
                    
                if not found:
                    print("Unknown Command.")
            else:
                print("Commands should start with '/'.")
                
            if command_input == "/exit":
                print("Exiting...")
                break
    
    
    def add_default_commands(self):
        self.menu_itens.append(Item("To see the commands", "help", "hp", self.help_command))
        self.menu_itens.append(Item("Clean Terminal", "clear", "cls", self.clean_terminal))
    
    def help_command(self):
        print("Here is the list of commands")
        for item in self.menu_itens:
            print("Comand :", "/"+item.command, "Information:", item.title)
            
    def clean_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')