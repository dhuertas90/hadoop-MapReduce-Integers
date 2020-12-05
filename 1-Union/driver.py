#!/bin/bash
"""driver.py"""

import os

#Limpiar la carpeta ../Union/Resultado generado por el job (en HDFS)
os.system("hdfs dfs -rm -r /user/hduser/TP-1/Union/*")

#Definicion del job
job = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job+= "-input /user/hduser/TP-1/ConjuntoDatos/A.txt "
job+= "-input /user/hduser/TP-1/ConjuntoDatos/B.txt "
job+= "-output /user/hduser/TP-1/Union/Resultado "
job+= "-mapper /home/hduser/guest-shared/TP-1/1-Union/mapper.py "
job+= "-reducer /home/hduser/guest-shared/TP-1/1-Union/reducer.py"

#Ejecucion del job
os.system(job)

#Comando de ejecucion: python "/home/hduser/guest-shared/TP-1/1-Union/driver.py"