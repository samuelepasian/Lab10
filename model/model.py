import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.grafo=nx.Graph()
        self.nazioni = DAO.get_allCountries()
        self.idMap= {}
        for a in self.nazioni:
            self.idMap[a.CCode] = a

    def add_nodi(self,year):
        lista_confini=DAO.get_confini(year)
        lista_nodi=[]
        for tupla in lista_confini:
            if tupla[0] not in lista_nodi:
                lista_nodi.append(tupla[0])
            if tupla[1] not in lista_nodi:
                lista_nodi.append(tupla[1])

        for i in lista_nodi:
            self.grafo.add_node(self.idMap[i])

    def add_archi(self,year):
        lista_confini = DAO.get_confini(year)
        for tupla in lista_confini:
            if tupla[2]==1:
                self.grafo.add_edge(self.idMap[tupla[0]],self.idMap[tupla[1]])

    def crea_grafo(self,year):
        self.add_nodi(year)
        self.add_archi(year)

    def stampa_grafo(self):
        stringa="Grafo creato\n"
        stringa=stringa+f"Il grafo ha {nx.number_connected_components(self.grafo)} componenti connesse\n"
        for nodo in sorted(self.grafo.nodes):
            stringa=stringa+f"{nodo.StateNme} -- {self.grafo.degree[nodo]} vicini\n"
        return stringa

    def stati_raggiungibili(self, nome_stato):
        nodo=""
        for i in self.grafo.nodes:
            if i.StateNme==nome_stato:
                nodo=i
                break
        tree=nx.bfs_tree(self.grafo,nodo)
        nodi=list(tree.nodes())
        stringa=""
        for stato in nodi:
            if stato.StateNme!=nome_stato:
                stringa=stringa+f"{stato.StateNme}\n"
        return stringa

    def stati_raggiungibili2(self, nome_stato):
        nodo = ""
        for i in self.grafo.nodes:
            if i.StateNme == nome_stato:
                nodo = i
                break
        conn = nx.node_connected_component(self.grafo, nodo)
        nodi = []
        for i in conn:
            nodi.append(i)
        stringa = ""
        for stato in nodi:
            if stato.StateNme != nome_stato:
                stringa = stringa + f"{stato.StateNme}\n"
        return stringa