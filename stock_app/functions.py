#Functions for my Stock Chart App
import pygal
from datetime import datetime

def Plot_Chart(stock_data, selected_checkboxes):
	"""Function to plot the pie chart for the investor"""

	#Plot portfolio information as a pie chart
	my_config = pygal.Config()
	my_config.height = 300
	chart = pygal.Pie(my_config, inner_radius=.4)
	chart.value_formatter = lambda y: "${:,.0f}".format(y)

	#Set chart titles and plot data
	chart.title = "Portfolio Breakdown"
	for stock in stock_data:
		if stock.stock_name in selected_checkboxes:
			chart.add(stock.stock_name, stock.market_value)
	
	#Return a string data URI
	chart = chart.render_data_uri()
	return chart
