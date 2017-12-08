__author__ = "Mario Figueiro Zemor"
__email__ = "mario.figueiro@ufgrs.br"

#import classes.Database as db; remove this comment
import logging

logger = logging.getLogger(__name__);
class Escola():
    def __init__(self,cod,nome,codmunicipio,dependenciaadm,situacaofuncionamento,tipo):
        self.cod = cod;
        self.nome = nome;
        self.codmunicipio = codmunicipio;
        self.dependenciaadm = dependenciaadm;
        self.situacaofuncionamento = situacaofuncionamento;
        self.tipo = tipo;

    @staticmethod
    def getQuery(query):
        queries = { 'INSERT' : """INSERT INTO (nome,sigla,codregiao) uf VALUES (%s,%s,%s)""",
                    'UPDATE' : """""",
                    'DELETE' : """ """,
                    'FIND_ALL' : """SELECT * FROM formatendnecessidades"""};
        try:
            ret = queries[query];
        except KeyError as e:
            ret = None;
            print("Query {} not found!".format(query));
        return ret;

    def toString(self):
        string = "Escola[{},{},{},{},{},{}]";
        return string.format(self.cod,self.nome,self.codmunicipio,self.dependenciaadm,self.situacaofuncionamento,self.tipo);
