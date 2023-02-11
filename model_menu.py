import model
import controller
import view

def select(number):
    if number == 1:
        model.save_number()
        repeat()
    elif number == 2:
        model.read_dict()
        repeat()
    elif number == 3:
        model.create_html()
        repeat()
    elif number == 4:    
        view.delete()
        controller.delete()
    elif number == 5:    
        view.exit()

def repeat():
    view.repeat()
    controller.start()
    
def delete(number):
    if number == 1:
        model.delete("csv")
    elif number == 2:
        model.delete("txt")
    elif number == 3:
        model.delete("html")
    elif number == 4:   
        model.delete("csv") 
        model.delete("txt")
        model.delete("html")
    repeat()