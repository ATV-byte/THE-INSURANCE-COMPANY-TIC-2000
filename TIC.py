from sklearn import datasets, tree, ensemble, metrics
import numpy as np
from sklearn.metrics import accuracy_score

#citeste fisier, r vine de la read pt ca vreau sa iau date din fisier

date = np.loadtxt("ticdata2000.txt", dtype='i', delimiter='	')
etichete = np.loadtxt("ticdata2000.txt", dtype='i', delimiter='	')
date_train = date[0:5822, 0:85]
etichete_train= etichete[0:5822,85]
print(etichete_train.shape)
list1 = [0.25, 0.5, 0.85]
list2 = [0.1, 0.5, 0.8]
date_test= np.loadtxt("ticeval2000.txt", dtype='i', delimiter='	')
target= np.loadtxt("tictgts2000.txt", dtype='i', delimiter='\r\n')
maxim=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        clf= ensemble.BaggingClassifier(base_estimator=None, n_estimators=10, max_samples=list1[i], max_features=list2[j], bootstrap=True,
                                   bootstrap_features=False, oob_score=False, warm_start=False, n_jobs=None,
                                   random_state=None, verbose=0)
        clf.fit(date_train, etichete_train)
        predictii = clf.predict(date_test)   
        print("Acuratetea cu procentul in bag: ", list1[i], "si numarul de dimensiuni dintr-un nod: ", list2[j], 
                          "este: ", accuracy_score(target, predictii))    
        maxim.append(accuracy_score(target, predictii))
print("Acuratetea cea mai mare este: ", max(maxim))
