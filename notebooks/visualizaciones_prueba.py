import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from flask import Flask, render_template
import os

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar datos
data_path = os.path.join('..', 'data', 'sample_data.csv')
data = pd.read_csv(data_path)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la visualización interactiva
@app.route('/visualizacion')
def visualizacion():
    fig = px.bar(data, x='Clave', y='Conteo por Clave', color='Tipo', title='Visualización Interactiva')
    graph_json = fig.to_json()
    return render_template('index.html', graph_json=graph_json)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)