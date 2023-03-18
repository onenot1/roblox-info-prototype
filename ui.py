import tkinter as tk
import tkinter.ttk as ttk
import api as ro

game_window = tk.Tk(className="game_info_window")
game_window.geometry("400x400")
game_window.wm_resizable(width=False,height=False)

def change_all(id):
    game_name_var.set("name: " + ro.get_game_info(id)["name"])
    game_desc_var.set("description: " + ro.get_game_info(id)["description"])
    game_builder_var.set("creator: " + ro.get_game_info(id)["builder"])

game_header = tk.Label(
    master=game_window,
    anchor="center",
    text="game_info_screen",
).pack(pady=10)

game_input_header = tk.Label(
    master=game_window,
    anchor="center",
    text="game_id"
).pack(pady=10)

game_id_var = tk.StringVar(master=game_window, value=0)
game_id_input = tk.Entry(
    master=game_window,
    justify="center",
    textvariable=game_id_var
).pack(pady=0)

game_id_check = tk.Button(
    game_window,
    anchor="center",
    text="check_id",
    width=20,
    command=lambda: change_all(game_id_var.get())
).pack(pady=5)

game_info_header = tk.Label(
    master=game_window,
    anchor="center",
    text="game_info"
).pack(pady=25)

main_frame = tk.Frame(game_window).pack()
scrollbar = tk.Scrollbar(master=main_frame, orient="vertical").pack(side="right", fill="y")

game_name_var = tk.StringVar(master=game_window, value="")
game_name = tk.Entry(
    master=game_window,
    justify="center",
    textvariable=game_name_var,
    width=40
).pack(pady=5)

game_desc_var = tk.StringVar(master=game_window, value="")
game_desc = tk.Entry(
    master=main_frame,
    justify="center",
    textvariable=game_desc_var,
    width=40
).pack(pady=5)

game_builder_var = tk.StringVar(master=game_window, value="")
game_builder = tk.Entry(
    master=main_frame,
    justify="center",
    textvariable=game_builder_var,
    width=40
).pack(pady=5)

game_window.mainloop()