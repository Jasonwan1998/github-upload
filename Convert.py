import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
# window name is convertor1
window.title("Convert")

window.columnconfigure(0, minsize = 1080, weight = 1)

# the list to store icon path of the menue
menue_left = [tk.PhotoImage(file = "Dashboard.png"),
              tk.PhotoImage(file = "Convert.png"),
              tk.PhotoImage(file = "PUSH.png"),
              tk.PhotoImage(file = "PULLED Reports.png")]

menue_right = [tk.PhotoImage(file = "Help.png"),
               tk.PhotoImage(file = "Notifications.png"),
               tk.PhotoImage(file = "Settings.png")]

table = {1:"Status", 2:"Value Date", 3:"PMT CCY", 4:"Txn", 5:"$ Value"}


# setup the frame frame_head and frame_centre
frame_menue = tk.Frame(master = window, pady = 2, borderwidth = 5, bg = "grey")
frame_centre = tk.Frame(master = window, pady = 2, borderwidth = 5, bg = "white")
frame_menue.grid(row = 0, column = 0, sticky = "new")
frame_centre.grid(row = 1, column = 0, sticky = "new")


# add left icon on menue
for photo in menue_left:
    button = tk.Button(master = frame_menue, image = photo)
    button.pack(side = tk.LEFT, padx = 10)

# add right icon on menue
for photo in menue_right:
    button = tk.Button(master = frame_menue, image = photo)
    button.pack(side = tk.RIGHT, padx = 10)

# show the progress bar
photo_progress = tk.PhotoImage(file = "progress.png")
progress = tk.Label(master = frame_centre, image = photo_progress)
progress.pack()

# making frame for frame_centre
frame_centre_content = tk.Frame(master = frame_centre, pady = 2, borderwidth = 5, bg = "white")
frame_bar = tk.Frame(master = frame_centre_content, pady = 2, borderwidth = 5, bg = "white")
frame_table = tk.Frame(master = frame_centre_content, pady = 10, borderwidth = 5)
frame_centre_content.pack(fill = tk.BOTH)
frame_bar.grid(row = 0, column = 0)
frame_table.grid(rowspan = 2, row = 0, column = 1)

# show the titles of the table in the frame_centre
label_title1 = tk.Label(master = frame_bar, text = "Input File (s): ", bg = "white")
label_title2 = tk.Label(master = frame_bar, text = "Output Format: ", bg = 'white')
label_title3 = tk.Label(master = frame_bar, text = "Output Folder: ", bg = 'white')
label_title1.grid(row = 0, column = 0, sticky = "ne")
label_title2.grid(row = 1, column = 0, sticky = "ne")
label_title3.grid(row = 2, column = 0, sticky = "ne")

# show the addresses of the table in the frame_centre
input_address = tk.Entry(master = frame_bar, width = 65)
output_format = tk.Entry(master = frame_bar, width = 65)
output_address = tk.Label(master = frame_bar, text = " address", bg = 'white')
input_address.grid(row = 0, column = 1, sticky = 'nw')
output_format.grid(row = 1, column = 1, sticky = 'nw')
output_address.grid(row = 2, column = 1, sticky = 'nw')

# show buttons of the table in the frame_centre
photo_add = tk.PhotoImage(file = "add.png")
add = tk.Button(master = frame_bar, image = photo_add)
add.grid(row = 0, column = 2, sticky = "nw")
photo_arrow = tk.PhotoImage(file = "arrow.png")
arrow = tk.Button(master = frame_bar, image = photo_arrow)
arrow.grid(row = 1, column = 2, sticky = "nw")
photo_convert = tk.PhotoImage(file = "Convert.png")
convert = tk.Button(master = frame_bar, image = photo_convert)
convert.grid(rowspan = 3, row = 0, column = 3, sticky = 'ne')

# show the label of the table under the frame_centre
results = tk.Label(master = frame_centre_content, height = 20, width = 90, text = " Convert log. Progress Sucessful or fail")
results.grid(row = 1, column = 0, sticky = 'nw')

# table Details
table_title = tk.Label(master = frame_table, text = "Summary Table", font = 'Helvetica 12 bold')
table_title.grid(columnspan = 6, row = 0, column = 0, sticky = 'nw', pady = 10)

table_input = tk.Button(master = frame_table, text = "G:\CitiFiles\Input\WLPMT010720.xlsx", width = 80)
table_input.grid(columnspan = 5, row = 1, column = 1, sticky = 'nw', pady = 5)

table_output = tk.Button(master = frame_table, text = "G:\CitiFiles\Output\WLPMT010720.xml", width = 80)
table_output.grid(columnspan = 5, row = 2, column = 1, sticky = 'nw', pady = 10)

for index_x in range(3,9):
        if index_x == 3:
            for index_y, title in table.items():
                table_label = tk.Label(master = frame_table, text = title, font = 'Helvetica 12 bold')
                table_label.grid(row = index_x, column = index_y, pady = 5)
        else:
            for index_y in range(1,6):
                table_label = tk.Label(master = frame_table, text = "data")
                table_label.grid(row = index_x, column = index_y, pady = 5)


window.mainloop()
