from sklearn.cluster import KMeans
import matplotlib.pyplot as mtp
import pandas as pd

dataset=pd.read_csv('data1.csv')
x=dataset.iloc[:, [3,4]].values
print(x)
wcss_list=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)
    wcss_list.append(kmeans.inertia_)
mtp.plot(range(1,11), wcss_list)
mtp.title("The Elbow method graph")
mtp.xlabel("Number of clusters")
mtp.ylabel("wcss_list")
mtp.show()
kmeans=KMeans(n_clusters=5, init='k-means++', random_state=42)
kmeans.fit(x)
y_predict=kmeans.predict(x)
mtp.scatter(x[y_predict == 0,0], x[y_predict == 0,1], s=100, c='red', label="cluster 1")
mtp.scatter(x[y_predict == 1,0], x[y_predict == 1,1], s=100, c='blue', label="cluster 2")
mtp.scatter(x[y_predict == 2,0], x[y_predict == 2,1], s=100, c='green', label="cluster 3")
mtp.scatter(x[y_predict == 3,0], x[y_predict == 3,1], s=100, c='orange', label="cluster 4")
mtp.scatter(x[y_predict == 4,0], x[y_predict == 4,1], s=100, c='magenta', label="cluster 5")

mtp.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c='black', label="cluster")
mtp.title("A vs B")
mtp.xlabel("A")
mtp.ylabel("B")
mtp.legend()
mtp.show()