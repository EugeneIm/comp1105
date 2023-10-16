# modularized programming
# each task within the program should be its own function
# top down design
# breaks the algo into different functions
# Hierarchy chart
# Depitction of relations between functions and the order they work together.

# IPO charts
# Input, Procession, Output.
# Design and document functions
# i.e
# IPO chart for a function to get a price of an item

input = "none"
processing = "get the user to input a price using float(input('...'))"
output = "the price that the user set it as"

# IPO chart to use that same price and make a discount
input = "price set by user"
processing = "calculation such as (price * 0.8) for a 20 percent discount"
output = "the price of the item after discount, i.e. $10 item on a 20 % discount is $8"


#Library functions are pre-written functions that come with python such as 'print', 'input', 'range', ...

#Calling a function from a module requires 'import ...' at the top of the program

