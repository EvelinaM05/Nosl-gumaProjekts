# Noslēguma Projekts 
***Projekta mērķis*** ir izstrādāt webscraping tehnoloģiju datu ievākšanai no Zalando.lv tiešsaites platformas apģērba un citu lietu iegādei. Izmantojot web seb scraping ir plānots ievākt informāciju par izpārdšonā esošām precēm. 
Tiks izmantota ievade un izvade, sekojoši lietotājam būs iespēja ievadīt vēlamo preci(t-krekls, kleita, svārki u.c.). Rīks pieprasīs un apstrādās Zalando.lv lapas saturu, meklējot pieprasītās preces. Tiks ievākti dati par preces nosaukumu, cenu, kā arī saiti uz preci. Ievāktie dati tiks sakārtoti augošā secībā pēc cenas un tiks saglabāti tabulā, vieglākai pārskatīšanai.

Vispirms lietotājs izvēlas kategoriju -  1.  Sieviete/2.Vīrietis/3.Bērns, un ievada atbilstošo kategorijas numuru (1/2/3). Nākamais solis, lietotājs ievada vēlamo preci, piemēram, kleita.
Tad atbilstoši kategorijai, skripts savāks, sakārtos un apstrādās informāciju no atbilstošās izpārdošanas sadaļas - "1": "https://www.zalando.lv/sievietem-izpardosana/?sale=true",
"2": "https://www.zalando.lv/viriesiem-izpardosana/?sale=true", 
"3":"https://www.zalando.lv/berniem-izpardosana/?sale=true" - un beigās informācija tiks atspoguļota CSV tabulā. 
