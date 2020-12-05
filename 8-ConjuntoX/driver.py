#!/bin/bash
"""driver.py"""

import os

#Limpiar todas las carpetas generadas por los jobs en ../ConjuntoX (HDFS)
os.system("hdfs dfs -rm -r /user/hduser/TP-1/ConjuntoX")

#Job1: B UNION C
job1 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job1 += "-input /user/hduser/TP-1/ConjuntoDatos/B.txt "
job1 += "-input /user/hduser/TP-1/ConjuntoDatos/C.txt "
job1 += "-output /user/hduser/TP-1/ConjuntoX/Union-Job1 "
job1 += "-mapper /home/hduser/guest-shared/TP-1/8-ConjuntoX/mapperUnion.py "
job1 += "-reducer /home/hduser/guest-shared/TP-1/8-ConjuntoX/reducerUnion.py"

#Job2: A - Job1
job2 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job2 +=	"-input /user/hduser/TP-1/ConjuntoX/Union-Job1/part-00000 "
job2 += "-input /user/hduser/TP-1/ConjuntoDatos/A.txt "
job2 += "-output /user/hduser/TP-1/ConjuntoX/Diferencia-Job2 "
job2 += "-mapper '/home/hduser/guest-shared/TP-1/8-ConjuntoX/mapperDiferencia.py A UNION' "
job2 += "-reducer /home/hduser/guest-shared/TP-1/8-ConjuntoX/reducerDiferencia.py"

#Job3: A UNION C
job3 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job3 += "-input /user/hduser/TP-1/ConjuntoDatos/A.txt "
job3 += "-input /user/hduser/TP-1/ConjuntoDatos/C.txt "
job3 += "-output /user/hduser/TP-1/ConjuntoX/Union-Job3 "
job3 += "-mapper /home/hduser/guest-shared/TP-1/8-ConjuntoX/mapperUnion.py "
job3 += "-reducer /home/hduser/guest-shared/TP-1/8-ConjuntoX/reducerUnion.py"

#Job4: B - Job3
job4 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job4 +=	"-input /user/hduser/TP-1/ConjuntoX/Union-Job3/part-00000 "
job4 += "-input /user/hduser/TP-1/ConjuntoDatos/B.txt "
job4 += "-output /user/hduser/TP-1/ConjuntoX/Diferencia-Job4 "
job4 += "-mapper '/home/hduser/guest-shared/TP-1/8-ConjuntoX/mapperDiferencia.py B UNION' "
job4 += "-reducer /home/hduser/guest-shared/TP-1/8-ConjuntoX/reducerDiferencia.py"

#Job5: A UNION B
job5 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job5 += "-input /user/hduser/TP-1/ConjuntoDatos/A.txt "
job5 += "-input /user/hduser/TP-1/ConjuntoDatos/B.txt "
job5 += "-output /user/hduser/TP-1/ConjuntoX/Union-Job5 "
job5 += "-mapper /home/hduser/guest-shared/TP-1/8-ConjuntoX/mapperUnion.py "
job5 += "-reducer /home/hduser/guest-shared/TP-1/8-ConjuntoX/reducerUnion.py"

#Job6: C - Job5
job6 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job6 +=	"-input /user/hduser/TP-1/ConjuntoX/Union-Job5/part-00000 "
job6 += "-input /user/hduser/TP-1/ConjuntoDatos/C.txt "
job6 += "-output /user/hduser/TP-1/ConjuntoX/Diferencia-Job6 "
job6 += "-mapper '/home/hduser/guest-shared/TP-1/8-ConjuntoX/mapperDiferencia.py C UNION' "
job6 += "-reducer /home/hduser/guest-shared/TP-1/8-ConjuntoX/reducerDiferencia.py"

#Job7: Job2 UNION Job4 UNION Job6
job7 = "hadoop jar /home/hduser/jarHadoop/hadoop-streaming-2.6.0.jar "
job7 +=	"-input /user/hduser/TP-1/ConjuntoX/Diferencia-Job2/part-00000 "
job7 +=	"-input /user/hduser/TP-1/ConjuntoX/Diferencia-Job4/part-00000 "
job7 +=	"-input /user/hduser/TP-1/ConjuntoX/Diferencia-Job6/part-00000 "
job7 += "-output /user/hduser/TP-1/ConjuntoX/Resultado "
job7 += "-mapper /home/hduser/guest-shared/TP-1/8-ConjuntoX/mapperUnion.py "
job7 += "-reducer /home/hduser/guest-shared/TP-1/8-ConjuntoX/reducerUnion.py"

#ejecucion de jobs union
os.system(job1)
os.system(job3)
os.system(job5)

#ejecucion de diferencias
os.system(job2)
os.system(job4)
os.system(job6)

#Ejecucion del job final
os.system(job7)