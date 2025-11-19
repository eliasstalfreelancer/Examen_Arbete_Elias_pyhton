    Health Study – Dataanalys i Python

Detta projekt analyserar ett hälsodataset med fokus på blodtryck, rökning, kolesterol och grundläggande hälsoparametrar. Projektet genomför beskrivande statistik, visualiseringar, simuleringar, konfidensintervall och hypotesprövning enligt givna uppgiftsinstruktioner.

    Innehåll

Projektet består av:

report.ipynb – Huvudfil med all analys, grafer och slutsatser

analysis.py – Funktioner för beskrivande statistik och konfidensintervall

viz.py – Funktioner för visualisering (histogram, boxplot, stapeldiagram)

sim.py – Funktioner för simulering av sjukdomssannolikhet

io_utils.py – Funktioner för att läsa in och strukturera data

health_study_dataset.csv – Datasetet som analyseras

    Beskrivande Statistik

Projektet beräknar:

Medelvärde

Median

Min / Max

för variablerna:

ålder

vikt

längd

systoliskt blodtryck

kolesterol

Resultatet sammanställs i en DataFrame för överblick.

    Visualiseringar

Minst tre grafer skapas, t.ex.:

Histogram över systoliskt blodtryck

Boxplot av vikt per kön

Stapeldiagram över andelen rökare

    Simulering

En simulering av 1000 slumpade personer genomförs baserat på den observerade sjukdomssannolikheten i datan.
Simulerad andel jämförs sedan med den verkliga andelen.

    Konfidensintervall

Ett 95% konfidensintervall för systoliskt blodtryck beräknas med:

Normalapproximation

(VG) Möjlighet till bootstrap-metod

Motivering och källa ges i rapporten.

    Hypotesprövning

Hypotesen testas:

”Rökare har högre medelvärde på systoliskt blodtryck än icke-rökare.”

Metod:

Ensidigt t-test (scipy.stats.ttest_ind)

Resultat och tolkning sammanställs i notebooken.

    Körning

Starta projektet genom att öppna report.ipynb i Jupyter Notebook eller JupyterLab.

Se till att installera nödvändiga paket:

pip install numpy pandas matplotlib scipy

    Källor och Referenser

Projektet bygger på:

Chalmers Föreläsning 4 – Normalfördelning & CLT (Axelson-Fisk, 2016)

SCB – Statistikens Grunder

SciPy dokumentation för ttest_ind

