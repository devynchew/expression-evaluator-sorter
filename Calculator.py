# Name: Devyn Chew Kim Hong
# Student ID: P2026578
# Class: DAAA/2B/04

import tkinter as tk
from Tokenize import Tokenize
from Parenthesized import Parenthesized
from BuildParseTree import BuildParseTree
from Evaluate import Evaluate

RESULT_FONT_STYLE = ("Arial", 38, "bold")
EXPRESSION_FONT_STYLE = ("Arial", 16)
ERROR_FONT_STYLE = ("Arial", 12)
BUTTONS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

CLEAR_COLOR = "#e76f51"
BUTTON_COLOR = "#264653"
EQUAL_COLOR = "#2a9d8f"
DISPLAY_COLOR = "#e9c46a"
LABEL_COLOR = "#ffffff"
EXPRESSION_COLOR = "#264653"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        # sets the width and height of window
        self.window.geometry("475x675")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.expression = "" # value of result
        self.result = "" # expression
        self.error = ""

        self.display_frame = self.create_display_frame() # create frame to store expression and result
        self.buttons_frame = self.create_buttons_frame() # create frame to store buttons
        # make the buttons fill the full space
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.expression_label, self.result_label, self.error_label = self.create_display_labels()

        # button : grid value of where to place the button
        self.buttons = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1), '**': (0,3), '\u0028': (4,3), '\u0029': (4,4)
        }

        self.operators = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.create_buttons() # create all buttons
        self.create_operator_buttons()
        self.create_equals_button()
        self.create_clear_button()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=DISPLAY_COLOR)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    # creating the label that takes in expression and the label that ouputs the result
    def create_display_labels(self):
        expression_label = tk.Label(self.display_frame, text=self.expression, anchor=tk.E, bg=DISPLAY_COLOR, fg=EXPRESSION_COLOR, padx=24, font=EXPRESSION_FONT_STYLE)
        expression_label.pack(expand=True, fill='both')

        result_label = tk.Label(self.display_frame, text=self.result, anchor=tk.E, bg=DISPLAY_COLOR,
                         fg=EXPRESSION_COLOR, padx=20, font=RESULT_FONT_STYLE)
        result_label.pack(expand=True, fill='both')

        error_label = tk.Label(self.display_frame, text=self.error, anchor=tk.E, bg=DISPLAY_COLOR,
                         fg=EXPRESSION_COLOR, padx=12, font=ERROR_FONT_STYLE, wraplength=450, justify="right")
        error_label.pack(expand=True, fill='both')

        return expression_label, result_label, error_label

    def create_buttons(self):
        for button, grid_value in self.buttons.items():
            button = tk.Button(self.buttons_frame, text=str(button), bg=BUTTON_COLOR, fg=LABEL_COLOR, font=BUTTONS_FONT_STYLE,
                               borderwidth=0, command=lambda x=button: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=BUTTON_COLOR, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.add_to_expression(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=EQUAL_COLOR, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=CLEAR_COLOR, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def clear(self):
        self.result = ""
        self.expression = ""
        self.error = ""
        self.update_expression_label()
        self.update_result_label()
        self.update_error_label()
    
    def update_expression_label(self):
        self.expression_label.config(text=self.expression)

    def update_result_label(self):
        self.result_label.config(text=self.result[:11])

    def update_error_label(self):
        self.error_label.config(text=self.error)
        self.error = ""

    def add_to_expression(self, value):
        self.expression += str(value)
        self.update_expression_label()

    # evaluating the expression
    def evaluate(self):

        try:
            self.error = ""
            expression_n = self.expression.replace(' ', '') # remove all whitespaces from expression
            expression_list = list(expression_n) # convert string to list

            valid = True # assume expression by user is valid first
            for i in range(len(expression_list)):
                if i == 0: # ensure first char in expression is a parenthesis
                    if len(expression_list) == 1:
                        self.error += 'Expression must be more than 1 character.'
                        valid = False
                        break
                    if expression_list[i] != '(':
                        self.error += 'Expression must start with parenthesis.'
                        valid = False
                        break
                elif i == len(expression_list) - 1: # ensure last char in expression is a parenthesis
                    if expression_list[i] != ')':
                        self.error += 'Expression must end with parenthesis.'
                        valid = False
                        break
                else: # ensure that only valid characters are used
                    if expression_list[i] not in ['+', '-', '*', '/', '(', ')', '.'] and not expression_list[i].isdigit():
                        self.error += 'Expression contains invalid characters. Only numbers, +, -, *, **, /, (, ) are allowed.'
                        valid = False
                        break
            if not valid: # input expression contains invalid characters
                self.update_error_label()
            else:
                # if we reached here, start tokenising
                tokenizeClass = Tokenize(exList=expression_list)
                l = tokenizeClass.tokenize()

                # Check if expressions are fully parenthesized
                parenthesizedClass = Parenthesized(exList=l)
                valid = parenthesizedClass.checkParenthesis()

                if not valid: # input expression is not fully parenthesized
                    self.error += 'Expression must be fully parenthesized.'
                    self.update_error_label()
                else: # we got a valid expression
                    tree = BuildParseTree.buildParseTree(l)
                    self.result = str(Evaluate.evaluate(tree))
                    self.update_result_label()
        except:
            self.error += 'Please enter a fully parenthesized expression.'
            self.update_error_label()

    def run(self):
        self.window.mainloop()
