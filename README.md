# Munchboka

## Hva er Munchboka
En digital lærebok i matematikk 1T utviklet for læreplanen i LK20 ut ifra undervisningen vi utfører ved Edvard Munch videregående skole. Boka er utviklet for å først og fremst være en nettside og ikke et statisk læremiddel som en PDF eller en trykt bok. Dette gir oss muligheten til å bruke interaktive vinduer for programmering, CAS og Geogebra direkte i boka, legge inn fasiter og løsningsforslag, hint og så videre. I tillegg er boka utviklet med tanke på at den skal være lett tilgjengelig for alle og at den skal være åpen kildekode slik at alle kan bruke innholdet, kopiere og modifisere det til eget bruk uten å måtte spørre om lov. Se mer om dette under [Lisens](#lisenser) hvis du kunne tenke deg å gjøre dette.

Matematikk 1T i LK20 kan deles inn i to hovedområder:
1. Funksjoner
2. Trigonometri

Hvis du har studert matematikk, så vet du at funksjoner uten tvil er den viktigste ideen noen gang oppfunnet.
Boka har derfor som mål å i stor grad dekke læreplanen i LK20 ved å gjøre funksjoner som den overordnede ideen bak teorien der algebraiske metoder, likninger, ulikheter, likningssystemer, optimeringsproblemer, algoritmisk tenking og programmering knyttes med direkte til funksjoner hele veien. Fremfor å se på likninger i isolasjon, ser vi på det som å stille spørsmål om funksjoner. Det betyr at det ikke finnes et eget kapittel for hvert av disse underordnede temaene, men at de er innflettet i delkapitler der en bestemt funksjonsstype er i fokus.  Dette gir en syklisk tilnærming til temaene der de underordnede temaene gjentas igjen og igjen.

## Hvordan bruke boka
Boka i sin helhet ligger på [munchboka.no](https://munchboka.no). Du kan bruke boka direkte i nettleseren din uten videre. 

Hvis du ønsker å bruke lage din egen versjon av boka med utgangspunkt i innholdet vårt her, kan du lage et kopi av repoet ut ifra en **template** og modifisere innholdet til egen bruk – men du må følge lisensene som prosjektet er underordnet. Se mer om dette under [Lisens](#lisenser). Dette er den anbefalte fremgangsmåten siden den inkluderer alle nødvendige filer inkludert hvordan man får Github til å bygge boka automatisk og publisere den på Github Pages. Hvis du trenger hjelp til dette, legg inn et issue i repoet så får du hjelp. 

For mer om hvordan du lager spesifikt innhold i boka se [HOWTOWRITE.md](HOWTOWRITE.md).

## Lisenser

### Kildekode

Kildekoden til dette prosjektet er lisensiert under **GNU Affero General Public License (AGPL-3.0)**. Dette sikrer at alle avledede verk og modifikasjoner av kodebasen må forbli åpen kildekode. Koden kan ikke brukes til kommersielle formål. Du kan lese hele lisensen [her](https://www.gnu.org/licenses/agpl-3.0.en.html). Denne lisensen gjelder alle filer i prosjektet som *ikke* ligger i `book`-mappen. Det vil si at alle filer i `book`-mappen er unntatt fra denne lisensen og er lisensiert under en annen lisens (se nedenfor).

For mer informasjon, se [LICENSE](LICENSE)-filen i rotmappen til repositoriet.

### Lærebokinnhold

Lærebokinnholdet, inkludert tekst, figurer, oppgaver, animasjoner og så videre, er lisensiert under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**. Denne lisensen tillater andre å dele, remikse og tilpasse innholdet så lenge de gir attribusjon. Det lisensen **ikke** tillatter er å bruke innholdet til kommersielle formål eller å dele videre under samme lisens. Du kan lese hele lisensen [her](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode). Denne lisensen gjelder alle filer i `book`-mappen.

For mer informasjon, se [LICENSE_CONTENT.md](LICENSE_CONTENT.md)-filen.


