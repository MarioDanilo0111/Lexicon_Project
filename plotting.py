import plotly.graph_objects as go
import numpy as np

def create_similarities_plot(titles, similarities, links, user_query):

  # Convert Similaritys to Percentages
  similarities_percentages = similarities * 100 

  fig = go.Figure(data=[go.Scatter(
    x=similarities_percentages,
    y=np.arange(len(similarities)),
    mode='markers+text',
    text=titles,
    marker=dict(
      size=20, color=similarities_percentages, colorscale='Bluered',
    ),
    customdata=links,
    hovertemplate=f"<br>%{{text}}</b> <br> similar in %{{x:.2f}} %<br> to {user_query}<extra></extra>",
    )])
  fig.update_layout(
    title='Click on a point to view details: ',
    xaxis_title="Cousine Similarity (%)",
    yaxis_title="Documents",
    yaxis=dict(showticklabels=False),
  )
  return fig