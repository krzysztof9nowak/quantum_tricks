#  Zabawa z fal(k)ami, czyli numeryczne rozwiązywanie równania Shrodingera
  
  
##  Wstęp
  
Chyba każdy, kto choć trochę interesuje się fizyką słyszał o pewnym żywo-martwym kocie i o uwięzionych elektronach, które są, lecz nie wiadomo gdzie. Nic w tym dziwnego, cuda mechaniki kwantowej zaprzątają nasze umysły. Zawsze jednak mierził mnie fakt, że opis mikroświata ukryty jest za trudnymi konceptami matematycznymi, a zwykłemu człowiekowi pozostają jednie jakościowe charakteryzacje . Postanowiłem to zmienić, i w sposób dosyć nieudolny, z pomocą komputera, a nie formalizmu matematycznego "pobawić się" elektronami.
  
##  Równanie Shrödingera
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?i&#x5C;hbar%20&#x5C;cfrac{&#x5C;partial&#x5C;psi}{&#x5C;partial%20t}%20=%20&#x5C;left[-&#x5C;cfrac{&#x5C;hbar^2}{2m}&#x5C;cfrac{&#x5C;partial^2}{&#x5C;partial%20x^2}%20+%20V(x,t)&#x5C;right]%20&#x5C;psi"/></p>  
  
  
Równanie Shrödingera jest podstawowym elementem mechaniki kwantowej. Opisuje funkcję falową oraz jej zmiany w czasie. Czym jest funkcja falowa <img src="https://latex.codecogs.com/gif.latex?&#x5C;psi"/>? Nie da się jej zinterpretować wprost, jednak zawiera wszystkie informacje o położeniu i pędzie analizowanej cząstki, które możemy wyłuskać przy użyciu odpowiednich operacji. Kwadrat modułu (w sensie liczb zespolonych) funkcji <img src="https://latex.codecogs.com/gif.latex?|&#x5C;psi|^2"/> opisuje gęstość prawdopodobieństwa, czyli szanse, że cząstka znajduje się w tej okolicy. 
  
Pozostałe literki? <img src="https://latex.codecogs.com/gif.latex?&#x5C;hbar"/> to stała Plancka kreślona V(x,t) to potencjał, opisuję jaką energię potencjalną miałaby cząstka, gdyby znalazła się w tym punkcie i czasie. 
  
  
<img src="https://latex.codecogs.com/gif.latex?&#x5C;psi(x,%20t)"/> zależy od położenia w przestrzeni i czasu, przyjmuje natomiast wartości zespolone. 
  
##  Jak to rozwiązać?
  
Najprostsze do rozwiązania są problemy stacjonarne, to znaczy takie, w których moduł funkcji nie zmienia się z upływem czasu, a funkcja drga niczym fala stojąca na sznurku. Wtedy równanie przyjmuje taką postać:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?E%20&#x5C;psi%20=%20&#x5C;left[-&#x5C;cfrac{&#x5C;hbar^2}{2m}&#x5C;cfrac{&#x5C;partial^2}{&#x5C;partial%20x^2}%20+%20V(x)&#x5C;right]%20&#x5C;psi"/></p>  
  
[wyprowadzenie](https://tutaj_wyprowadzenie_dodaj.com )
  
Równanie wygląda troszeczkę przyjmniej, jednak wciąż niezbyt wiadomo co można z nim zrobić. Z odsieczą przyjdzie nam kilka matematycznych sztuczek. Wyobraźmy sobie, że <img src="https://latex.codecogs.com/gif.latex?&#x5C;psi(t)"/> jest wektorem o nieskończonej liczbie wymiarów (ściślej mówiąc, jest w przestrzeni Hilberta), a każdy wymiar wektora opisuje jeden punkt w przestrzeni funkcji. Rysunek poniżej jest jedynie poglądowy, gdzyż pomija fakt, że <img src="https://latex.codecogs.com/gif.latex?&#x5C;psi"/> jest zespolone, a wektor ma continuum wymiarów. 
![nibywektor](pseudo_Hilbert.png )
  
Taka wektorowa interpretacja pozwoli nam na stosowanie metod algebry liniowej. Niestety komputery krzemowe nie pojmują nieskończoności, dlatego zamiast martwić się continuum wymiarowym wektorem, wygodnie podzielimy przestrzeń na <img src="https://latex.codecogs.com/gif.latex?n=1000"/> odcinków.  
  
Chcielibyśmy myśleć o <img src="https://latex.codecogs.com/gif.latex?&#x5C;hat{H}%20=%20&#x5C;left[-&#x5C;cfrac{&#x5C;hbar^2}{2m}&#x5C;cfrac{&#x5C;partial^2}{&#x5C;partial%20x^2}%20+%20V(x)&#x5C;right]"/> jak o macierzy, która działa jako operator (zwany operatorem Hamiltona) na wektorze <img src="https://latex.codecogs.com/gif.latex?&#x5C;psi"/>. Problem jest jendak jak sprowadzić <img src="https://latex.codecogs.com/gif.latex?&#x5C;frac{&#x5C;partial^2}{&#x5C;partial%20x^2}"/> do macierzy? Rozważmy jeden punkt w przestrzeni. Obserwując różnice Korzystając z szeregu Taylora, możemy wyliczyć następującą postać aproksymacji w punkcie x:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;frac{&#x5C;partial^2&#x5C;psi}{&#x5C;partial%20x^2}(x)%20&#x5C;approx%20&#x5C;frac{&#x5C;psi(x+&#x5C;Delta%20x)%20-2&#x5C;psi(x)%20+%20&#x5C;psi(x-&#x5C;Delta%20x)%20}{(&#x5C;Delta%20x)^2}"/></p>  
,gdzie <img src="https://latex.codecogs.com/gif.latex?&#x5C;Delta%20x%20=%20&#x5C;cfrac{x_n%20-%20x_1}{n}"/>.
  
Zauważmy, że są to przekształcenia liniowe, dlatego możemy wpisać współczynniki w odpowiednie miejsca macierzy
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;frac{&#x5C;partial^2}{&#x5C;partial%20x^2}%20=%20&#x5C;cfrac{1}{(&#x5C;Delta%20x)^2}&#x5C;begin{pmatrix}2%20&amp;%20-5%20&amp;%204%20&amp;%20-1%20&amp;%200%20&amp;%200%20&amp;%20&#x5C;dots%20&amp;%200&#x5C;&#x5C;1%20&amp;%20-2%20&amp;%201%20&amp;%200%20&amp;%200%20&amp;%200%20&amp;%20&#x5C;dots%20&amp;%200&#x5C;&#x5C;0%20&amp;%201%20&amp;%20-2%20&amp;%201%20&amp;%200%20&amp;%200%20&amp;%20&#x5C;dots%20&amp;%200&#x5C;&#x5C;0%20&amp;%200%20&amp;%201%20&amp;%20-2%20&amp;%201%20&amp;%200%20&amp;%20&#x5C;dots%20&amp;%200&#x5C;&#x5C;0%20&amp;%200%20&amp;%200%20&amp;%201%20&amp;%20-2%20&amp;%201%20&amp;%20&#x5C;dots%20&amp;%200&#x5C;&#x5C;&#x5C;vdots&#x5C;end{pmatrix}_{n&#x5C;times%20n}"/></p>  
  
  
Taka macierz nazywana jest Hamiltonianem (operatorem Hamiltona) i jest oznaczna H. Tralala liczy energie falki.
  
Podsumowując, chcemy rozwiązać równanie <img src="https://latex.codecogs.com/gif.latex?E%20&#x5C;psi%20=%20H%20&#x5C;psi"/>, gdzie <img src="https://latex.codecogs.com/gif.latex?H"/> to macierz, E skalar, a <img src="https://latex.codecogs.com/gif.latex?&#x5C;psi"/> wektor. Czy to czegoś nie przypomina? Ależ oczywiście, jest to problem znajdowania wektorów i wartości własnych macierzy, który można spotkać na wykładzie z algebry liniowej. Szczerze mówiąc, byłem ogromnie uradowany, że tak pozornie nudny koncept, który niedawno poznałem, okaże się użyteczny w takim miejscu. 
  
Na szczęście wyznaczanie wartości własnych jest całkiem popularnym problem, także nie musimy się nim martwić. Sprowadziliśmy problem do zagadnienia już rozwiązanego, a czyż nie o to w życiu chodzi?
  
##  Studnia potencjału
  
Najprostszy problem fizyki kwantowej, który można stosunkowo łatwo rozwiązać, nawet metodami analitycznymi to elektron umieszczony w tak zwanej studni potencjału. Studnia potencjału to potencjał, taki, że na pewnym przedziale przyłożony potencjał zewnętrzny jest równy zeru, poza nim natomiast wynosi on nieskończoność. Elektron jest spułapkowany "na dnie studni", gdyż jego energia kinetyczna i potencjalnie jest niewystarczajacą do przekroczenia nieskończenie wysokiej bariery. Poza teoretycznym rozważaniem, takiem układem mogą być dwie płyty oddalone o (naście wstaw tutaj jakąś liczbę nm).
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;hbar%20=%20m%20=%201"/></p>  
  
  
  
![1](1_finite_well.png )
  
##  Upływ czasu
  
A co gdybyśmy chcieli zobaczyć nasz elektron w ruchu? Możemy skorzystać z metody Cranka-Nicolson. Znając obecną wartość <img src="https://latex.codecogs.com/gif.latex?&#x5C;psi(t)"/> możliwe jest wyliczenie przybliżonej wartości w momencie <img src="https://latex.codecogs.com/gif.latex?t+&#x5C;Delta%20t"/>
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;left(1-&#x5C;frac{H%20&#x5C;Delta%20t}{2i&#x5C;hbar}&#x5C;right)&#x5C;psi(t+&#x5C;Delta%20t)%20=%20&#x5C;left(1+&#x5C;frac{H%20&#x5C;Delta%20t}{2i&#x5C;hbar}&#x5C;right)&#x5C;psi(t)"/></p>  
  
  
  
  
##  Wolna cząsteczka i zasada nieoznaczoności
  
Rozważmy elektron poruszający się z pewną prędkością w prawo, bez oddziaływań zewnętrznych. Zadamy go następującym pakietem:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;psi(x,%20t=0)%20=%20e^{-&#x5C;dfrac{1}{2}&#x5C;left(&#x5C;dfrac{x-x_0}{&#x5C;sigma_x}&#x5C;right)^2}e^{-ikx},"/></p>  
 gdzie <img src="https://latex.codecogs.com/gif.latex?x_0"/> to położenie początkowe, <img src="https://latex.codecogs.com/gif.latex?k"/> liczba falowa, <img src="https://latex.codecogs.com/gif.latex?&#x5C;sigma_x"/> niepewność położenia początkowego. W jednym przypadku weźmy <img src="https://latex.codecogs.com/gif.latex?&#x5C;sigma_x%20=%200.1"/>,
![2](2_free_01.gif )
a w drugim <img src="https://latex.codecogs.com/gif.latex?&#x5C;sigma_x%20=%200.2"/>.
![2](2_free_02.gif )
  
W obu przypadkach wraz z upływem czasu niepewność położenia wzrasta. Jest to spowodowane tym, że zgodnie z zasadą nieoznaczoności pęd (więc również prędkość) nie może być dokładnie znana.
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;sigma_p%20&#x5C;geq%20&#x5C;cfrac{&#x5C;hbar}{2&#x5C;sigma_x}"/></p>  
  
Im dokładniej znamy położenie <img src="https://latex.codecogs.com/gif.latex?&#x5C;sigma_x"/> tym większą niepewność <img src="https://latex.codecogs.com/gif.latex?&#x5C;sigma_p"/>. Co za tym idzie wierzchołek na górnym wykresie ulega znacznie szybszemu spłaszczeniu, bo zawiera dokładniejszą informację o pozycji. Pod koniec symulacji oba wykresy niemalże zrównuje się, ponieważ zawierały taką samą, maksymalną ilość informacji. Warto podkreślić, że takie zachowanie nie jest spowodowane jakąkolwiek niedoskonałością fizycznych pomiarów, bądź symulacji, lecz jest elementem działania wszechświata, który został zakodowany w równaniu Shrödingera.
  
##  Atom wodoru w 3D
  
  
##  Eigenstany
  
- Rozkład na stany
- eigenvalues to Energie
  
##  Kody
  
Kod źródłowy do wykonania obliczeń jest dostępny na [moim GitHubie](https://github.com/krzysztof9nowak/quantum_tricks ).
  
##  Bibliografia
  
Włodzimierz Salejda 
  
https://www.caam.rice.edu/software/ARPACK/UG/node45.html
  
https://dantoudai.wordpress.com/2020/06/07/schrodingers-python-2/
  
Quatnum Mechanics, B.H. Bransden & C.J. Joachain
  
http://www.physics.utah.edu/~detar/phycs6730/handouts/crank_nicholson/crank_nicholson/
  
https://jakevdp.github.io/blog/2012/09/05/quantum-python/
  