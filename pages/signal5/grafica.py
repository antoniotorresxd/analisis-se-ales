import numpy as np
import plotly.graph_objects as go

# Definir el rango de t y dt
dt = np.pi / 20
t = np.arange(0, 2 * np.pi, dt)

# Calcular el contorno de la cara
x = np.cos(t)
y = np.sin(t)
z_face = np.zeros_like(x)  # z=0 para el contorno de la cara

# Crear la figura
fig = go.Figure()

# Añadir el contorno de la cara
fig.add_trace(go.Scatter3d(x=x, y=y, z=z_face, mode='lines', line=dict(color='black', width=4), name='Cara'))

# Dibujar el ojo izquierdo con círculos concéntricos en 3D
for k in np.arange(0.8, 0.05, -0.05):
    fig.add_trace(go.Scatter3d(
        x=k * 0.1 * x - 0.3,
        y=k * 0.15 * y + 0.1,
        z=np.full_like(x, 0.1),  # Un poco elevado en el eje z
        mode='lines',
        line=dict(color='blue', width=2),
        showlegend=False
    ))

# Dibujar el ojo derecho con círculos concéntricos en 3D
for k in np.arange(0.8, 0.05, -0.05):
    fig.add_trace(go.Scatter3d(
        x=k * 0.1 * x + 0.3,
        y=k * 0.15 * y + 0.1,
        z=np.full_like(x, 0.1),  # Un poco elevado en el eje z
        mode='lines',
        line=dict(color='blue', width=2),
        showlegend=False
    ))

# Dibujar la boca en 3D
s1 = 3 * np.pi / 2 - 1.1
s2 = 3 * np.pi / 2 + 1.1
s = np.arange(s1, s2, dt)
xs = 0.5 * np.cos(s)
ys = 0.5 * np.sin(s)
zs = np.full_like(xs, -0.1)  # Un poco hundido en el eje z
fig.add_trace(go.Scatter3d(x=xs, y=ys, z=zs, mode='lines', line=dict(color='red', width=3), name='Boca'))

# Configuración del diseño en 3D
fig.update_layout(
    title="Cara 3D con Ojos y Boca",
    scene=dict(
        xaxis=dict(range=[-1, 1], showgrid=False, zeroline=False),
        yaxis=dict(range=[-1, 1], showgrid=False, zeroline=False),
        zaxis=dict(range=[-0.5, 0.5], showgrid=False, zeroline=False),
    ),
    width=700,
    height=700
)

# Guardar la figura como un archivo HTML
fig.write_html("plot-3d.html")
