import flet as ft
import networkx as nx

from model.model import Model
from UI.view import View

class Controller:
    def __init__(self, view:View, model:Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        try:
            anno=int(self._view._txtAnno.value)
            if anno<1816 or anno>2016:
                self._view.create_alert("Devi inserire anno compreso tra 1816 e 2016")
                self._view.update_page()
            else:
                self._model.grafo=nx.Graph()
                self._model.crea_grafo(anno)
                stringa=self._model.stampa_grafo()
                self._view._txt_result.controls.append(ft.Text(stringa))
                self._view._dd_stato.disabled = False
                self._view._btn_stati.disabled=False
                self.get_options()
                self._view.update_page()

        except ValueError:
            self._view.create_alert("Non hai inserito un numero")
            self._view.update_page()

    def handle_change(self,e):
        self._view._dd_stato.disabled=True
        self._view._btn_stati.disabled = True
        self._view.update_page()

    def get_options(self):
        for i in sorted(self._model.grafo.nodes):
            self._view._dd_stato.options.append(ft.dropdown.Option(i.StateNme))

    def handleRaggiungibili(self,e):
        self._view._txt_result.controls.clear()
        self._view.update_page()
        nome_stato=self._view._dd_stato.value
        self._view._txt_result.controls.append(ft.Text(self._model.stati_raggiungibili2(nome_stato)))
        self._view.update_page()