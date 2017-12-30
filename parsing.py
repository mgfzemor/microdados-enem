from classes.Estudante import *
from classes.ProvaObjetiva import *
from classes.ProvaRedacao import *
from classes.Database import *
import classes.file as csvfile
import logging
import config.logger as log

logger = logging.getLogger(__name__);

MAX_TO_COMMIT=6

def insertEstudents(data,dd):
    conn = Database.connect();
    cursor = conn.cursor();
    i = 0;
    while True:
        try:
            line = csvfile.readLine(data);
            values = Estudante.getValues(line,dd);
            Estudante.insert(values,cursor);
            i = i +1;
            if i%MAX_TO_COMMIT ==0:
                print("commit: total students: {}".format(i));
                conn.commit();
        except Exception as e:
            logger.error("Exception during inserting students: {}.".format(e));
            print("error: {}".format(e));
            conn.commit();
            break;

def inserirEscolas():
    escolas = {};
    while True:
        try:
            line = csvfile.readLine(data);
            

def inserirProvas(data,dd):
    conn = Database.connect();
    cursor = conn.cursor();
    i = 0;
    while True:
        try:
            columns = csvfile.readLine(data);
            valuesProvaObjetiva = ProvaObjetiva.getValues(columns,dd,i);
            valuesProvaRedacao = ProvaRedacao.getValues(columns,dd,i+1);
            ProvaObjetiva.insert(valuesProvaObjetiva, cursor);
            ProvaRedacao.insert(valuesProvaRedacao, cursor);
            i = i+2;
            if i%MAX_TO_COMMIT ==0:
                print("commit: total Provas: {}".format(i));
                conn.commit();
        except Exception as e:
            logger.error("Exception during inserting objective tests: {}.".format(e));
            print("erro during inseirProvaObjetiva: {}".format(e));
            conn.commit();
            break;

def inserirProvaRedacao(data,dd):
    conn = db.connect();
    cursor = conn.cursor();
    i = 0;
    while True:
        try:
            columns = csvfile.readLine(data);
            values = ProvaRedacao.getValues(columns,dd);
            ProvaRedacao.insert(values,cursor);
            i = i +1;
            if i%MAX_TO_COMMIT ==0:
                print("commit: total ProvaRedacao: {}".format(i));
                conn.commit();
        except Exception as e:
            logger.error("Exception during inserting students: {}.".format(e));
            print("error: {}".format(e));
            conn.commit();
            break;

def findAllEstudents():
    conn = db.connect();
    cursor = conn.cursor();
    Estudante.findAll(cursor);

def findStudentByCod():
    estudante = Estudante.findByCod(140000000003);
    if estudante:
        print(estudante.toString());
    else:
        print("Estudante nao encontrado");

if __name__ == "__main__":
    logging.basicConfig(filename=log.filename, level=log.level,format=log.lineformat, datefmt=log.datefmt)

    microdados =  "csv/microdados.csv";
    open_mode = "rb";
    data = csvfile.openFile(microdados,open_mode);
    data_dict = csvfile.createDict(data);
    Estudante.groupSchool();
    print("done!");
