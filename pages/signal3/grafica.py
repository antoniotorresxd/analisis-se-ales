import numpy as np
import plotly.graph_objects as go

# Definir el rango de valores para x y y
xa = np.arange(-2, 2.2, 0.2)
ya = np.arange(-2, 2.2, 0.2)
x, y = np.meshgrid(xa, ya)

# Calcular los valores de z
z = x * np.exp(-x**2 - y**2)

# Crear la gráfica 3D con Plotly
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis')])

# Personalizar la gráfica
fig.update_layout(
    title="Esta es la gráfica 3D de z = x * e^{-(x^2 + y^2)}",
    scene=dict(
        xaxis_title="x",
        yaxis_title="y",
        zaxis_title="z",
    )
)

# Guardar la figura como un archivo HTML
fig.write_html("plot-3d.html")