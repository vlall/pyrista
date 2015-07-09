from __future__ import absolute_import
from bokeh.charts import HeatMap, output_file, show
#from bokeh.sampledata.unemployment1948 import data
from bokeh.models.widgets import TextInput, DataTable, DateFormatter, TableColumn
from bokeh.models import ColumnDataSource
from os.path import dirname, join
from bokeh.io import output_file, show, vform
from bokeh.embed import autoload_static
import pyrista
from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, show


class Make_Site:
	def __init__(self, local_ip='n/a', public_ip='n/a', arp = []):

		# Set palette of colors for n vlans 
		palette = [
		"#004529", "#006837", "#238443", "#41ab5d", "#78c679", "#addd8e", 
		"#d9f0a3", "#f7fcb9", "#ffffe5","#084081", "#0868ac", "#2b8cbe", "#4eb3d3", "#7bccc4", 
		"#a8ddb5", "#ccebc5", "#e0f3db", "#f7fcf0","#4d004b", "#810f7c", "#88419d", "#8c6bb1",
		"#EFEFEF","#CFCFCF","#5F5F5F","#000000", "#8c96c6", "#9ebcda", "#bfd3e6", "#e0ecf4", 
		"#f7fcfd","#fff7fb", "#ece2f0", "#d0d1e6", "#a6bddb", "#67a9cf", "#3690c0", "#02818a", 
		"#016c59", "#014636","#67001f", "#980043", "#ce1256","#e7298a", "#df65b0", "#c994c7", 
		"#d4b9da", "#e7e1ef", "#f7f4f9", "#fff7ec", "#fee8c8", "#fdd49e", "#fdbb84", "#fc8d59", 
		"#ef6548", "#d7301f", "#b30000", "#7f0000"
		]
		try:
		    import pandas as pd
		except ImportError as e:
		    raise RuntimeError("Data requires pandas (http://pandas.pydata.org) to be installed")

		data = pd.read_csv(join(dirname(__file__), "vlan.csv"))
		# pandas magic
		df = data[data.columns[:-1]]
		df2 = df.set_index(df[df.columns[0]].astype(str))
		df2.drop(df.columns[0], axis=1, inplace=True)
		df3 = df2.transpose()
		output_file("switch.html", title = 'vlan map')
		# text_input = TextInput(value="VLAN NAME", title="Make Vlan:", callback= )


		hover = HoverTool(
		    tooltips = [
		        ("index", "$index"),
		        ("(x,y)", "($x, $y)"),
		        ("desc", "@desc"),
		    ]
		)

		# Make Heapmap
		hm = HeatMap(df3, title="VLANs", width=950, palette=palette)

		# Make Ip/Arp Table		
		x = [ 'Local', 'Public']
		y = [ local_ip,public_ip]
		for i in arp:
			valueX = i[1].strip().strip("()")
			valueY = i[0].strip().strip("()")			
			x.append(valueX)
			y.append(valueY)
		data = dict(
		    sourceCol=x,
		    ipCol=y,
		)
		source = ColumnDataSource(data)
		columns = [
		    TableColumn(field="sourceCol", title="Source"),
		    TableColumn(field="ipCol", title="IP Address"),
		]

		data_table = DataTable(source=source, columns=columns, width=650, height=450)
		p = vform(hm,data_table)
		show(p)

		# Print autoload_static(p,'relative', '/')
if __name__ == '__main__':
	# Useless if ran directly. Run pyrista.py
	x = Make_Site()
