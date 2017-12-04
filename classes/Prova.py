__author__ = "Mario Figueiro Zemor"
__email__ = "mario.figueiro@ufgrs.br"

import classes.Database as db;
import logging

logger = logging.getLogger(__name__);

class Prova():
    def __init__(self,cod,cod_inscricao,nota):
        self.cod = cod;
        self.cod_inscricao = cod_inscricao;
        self.nota = nota; 
