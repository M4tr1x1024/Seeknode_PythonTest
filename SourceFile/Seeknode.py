from pyvis.network import Network
import pandas as pd

got_net = Network(height='1920px', width='100%', bgcolor='#F9F9FB',
font_color='#232333', notebook = False, select_menu = True)

# set the physics layout of the network
got_net.barnes_hut()
got_data = pd.read_csv('diseasesymp.csv')

sources = got_data['Disease']
targets = got_data['Symptom']
weights = got_data['weight']

edge_data = zip(sources, targets, weights)




for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    got_net.add_node(src, src, title=src, color='#F46223')
    got_net.add_node(dst, dst, title=dst, color='#F4D823')
    got_net.add_edge(src, dst, value=w, color = '#E8E8E8')

neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
for node in got_net.nodes:
    node['title'] += ' Neighbors:<br>' +
'<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])

# got_net.show_buttons(filter_=['physics'])

got_net.set_options("""
    const options = {
      "physics": {
        "forceAtlas2Based": {
          "gravitationalConstant": -86,
          "springLength": 100
        },
        "minVelocity": 0.75,
        "solver": "forceAtlas2Based"
      }
    }
""")

got_net.show('index.html')
