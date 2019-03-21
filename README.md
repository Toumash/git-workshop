# Git Tutorial

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

<!-- Cały proces git (raczej na koniec prezentacji jako podsuwmowanie)
![proces](https://qph.fs.quoracdn.net/main-qimg-abc66334a6d43a41b14e2e38898c4e8b) -->

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

Dodaj Alice jako kontrybutora.
Jak dodać kontrybutora? Ilustracja poniżej

Repozytorium, które chcemy współdzielić -> Settings -> Collaborators -> wpisanie loginu osoby, którą chcemy dodać
-> Add Collaborator -> Druga osoba musi poprzez e-maila potwierdzić kolaborację

![image](https://user-images.githubusercontent.com/26259455/54761520-8827f680-4bf2-11e9-944f-05b52e22c17e.png)

![image](https://user-images.githubusercontent.com/26259455/54761640-c0c7d000-4bf2-11e9-9680-91077d910820.png)


![prez1](https://user-images.githubusercontent.com/26259455/54634382-64de3980-4a82-11e9-81bb-a60986d419ca.png)

1. Zforkuj repozytorium klikając Fork w prawym górnym rogu panelu repozytorium
2. Zclonuj repozytorium na swój komputer

```shell
git clone <link z githuba>
```

3. Stwórz i przełącz się na nowy branch `feature/wiecej-opcji`

```shell
git branch feature/wiecej-opcji
git checkout feature/wiecej-opcji
```

4. Zacznij implementacje `feature/wiecej-opcji` zgodnie z kodem poniżej

Zmienia zakres liczb na (1,9) i dodaje kolejny elif "My answers are real"

![image](https://user-images.githubusercontent.com/9840635/54718996-11d8b500-4b5c-11e9-81f2-1f5fdbbd80f5.png)

5. Zacommituj zmiany na brancha

```shell
git add .
git commit -m "zmienia sposob wyswietlania wiadomosci"
git push origin feature/wiecej-opcji
```

6. Zobacz jak to wyglada w historii za pomocą aliasu, który stworzyliśmy wcześniej.

```shell
git lg
```

7. Wejdz na mastera jako pierwszy (przed Alicją) i zmerguj zmiany

```shell
git checkout master
git merge feature/wiecej-opcji
git push origin master
```

8. Pomóż w razie potrzeby swojemu partnerowi/partnerce

9. Po ukończeniu wszystkiego `git lg` powinien na obu kontach wygladac podobnie do tego

![image](https://user-images.githubusercontent.com/9840635/54719877-51080580-4b5e-11e9-837d-a347092ea377.png)

## Kolaboracja w dwie osoby - konflikt i rozwiazanie (VS Code albo coś innego)

Tom zmienia zakres liczb na (1,9) i dodaje kolejny elif "My answers are real"
Alice zmienia zakres liczb na (1,9) i dodaje kolejny elif "My answers are not of any importance"

### Instrukcja dla **Alice**

Znajdź konto Toma na githubie i zrób clone jego sforkowanego repozytorium git-workshop. W tym celu w wybranym repozytorium wybierz opcję "Clone or Download"

![prezi5](https://user-images.githubusercontent.com/26259455/54635590-ce5f4780-4a84-11e9-9025-4333b97f3c76.png)

Następnie w konsoli wejdź do wybranego folderu, gdzie chcesz umieścić to repozytorium i wpisz komendę git clone razem ze skopiowanym linkiem

![prezi4](https://user-images.githubusercontent.com/26259455/54635395-55f88680-4a84-11e9-8e4b-6de0a17a97f4.png)

Teraz będziemy robić konflikt.

Utwórz nowy branch, na którym będziesz pracować.

```shell
git branch feature/nowa-opcja
git checkout feature/nowa-opcja
```

Otwórz plik magic-ifs.py dowolnym edytorze. Dodaj zakres liczb na (1,9) i dodaje kolejny elif "My answers are not of any importance"

![prezi7](https://user-images.githubusercontent.com/26259455/54637015-fbf9c000-4a87-11e9-9193-0ba21dc03e7a.png)

Kod ma wyglądać jak wyżej.

Następnie wracamy do konsoli i wpisujemy:

![prezi8](https://user-images.githubusercontent.com/26259455/54715477-ddf99180-4b53-11e9-873b-3b2e0d05af3c.png)

A następnie

```shell
git push origin feature/nowa-opcja
```

Jeżeli druga osoba zrobiła commit brancha i merge to powinien powstać konflikt jak poniżej

![prezi10](https://user-images.githubusercontent.com/26259455/54719220-9fb4a000-4b5c-11e9-8112-0fcd689befa6.png)

aby otworzyc VS Code

```shell
code .
```

Wybierz opcję Accept Both Changes i zmien jak ponizej

![image](https://user-images.githubusercontent.com/26259455/54719668-c1625700-4b5d-11e9-8778-b900f0d9776c.png)

I ponownie w konsoli

```shell
git add .
git commit -m "Rozwiazuje konflikt"
git push origin master
```

Po ukończeniu wszystkiego `git lg` powinien na obu kontach wygladac podobnie do tego

![image](https://user-images.githubusercontent.com/9840635/54719877-51080580-4b5e-11e9-837d-a347092ea377.png)

## Followup

- Git checksheet ([kliknij aby pobrać](https://www.atlassian.com/dam/jcr:8132028b-024f-4b6b-953e-e68fcce0c5fa/atlassian-git-cheatsheet.pdf))
  [![git cheatsheet](https://wac-cdn.atlassian.com/dam/jcr:e16145b5-176c-4e82-adaf-fb9c65a18164/gitcheat-1200x-top.png?cdnVersion=ld)](https://www.atlassian.com/dam/jcr:8132028b-024f-4b6b-953e-e68fcce0c5fa/atlassian-git-cheatsheet.pdf)
- [git.wtf](https://git.wtf/) - najczęstsze problemy z gitem
- [Git branching by Atlassian](https://www.atlassian.com/git/tutorials/using-branches) - Gałęzie wytłumaczone przez Atlassian

# Contributors

**Made with ♥ in 2019 on github**

- [Alicja](https://github.com/AlicjaDobrzeniecka)
- [Tomi](https://github.com/Toumash)
