import tkinter # karena bisa di-import, berarti tkinter ini merupakan package atau modul

main_window = tkinter.Tk() # Tk merupakan sebuah class (tanda sederhananya karena dimulai dengan huruf besar -- sesuai konvensi)

label1 = tkinter.Label(main_window, text='Label 1') # Label merupakan sebuah class (tanda sederhananya karena dimulai dengan huruf besar -- sesuai konvensi)
label2 = tkinter.Label(main_window, text='Label 2')

tombol1 = tkinter.Button(main_window, text='Tombol 1') # Button merupakan sebuah class (tanda sederhananya karena dimulai dengan huruf besar -- sesuai konvensi)
tombol2 = tkinter.Button(main_window, text='Tombol 2')

# method positioning
label1.pack() # pack merupakan sebuah method (tanda sederhananya karena dimulai dengan huruf kecil -- sesuai konvensi)
label2.pack()

tombol1.pack()
tombol2.pack()

# menthod menampilkan GUI
main_window.mainloop() # mainloop merupakan sebuah metod (tanda sederhananya karena dimulai dengan huruf kecil -- sesuai konvensi)