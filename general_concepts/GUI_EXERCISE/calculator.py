import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")

# Set window background color
root.config(bg="lightgray")

# Define button colors
button_bg = "#4CAF50"  # Green button background
button_fg = "white"  # White button text

# Define display colors
display_bg = "black"  # Black background for display
display_fg = "white"  # White text in display

# Create display
display = tk.Entry(root, bg=display_bg, fg=display_fg, font=("Arial", 20), bd=10, insertwidth=4, width=14,
                   borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

# Create buttons (just as an example)
button1 = tk.Button(root, text="1", padx=20, pady=20, bg=button_bg, fg=button_fg)
button1.grid(row=1, column=0)

button2 = tk.Button(root, text="2", padx=20, pady=20, bg=button_bg, fg=button_fg)
button2.grid(row=1, column=1)

# Additional buttons and layout can go here...

root.mainloop()
