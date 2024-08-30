import tkinter as tk
import funcs

root = tk.Tk()
root.geometry("500x600")
root.title("GarbageBin Scanner")

label = tk.Label(root, text="GarbageBin Scanner", font=('Arial', 18))
label.pack(padx=20, pady=20)
label = tk.Label(root, text="NETWORKSISMS", font=('Arial', 14))
label.pack(padx=30, pady=30)

# start
button = tk.Button(root, text="Start", command=funcs.func, font=('Arial', 18))
button.pack(padx=10, pady=10)
# stop
#button = tk.Button(root, font=('Arial', 18), text="Stop")
#button.pack(padx=10, pady=10)
# viewphoto
#button = tk.Button(root, text="View Photo ", font=('Arial', 18))
#button.pack(padx=10, pady=10)

label = tk.Label(root, text="Press Q to STOP",font=('Arial,50'))
label.pack(padx=60,pady=60)



label = tk.Label(root, text="Check captured images in Data directory ",font=('Arial,35'))
label.pack(padx=60,pady=60)

# myentry = tk.Entry(root)
# myentry.pack()
 

root.mainloop()
