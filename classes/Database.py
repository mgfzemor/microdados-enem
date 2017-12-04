__author__ = "Mario Figueiro Zemor";
__email__ = "mario.figueiro@ufgrs.br";

import psycopg2
import config.db as db
import logging

logger = logging.getLogger(__name__);

def connect():
    ret = None;
    try:
        logger.debug("connecting to postgres db: {} {} {}".format(db.host,db.user,db.dbname));
        conn = psycopg2.connect(host=db.host,user=db.user,password=db.password,dbname=db.dbname);
        ret = conn;
    except Exception as e:
        logger.error("Exception during postgres connetion: {}".format(e));
    return ret;
