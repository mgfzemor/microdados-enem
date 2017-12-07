from classes.Estudante import *;
from classes.ProvaObjetiva import *;
import classes.Database as db;
import classes.file as csvfile;
import logging
import config.logger as log;

logger = logging.getLogger(__name__);

MAX_TO_COMMIT=5

def insertEstudents(data,dd):
    conn = db.connect();
    cursor = conn.cursor();
    i = 0;
    while True:
        try:
            line = csvfile.readLine(data);
            values = Estudante.getValues(columns,dd);
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

def inserirProvaObjetiva(data,dd):
    conn = db.connect();
    cursor = conn.cursor();
    i = 0;
    while True:
        try:
            columns = csvfile.readLine(data);
            valuesCN = ProvaObjetiva.getValuesCN(columns,dd);
            valuesCH = ProvaObjetiva.getValuesCH(columns,dd);
            valuesLC = ProvaObjetiva.getValuesLC(columns,dd);
            valuesMT = ProvaObjetiva.getValuesMT(columns,dd);

            ProvaObjetiva.insert(valuesCN,cursor);
            ProvaObjetiva.insert(valuesCH,cursor);
            ProvaObjetiva.insert(valuesLC,cursor);
            ProvaObjetiva.insert(valuesMT,cursor);
            i = i+1;
            if i%MAX_TO_COMMIT ==0:
                print("commit: total ProvaObjetiva: {}".format(i));
                conn.commit();
                break;
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

if __name__ == "__main__":
    logging.basicConfig(filename=log.filename, level=log.level,format=log.lineformat, datefmt=log.datefmt)

    microdados =  "csv/dados.csv";
    open_mode = "rb";
    data = csvfile.openFile(microdados,open_mode);
    data_dict = csvfile.createDict(data);
    #insertEstudents(data,data_dict);
    inserirProvaObjetiva(data,data_dict);
    print("done!");
