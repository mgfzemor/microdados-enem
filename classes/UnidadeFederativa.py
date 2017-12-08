__author__ = "Mario Figueiro Zemor"
__email__ = "mario.figueiro@ufgrs.br"

#import classes.Database as db; remove this comment
import logging

logger = logging.getLogger(__name__);

class UnidadeFederativa():
    def __init__(self,cod,nome,sigla,codregiao):
        self.cod = cod;
        self.nome = nome;
        self.sigla = sigla;
        self.codregiao = codregiao;

    @staticmethod
    def getQuery(query):
        queries = { 'INSERT' : """INSERT INTO (nome,sigla,codregiao) uf VALUES (%s,%s,%s)""",
                    'UPDATE' : """""",
                    'DELETE' : """ """,
                    'FIND_ALL' : """SELECT * FROM formatendnecessidades"""};
        path = "uf - getQuery - Error:";
        try:
            ret = queries[query];
        except KeyError as e:
            ret = None;
            print("{} Query '{}' not found in dict of Queries!".format(path,query));
        except Exception as e:
            print("{} {}".format(path,e));
        return ret;

    def toString(self):
        string = "UnidadeFederativa[{},{},{},{}]";
        return string.format(self.cod,self.nome,self.sigla,self.codregiao);
