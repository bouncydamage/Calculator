  import tkinter

  cal_buttons = [
    ["AC", "+/-", "%", "÷"]
    ["7", "8", "9", "x"]
    ["4", "5", "6", "-"]
    ["1", "2", "3", "+"]
    ["0", ".", "√", "="]
  ]

  row_count = len(cal_buttons)
  column_count = len(cal_buttons[0])

  right_symbol = ["÷", "x", "-", "+", "="]
  top_symbol = ["AC", "+/-", "%"]

  color_light_gray = "gray"
  color_black = "black"
  color_dark_gray = "blue"
  color_orange = "orange"
  color_white = "white"

#setup window
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("arial", 45, "bold"), background=color_black, foreground=color_white anchor="e", width="column_count")

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

  for row in range(row_count):
    for column in range(column_count):
      value = cal_buttons[row][column]
      button = tkinter.Button(frame, text=value, font=("Arial", 30),
                              width=column_count-1, height=1,
                              command=lambda value=value: button_clicked(value))
      if value in top_symbol:
        button.config(foreground=color_black, background=color_light_gray)
      elif value in right_symbol:
        button.config(foreground=color_white, background=color_orange)
      else:
        button.config(foreground=color_white, background=color_dark_gray)
      button.grid(row=row+1, column=column)

frame.pack()


A = "0"
operator = None
B = None

def clear_all():
  global A, B, operator

def remove_decimal(num)
  if num % 1 == 0:
    num = int(num)
  return str(num)

  def button_clicked(value):
    global right_symbol, top_symbol, label, A, B, operator

    if value in right_symbol:
        if value = "=":
          if A is not None and operator os not None:
            B = label["text"]
            numA = float(A)
            numB = float(B)
            if operator == "+":
              label["text"] = remove_decimal(NumA + NumB)
            elif operator == "-":
              label["text"] = remove_decimal(NumA - NumB)
            elif operator == "x":
              label["text"] = remove_decimal(NumA * NumB)
            elif operator == "÷":
              label["text"] = remove_decimal(NumA / NumB)

            clear_all()
      
        elif value in "+-x÷"
          if operator is None:
            A = label["text"]
            label["text"] = "0"
            B = "0"
          operator = value
    
    elif value in top_symbol:
        if value == "AC":
          label["text"] = "0"
        elif value == "+/-":
          result = float(label["text"] * -1)
          label["text"] = remove_decimal(result)
        elif value == "%":
          result = float(label["text"] / 100)
          label["text"] = remove_decimal(result)
        elif value == "√":
          result = float(label["text"] / )
          label["text"] = remove_decimal(result)
    else:
      if value == ".":
          if value not in label["text"]:
            label["text"] += value
      elif value in "0123456789":
        if label["text"] == "0"
            label["text"] = value
        else:
          label["text"] += value
        

#center window 
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")



window.mainloop()
