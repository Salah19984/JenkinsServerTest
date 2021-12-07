# Jenkins Server Project
Test Repo for the Continuous Integration Project at RWU


## Installation des Continuous Integration Tools
Auf die Erklärung zur Einrichtung der VM wird nicht weiter eingegangen. Es wird eine VM mit Linux Ubuntu 18.04 Bionic Beaver verwendet.  
Der folgende Abschnitt befasst sich mit den nötigen Tools und Bibliotheken, die für die Inbetriebnahme des CI Servers erforderlich sind.  

## 2.1	Einrichten der Virtuellen Maschine
Auf der Jenkins Homepage wird mindestens eine Java Version 8 empfohlen um zu funktionieren. Auf Linux Ubuntu ist Java nicht standardmäßig vorinstalliert.  
Das kann im Terminal mit ***java -version*** überprüft werden.  
 
![Abbildung 1: Java Versions Check](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)
  
Nun kann eine Java Version über den Paketmanager apt mit dem Befehl  
sudo apt-get install openjdk-11-jdk installiert werden. Das Versionsmanagement Tool Git, wird mit dem Befehl ***sudo apt-get install git*** installiert.  
Git muss auf der Maschine installiert sein, da Jenkins darauf zugreift, wenn ein Build Job erstellt wird und die Versionskontrolle als Quelle angibt.  
Zusätzlich muss eine vollständige Python Umgebung inklusive dem Paketmanager pip installiert sein, damit die Unittests von Jenkins ausgeführt werden können.  
Alle Python Bibliotheken, die im Projekt verwendet werden müssen, ebenfalls auf dem Jenkins Server vorhanden sein, sofern beispielsweise per bash Befehlsscripts  
ausgeführt werden sollen, die diese Bibliotheken verwenden. Darum muss noch pytest mit dem Befehl ***sudo apt install python-pytest*** installiert werden.  
Gerade dieser Punkt kann zu erheblichen Problemen führen, wie im vorherigen Abschnitt unter Limitierungen beschrieben wird.  

## 2.2	Installation von Jenkins
Sind diese Anforderungen erfüllt, kann die Installation von Jenkins beginnen. Je nach Betriebssystem verläuft diese Installation etwas unterschiedlich.  
Hier wird die Installation unter Linux Ubuntu 18.04 Bionic Beaver gezeigt. Jenkins ist in den Repositories von Ubuntu nicht standardmäßig enthalten,  
darum muss zuerst das Repo lokal in der sources.list Datei hinzugefügt werden mit  
***sudo wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add und sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'***  
Anschließend werden noch die Quellen geupdated mit ***sudo apt-get update*** und die Installation von Jenkins wird mit ***sudo apt-get install jenkins*** ausgeführt.  
Der Jenkins Service wird nach der Installation automatisch gestartet. Dies kann mit dem Befehl service jenkins status überprüft werden.  
 
![Abbildung 2: Jenkins Service Status](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

## 2.3 Einrichtung von Jenkins
Jenkins wird über seine Weboberfläche bedient. Um den Server einzurichten, wird eine Verbindung mithilfe eines Webbrowsers hergestellt.  
Dazu muss die Adresse im Format ***IP:port*** eingegeben werden.  
 
![Abbildung 3: Unlock Jenkins Aufforderung](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

Das initialAdminPassword, welches unter dem auf der Seite angegebenen Pfad zu finden ist wird hier eingegeben. Auf der nächsten Seite werden zwei verschiedene   Optionen angezeigt  
-	die vorgeschlagenen Plugins zu installieren 
-	oder selbst zu wählen welche installiert werden sollen.
 
![Abbildung 4: Plugins installieren](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)  
  
Wird die zweite Möglichkeit gewählt, sind die vorgeschlagenen Plugins bereits vorgemerkt. Hier werden die vorgeschlagenen Plugins installiert,  
die beispielsweise aus dem Pipeline Plugin und dem Git Plugin bestehen welche im weiteren Verlauf noch benötigt werden. Die Liste der vorgeschlagenen Plugins ist auf Abbildung 5 zu sehen.  
![Abbildung 5: Plugin Installationsvorgang](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

Danach wird der Admin-Nutzer angelegt. Für private Zwecke kann die Emailadresse auch falsch sein oder leer gelassen werden, jedoch bietet es sich an eine gültige   Adresse anzugeben um als Admin über das Email Extension Plugin beispielsweise Benachrichtigungen zu versenden wenn ein Build fertig oder fehlgeschlagen ist.  
 
![Abbildung 6: Admin Konto erstellen](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

Zum Abschluss wird noch die Jenkins URL verändert auf eine gewünschte URL wie beispielsweise eine bereits reservierte Domain. Da der Server nur eine VM mit   
Netzwerkbrücke und fester IP-Adresse ist und für Demonstrationszwecke nur im eigenen Netzwerk erreichbar sein muss, bleibt sie vorerst unverändert.  
Damit ist die Grundeinstellung abgeschlossen.  
 
![Abbildung 7: Jenkins URL anpassen](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)
# 3	Jenkins Funktionalitäten

## 3.1	Build Jobs
Die Jobs dienen dazu einzelne Schritte im CI Prozess einzurichten. Hier können die Parameter festgelegt werden, mit denen der Build gesteuert wird. Auch werden in   
einer Console pro Job der Buildverlauf und mögliche Fehler als Log ausgegeben. Dazu muss nur der abgeschlossene Job auf der linken Seite der Weboberfläche angeklickt   
und im Untermenü Console Output gewählt werden wie im Bild zu sehen ist.  
 
![Abbildung 8: Untermenü für abgeschlossene Jobs](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

## 3.2	Build Job erstellen
Die Jobs können einzeln durchgeführt werden, jedoch können sie auch verkettet werden. Damit lassen sich schnell verschiedene sogenannte Buildsteps realisieren.  
Um das Demo Projekt zu bauen, wird zu Beginn ein einfacher Job über den Reiter Element anlegen erstellt.  
Es ist verpflichtend einen Namen für den neuen Buildjob anzugeben. Danach wird *„Freestyle Softwareprojekt“* bauen ausgewählt. Daraufhin wird die Konfigurations-Seite   
gezeigt, die viele Möglichkeiten bietet. Wenn alle Einstellungen getroffen sind, muss unbedingt auf Speichern geklickt werden. Damit wird für den erstellten Job ein   
eigener workspace angelegt in dem er ausgeführt werden kann. In Linux Ubuntu 18.04 befindet sich der workspace Ordner im Jenkins Verzeichnis unter */var/lib/Jenkins/workspace*  
Um das Git Projekt zu bauen, wird Reiter Source-Code-Management der Punkt Git angewählt. Das Github Projekt JenkinsServerTest, verfügbar unter der Adresse  
*https://github.com/Salah19984/JenkinsServerTest* ist öffentlich und somit sind keine Credentials nötig. Soll ein als privat markiertes Projekt gebaut werden,  
müssen unter dem Punkt *Credentials* die **GitHub Credentials** eingegeben und gespeichert werden.  
 
![Abbildung 9: Build Job erstellen](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

Es ist möglich, Builds mittels Webhook aus dem Github Plugin zu starten. Damit können die Builds so automatisiert werden, dass wenn immer ein push auf den angegebenen   
Github Branch stattfindet, auch ein Build ausgelöst wird. Das ist eine ressourcenschonende Möglichkeit, um den Build zu automatisieren. Dazu muss das Github Plugin   
installiert sein und der Jenkins Server muss aus dem Internet erreichbar sein.  
Die unelegante Lösung wird hier zu Demonstrationszwecken verwendet, indem im *Build Trigger* Reiter *Poll SCM* ausgewählt wird. Dort wird bei *Schedule* ein Zeitplan   
eingetragen im Cronjob Format wie es aus Linux bekannt ist. Diese Lösung wird gern für die Integration Test- sowie Unit Test Pipelines verwendet, um Sie   
beispielsweise nachts ausführen zu können und die Reports am nächsten Morgen einzusehen.  
 
![Abbildung 10: Polling auf das Github Projekt](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

Der oben zu sehende Schedule ruft alle 15 Minuten das Github Repository ab und löst bei einer erkannten Veränderung den Build aus. Getestet werden kann der Schedule,  
indem im Github Projekt z.B. eine neue Datei erstellt wird, die anschließend ins Repository gepusht wird.  
 
![Abbildung 11: Build Trigger Test](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

## 3.3	Build Jobs verketten
Mehrere Build Jobs können miteinander verkettet werden, um eine Art Build Pipeline darzustellen. Das stellt die einfachste Art und Weise dar einen kompletten CD   
Prozess abbilden zu können und genügt für kleine Projekte. Diese Art wird in größeren Projekten jedoch schnell unübersichtlich, da die Verkettung aller Jobs samt   
ihrer Buildsteps, post Buildsteps sowie den im jeweiligen Job ausgeführten Scripts manuell gesteuert und überwacht werden muss.  
 
## 3.4	Unit Tests integrieren mit verketteten Jobs
Dazu muss ein neuer Job angelegt werden, um die Unit Tests auszuführen, nachdem der Buildjob durchgeführt wurde. Bei den *Build Triggers* wird die Option *build after other projects are built*  
gesetzt und bei *Projects to watch* der Namen des gewünschten vorherigen Jobs angegeben wie in Abbildung 12 zu sehen ist. Jenkins bietet hier eine Auto-Completion an.  
Da es nur Sinn macht die Unittests auszuführen, wenn der Build stable, also ohne erkannte Fehler war, wird die Option *Trigger only if build is stable* ausgewählt. Auch wie im  
letzten Job wird wieder das Repo gepullt in dem später die Unittests ausgeführt werden. Also muss der Punkt *Git* wieder ausgewählt und das Projekt angegeben werden. Damit wird  
auch für diesen Job wieder ein eigener Workspace von Jenkins angelegt in dem gearbeitet wird.  
 
![Abbildung 12: Verkettung von Jobs](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

Anschließend wird der build step *execute shell* hinzugefügt. Hier wird nur noch der vorher gebaute Unittest ausgeführt mit dem Befehl ***python3 test_calc.py***.     
![Abbildung 13: Build Step hinzufügen](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)
 
## 3.5	Pipelines
Jobs in einer Pipeline zu organisieren ist der bevorzugte Weg gerade in größeren Projekten. Dazu bietet Jenkins wie immer ein Plugin an welches einfach unter *Manage  
Jenkins > Manage Plugins* heruntergeladen und installiert werden kann. Da bereits zu Beginn bei der Einrichtung die vorgeschlagenen Plugins installiert wurden ist das   
Pipeline Plugin hier bereits vorhanden.  
 
![Abbildung 14: Pipeline Plugin installieren](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

Eine CD Pipeline ist in der agilen Softwareentwicklung das Mittel der Wahl um seine Software in kurzen Abständen wiederholt und automatisiert zu releasen. Der  
typische Weg einer Pipeline sieht folgendermaßen aus:  
- Checkout aus der Versionsverwaltung
- Build
- Unit-Tests
- Integrationstests
- Statische Code-Analyse
- Deployment in einer Staging-Umgebung
- Funktionale und/oder manuelle Tests
- Deployment in Produktion
 
![Abbildung 15: Darstellung einer Pipeline](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

Ein Plugin, welches die Arbeit mit Pipelines sehr vereinfacht ist das *Jenkins Plugin  
Blue Ocean*.  
Es bietet eine aufgeräumte und erweiterte Ansicht für Pipelines auf der Jenkins Weboberfläche. Dieses Plugin kann für die Pipeline Erstellung noch über   
*Manage Plugins* installiert werden. Nach der Plugin Installation wird wieder *new item* gewählt und ein eindeutiger Name vergeben. Diesmal wird jedoch statt *Freestyle Project* die Pipeline ausgewählt.  
![Abbildung 16: Pipeline anlegen](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)
In dieser Option ist es nicht mehr notwendig wie im vorherigen Buildjob alle Schritte einzeln einzurichten, um das Github Repo nach etwaigen Änderungen zu bauen.  
Nur der neue Reiter *Pipeline* ist interessant, da mithilfe der Jenkinsfile alle vorherigen Auswahlmöglichkeiten in Groovy dargestellt werden können. Hier ist es möglich,  
das Pipeline Script direkt einzugeben oder es aus dem SCM zu starten. Für diese Demonstration wird es aus dem SCM gestartet, da so die Jenkinsfile in die Versionierung mit  
aufgenommen werden kann, was die Pflege der Dateien vereinfacht. Im Script selbst sind alle Anweisungen bereits in der richtigen Reihenfolge angegeben um das gesamte Projekt  
auszuchecken, zu bauen, zu testen und zu deployen.  
![Abbildung 17: Pipeline einrichten und Jenkinsfile aus SCM ausführen](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

Am unteren Ende der Seite befindet sich der Link *Pipeline Syntax* welcher in den Snippet Generator führt. Dieser eignet sich sehr gut um sich mit der Groovy Syntax vertraut zu machen. 
## 3.6	Jenkinsfile
Die Jenkinsfile dient dazu alle nötigen Arbeitsschritte zentral in einem Textfile abzulegen, um nacheinander in der Pipeline die einzelnen CD-Arbeitsschritte abzuarbeiten.  
Im vorigen Abschnitt wurde darauf eingegangen, dass die Jenkinsfile direkt im Git Repository abgelegt wird. Der Grund ist, dass die Jenkinsfile dadurch   
auch automatisch von der Versionierungssoftware erfasst wird. So ist es „good practice“, der Jenkinsfile eine eigene Versionsnummer zuzuweisen, und sie vom SCM System  
erfassen zu lassen. Bei Änderungen wird die Versionsnummer folgend mit hochgezählt. Die Sprache in der Jenkinsfiles geschrieben werden ist Groovy. Sie wird auf der  
Java VM ausgeführt und ist daher bestens geeignet für den Einsatz in Jenkins. Die Jenkinsfile wird in diesem Projekt im declarative Mode geschrieben wie in Abbildung 18 zu sehen ist.
 
![Abbildung 18: Jeninsfile im Declarative Mode](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

Es gibt auch die Möglichkeit sie im Scripted Mode zu schreiben und reine Codeform zu verwenden. Beide Schreibweisen bieten Vor- wie auch Nachteile. Der declarative  
Mode hat z.B. den Nachteil, dass er nicht den vollen Funktionsumfang bietet wie der Scripted Mode, d.h. einige Möglichkeiten sind hier durch strikte Vorgaben in der  
Struktur eingeschränkt. Er bietet andererseits den großen Vorteil, dass er einfach und gut menschenlesbar ist, wie in Abbildung 18 zu sehen ist. Es gibt in der  
Community noch keine eindeutige Präferenz darüber, welcher der beiden Modi sich am Ende durchsetzen kann. Pipelines wurden ursprünglich nur mit dem Scripted Modus  
geplant. Der declarative Modus wurde später hinzugefügt. Da beide jedoch auf der Groovy DSL basieren, unterscheiden Sie sich maßgeblich nur in Syntax und  
Funktionsumfang. Jedoch gestattet es Groovy auch beide Modi zu vermischen:  
Z.B. können einige nützliche Groovy Funktionen definiert und anschließend in der deklarativen Struktur aufgerufen werden. Beispielsweise kann mithilfe einer Schleife  
über Ordner iteriert werden, um nacheinander die enthaltenen Unit Tests auszuführen, anstatt jeden Test in der Teststage nacheinander mit redundantem Code aufzurufen.  
Am übersichtlichsten und daher „good practice“ ist jedoch, sich für einen Modus zu entscheiden.  

# 4.	Unit Tests
Damit die Unittests möglichst häufig ausgeführt werden und dabei wenig Zeit verloren geht, ist es wichtig, dass alle Unittests automatisiert immer wieder ausgeführt  
werden, oder zumindest mit nur einem Knopfdruck. Hier wird im Folgenden gezeigt wie Unit Tests in einen CI Prozess eingebunden werden können und bei jedem neuen Build  
Durchgang automatisch ausgeführt werden.

## 4.1	Beispiel Python Unittests
Im Testprojektordner unittest existiert eine Datei mit Namen *test_calc.py*. Diese nutzt das unittest Modul das bereits in der Standardbibliothek von Python enthalten  
ist. Es werden einige Tests auf die Funktionen ausgeführt, um die Ausgabewerte zu überprüfen. Das Modul führt die Tests nacheinander aus und speichert den Output aus  
der Konsole automatisch in eine *results.xml* Datei im Git Repository. Auf diese Weise können alle Testergebnisse auch in menschenlesbarer Form zusätzlich geloggt  
werden. Es ist die übliche Vorgehensweise, die Testergebnisse als xml Datei darzustellen. So können mithilfe des Jenkins Servers unter anderem auch Statistiken  
dargestellt werden, die die Erfolgsrate der Tests zeigen und anhand derer der Build als „stable“ oder „unstable“ bewertet werden kann. Die Module JUnit oder xUnit  
welche zusätzlich installiert werden können bieten hier sehr viele Möglichkeiten. Mit diesen Modulen ist es auch einfach möglich, die xml Datei in eine .html Datei zu  
parsen und den Report zu veröffentlichen. Gerade für die interne Dokumentation und die Überprüfung der Definition of Done (DoD) ist dies hilfreich.  
Um dieses Feature nutzen zu können wird zuerst in Jenkins das JUnit Plugin installiert.  
 
![Abbildung 19: Junit Plugin Installation](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)  
In der in Abbildung 18 zu sehenden Jenkinsfile wird der Schritt ***step([$class: 'JUnitResultArchiver', checksName:‘ ‘, testResults: 'test_results/results.xml'])*** in der  
Test Stage hinzugefügt. Darin wird unter *checksName* angegeben welche xml Datei verglichen werden soll, und unter *testResults* wird der Pfad angegeben, unter dem sich  
die *results.xml* Datei befindet.  
Bei *checksName* wird keine Datei angegeben, da die *results.xml* Datei bei jedem Durchlauf überschrieben wird und nur mit sich selbst verglichen werden würde. Jenkins  
findet diese xml Datei, die mit dem JUnit Plugin erstellt wurde, automatisch im workspace und auf der Weboberfläche wird nun zusätzlich in der jeweiligen Iteration  
der Pipeline ein Punkt ***Test Result(no failures)*** angezeigt wie in Abbildung 20 zu sehen ist.  
 
![Abbildung 20: JUnit Test Result](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

Wenn die Pipeline mehr als einmal durchlaufen wurde, wird zusätzlich ein Test Result Trend auf der Weboberfläche von Jenkins als Statistik angezeigt wie in Abbildung 21 zu  sehen ist.
 
![Abbildung 21: JUnit Test Result Trend](https://github.com/Salah19984/JenkinsServerTest/blob/main/Pictures/Abb1.png)

 
