# P-NP
Problema matemático para demostrar que P = NP

Primera línea de trabajo, actuar sobre el espacio de soluciones, los programas tenderán a explorar varias veces la misma
subsolución optimizando esto se puede ganar en complejidad.

Segunda línea de trabajo, el programa es analizado y se detectan secuencias de código que se repiten en varias iteracines, 
se pueden optimizar.

Cuidadín como afecta a la complejidad espacial todo esto cuando se pasa a usar la memoria para recordar lo realizado 
previamente.

python -m memory_profiler subconjuntos.py



Preparando el entorno:
sudo apt-get  update; sudo apt-get install  python-dev -y
sudo apt install python-pip
sudo pip install -U memory_profiler
sudo pip install psutil
