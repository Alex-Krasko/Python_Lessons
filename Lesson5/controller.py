import modul
import view

def Button_Click():
    value_a = view.get_value()
    value_b = view.get_value()
    modul.Init(value_a, value_b)
    result = modul.sum()
    result1 = modul.mult()
    view.view_data(result, 'Sum')
    view.view_data(result1, 'Mult')