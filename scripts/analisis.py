import pandas as pd

# Leer datos
df = pd.read_csv("datos/ventas.csv")

# Calcular importe
df["importe"] = df["cantidad"] * df["precio"]

# Ventas totales
ventas_totales = df["importe"].sum()

# Producto más vendido
producto_mas_vendido = (
    df.groupby("producto")["cantidad"]
    .sum()
    .idxmax()
)

print("VENTAS TOTALES:", ventas_totales)
print("PRODUCTO MÁS VENDIDO:", producto_mas_vendido)
