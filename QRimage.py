from amzqr import amzqr
import os
import usesleft
Filename = usesleft.usesleft()
Filename = str(Filename) + '.png'
Link = str(input("Vul hier een link in of tekst, afbeelding adres om te displayen: "))
version, level, qr_name = amzqr.run(
    words=Link,
    version=10,
    level='M',
    picture='logo.png',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name=Filename,
    save_dir=os.getcwd()
)

