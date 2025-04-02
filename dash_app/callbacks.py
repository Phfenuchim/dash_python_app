# dash_app/callbacks.py
from dash import Input, Output, State, ctx
import plotly.express as px
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.io as pio
from flask import send_file
import io

# Dataset original
df_original = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Tema e layout
light_style = {
    'backgroundColor': '#f5f5f7',
    'color': '#1d1d1f'
}

dark_style = {
    'backgroundColor': '#1d1d1f',
    'color': '#f5f5f7'
}

# === Callback para atualizar layout e gráficos ===
def register_callbacks(app):
    @app.callback(
        Output('pagina', 'style'),
        Output('grafico-barras', 'figure'),
        Output('grafico-pizza', 'figure'),
        Output('grafico-linha', 'figure'),
        Input('btn-tema', 'n_clicks'),
        Input('filtro-continente', 'value')
    )
    def atualizar_dashboard(n, continente):
        is_dark = n % 2 == 1
        style = dark_style if is_dark else light_style
        template = 'plotly_dark' if is_dark else 'plotly'

        df = df_original[df_original['continent'] == continente]

        fig_bar = px.bar(df.sort_values(by='pop', ascending=False).head(10),
                         x='country', y='pop',
                         title='Top 10 Países por População',
                         template=template)

        fig_pizza = px.pie(df, names='country', values='pop',
                           title='Distribuição Populacional',
                           template=template)

        fig_linha = px.scatter(df, x='gdpPercap', y='lifeExp',
                               size='pop', color='country',
                               title='Expectativa de Vida x PIB',
                               template=template,
                               hover_name='country', size_max=60)

        return {
            'padding': '40px',
            **style,
            'fontFamily': '-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif'
        }, fig_bar, fig_pizza, fig_linha