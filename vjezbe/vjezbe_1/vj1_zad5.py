import matplotlib.pyplot as plt

def graf_pravca(x1, x2, y1, y2, pros_pravca=1, spremi_pdf=False, ime_pdfa="graf_pravca"):
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    
    x_lista = [x1, x2]
    y_lista = [y1, y2]
    
    x_min = min(x_lista) - pros_pravca
    x_max = max(x_lista) + pros_pravca
    y_min = m * x_min + c
    y_max = m * x_max + c
    
    plt.plot([x_min, x_max], [y_min, y_max], label=f"Pravac: y = {m}x + {c}")
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("graf_pravca")
    plt.grid(True)
    
    if spremi_pdf:
        plt.savefig(f"{ime_pdfa}.pdf")
        print("Graf uspješno spremljen.")
    else:
        plt.show()

x1, y1 = 2, 4
x2, y2 = 6, 8
graf_pravca(x1, x2, y1, y2, pros_pravca=2, spremi_pdf=False, ime_pdfa="marko")
