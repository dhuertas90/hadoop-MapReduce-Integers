#!/bin/bash
"""driver.py"""

import os


os.system("hdfs dfs -rm -r /user/hduser/TP-1/Cardinalidad/*")

#Definicion del job
job = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job+= "-input /user/hduser/TP-1/ConjuntoDatos/A.txt "
job+= "-output /user/hduser/TP-1/Cardinalidad/Resultado "
job+= "-mapper /home/hduser/guest-shared/TP-1/5-Cardinalidad/mapper.py "
job+= "-reducer /home/hduser/guest-shared/TP-1/5-Cardinalidad/reducer.py"

#Ejecucion del job
os.system(job)