__author__ = "Mario Figueiro Zemor"
__email__ = "mario.figueiro@ufgrs.br"

from Prova import Prova;
import classes.Database as db;
import logging

logger = logging.getLogger(__name__);

def ProvaObjetiva(Prova):
    def __init__(self,cod,cod_inscricao,nota,presenca,cor_caderno,tipo_prova,respostas,gabarito):
        self.presenca = presenca;
        self.cor_caderno = cor_caderno;
        self.tipo_prova = tipo_prova;
        self.respostas = respostas;
        self.gabarito = gabarito;
        Prova.__init__(self,cod,cod_inscricao,nota);

    @staticmethod
    def insert(values,cursor):
        try:
            logger.debug("Inserting values: {} into Student.".format(values));
            query = 'INSERT INTO prova_objetiva VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'; #queries["INSERT"];
            cursor.execute(query,values);
        except Exception as e:
            logger.error("Exception during insert values into Student: {}".format(e));
