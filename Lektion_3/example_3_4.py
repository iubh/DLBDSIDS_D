################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

#############################################################################
#                                                                           # 
#   PYTHON ROUTINE zur Analyse und Illustration von Social Network Graphen  #
#                                                                           # 
############################################################################# 

####################################################################################################################################################
#                                                                                                                                                  #          
#   Original Source Code from https://medium.com/towards-artificial-intelligence/extracting-communities-from-social-graph-network-d9213ed9d25a     #
#                                                                                                                                                  #              
####################################################################################################################################################

########################################################################################
#                                                                                      #          
#   Original Facebook Data from https://snap.stanford.edu/data/gemsec-Facebook.html    #
#                                                                                      #              
########################################################################################

# Define libraries and packages (install with pip3 on mac or linux)

# Originale Kommentare #

import pandas as pd
import networkx as nx
from node2vec import Node2Vec
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 

# Initialize the pandas dataframe

df = pd.read_csv('facebook_clean_data/athletes_edges.csv')
G = nx.from_pandas_edgelist(df, source='node_1', target='node_2')
print('Number of Nodes in the graph: ', G.number_of_nodes())
print('Number of Edges in the graph: ', G.number_of_edges())
df.head()

# Initialize and run Node2Vec on the edges of the network (data)

edge_list = list(zip(df['node_1'],df['node_2']))
KG = nx.Graph(edge_list)

# Create graph from the network vector

n2v_obj = Node2Vec(KG, dimensions=64, walk_length=5, num_walks=10, p=1, q=1, workers=1)

# Initialize network model

model = n2v_obj.fit(window=10, min_count=1, batch_words=4)
node_list = df.node_1.unique()
node_str = []

# Embeddings in the graph are extracted and stored into a pandas dataframe

for n in node_list:

    node_str.append(str(n))

embedding_df = pd.DataFrame()

for i in node_str:

    t1 = pd.DataFrame(model.wv.get_vector(i)).T
    embedding_df = embedding_df.append(t1)
    embedding_df = embedding_df.reset_index(drop=True)

print(embedding_df)

# Clustering of the different network embeddings are performed using KMeans Clustering method (see Scikit Learn)

num_clusters = 5

kmeans = KMeans(n_clusters = num_clusters)
kmeans.fit(embedding_df.values)
labels = kmeans.predict(embedding_df)
embedding_df['cluster'] = labels
embedding_df.head()

# Visualisation of embeddings and clustering results

pca = PCA(n_components = 2)

principalcomponents = pca.fit_transform(embedding_df.values)
principalDf = pd.DataFrame(data = principalcomponents, columns = ['pca1', 'pca2'])

principalDf['cluster']=embedding_df['cluster']
principalDf.cluster.value_counts()

# Plot clusters in a .png figure

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('PCA-1', fontsize = 10)
ax.set_ylabel('PCA-2', fontsize = 10)
ax.set_title('2-Component PCA', fontsize = 10)

cluster = [0,1,2,3,4,5]
color = ['g','r','y','b','c']

for cluster, color in zip(cluster, color):

    indicesToKeep = principalDf['cluster']==cluster
    ax.scatter(principalDf.loc[indicesToKeep,'pca1'],
    principalDf.loc[indicesToKeep, 'pca2'],
    c = color,
    s = 2)

ax.grid()

plt.savefig('fig_3_4.png') # Find path with command 'pwd' in your terminal
