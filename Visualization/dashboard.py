"""
Code to visualize the algorithm solving a knapsack instance
"""

# Import Libraries
from dash import Dash, dcc, html, Input, Output


# Initialize app
app = Dash(__name__)

# Set colors
colors = {"Items":"#fdfb7e", "Item-Selected":"#bafd7e",
          "Actions":"#ebffd8", "Action-used":"#ff745e",
          "Background":"#fffce7"}


# Create layout
app.layout = html.Div(
    style={"backgroundColor": colors["Background"]},
    children=[

        # Title and header
        html.Div([
            html.H2("0/1 Knapsack", style={"textAlign": "center"}),
            html.Br(),
        ]),

        # Select Instance to solve
        html.Div([
            html.H3("Select instance to solve:"),
            dcc.Dropdown(["Instance-1", "Instance-2"], "Instance-1")
        ], style={"width": "33%", "textAlign": "center", "margin-left": "auto", "margin-right": "auto"}),

        
        # Body
        html.Div(
            children=[

                # Left side: Items Available
                html.Div([
                    html.H4("Available Items", id="available-items-title", style={"textAlign": "center"}),
                    dcc.Graph(id="available-items-graph")
                
                ], style={"width":"45%", "display": "inline-block", "padding": "0 20"}),
            
                
                # Middle: Actions
                html.Div([
                    html.H4("Heuristics", style={"textAlign": "center"})
                ], style={"width":"10%", "display": "inline-block", "padding": "0 20"}),


                # Right side: Packed Items
                html.Div([
                    html.H4("Packed Items", id="knapsack-title", style={"textAlign": "center"}),
                    dcc.Graph(id="knapsack-graph")

                ], style={"width":"45%", "display": "inline-block", "padding": "0 20"})

            ]
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)