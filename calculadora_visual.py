import tkinter as tk

# Cores
BG_COLOR = "#1e1e1e"
BTN_COLOR = "#333333"
BTN_TEXT = "#ffffff"
BTN_HOVER = "#444444"
BTN_ACTIVE = "#555555"
ENTRY_BG = "#2c2c2c"
HIST_BG = "#2a2a2a"
HIST_TEXT = "#cccccc"

FONT = ("Helvetica", 18)
HIST_FONT = ("Consolas", 12)

#Funções
def clicar(botao):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + str(botao))

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    expressao = entrada.get()
    try:
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
        adicionar_historico(f"{expressao} = {resultado}")
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")
        adicionar_historico(f"{expressao} = Erro")

def adicionar_historico(texto):
    historico.config(state="normal")
    historico.insert(tk.END, texto + "\n")
    historico.see(tk.END)
    historico.config(state="disabled")

def on_enter(e):
    e.widget["bg"] = BTN_HOVER

def on_leave(e):
    e.widget["bg"] = BTN_COLOR

# Janela
janela = tk.Tk()
janela.title("🖤 Calculadora com Histórico")
janela.configure(bg=BG_COLOR)
janela.resizable(False, False)

# Layout com  2 colunas: calculadora | histórico
frame_calc = tk.Frame(janela, bg=BG_COLOR)
frame_calc.grid(row=0, column=0, padx=10, pady=10)

frame_hist = tk.Frame(janela, bg=HIST_BG)
frame_hist.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="ns")

# Entrada
entrada = tk.Entry(frame_calc, font=FONT, borderwidth=0, relief=tk.FLAT, justify="right",
                   bg=ENTRY_BG, fg=BTN_TEXT, insertbackground=BTN_TEXT)
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=(0, 20), ipadx=10, ipady=15, sticky="we")
   
# Botões
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (texto, linha, coluna) in botoes:
    if texto == '=':
        cmd = calcular
    else:
        cmd = lambda t=texto: clicar(t)

    botao = tk.Button(
       frame_calc,
       text=texto,
       command=cmd,
       font=FONT,
       bg=BTN_COLOR,
       fg=BTN_TEXT,
       activebackground=BTN_ACTIVE,
       activeforeground=BTN_TEXT,
       bd=0,
       relief=tk.FLAT,
       width=5,
       height=2
    )
    botao.grid(row=linha, column=coluna, padx=5, pady=5)
    botao.bind("<Enter>", on_enter)
    botao.bind("<Enter>", on_leave)

# Botão Limpar
botao_limpar = tk.Button(
    frame_calc,
    text="C",
    command=limpar,
    font=FONT,
    bg="#cc3333",
    fg="white",
    activebackground="#ff4444",
    activeforeground="white",
    bd=0,
    relief=tk.FLAT,
    width=23,
    height=2
)
botao_limpar.grid(row=5, column=0, columnspan=4, padx=5, pady=(10, 0))

# Área de histórico
titulo_hist = tk.Label(frame_hist, text="Histórico", font=("Helvetica", 14), bg=HIST_BG, fg=HIST_TEXT)
titulo_hist.pack(pady=(0, 10))

historico = tk.Text(frame_hist, font=HIST_FONT, bg=HIST_BG, fg=HIST_TEXT, height=20, width=25, borderwidth=0)
historico.pack()
historico.config(state="disabled")

# Fade-in
def fade_in(alpha=0.0):
    if alpha < 1.0:
        alpha += 0.05
        janela.attributes("-alpha", alpha)
        janela.after(20, lambda: fade_in(alpha))

janela.attributes("-alpha", 0.0)
fade_in()

# Iniciar
janela.mainloop()