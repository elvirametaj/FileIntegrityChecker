## File Integrity Checker
### Përshkrimi
File Integrity Checker është një skript Python i dizajnuar për të verifikuar integritetin e file-ve duke llogaritur hash-et MD5 dhe SHA-256. Ky skript lexon një file të specifikuar nga përdoruesi dhe llogarit shenjat hash për të siguruar që përmbajtja e file-s nuk është ndryshuar ose korruptuar.

### Përdorimi
Për të përdorur skriptin:
Thjesht ekzekutoni skriptin duke specifikuar path-in e skriptit dhe path-in e file-s për të cilën do të llogariten shenjat:
python ./.venv/FileIntegrityChecker.py ./.venv/file.txt

#### Argumentet
<./.venv/FileIntegrityChecker.py>: Path-i për skriptin për të ekzekutuar.
<./.venv/file.txt>: Path-i për file-n për të cilën do të llogariten shenjat MD5 dhe SHA-256.

### Shembulli i Skriptit
Skripti merr path-in e file-s si një argument dhe pastaj llogarit shenjat MD5 dhe SHA-256 për atë file. Nëse ndodh ndonjë problem gjatë leximit të file-s, shfaqet një mesazh gabimi për përdoruesin

### Algoritmet e Hash-it
#### MD5
MD5 (Message Digest Algorithm 5) është një algoritëm hash-i 128-bit që përdoret gjerësisht për të verifikuar integritetin e të dhënave. Edhe pse është i shpejtë dhe efikas, MD5 nuk është i sigurt ndaj sulmeve të kolizionit dhe prandaj nuk rekomandohet për përdorime të sigurisë së lartë.

### SHA-256
SHA-256 (Secure Hash Algorithm 256-bit) është pjesë e familjes SHA-2 të algoritmeve të hash-it dhe ofron një nivel më të lartë sigurie në krahasim me MD5. SHA-256 prodhon një shenjë hash 256-bit dhe përdoret gjerësisht në aplikacione që kërkojnë siguri të lartë të të dhënave, siç janë nënshkrimet digjitale dhe verifikimi i certifikatave.

Autorët
--- [Elvira Metaj](https://github.com/elvirametaj)
--- [Ema Zeqiri](https://github.com/emazech)
--- [Elonita Krasniqi](https://github.com/elonitakrasniqi1)
