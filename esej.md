# Zabawa z fal(k)ami, czyli numeryczne rozwiązywanie równania Shrodingera

## Wstęp
O tym, że chciałem jakieś ilościowe wyniki, nie jedynie jakościowe bajki
O falowości materii i kontekście historycznym

## Równanie Shrödingera
$$i\hbar \cfrac{\partial\psi}{\partial t} 
= \left[-\cfrac{\hbar^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x,t)\right] \psi$$

Co my tu właściwie mamy. Centralnym elementem całego problemu jest funkcja falowa $\psi(x, t)$. W ogólności zależy ona od położenia oraz czasu, przyjmuje ona natomiast wartości zepsolone. Jak jednak $\psi$ ma się do położenia analizowanej cząsteczki? 

## Studnia potencjału
Najprostszy problem fizyki kwantowej, który można stosunkowo łatwo rozwiązać, nawet metodami analitycznymi to elektron umieszczony w tak zwanej studni potencjału. Studnia potencjału to potencjał, taki, że na pewnym przedziale przyłożony potencjał zewnętrzny jest równy zeru, poza nim natomiast wynosi on nieskończoność. Elektron jest spułapkowany "na dnie studni", gdyż jego energia kinetyczna i potencjalnie jest niewystarczajacą do przekroczenia nieskończenie wysokiej bariery. Poza teoretycznym rozważaniem, takiem układem mogą być dwie płyty oddalone o (naście wstaw tutaj jakąś liczbę nm).

$$ \hbar = e = m = 1$$
Problem studni można rozważać jako niezależny od upływu czasu, wtedy równanie przyjmuje następującą postać:
$$ E \psi = \left[-\cfrac{\hbar^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x)\right] \psi$$
Myślę, że materią tej pracy nie jest przedstawienie dokładnych wyprowadzeń, lecz można znaleźć je tutaj: [link do ref](https://google.com).

Równanie wygląda troszeczkę przyjmniej, jednak wciąż niezbyt wiadomo co można z tym zrobić. Z odsieczą przyjdzie nam kilka matemateycznych konceptów. Okazuje się, że $\psi$ można utożsamiać z wektorem o nieskończonej liczbie wymiarów (ściślej mówiąc z wektorem z przestrzeni Hilberta). Jeżeli $\psi$ jest wektorem to czym jest $\left[-\cfrac{\hbar^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x)\right]$? Otóż jest to macierz kwadratowa, 

Jak możemy policzyć pochodną dla dyskretnej funkcji? Możemy użyc pierwszych wyrazów szeregu Talora, lecz na odwrót niż zwykle. Przybliżenia pierwszego stopnia drugiej pochodnej wyglądają następujaco:

$$\frac{\partial^2\psi}{\partial x^2}(x) = \frac{1\psi(x+\Delta x) -2\psi(x) + 1\psi(x-\Delta x) }{(\Delta x)^2}$$

$$\frac{\partial^2}{\partial x^2} = \begin{pmatrix}
2 & -5 & 4 & -1 & 0 & 0 & \dots & 0\\
0 & 1 & -2 & 1 & 0 & 0 & \dots & 0\\
0 & 0 & 1 & -2 & 1 & 0 & \dots & 0\\
0 & 0 & 0 & 1 & -2 & 1 & \dots & 0\\
\vdots
\end{pmatrix}_{N\times N}$$

Taka macierz nazywana jest Hamiltonianem (operatorem Hamiltona) i jest oznaczna H. Tralala liczy energie falki.

Niestety komputer krzemowe nie radzą sobie najlepiej z nieskończonościami, dlatego będziemy musieli zadowolić się aproksymacją przez wektor o $n=1000$ wymiarach. 

Podsumowując, chcemy rozwiązać równanie $E \psi = H \psi$, gdzie $H$ to macierz, E skalar, a $\psi$ wektor. Czy to czegoś nie przypomina? Ależ oczywiście, jest to problem znajdowania wektorów i wartości własnych macierzy, który można spotkać na wykładzie z algebry liniowej. Szczerze mówiąc, byłem ogromnie uradowany, że tak pozornie nudny koncept, który niedawno poznałem, okaże się użyteczny w takim miejscu. 

Na szczęście wyznaczanie wartości własnych jest całkiem popularnym problem, także nie musimy się nim martwić. Sprowadziliśmy problem do zagadnienia już rozwiązanego, a czyż nie o to w życiu chodzi?

## Atom wodoru w 3D

## Ewolucja w czasie
## Eigenstany
- Rozkład na stany
- eigenvalues to Energie


Włodzimierz Salejda 