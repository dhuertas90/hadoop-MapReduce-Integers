#!/bin/bash
"""program.py"""

import os

#ELiminar carpetas creadas
os.system("hdfs dfs -rm -R /user/hduser/TP-1/Programa")

#El calculo del conjunto X del ejercicio 8,usando los conjuntos A, B y C.
os.system("python /home/hduser/guest-shared/TP-1/8-ConjuntoX/driver.py")

#Que determine la cardinalidad de X.
job1 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job1 += "-input /user/hduser/TP-1/ConjuntoX/Resultado/part-00000 "
job1 += "-output /user/hduser/TP-1/Programa/CardinalidadX "
job1 += "-mapper /home/hduser/guest-shared/TP-1/5-Cardinalidad/mapper.py "
job1 += "-reducer /home/hduser/guest-shared/TP-1/5-Cardinalidad/reducer.py"
os.system(job1)

#Que determine la pertenencia o no de los elementos de E en X.
job2 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job2 += "-input /user/hduser/TP-1/ConjuntoDatos/E.txt "
job2 += "-output /user/hduser/TP-1/Programa/ElementosE "
job2 += "-mapper /home/hduser/guest-shared/TP-1/6-Pertenencia/mapperE.py "
job2 += "-reducer /home/hduser/guest-shared/TP-1/6-Pertenencia/reducer.py"
os.system(job2)

job3 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job3 += "-input /user/hduser/TP-1/ConjuntoX/Resultado/part-00000 "
job3 +=	"-input /user/hduser/TP-1/Programa/ElementosE/part-00000 "
job3 += "-output /user/hduser/TP-1/Programa/PertenenciaX "
job3 += "-mapper /home/hduser/guest-shared/TP-1/6-Pertenencia/mapperFinal.py "
job3 += "-reducer /home/hduser/guest-shared/TP-1/6-Pertenencia/reducerFinal.py"
os.system(job3)