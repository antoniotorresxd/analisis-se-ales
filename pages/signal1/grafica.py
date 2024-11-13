import numpy as np
import plotly.graph_objects as go

# Crear los datos para x, y, z
x = np.linspace(0, 10, 50)  # Valores de x de 0 a 10
y = np.linspace(0, 10, 50)  # Valores de y de 0 a 10
X, Y = np.meshgrid(x, y)  # Crear una malla 2D de valores
Z = np.sin(X) * np.exp(-0.4 * X)  # Calcular Z en función de X

# Crear la figura de Plotly
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])

# Configuración de la gráfica
fig.update_layout(
    title='3D Plot of z = sin(x) * exp(-0.4 * x)',
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z'
    )
)

# Guardar la figura como un archivo HTML
fig.write_html("interactive_plot.html")
