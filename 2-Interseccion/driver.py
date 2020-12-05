#!/bin/bash
"""driver.py"""

import os

#Limpiar todas las carpetas generadas por los jobs en ../Interseccion (HDFS)
os.system("hdfs dfs -rm -r /user/hduser/TP-1/Interseccion/*")

#Definicion de jobs 1 y 2 para archivos A.txt y B.txt respectivamente
job1 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job1 += "-input /user/hduser/TP-1/ConjuntoDatos/A.txt "
job1 += "-output /user/hduser/TP-1/Interseccion/TipoA "
job1 += "-mapper /home/hduser/guest-shared/TP-1/2-Interseccion/mapperA.py "
job1 += "-reducer /home/hduser/guest-shared/TP-1/2-Interseccion/reducer.py"

job2 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job2 += "-input /user/hduser/TP-1/ConjuntoDatos/B.txt "
job2 += "-output /user/hduser/TP-1/Interseccion/TipoB "
job2 += "-mapper /home/hduser/guest-shared/TP-1/2-Interseccion/mapperB.py "
job2 += "-reducer /home/hduser/guest-shared/TP-1/2-Interseccion/reducer.py"

#Ejecucion de jobs 1 y 2
os.system(job1)
os.system(job2)

#Limpiar solo carpeta Resultados generada por job1 y job2 en ../2-Interseccion/Resultado (HDFS)
#os.system("hdfs dfs -rm -r /user/hduser/TP-1/Interseccion/Resultado")

#Definicion del job 3 - final
job3 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job3 += "-input /user/hduser/TP-1/Interseccion/TipoA/part-00000 "
job3 +=	"-input /user/hduser/TP-1/Interseccion/TipoB/part-00000 "
job3 += "-output /user/hduser/TP-1/Interseccion/Resultado "
job3 += "-mapper /home/hduser/guest-shared/TP-1/2-Interseccion/mapperFinal.py "
job3 += "-reducer /home/hduser/guest-shared/TP-1/2-Interseccion/reducerFinal.py"

#Ejecucion del job 3 - final
os.system(job3)

#Ejecutar en Terminal: python "/home/hduser/guest-shared/TP-1/2-Interseccion/driver.py"