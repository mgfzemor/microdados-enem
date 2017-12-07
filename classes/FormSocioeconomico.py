__author__ = "Mario Figueiro Zemor"
__email__ = "mario.figueiro@ufgrs.br"

import classes.Database as db;
import logging

logger = logging.getLogger(__name__);

class FormSocioeconomico():

    queries = { 'INSERT' : '',
                'UPDATE' : '',
                'DELETE' : '',
                'FIND_ALL' : ''};

    def __init__(self,inscricao,idade,sexo,cod_nacionalidade,cod_escola,cod_municipio_nasc,cod_uf_nasc,cod_municipio_resid,cod_conclusao_EM,ano_conclusao_EM,estado_civil,raca):


    def toString():
        return "Estudante["+self.inscricao+"]";

    @staticmethod
    def getQuery(query):
        return queries[query];

    @staticmethod
    def insert(values,cursor):
        try:
            logger.debug("Inserting values: {} into Student.".format(values));
            query = 'INSERT INTO estudante VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'; #queries["INSERT"];
            cursor.execute(query,values);
        except Exception as e:
            logger.error("Exception during insert values into Student: {}".format(e));

    @staticmethod
    def getValues(columns,dd):
        try:
            q1 = columns[dd['IDADE']];
            logger.debug("Getting values from file columns.");
            inscricao = int(columns[dd['NU_INSCRICAO']]);
            idade = int(columns[dd['IDADE']]);
            sexo = columns[dd['TP_SEXO']];
            cod_nacionalidade = int(columns[dd['NACIONALIDADE']]);
            cod_escola = -1 if columns[dd['COD_ESCOLA']] == '' else int(columns[dd['COD_ESCOLA']]);
            cod_municipio_nasc = -1 if columns[dd['COD_MUNICIPIO_NASCIMENTO']] == '' else int(columns[dd['COD_MUNICIPIO_NASCIMENTO']]);
            cod_uf_nasc = -1 if columns[dd['COD_UF_NASCIMENTO']] == '' else int(columns[dd['COD_UF_NASCIMENTO']]);
            cod_municipio_resid = int(columns[dd['COD_MUNICIPIO_RESIDENCIA']]);
            cod_conclusao_EM = int(columns[dd['ST_CONCLUSAO']]);
            no_conclusao_EM = -1 if columns[dd['ANO_CONCLUIU']] == '' else int(columns[dd['ANO_CONCLUIU']]);
            estado_civil = int(columns[dd['TP_ESTADO_CIVIL']]);
            raca = int(columns[dd['TP_COR_RACA']]);
            values = (inscricao,idade,sexo,cod_nacionalidade,cod_escola,cod_municipio_nasc,cod_uf_nasc,cod_municipio_resid,cod_conclusao_EM,no_conclusao_EM,estado_civil,raca);
            ret = values;
        except Exception as e:
            logger.error("Exception during get values from columns: {}".format(e));
            ret = None;
        return ret;
