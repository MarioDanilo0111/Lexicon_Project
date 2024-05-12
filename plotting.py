import plotly.graph_objects as go
import numpy as np

def create_similarities_plot(titles, similarities, links):
  fig = go.Figure(data=[go.Scatter(
    x=similarities,
    y=np.arange(len(similarities)),
    mode='markers+text',
    text=titles,
    marker=dict(
      size=20, color=similarities, colorscale='Bluered',
    ),
    customdata=links,
    hovertemplate="<br>%{text}</b><br><br>Similarity: %{x:.3f}<extra></extra>",
    )])
  fig.update_layout(
    title='Click on a point to view details: ',
    xaxis_title="Cousine Similarity",
    yaxis_title="Documents",
    yaxis=dict(showticklabels=False),
  )
  return fig