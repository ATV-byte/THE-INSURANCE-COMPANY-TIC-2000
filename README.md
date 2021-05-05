# THE-INSURANCE-COMPANY-TIC-2000
PROIECT INGINERIA SISTEMELOR CU INTELIGENTA ARTIFICIALA - anul 2

Baza de date ce mi-a fost atribuita, pe numele ei THE INSURANCE COMPANY (TIC) 2000, a fost constituita din mai multe fisiere: TICDATA2000.txt, TICEVAL2000.txt, TICTGTS2000.txt.

Aceasta baza de date contine informatii social-demografice despre clientii unei companii de asigurari ( venituri, avere, proprietati etc.), iar scopul a fost determinarea pe baza acestor informatii daca clientii detin sau nu proprietati mobile ( caravane / traielere ), folosind algoritmul Random Forest.

TICDATA2000.txt este fisierul ce contine data-setul pentru ANTRENARE. In acest fisier avem informatii despre 5822 de persoane cu 86 de atribute fiecare. In acest fisier este mentionat daca persoanele au sau nu au proprietati mobile (coloana 86), deci se poate afirma faptul ca invatarea este SUPERVIZATA.

TICEVAL2000.txt este fisierul ce contine data-setul pentru TEST. In  acest fisier avem informatii despre 4000 de persoane strucutrate ca in data-setul de antrenare, doar ca in acest fisier NU mai este mentionat daca persoanele au sau nu mobile.

Scopul programului este sa returneze o lista de 0/1 ce are ca insemnatate faptul ca persoana cu acelasi index cu cel al raspunsului are sau nu proprietati mobile.
In TICTGTS2000.txt este o lista de “verificare” unde se afla raspunsul real al clientilor din data-setul de test, astfel putand sa calculam acuratetea algoritmului.
 
Folosind np.loadtxt a fost foarte usor de importat toate datele in algoritm sub forma matriceala.
Am divizat datele in modul specific, invatat la laborator (in date_train si etichete ), am setat parametrii necesari pentru ensemble.BaggingClassifier, am antrenat sistemul, folosind fit(date_train, etichete_train), iar apoi am folosit predict(date_test) pentru a obtine rezultatul dorit.
Pentru a masura acuratetea am folosit accuracy_score(target, predictii), unde target contine datele importate din TICTGTS2000.txt, iar predictii contine rezultatele algoritmului.

Ruland programul am observat ca acuratetea este destul de mare pentru orice parametrii variati in decursul acestei teme, iar algoritmul se comporta corect pe aceasta baza de date.

