__author__ = "Mario Figueiro Zemor"
__email__ = "mario.figueiro@ufgrs.br"

from Prova import Prova;
import classes.Database as db;
import logging

logger = logging.getLogger(__name__);

class ProvaObjetiva(Prova):
    def __init__(self,cod,cod_inscricao,nota,presenca,cor_caderno,tipo_prova,respostas,gabarito):
        Prova.__init__(self,cod,cod_inscricao,nota);
        self.presenca = presenca;
        self.cor_caderno = cor_caderno;
        self.tipo_prova = tipo_prova;
        self.respostas = respostas;
        self.gabarito = gabarito;
        

    @staticmethod
    def insert(values,cursor):
        try:
            logger.debug("Inserting values: {} into table prova_objetiva.".format(values));
            query = """INSERT INTO prova_objetiva (codigo_inscricao,nota,presenca,cor_caderno,tipo,respostas,gabarito) VALUES (%s,%s,%s,%s,%s,%s,%s)"""; #queries["INSERT"];
            cursor.execute(query,values);
        except Exception as e:
            logger.error("Exception during insert values into prova_objetiva: {}".format(e));

    @staticmethod
    def getValuesCN(columns,dd):
        try:
            logger.debug("Getting values CN from file columns.");
            inscricao = int(columns[dd['NU_INSCRICAO']]);
            nota = -1 if columns[dd['NOTA_CN']] == '' else float(columns[dd['NOTA_CN']])
            presenca = int(columns[dd['IN_PRESENCA_CN']]);
            cor_caderno = int(columns[dd['IN_PRESENCA_CN']]);
            tipo_prova = 1;
            respostas = str(columns[dd['TX_RESPOSTAS_CN']]);
            gabarito = str( columns[dd['GABARITO_CN']]);
            values = (inscricao,nota,presenca,cor_caderno,tipo_prova,respostas,gabarito);
            ret = values;
        except Exception as e:
            logger.error("Exception during get values CN from columns: {}".format(e));
            ret = None;
        return ret;

    @staticmethod
    def getValuesCH(columns,dd):
        try:
            logger.debug("Getting values CH from file columns.");
            inscricao = int(columns[dd['NU_INSCRICAO']]);
            nota = -1 if columns[dd['NOTA_CH']] == '' else float(columns[dd['NOTA_CH']]);
            presenca = int(columns[dd['IN_PRESENCA_CH']]);
            cor_caderno = int(columns[dd['IN_PRESENCA_CH']]);
            tipo_prova = 2;
            respostas = columns[dd['TX_RESPOSTAS_CH']];
            gabarito = columns[dd['GABARITO_CH']];
            values = (inscricao,nota,presenca,cor_caderno,tipo_prova,respostas,gabarito);
            ret = values;
        except Exception as e:
            logger.error("Exception during get values CH from columns: {}".format(e));
            ret = None;
        return ret;

    @staticmethod
    def getValuesLC(columns,dd):
        try:
            logger.debug("Getting values LC from file columns.");
            inscricao = int(columns[dd['NU_INSCRICAO']]);
            nota = -1 if columns[dd['NOTA_LC']] == '' else float(columns[dd['NOTA_LC']])
            presenca = int(columns[dd['IN_PRESENCA_LC']]);
            cor_caderno = int(columns[dd['IN_PRESENCA_LC']]);
            tipo_prova = 3;
            respostas = columns[dd['TX_RESPOSTAS_LC']];
            gabarito = columns[dd['GABARITO_LC']];
            values = (inscricao,nota,presenca,cor_caderno,tipo_prova,respostas,gabarito);
            ret = values;
        except Exception as e:
            logger.error("Exception during get values LC from columns: {}".format(e));
            ret = None;
        return ret;

    @staticmethod
    def getValuesMT(columns,dd):
        try:
            logger.debug("Getting values MT from file columns.");
            inscricao = int(columns[dd['NU_INSCRICAO']]);
            nota = -1 if columns[dd['NOTA_MT']] == '' else float(columns[dd['NOTA_MT']])
            presenca = int(columns[dd['IN_PRESENCA_MT']]);
            cor_caderno = int(columns[dd['IN_PRESENCA_MT']]);
            tipo_prova = 4;
            respostas = columns[dd['TX_RESPOSTAS_MT']];
            gabarito = columns[dd['GABARITO_MT']];
            values = (inscricao,nota,presenca,cor_caderno,tipo_prova,respostas,gabarito);
            ret = values;
        except Exception as e:
            logger.error("Exception during get values MT from columns: {}".format(e));
            ret = None;
        return ret;

