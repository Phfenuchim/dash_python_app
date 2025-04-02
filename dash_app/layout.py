# dash_app/layout.py
from dash import Dash, html, dcc
from dash_app.callbacks import register_callbacks
import pandas as pd

# Carrega dataset
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

continentes = df['continent'].unique()

def init_dash(server):
    app = Dash(
        __name__,
        server=server,
        url_base_pathname='/dash/',
        suppress_callback_exceptions=True
    )

    app.layout = html.Div([
        html.Header([
            html.H2('🌍 Dashboard Mundial 2007', id='titulo'),
            html.Div([
                html.Button("🌗 Alternar Tema", id="btn-tema", n_clicks=0),
                html.Button("⛶ Tela Inteira", id="btn-fullscreen", n_clicks=0),
                html.Button("⛶ Gráfico Maior", id="btn-full-grafico", n_clicks=0)
            ], style={'textAlign': 'center', 'marginBottom': '30px', 'display': 'flex', 'gap': '10px', 'justifyContent': 'center'})
        ]),

        html.Div([
            html.Label("Filtrar por continente:"),
            dcc.Dropdown(
                id='filtro-continente',
                options=[{'label': c, 'value': c} for c in continentes],
                value=continentes[0],
                clearable=False,
                style={'width': '100%'}
            )
        ], style={'maxWidth': '300px', 'margin': '0 auto 30px'}),

        html.Div([
            dcc.Graph(id='grafico-barras', style={'flex': 1}),
            dcc.Graph(id='grafico-pizza', style={'flex': 1})
        ], style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '30px'}),

        html.Div([
            dcc.Graph(id='grafico-linha')
        ], style={'marginTop': '40px'}),

        html.Div([
            html.Label("Exportar como:"),
            dcc.RadioItems(
                id='modo-exportacao',
                options=[
                    {'label': 'Selecionado', 'value': 'selecionado'},
                    {'label': 'Todos', 'value': 'todos'}
                ],
                value='selecionado',
                labelStyle={'display': 'inline-block', 'marginRight': '15px'}
            ),
            html.Button("⬇️ Exportar PDF", id="btn-exportar-pdf"),
            html.Button("⬇️ Exportar CSV", id="btn-exportar-csv")
        ], style={'textAlign': 'center', 'marginTop': '40px'}),
        html.Div([
            html.A("🔓 Sair", href="/logout", style={
                "padding": "10px 18px",
                "backgroundColor": "#dc3545",
                "color": "white",
                "borderRadius": "8px",
                "textDecoration": "none",
                "fontWeight": "600",
                "marginLeft": "20px"
            }),
        ], style={"textAlign": "right", "marginBottom": "20px"}),

        html.Div("Fonte: Gapminder", style={'textAlign': 'center', 'marginTop': '40px', 'color': '#888'})

    ], id='pagina', style={
        'padding': '40px',
        'backgroundColor': '#f5f5f7',
        'color': '#1d1d1f',
        'fontFamily': '-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif'
    })

    register_callbacks(app)

    return app
