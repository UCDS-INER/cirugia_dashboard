from flask import Flask, render_template
import os
import pandas as pd
import plotly.express as px

app = Flask(__name__, template_folder='app/templates')

# Cargar datos
data_path = os.path.join('data', 'sample_data.csv')
if os.path.exists(data_path):
    data = pd.read_csv(data_path)
else:
    data = pd.DataFrame({'Clave': [], 'Conteo por Clave': [], 'Tipo': []})  # Manejo de error si no hay datos

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html', graph_json=None)

# Ruta para la visualización interactiva
@app.route('/visualizacion')
def visualizacion():
    if not data.empty:
        fig = px.bar(data, x='Clave', y='Conteo por Clave', color='Tipo', title='Visualización Interactiva')
        graph_json = fig.to_json()
    else:
        graph_json = None  # Manejo de error si no hay datos
    return render_template('index.html', graph_json=graph_json)

if __name__ == '__main__':
    app.run(debug=True)