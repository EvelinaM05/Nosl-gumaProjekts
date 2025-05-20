# Noslēguma Projekts "Pārtikas cenu uzskaites sistēma"

### Projekta mērķis ###

Šī projekta mērķis ir izveidot viegli saprotamu rīku, kas palīdz lietotājam sekot līdzi pārtikas produktu cenu izmaiņām laika gaitā. Mūsu programma ļauj saglabāt cenas, analizēt tās statistiski, kā arī importēt/eksportēt datus uz Excel. Mērķis ir palīdzēt labāk plānot pārtikas budžetu un tādā veidā atvieglot ikdienu.

### Funkcionalitāte ###

Mūsu programma piedāvā šādas opcijas:

•⁠  ⁠Pievienot produkta cenu un datumu;

•⁠  ⁠Apskatīt produktu sarakstu ar aktuālām cenām;

•⁠  ⁠Uzstādīt cenu brīdinājumus;

•⁠  ⁠Eksportēt/importēt datus uz/no Excel;

•⁠  ⁠Veikt statistiku ar minimālo, maksimālo un vidējo cenu;

•⁠  ⁠Dzēst produktus no datubāzes;

•⁠  ⁠Automātiski atgādināt par datu ievadi katru dienu, kas mūsu gadījumā ir 18:30, bet to var mainīt.



### Izmantotās datu struktūras un algoritmi ###

**Datu struktūras:**

•⁠  ⁠⁠dict⁠- saglabā katru produktu kā atslēgu ar vērtību, tātad sarakstu ar cenas ierakstiem;

•⁠  ⁠⁠list- saraksts ar vairākiem ierakstiem katram produktam;

•⁠  ⁠Ieraksti- ir vārdnīcas ar ⁠price ⁠un ⁠date ⁠laukiem.


**Algoritmi:**

•⁠  ⁠Meklēšana- tiek izmantota lineāra pārbaude pēc produkta nosaukuma. Šis algoritms parādās piemēram: set_alert() ;

•⁠  ⁠Šķirošana- cenu grafiki tiek balstīti uz datumu šķirošanas algoritmiem. Šis ir redzams piemēram: price_chart() ;

•⁠  ⁠Statistikas aprēķins- ⁠ min() ⁠, ⁠ max() ⁠, ⁠ sum() ⁠ un ⁠ len() ⁠ funkcijas. Šis ir redzams statistics() .



### Izmantotās bliotēkas ###

•⁠  ⁠json- izmanto datu ielādei un saglabāšanai .json formātā. Tas ļauj viegli pārveidot vārdnīcu uz failu un otrādāk;

•  os– nodrošina failu sistēmas pārbaudi, piemēram, vai eksistē konkrētie dati pirms to ielādes;

•  datetime– ļauj iegūt tagadējo datumu un laiku, kuru izmanto kā "zīmogu" katram ierakstam;

•  pandas– dod iespēju importēt un eksportēt datus no/uz Excel failiem, kā arī strukturēti apstrādāt datus;

•  matplotlib.pyplot– to izmanto cenu pārmaiņu attēlošanai grafikā, kas ļauj lietotājam visu ērtāk pārskatīt;

•  tabulate– palīdz izvadīt tabulu terminālī ērtā un formatētā veidā;

•  schedule– ļauj izplānot regulārus uzdevumus, kas mūsu gadījumā ir atgādinājumi katru dienu 18:30;

•  time– ir nepieciešams, lai palaistu ciklu, kas seko līdzi ieplānotajiem uzdevumiem- schedule funkcionalitātei.
