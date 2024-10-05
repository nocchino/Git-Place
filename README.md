# Git-Place
**English**

Git-Place is a project inspired by [r/place di Reddit](https://www.reddit.com/r/place/). **Everyone can partecipate** edit one or more pixels of a white canvas of 500x500 pixels.

### Prerequisites
- Python3.x
- Pillow (for image manipulation)

### How to install Pillow
run the command:

```bash
   pip install Pillow
   ```
## How to participate
**1. Fork the project:**

**2. Create a New Branch:**

**3. Edit:**
In the terminal run the command:
```bash
   python3 main.py
   ```
After run, the programm will print the position of the first white pixel to edit (ex (125,35)).

*You can edit any pixels you want in the range of 0-499*

After choosing which pixel to change open main.py and edit
'''python
   canvas.putpixel((x,y),(r,g,b))
'''
where x and y are the coordinate and rgb the chosen color.

After choosing the pixel to draw, remove the "#" from canvas.save("image.png") and run the program again to see the changes in image.png (*the change will be only one pixel so it will be difficult to see the change*)

**4. Raise a Pull Request:**

**Current Canvas:**



![photo](https://github.com/nocchino/Git-Place/blob/main/image.png)


Feel free to edit and improve ReadME.md


---
# Git-Place
**Italiano**

Git-Place è un progetto ispirato ad [r/place di Reddit](https://www.reddit.com/r/place/). **Chiunque può partecipare** modificando uno o più pixel di una tela bianca di dimensione 500x500 pixel.

### Prerequisiti
- Python3.x
- Pillow (per la manipolazione delle immagini)

### Come installare Pillow
esegui il comando:

```bash
   pip install Pillow
   ```

## Come partecipare

**1. Fork the project:**

**2. Create a New Branch:**

**3. Edit:**
Nel terminale esegui il comando 
```bash
   python3 main.py
   ```
dopo averlo eseguito il programma ti dirà la posizione del primo pixel bianco da modificare (esempio (125,35)). 
*Puoi modificare qualsiasi pixel tu voglia (nel range da 0 a 499)*


Dopo aver deciso quale pixel cambiare apri main.py e modifica 
'''python
   canvas.putpixel((x,y),(r,g,b))
'''
dove x e y sono le coordinate e rgb il colore scelto come valore RGB.

Dopo aver scelto il pixel da disegnare togli il "#" da canvas.save("image.png") ed esegui il programma di nuovo per vedere le modifiche di image.png (*la modifica sarà di un solo pixel perciò sarà difficile vedere il cambiamento*)

**4. Raise a Pull Request:**

Sentitevi liberi di migliorare il file ReadME.md
