#Created by: Justin Bronson
#Created on: Oct 2017
#

import ui

def calculate_leap_year_touch_up_inside(sender):
    leapyear = int(view['year_textfield'].text)
    
    if (leapyear % 4) == 0:
      if (leapyear % 100) == 0:
        if (leapyear % 400) == 0:
          view['answer_label'].text = 'It is a leap year.'
        else:
          view['answer_label'].text = 'It is not a leap year.'
      else:
        view['answer_label'].text = 'It is a leap year.'
    else:
      view['answer_label'].text = 'It is not a leap year.'

view = ui.load_view()
view.present('sheet')
