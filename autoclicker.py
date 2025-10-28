"""
MindClicker X – Red Hacker Edition
Autor: Hugo Farranha
Versão: 3.1
Descrição:
Auto-clicker RGB vermelho com menus ícones, log em tempo real e modo Turbo via janela.
Compatível com ícone no .exe e barra de tarefas do Windows.
"""

import threading
import sys
import os
import time
import itertools
import tkinter as tk
import ctypes
from tkinter import ttk, messagebox
from pynput.mouse import Button, Controller
from pynput import keyboard

# ------------------ ESTADO PRINCIPAL ------------------
mouse = Controller()
clicking = False
click_thread = None
click_button = Button.left
click_delay = 0.01
click_count = 0
turbo_enabled = False
turbo_window = None

# ------------------ FUNÇÕES DE CLIQUE ------------------
def click_loop():
    global clicking, click_count
    log_event("Thread de cliques iniciada.")
    while clicking:
        mouse.click(click_button)
        click_count += 1
        update_counter(click_count)
        time.sleep(click_delay)
    log_event("Thread de cliques encerrada.")

def toggle_clicker():
    global clicking, click_thread, click_delay
    clicking = not clicking

    # Ativa modo turbo se janela marcada
    if clicking and turbo_enabled:
        click_delay = 0.001
        log_event("Modo TURBO ativado ⚡ (delay 0.001s)")
    elif clicking:
        click_delay = speed_var.get()

    if clicking:
        click_thread = threading.Thread(target=click_loop)
        click_thread.start()
        update_ui("ATIVADO", "#1db6f3")
        log_event("Auto-clicker ATIVADO.")
    else:
        update_ui("DESATIVADO", "gray")
        log_event("Auto-clicker DESATIVADO.")

def toggle_button():
    global click_button
    if click_button == Button.left:
        click_button = Button.right
        update_click_mode("Botão: Direito (F7)")
        log_event("Alterado para botão direito.")
    else:
        click_button = Button.left
        update_click_mode("Botão: Esquerdo (F7)")
        log_event("Alterado para botão esquerdo.")

def stop_program():
    global clicking
    clicking = False
    update_ui("ENCERRADO", "gray")
    log_event("Encerrando programa...")
    root.after(1000, root.destroy)
    return False

# ------------------ APPID + ÍCONE DO EXECUTÁVEL E JANELA ------------------
try:
    myappid = 'HugoFarranha.MindClickerX.RedHacker'  # ID único para fixar ícone na taskbar
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception as e:
    print(f"⚠️ Erro ao aplicar AppID: {e}")

# Criação da janela principal
root = tk.Tk()
root.title("💀 MindClicker X – Red Hacker Edition")

# Define caminho seguro do ícone (funciona no .exe e no .py)
icon_path = os.path.join(
    getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))),
    "icon.ico"
)
try:
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"⚠️ Erro ao carregar ícone: {e}")

root.geometry("450x400")
root.resizable(False, False)
root.configure(bg="#0a0a0a")

# ------------------ ESTILO ------------------
style = ttk.Style()
style.configure("TLabel", background="#0a0a0a", foreground="#1db6f3", font=("Consolas", 11))
style.configure("Title.TLabel", background="#0a0a0a", foreground="#ff5555", font=("Consolas", 15, "bold"))

# ------------------ MENU SUPERIOR COM ÍCONES ------------------
def show_about():
    messagebox.showinfo("💀 Sobre", "MindClicker X – Red Hacker Edition\nAutor: Hugo Farranha\nVersão 3.1")

def show_help():
    messagebox.showinfo("❓ Ajuda", "Atalhos:\n• F6 → Ligar/Desligar\n• F7 → Alternar Botão\n• ESC → Sair")

def open_turbo_window():
    global turbo_window, turbo_var
    if turbo_window and tk.Toplevel.winfo_exists(turbo_window):
        turbo_window.focus_force()
        return

    turbo_window = tk.Toplevel(root)
    turbo_window.title("⚡ Controle de Turbo")
    turbo_window.geometry("260x140")
    turbo_window.configure(bg="#111")

    ttk.Label(turbo_window, text="⚡ Ativar modo Turbo", style="TLabel").pack(pady=10)
    turbo_var = tk.BooleanVar(value=turbo_enabled)

    def toggle_turbo_var():
        global turbo_enabled
        turbo_enabled = turbo_var.get()
        state = "ativado" if turbo_enabled else "desativado"
        log_event(f"Modo Turbo {state.upper()} na janela.")
        turbo_window.lift()

    tk.Checkbutton(turbo_window, text="Ativar Turbo (F6 usa delay 0.001s)",
                   variable=turbo_var, bg="#111", fg="#1db6f3",
                   selectcolor="#222", font=("Consolas", 10),
                   command=toggle_turbo_var).pack(pady=10)

    ttk.Button(turbo_window, text="Fechar", command=turbo_window.destroy).pack(pady=5)

# Menus
menu_bar = tk.Menu(root)
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="💾 Zerar Contador", command=lambda: reset_counter())
menu_file.add_separator()
menu_file.add_command(label="🚪 Sair", command=lambda: stop_program())
menu_bar.add_cascade(label="💾 Arquivo", menu=menu_file)

menu_config = tk.Menu(menu_bar, tearoff=0)
menu_config.add_command(label="⚙️ Controle Turbo", command=open_turbo_window)
menu_config.add_command(label="🖱️ Alternar Botão (F7)", command=toggle_button)
menu_bar.add_cascade(label="⚙️ Configurações", menu=menu_config)

menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label="❓ Ajuda", command=show_help)
menu_help.add_command(label="💀 Sobre", command=show_about)
menu_bar.add_cascade(label="❓ Ajuda", menu=menu_help)

root.config(menu=menu_bar)

# ------------------ ELEMENTOS PRINCIPAIS ------------------
ttk.Label(root, text="💀 MindClicker X – Red Hacker", style="Title.TLabel").pack(pady=10)

status_label = ttk.Label(root, text="Status: DESATIVADO (F6)", style="TLabel", foreground="gray")
status_label.pack(pady=3)

counter_label = ttk.Label(root, text="Cliques: 0", style="TLabel")
counter_label.pack(pady=3)

click_mode_label = ttk.Label(root, text="Botão: Esquerdo (F7)", style="TLabel")
click_mode_label.pack(pady=3)

ttk.Label(root, text="Velocidade dos Cliques", style="TLabel").pack(pady=3)
speed_var = tk.DoubleVar(value=click_delay)
speed_slider = tk.Scale(root, from_=0.001, to=0.1, resolution=0.001,
                        orient="horizontal", length=250, bg="#0a0a0a",
                        fg="#1db6f3", troughcolor="#222", highlightthickness=0,
                        variable=speed_var)
speed_slider.pack(pady=3)

# Log de eventos fixo na tela principal
ttk.Label(root, text="🧾 Log de Eventos", style="TLabel").pack(pady=4)
log_box = tk.Text(root, height=7, width=55, bg="#101010", fg="#1db6f3", font=("Consolas", 9))
log_box.pack(padx=8, pady=5)
log_messages = []

def log_event(msg):
    log_messages.append(msg)
    log_box.insert(tk.END, f"> {msg}\n")
    log_box.see(tk.END)
    print(msg)

def update_ui(status_text, color):
    status_label.config(text=f"Status: {status_text} (F6)", foreground=color)

def update_counter(value):
    counter_label.config(text=f"Cliques: {value}")

def update_click_mode(text):
    click_mode_label.config(text=text)

def reset_counter():
    global click_count
    click_count = 0
    update_counter(0)
    log_event("Contador zerado.")

# ------------------ ANIMAÇÃO VERMELHA ------------------
def red_cycle():
    for i in itertools.cycle(range(0, 255, 4)):
        yield (i, int(i * 0.1), int(i * 0.1))

def animate_red_bg():
    r, g, b = next(red_colors)
    root.configure(bg=f'#{r:02x}{g:02x}{b:02x}')
    root.after(60, animate_red_bg)

red_colors = red_cycle()
animate_red_bg()

# ------------------ LISTENER DE TECLADO ------------------
def on_press(key):
    try:
        if key == keyboard.Key.f6:
            toggle_clicker()
        elif key == keyboard.Key.f7:
            toggle_button()
        elif key == keyboard.Key.esc:
            return stop_program()
    except Exception as e:
        log_event(f"[ERRO] {e}")

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("💀 MindClicker X Red Hacker Edition iniciado!")
root.mainloop()