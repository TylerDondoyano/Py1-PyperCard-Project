"""
This simple app demonstrates how cards can automatically advance to another
card after a certain amount of time. The auto_advance can either be a string
containing the name of the next card, or a function to call that returns the
name of the next card.
"""
from pypercard import App, Card


# The templates for these cards can be found in pypercard.html.
cards = [
    Card("card1"),
    Card("card2"),
    Card("card3"),
    Card("card4"),
    Card("card5"),
    Card("card6"),
]

# Create the app
carousel_app = App(
    name="PyperCard carousel", cards=cards
)

@carousel_app.transition("card1", "click", "Yes")
def Yes(app, card):
    return "card2"

@carousel_app.transition("card1", "click", "No")
def No(app, card):
    return "card3"

@carousel_app.transition("card2", "click", "Work_alone")
def Work_by_yourself(app, card):
    return "card4"

@carousel_app.transition("card4", "click", "Return")
def Return(app, card):
    return "card1"

@carousel_app.transition("card2", "click", "Cheat")
def Cheat(app, card):
    return "card5"

@carousel_app.transition("card5", "click", "Return")
def Return(app, card):
    return "card1"

@carousel_app.transition("card3", "click", "Attempt_project")
def Attempt_project(app, card):
    return "card2"

@carousel_app.transition("card3", "click", "Never_do_project")
def Never_do_project(app, card):
    return "card6"

@carousel_app.transition("card6", "click", "Return")
def Return(app, card):
    return "card1"

carousel_app.start("card1")