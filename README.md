# Git Tutorial

## Checklist

Do sprawdzenia czy kazda z tych kwestii jest dostatecznie dobrze opisana

- działanie
- instalacja
- praca samemu
- praca w grupach
- praca na featurach
- profil github

## Narzędzia

- VS Code

## Teoria (15m)

### Po co jest git? Co zamiast gita?

System kontroli wersji - oprogramowanie służące do śledzenia zmian głównie w kodzie źródłowym oraz pomocy programistom w łączeniu zmian dokonanych w plikach przez wiele osób w różnym czasie.

Dwie osoby pracujące na jednym pliku zmierzają do jednego dużego efektu końcowego -mastera- projektu jako całości. Każda gałąź to jedna osoba.

![prosty schemat](https://cdn-images-1.medium.com/max/1104/1*PiduCtSA7kMwdPiMZo1nHw.jpeg)

Git - rozproszony system kontroli wersji zapoczątkowany przez Linusa Trovalda (twórcę Linuxa)
(DVCS - distributed version control system)

### Jak działa git?

### Dystrybuowany? Że co?

Praca offline!
Wszyscy posiadają własną kopię repozytorium, do której może zapisywać zmiany bez połączenia z siecią, następnie zmiany mogą być wymieniane między lokalnymi repozytoriami.

### Co to jest GitHub?

Strona internetowa i serwis służący do przechowywania projektów i dzielenia się kodem z innymi użytkownikami.

## Instalacja gita

[Pobieramy gita](http://git-scm.com)
Next, next, next

### Konfiguracja gita

```shell
git config --global user.name "toumash" # login z githuba
git config --global user.email "mr.toumash@gmail.com" # adres email z githuba
```

## Pierwszy commit

3 stany w których jest każdy plik:

1. Working directory
2. Staging area
3. Git directory

Workflow ![](https://toolsqa.com/wp-content/gallery/git/Git-Push.png)

Cały proces git (raczej na koniec prezentacji jako podsuwmowanie)
![proces](https://qph.fs.quoracdn.net/main-qimg-abc66334a6d43a41b14e2e38898c4e8b)

```shell
mkdir projekt # tworzymy katalog
cd projekt # przelaczamy sie do niego
git init # tworzymy repo
ls -alh # wszystkie pliki, dodatkowy ukryty folder .git
touch README.md # stworzenie pliku REAMDE.md
code README.md # edytujemy edycje pliku w swoim ulubionym programie w tym wypadku VS Code
git add README.md # dodanie pliku na stage
git add . # dodanie wszystkic plikow na stage
git status # status plikow
git commit -m "wiadomosc" # commit, zapis na dysk
git log --oneline --graph # historia commitow na dysku
```

## Branche

```shell
git status # pokazuje aktualny branch
git branch feature/ficzerx # stworzenie brancha
git checkout feature/ficzerx # zmiana brancha
git checkout -b feature/ficzerx # stworzenie i zmiana brancha
git touch innyplik.txt # dodaje kolejny plik na nowym branchu
git add .
git commit -m "dodaje kolejny plik potrzebny do tego ficzera"
git log --oneline --graph # pokazuje nam ladne drzewko zmian na kazdym branchu
```

## Merge

```shell
git status
git checkout feature/ficzerx # wchodzimy na brancha jesli jeszcze nie bylismy
git checkout master
git merge feature/ficzerx
git log --oneline --graph # drzewko powinno wskazywac oba branche w tym samym miejscu
```

Tutaj moze byc juz potrzebny ladniejszy log

```shell
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

potem tylko

```
git lg
```

Zamiast tego
![brzydki gitlog bez kolorow i grafu](https://i.imgur.com/AwZKW.jpg)
będzie to
![ladny gitlog z kolorami i wiecej info](https://i.imgur.com/tSgaU.jpg)

## GitHub

- Do czego służy?
- W jaki sposób wrzucić kod z dysku?
- Dzielimy się na pary Tomasz i Alicja

1. Tworzymy repo na githubie  
   ![image](https://user-images.githubusercontent.com/9840635/54633578-bf769600-4a80-11e9-87e0-c721e0fb7e05.png)  
   ![image](https://user-images.githubusercontent.com/9840635/54633703-05335e80-4a81-11e9-8c1c-e8da63361181.png)

   ![image](https://user-images.githubusercontent.com/9840635/54633784-285e0e00-4a81-11e9-9702-256138b4a0e2.png)

2. Uruchamiamy proponowany przez githuba kod (**przełączamy linka z SSH na HTTPS**)

```shell
git remote add origin <link z githuba> # dodajemy githuba jako server
git push origin master # wgrywamy historie na githuba
```

## Fork Data-Science-PG

Teraz zajmiemy się wspólną pracą nad projektem.
Do tego celu musimy się podzielić na pary.  
**Następnie wybieramy jedną z dwóch postaci:**

- **Tom**
- **Alice**

### Intrukcja dla **Toma**

![prez1](https://user-images.githubusercontent.com/26259455/54634382-64de3980-4a82-11e9-81bb-a60986d419ca.png)

1. Zforkuj repozytorium klikając Fork w prawym górnym rogu panelu repozytorium
2. Zclonuj repozytorium na swój komputer

```shell
git clone <link z githuba>
```

3. Stwórz i przełącz się na nowy branch `feature/lepsze-wyswietlanie`

```shell
git branch feature/lepsze-wyswietlanie
git checkout feature/lepsze-wyswietlanie
```

3. Zacznij implementacje `feature/lepsze-wyswietlanie` zgodnie z kodem poniżej

```python
print('<b>hehehe</b>') # TODO: alicja
```

3. Zacommituj zmiany na brancha

```shell
git add .
git commit -m "zmienia sposob wyswietlania wiadomosci"
git push origin feature/lepsze-wyswietlanie
```

4. Zobacz jak to wyglada w historii za pomocą aliasu, który stworzyliśmy wcześniej.

```shell
git lg
```

## Kolaboracja w dwie osoby - konflikt i rozwiazanie (VS Code albo coś innego)

Tom zmienia zakres liczb na (1,9) i dodaje kolejny elif "My answers are real"

## Kolaboracja w dwie osoby - jedna robi pull requesta a druga review

### Instrukcja dla **Alice**

Znajdź konto Toma na githubie i zrób clone jego sforkowanego repozytorium git-workshop. W tym celu w wybranym repozytorium wybierz opcję "Clone or Download"

![prezi5](https://user-images.githubusercontent.com/26259455/54635590-ce5f4780-4a84-11e9-9025-4333b97f3c76.png)

Następnie w konsoli wejdź do wybranego folderu, gdzie chcesz umieścić to repozytorium i wpisz komendę git clone razem ze skopiowanym linkiem

![prezi4](https://user-images.githubusercontent.com/26259455/54635395-55f88680-4a84-11e9-8e4b-6de0a17a97f4.png)

Utwórz nowy branch, na którym będziesz pracować.

git branch feature/nowa-cecha
git checkout feature/nowa-cecha

![prezi6](https://user-images.githubusercontent.com/26259455/54636810-82fa6880-4a87-11e9-96f6-e2b0afd2b184.png)

Teraz będziemy robić konflikt. Otwórz plik magic-ifs.py w VS Code.
Aliss zmienia zakres liczb na (1,9) i dodaje kolejny elif "My answers are not of any importance"

![prezi7](https://user-images.githubusercontent.com/26259455/54637015-fbf9c000-4a87-11e9-9193-0ba21dc03e7a.png)

Kod ma wyglądać jak wyżej.

git commit -m "Dodaje nowa opcje"
git push origin nowa-cecha ?

## Followup

- Git checksheet ([kliknij aby pobrać](https://www.atlassian.com/dam/jcr:8132028b-024f-4b6b-953e-e68fcce0c5fa/atlassian-git-cheatsheet.pdf))
  [![git cheatsheet](https://wac-cdn.atlassian.com/dam/jcr:e16145b5-176c-4e82-adaf-fb9c65a18164/gitcheat-1200x-top.png?cdnVersion=ld)](https://www.atlassian.com/dam/jcr:8132028b-024f-4b6b-953e-e68fcce0c5fa/atlassian-git-cheatsheet.pdf)
- [git.wtf](https://git.wtf/) - najczęstsze problemy z gitem
- [Git branching by Atlassian](https://www.atlassian.com/git/tutorials/using-branches) - Gałęzie wytłumaczone przez Atlassian

# Contributors

**Made with ♥ in 2019 on github**

- [Alicja](https://github.com/AlicjaDobrzeniecka)
- [Tomi](https://github.com/Toumash)
