import numpy as np
import plotly.graph_objects as go

# Definir el rango de t
t = np.arange(0, np.pi + 0.01, 0.05)

# Calcular los valores de y
y = np.sin(3 * t) * np.exp(-0.3 * t)

# Crear las coordenadas para el gráfico 3D
x = y * np.cos(t)  # Coordenada x en términos polares
y_3d = y * np.sin(t)  # Coordenada y en términos polares
z = t  # Usamos el tiempo t como el eje z para la visualización 3D

# Crear la gráfica con Plotly
fig = go.Figure(data=go.Scatter3d(x=x, y=y_3d, z=z, mode='lines', line=dict(color='blue', width=2)))
fig.update_layout(
    title="Gráfica Polar de una Señal Amortiguada (3D)",
    scene=dict(
        xaxis_title="X (y * cos(t))",
        yaxis_title="Y (y * sin(t))",
        zaxis_title="Z (t)"
    )
)

# Guardar la figura como un archivo HTML
fig.write_html("plot-3d.html")