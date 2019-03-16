# Git Tutorial

## Checklist

Do sprawdzenia czy kazda z tych kwestii jest dostatecznie dobrze opisana

-   działanie
-   instalacja
-   praca samemu
-   praca w grupach
-   praca na featurach
-   profil github

## Narzędzia

-   VS Code

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

-   Do czego służy?
-   W jaki sposób wrzucić kod z dysku?
-   Dzielimy się na pary Tomasz i Alicja

1. Tworzymy repo na github
2. Dodajemy githuba jako server

```shell
git remote add origin <link z githuba>
```

3. Wgrywamy historie na githuba

```shell
git push origin master # branch ktory chcemy wrzucic na serwer
```

## Fork Data-Science-PG

(zmiana i commit samemu)

## Kolaboracja w dwie osoby - konflikt i rozwiazanie (VS Code albo coś innego)

## Kolaboracja w dwie osoby - jedna robi pull requesta a druga review

## Followup

-   Git checksheet ([kliknij aby pobrać](https://www.atlassian.com/dam/jcr:8132028b-024f-4b6b-953e-e68fcce0c5fa/atlassian-git-cheatsheet.pdf))
    [![git cheatsheet](https://wac-cdn.atlassian.com/dam/jcr:e16145b5-176c-4e82-adaf-fb9c65a18164/gitcheat-1200x-top.png?cdnVersion=ld)](https://www.atlassian.com/dam/jcr:8132028b-024f-4b6b-953e-e68fcce0c5fa/atlassian-git-cheatsheet.pdf)
-   [git.wtf](https://git.wtf/) - najczęstsze problemy z gitem
-   [Git branching by Atlassian](https://www.atlassian.com/git/tutorials/using-branches) - Gałęzie wytłumaczone przez Atlassian

# Contributors

**Made with ♥ in 2019 on github**

-   [Alicja](https://github.com/AlicjaDobrzeniecka)
-   [Tomi](https://github.com/Toumash)
