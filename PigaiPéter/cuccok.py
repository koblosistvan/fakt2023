def vonal():
    print('> ' * 15, '.', '< '*15)

def prime(szam):
    a = True
    for i in range(2, szam):
        if (szam % i == 0):
            a = False
    return a

def andor(x):
    a = '' + 'I'
    for i in range(1, x + 1):
        a += 'I'
        print(f'print(f', '"', '{', f'{a}', 'hely', '}', '"', ')')

def soos(b):
    a = '' + 'I'
    for i in range(1, b + 1):
        print(f'elif {a} == i:\n\t\t {a} += 1')
        a += 'I'

def on_closing(r):
    r.destroy()

    for i in range(2):
        window()


def window():
    root = tk.Toplevel()
    root.title("Hydra")

    # Position the window
    w = 450
    h = 250
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = random() * sw
    y = random() * sh
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    path = "h.png"
    message = "I mean its alright like"
    tk.Label(root, text=message, width=120, height=20).pack()

    root.protocol("WM_DELETE_WINDOW", lambda arg=root: on_closing(arg))
