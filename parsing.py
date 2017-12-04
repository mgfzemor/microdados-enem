from classes.Estudante import *;
import classes.Database as db;
import classes.file as csvfile;
import logging
import config.logger as log;

logger = logging.getLogger(__name__);

def insertEstudents(data,dd):
    conn = db.connect();
    cursor = conn.cursor();
    i = 0;
    while True:
        try:
            columns = csvfile.readLine(data);
            values = Estudante.getValues(columns,dd);
            Estudante.insert(values,cursor);
            i = i +1;
            if i%50000 ==0:
                print("commit: total students: {}".format(i));
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
    insertEstudents(data,data_dict);
    print("done!");
