import numpy as np
import plotly.graph_objects as go

# Definir el rango de tiempo t
t = np.arange(0, 20.1, 0.1)

# Calcular los valores de r, theta y z
r = np.exp(-0.2 * t)
th = np.pi * t * 0.5
z = t

# Calcular las coordenadas x e y
x = r * np.cos(th)
y = r * np.sin(th)

# Crear la gráfica 3D con Plotly
fig = go.Figure()

# Añadir la curva en espiral
fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='blue', width=3), name='Spiral'))

# Añadir la línea vertical en el punto A
fig.add_trace(go.Scatter3d(x=[1, 1], y=[-0.5, 0], z=[0, 0], mode='lines', line=dict(color='red', width=2), name='Line to A'))

# Añadir anotaciones para los puntos A y B
fig.add_trace(go.Scatter3d(x=[1], y=[-0.7], z=[0], mode='text', text=['A'], textposition='bottom right', showlegend=False))
fig.add_trace(go.Scatter3d(x=[x[-1]], y=[y[-1]], z=[z[-1] + 2], mode='text', text=['B'], textposition='top center', showlegend=False))

# Etiquetas y título
fig.update_layout(
    title="Gráfica 3D en Espiral con Anotaciones",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z"
    )
)

# Guardar la figura como un archivo HTML
fig.write_html("plot-3d.html")
