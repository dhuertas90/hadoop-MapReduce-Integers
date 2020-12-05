#!/bin/bash
"""driver.py"""

import os

#os.system("hdfs dfs -rm -r /user/hduser/TP-1/Pertenencia/*")

#Definicion del job1
job1 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job1+= "-input /user/hduser/TP-1/ConjuntoDatos/A.txt "
job1+= "-output /user/hduser/TP-1/Pertenencia/TipoA "
job1+= "-mapper /home/hduser/guest-shared/TP-1/6-Pertenencia/mapperA.py "
job1+= "-reducer /home/hduser/guest-shared/TP-1/6-Pertenencia/reducer.py "

os.system(job1)

#Definicion del job2
job2 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job2+= "-input /user/hduser/TP-1/ConjuntoDatos/E.txt "
job2+= "-output /user/hduser/TP-1/Pertenencia/ElementosE "
job2+= "-mapper /home/hduser/guest-shared/TP-1/6-Pertenencia/mapperE.py "
job2+= "-reducer /home/hduser/guest-shared/TP-1/6-Pertenencia/reducer.py "

os.system(job2)

#Definicion del job 3 - final
job3 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job3 += "-input /user/hduser/TP-1/Pertenencia/TipoA/part-00000 "
job3 +=	"-input /user/hduser/TP-1/Pertenencia/ElementosE/part-00000 "
job3 += "-output /user/hduser/TP-1/Pertenencia/Resultado "
job3 += "-mapper /home/hduser/guest-shared/TP-1/6-Pertenencia/mapperFinal.py "
job3 += "-reducer /home/hduser/guest-shared/TP-1/6-Pertenencia/reducerFinal.py"

#os.system("hdfs dfs -rm -r /user/hduser/TP-1/Pertenencia/Resultado")

os.system(job3)
