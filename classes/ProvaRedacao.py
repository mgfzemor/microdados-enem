__author__ = "Mario Figueiro Zemor"
__email__ = "mario.figueiro@ufgrs.br"

from Prova import Prova;
import classes.Database as db;
import logging

logger = logging.getLogger(__name__);

def ProvaRedacao(Prova):
    def __init__(self,cod,cod_inscricao,nota,status,lingua_estrangeira,nota_comp1,nota_comp2,nota_comp3,nota_comp4,nota_comp5):
        self.status = status;
        self.llingua_estrangeira = lingua_estrangeira;
        self.nota_comp1 = nota_comp1;
        self.nota_comp2 = nota_comp2;
        self.nota_comp3 = nota_comp3;
        self.nota_comp4 = nota_comp4;
        self.nota_comp5 = nota_comp5;
        Prova.__init__(self,cod,cod_inscricao,nota);
