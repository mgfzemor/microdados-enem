__author__ = "Mario Figueiro Zemor"
__email__ = "mario.figueiro@ufgrs.br"

import classes.Database as db;
import logging

logger = logging.getLogger(__name__);

class FormAtendNecessidades():

    def __init__(self,cod_estudante,braile,ampliada_24,ampliada_18,ledor,acesso,transcricao,libras,leitural_labial,mesa_cadeira_rodas,mesa_cadeira_separada,apoio_perna,guia_interprete):
        self.cod_estudante = cod_estudante;
        self.braile = braile;
        self.ampliada_24 = ampliada_24;
        self.ampliada_18 = ampliada_18;
        self.ledor = ledor;
        self.acesso = acesso;
        self.transcricao = transcricao;
        self.libras = libras;
        self.leitural_labial = leitural_labial;
        self.mesa_cadeira_rodas = mesa_cadeira_rodas;
        self.mesa_cadeira_separada = mesa_cadeira_separada;
        self.apoio_perna = apoio_perna;
        self.guia_interprete = guia_interprete;
        


    def toString():
        return "FormAtendNecessidades["+self.cod_estudante+"]";

    @staticmethod
    def getQuery(query):
        queries = { 'INSERT' : """INSERT INTO formatendnecessidades VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    'UPDATE' : """""",
                    'DELETE' : """""",
                    'FIND_ALL' : """SELECT * FROM formatendnecessidades"""};

        return queries[query];

    @staticmethod
    def insert(values,cursor):
        try:
            logger.debug("Inserting values: {} into formatendnecessidades.".format(values));
            query = getQuery("INSERT");
            cursor.execute(query,values);
        except Exception as e:
            logger.error("Exception during insert values into formatendnecessidades: {}".format(e));

    @staticmethod
    def getValues(columns,dd):
        try:
            logger.debug("Getting values from file columns.");
            cod_estudante = int(columns[dd['NU_INSCRICAO']]);
            braile = False if columns[dd['IN_BRAILLE']] == '0' else True;
            ampliada_24 = False if columns[dd['IN_BRAILLE']] == '0' else True;
            ampliada_18 = False if columns[dd['IN_BRAILLE']] == '0' else True;
            ledor = False if columns[dd['IN_BRAILLE']] == '0' else True;
            acesso = False if columns[dd['IN_BRAILLE']] == '0' else True;
            transcricao = False if columns[dd['IN_BRAILLE']] == '0' else True;
            libras = False if columns[dd['IN_BRAILLE']] == '0' else True;
            leitural_labial = False if columns[dd['IN_BRAILLE']] == '0' else True;
            mesa_cadeira_rodas =False if columns[dd['IN_BRAILLE']] == '0' else True;
            mesa_cadeira_separada = False if columns[dd['IN_BRAILLE']] == '0' else True;
            apoio_perna = False if columns[dd['IN_BRAILLE']] == '0' else True;
            guia_interprete = False if columns[dd['IN_BRAILLE']] == '0' else True;
            values = (cod_estudante,braile,ampliada_24,ampliada_18,ledor,acesso,transcricao,libras,leitural_labial,mesa_cadeira_rodas,mesa_cadeira_separada,apoio_perna,guia_interprete);
            ret = values;
        except Exception as e:
            logger.error("Exception during get values from columns: {}".format(e));
            ret = None;
        return ret;
