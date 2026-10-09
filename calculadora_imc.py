"""Calculadora de IMC (Índice de Massa Corporal) com interface Tkinter."""

import tkinter as tk
from tkinter import messagebox

FAIXAS = [
    (18.5, "Abaixo do peso", "#3498db"),
    (25.0, "Peso normal", "#27ae60"),
    (30.0, "Sobrepeso", "#f39c12"),
    (35.0, "Obesidade grau I", "#e67e22"),
    (40.0, "Obesidade grau II", "#e74c3c"),
    (float("inf"), "Obesidade grau III", "#c0392b"),
]


def calcular_imc(peso, altura):
    """Retorna o IMC dado peso (kg) e altura (m)."""
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero.")
    return peso / altura ** 2


def classificar(imc):
    """Retorna (classificação, cor) para o IMC informado."""
    for limite, nome, cor in FAIXAS:
        if imc < limite:
            return nome, cor


class CalculadoraIMC(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de IMC")
        self.resizable(False, False)
        self.configure(padx=20, pady=20)

        tk.Label(self, text="Calculadora de IMC", font=("Arial", 16, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(0, 15)
        )

        tk.Label(self, text="Peso (kg):").grid(row=1, column=0, sticky="w")
        self.entrada_peso = tk.Entry(self, width=15)
        self.entrada_peso.grid(row=1, column=1, pady=5)

        tk.Label(self, text="Altura (m ou cm):").grid(row=2, column=0, sticky="w")
        self.entrada_altura = tk.Entry(self, width=15)
        self.entrada_altura.grid(row=2, column=1, pady=5)

        botoes = tk.Frame(self)
        botoes.grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(botoes, text="Calcular", width=10, command=self.calcular).pack(side="left", padx=5)
        tk.Button(botoes, text="Limpar", width=10, command=self.limpar).pack(side="left", padx=5)

        self.resultado = tk.Label(self, text="", font=("Arial", 13, "bold"))
        self.resultado.grid(row=4, column=0, columnspan=2)
        self.classificacao = tk.Label(self, text="", font=("Arial", 12))
        self.classificacao.grid(row=5, column=0, columnspan=2)

        self.bind("<Return>", lambda _e: self.calcular())
        self.entrada_peso.focus()

    def calcular(self):
        try:
            peso = float(self.entrada_peso.get().replace(",", "."))
            altura = float(self.entrada_altura.get().replace(",", "."))
            if altura > 3:  # provavelmente informada em centímetros
                altura /= 100
            imc = calcular_imc(peso, altura)
        except ValueError:
            messagebox.showerror("Erro", "Informe valores numéricos válidos e maiores que zero.")
            return

        nome, cor = classificar(imc)
        self.resultado.config(text=f"IMC: {imc:.2f}", fg=cor)
        self.classificacao.config(text=nome, fg=cor)

    def limpar(self):
        self.entrada_peso.delete(0, tk.END)
        self.entrada_altura.delete(0, tk.END)
        self.resultado.config(text="")
        self.classificacao.config(text="")
        self.entrada_peso.focus()


if __name__ == "__main__":
    CalculadoraIMC().mainloop()
