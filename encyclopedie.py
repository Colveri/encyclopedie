# créé par Colveri le 17/11/22
# Dernière màj par Colveri le 14/03/23

# changelog (à partir du 13/05/23)
# Maintenant accessible depuis GitHub (https://github.com/e-psi-lon/encyclopedie)
# Version orignale (dépréciée, nouvelle version dans encyclopedie_rework.py)
# IMPORTS MODULES

import math
import time
from ion import *
from kandinsky import fill_rect as drawRect, draw_string as drawTxt


# Pour faire une meilleure interface
def kd(key):
    if keydown(key):
        while keydown(key):
            pass
        return True
    return False


def menu(x, y, elements, col=(0, 0, 0), bg_col=(255, 255, 255)):
    kd(4)
    el_size, select, txt_size, draw = 25, 0, [0 for _ in range(len(elements))], 1
    while True:
        if kd(1):
            draw = 1
            select = max(0, select - 1)
        if kd(2):
            draw = 1
            select = min(len(elements) - 1, select + 1)
        if kd(0):
            draw = 1
            elem_type = elements[select][0]
            if elem_type == "sld":
                elements[select][-1] = max(elements[select][-1] - 1, elements[select][2][0])
            if elem_type == "lst":
                elements[select][-1] = max(elements[select][-1] - 1, 0)
        if kd(3):
            draw = 1
            elem_type = elements[select][0]
            if elem_type == "sld":
                elements[select][-1] = min(elements[select][-1] + 1, elements[select][2][1])
            if elem_type == "lst":
                elements[select][-1] = min(elements[select][-1] + 1, len(elements[select][2]) - 1)
        if kd(4) and elements[select][0] == "btn":
            break

        if draw:
            for nb, el in enumerate(elements):
                drawRect(x, y + el_size * nb, 10 * txt_size[nb], el_size, bg_col)
                slcted = 1 if nb == select else 0
                elem_type = el[0]
                name = el[1]
                val = el[-1]
                if elem_type == "btn":
                    disp_txt = name
                elif elem_type == "sld":
                    disp_txt = name + " : {}".format(val)
                elif elem_type == "lst":
                    disp_txt = name + " : {}".format(el[2][val])
                else:
                    disp_txt = "error"
                if slcted:
                    disp_txt = "> " + disp_txt
                txt_size[nb] = len(disp_txt)
                drawTxt(disp_txt, x, y + nb * el_size, col, bg_col)
                draw = 0
    return elements[select][1], {x[1]: x[-1] for x in elements if x[0] != "btn"}


# Fonction detection touches

def cinput():
    value_to_edit = ""
    while True:
        if kd(KEY_ONE):
            value_to_edit = value_to_edit + "1"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_TWO):
            value_to_edit = value_to_edit + "2"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_THREE):
            value_to_edit = value_to_edit + "3"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_FOUR):
            value_to_edit = value_to_edit + "4"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_FIVE):
            value_to_edit = value_to_edit + "5"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_SIX):
            value_to_edit = value_to_edit + "6"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_SEVEN):
            value_to_edit = value_to_edit + "7"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_EIGHT):
            value_to_edit = value_to_edit + "8"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_NINE):
            value_to_edit = value_to_edit + "9"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_ZERO) and len(value_to_edit) != 0 and value_to_edit[0] != "-":
            value_to_edit = value_to_edit + "0"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if len(value_to_edit) == 0 and kd(KEY_MINUS):
            value_to_edit = value_to_edit + "-"
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_DOT) and ("." not in value_to_edit):
            value_to_edit = value_to_edit + "."
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_BACKSPACE) and len(value_to_edit) != 0:
            value_to_edit = value_to_edit[:len(value_to_edit) - 1]
            drawRect(0, 70, 340, 20, (255, 255, 255))
            drawTxt(value_to_edit, 0, 70)
        if kd(KEY_OK) or kd(KEY_EXE):
            if "." in value_to_edit:
                return float(value_to_edit)
            elif len(value_to_edit) == 0:
                return 0
            else:
                return int(value_to_edit)


# DEF COMMANDES


class Sciences:
    def __init__(self):
        drawTxt("Sciences :", 0, 0)
        Rangee = menu(0, 30, [["btn", "Mathématiques"], ["btn", "SVT"], ["btn", "Physique"], ["btn", "Chimie"],
                              ["btn", "Retour"]])[0]
        drawRect(0, 0, 340, 230, (255, 255, 255))
        if Rangee == "Mathématiques":
            Sciences.Maths()
        if Rangee == "SVT":
            Sciences.SVT()
        if Rangee == "Physique":
            Sciences.Physique()
        if Rangee == "Retour":
            Main.colonne()

    # Physique
    class Physique:
        def __init__(self):
            Chapitre = menu(0, 30, [["btn", "La Lumière"], ["btn", "Retour"]])[0]
            drawRect(0, 0, 340, 230, (255, 255, 255))
            if Chapitre == "La Lumière":
                Sciences.Physique.Lumiere()
                drawRect(0, 0, 340, 230, (255, 255, 255))
                time.sleep(2)
            if Chapitre == "Retour":
                Sciences()

        class Lumiere:
            def __init__(self):
                drawTxt("Physique/La Lumière :", 0, 0)
                Theme = menu(0, 30, [["btn", "Colorimétrie"], ["btn", "Retour"]])[0]
                drawRect(0, 0, 340, 230, (255, 255, 255))
                if Theme == "Colorimétrie":
                    Sciences.Physique.Lumiere.Colorimetrie()
                if Theme == "Retour":
                    Sciences.Physique()

            class Colorimetrie:
                def __init__(self):
                    drawTxt("Physique/La Lumière/ Colorimétrie:", 0, 0)
                    Theme = \
                        menu(0, 30,
                             [["btn", "Synthèse additive"], ["btn", "Synthèse soustractive"], ["btn", "Retour"]])[0]
                    drawRect(0, 0, 340, 230, (255, 255, 255))
                    if Theme == "Synthèse additive":
                        Sciences.Physique.Lumiere.Colorimetrie.synt_add_phy()
                    if Theme == "Synthèse additive":
                        Sciences.Physique.Lumiere.Colorimetrie.synt_sou_phy()
                    if Theme == "Retour":
                        Sciences.Maths.Vecteurs()

                @staticmethod
                def synt_add_phy():
                    drawTxt("EN CONSTRUCTION", 0, 0)
                    time.sleep(3)
                    drawRect(0, 0, 340, 230, (255, 255, 255))

                @staticmethod
                def synt_sou_phy():
                    drawTxt("EN CONSTRUCTION", 0, 0)
                    time.sleep(3)

    # Maths
    class Maths:
        def __init__(self):
            drawTxt("Mathématiques :", 0, 0)
            Chapitre = menu(0, 30, [["btn", "Équations"], ["btn", "Vecteurs"], ["btn", "Retour"]])[0]
            drawRect(0, 0, 340, 230, (255, 255, 255))
            if Chapitre == "Équations":
                Sciences.Maths.Equation()
            elif Chapitre == "Vecteurs":
                Sciences.Maths.Vecteurs()
            elif Chapitre == "Retour":
                Sciences()

        class Equation:
            def __init__(self):
                drawTxt("Mathématiques/Équations :", 0, 0)
                Theme = menu(0, 30, [["btn", "Discriminant"], ["btn", "Retour"]])[0]
                drawRect(0, 0, 340, 230, (255, 255, 255))
                if Theme == "Discriminant":
                    drawRect(0, 0, 340, 230, (255, 255, 255))
                    drawTxt(Sciences.Maths.Function.discriminant(), 0, 0)
                    drawRect(0, 0, 340, 230, (255, 255, 255))
                    time.sleep(3)
                if Theme == "Retour":
                    Sciences.Maths()

        class Vecteurs:
            def __init__(self):
                drawTxt("Mathématiques/Vecteurs :", 0, 0)
                Theme = menu(0, 30, [["btn", "Norme"], ["btn", "Coordonnées"], ["btn", "Retour"]])[0]
                drawRect(0, 0, 340, 230, (255, 255, 255))
                if Theme == "Norme":
                    Sciences.Maths.Vecteurs.Norme()
                if Theme == "Coordonnées":
                    Sciences.Maths.Vecteurs.Coordonnees()
                if Theme == "Retour":
                    Sciences.Maths()

            class Norme:
                def __init__(self):
                    drawTxt("Mathématiques/Vecteurs/Norme :", 0, 0)
                    Theme = menu(0, 30, [["btn", "Norme d'un vecteur"], ["btn", "Retour"]])[0]
                    drawRect(0, 0, 340, 230, (255, 255, 255))
                    if Theme == "Norme d'un vecteur":
                        Sciences.Maths.Vecteurs.Norme.norme_vecteur()
                    if Theme == "Retour":
                        Sciences.Maths.Vecteurs()

                @staticmethod
                def norme_vecteur():
                    drawTxt("Norme d'un vecteur :", 0, 0)
                    drawTxt("x", 0, 30)
                    x = cinput()
                    drawRect(0, 70, 340, 20, (255, 255, 255))
                    drawTxt("y", 0, 30)
                    y = cinput()
                    drawRect(0, 70, 340, 20, (255, 255, 255))
                    drawTxt("La norme du vecteur est :\n" + str(math.sqrt(x ** 2 + y ** 2)), 0, 0)
                    time.sleep(3)
                    drawRect(0, 0, 340, 230, (255, 255, 255))

            class Coordonnees:
                def __init__(self):
                    drawTxt("Mathématiques/Vecteurs/Coordonnées :", 0, 0)
                    Theme = menu(0, 30, [["btn", "Coordonnées d'un vecteur"], ["btn", "Retour"]])[0]
                    drawRect(0, 0, 340, 230, (255, 255, 255))
                    if Theme == "Coordonnées d'un vecteur":
                        Sciences.Maths.Vecteurs.Coordonnees.coordonnees_vecteur()
                    if Theme == "Retour":
                        Sciences.Maths.Vecteurs()

                @staticmethod
                def coordonnees_vecteur():
                    drawTxt("Coordonnées d'un vecteur :", 0, 0)
                    drawTxt("Coordonnées x du premier point :", 0, 30)
                    x = cinput()
                    drawTxt("Coordonnées y du premier point :", 0, 30)
                    y = cinput()
                    drawTxt("Coordonnées x du deuxième point :", 0, 30)
                    x2 = cinput()
                    drawTxt("Coordonnées y du deuxième point :", 0, 30)
                    y2 = cinput()
                    drawRect(0, 70, 340, 20, (255, 255, 255))

                    drawTxt("Les coordonnées du vecteur sont : \n" + str(x2 - x) + " " + str(y2 - y), 0, 0)
                    time.sleep(3)

        class Function:
            @staticmethod
            def discriminant():
                drawTxt("Résoudre l'équation ax^2+bx+c=0", 0, 0)
                drawTxt("a", 0, 30)
                a = 0
                while a == 0:
                    a = cinput()
                drawRect(0, 70, 340, 20, (255, 255, 255))
                drawTxt("b", 0, 30)
                b = cinput()
                drawRect(0, 70, 340, 20, (255, 255, 255))
                drawTxt("c", 0, 30)
                c = cinput()

                delta = b ** 2 - 4 * a * c
                if delta > 0:
                    x1 = -(-b ** 2 + math.sqrt(delta)) / (2 * a)
                    x2 = -(-b ** 2 - math.sqrt(delta)) / (2 * a)
                    return "Cette équation a pour delta :\n " + delta + "\n et pour racines : \n" + str(
                        x1) + "\n" + str(x2)
                if delta == 0:
                    x = -b / (2 * a)
                    return "Cette équation a pour racine : \n" + str(x)
                if delta < 0:
                    return "Cette équation n'a aucune \nracine réelle."

    # SVT

    class SVT:
        def __init__(self):
            drawTxt("SVT :", 0, 0)
            Chapitre = menu(0, 30, [["btn", "La Cellule"], ["btn", "Retour"]])[0]
            drawRect(0, 0, 340, 230, (255, 255, 255))
            if Chapitre == "La Cellule":
                drawTxt("SVT/La Cellule", 0, 0)
                Theme = menu(0, 30, [["btn", "Théorie Cellulaire"], ["btn", "Retour"]])[0]
                drawRect(0, 0, 340, 230, (255, 255, 255))
                if Theme == "Théorie Cellulaire":
                    drawTxt(self.theorie_cellulaire(), 0, 0)
                    time.sleep(5)
                    drawRect(0, 0, 340, 230, (255, 255, 255))
                if Theme == "Retour":
                    drawTxt("SVT :", 0, 0)
                    Chapitre = menu(0, 30, [["btn", "La Cellule"], ["btn", "Retour"]])[0]
                    drawRect(0, 0, 340, 230, (255, 255, 255))
            if Chapitre == "Retour":
                Main.colonne()

        @staticmethod
        def theorie_cellulaire():
            return "- Tout organisme vivant est\ncomposé d'une ou plusieurs\ncellules \n- La cellule est l'unité " \
                   "de\nstructure et de fonction du\nvivant \n- Toute cellule provient d'une\nautre cellule par " \
                   "division\ncellulaire"

    # Chimie
    class Chimie:
        def __init__(self) -> None:
            drawTxt("Chimie :", 0, 0)
            Chapitre = menu(0, 30, [["btn", "Retour"]])[0]
            drawRect(0, 0, 340, 230, (255, 255, 255))
            if Chapitre == "Retour":
                Sciences()

    # Physique


class Litteraire:
    def __init__(self):
        drawTxt("Litteraire :", 0, 0)
        Rangee = menu(0, 30, [["btn", "Francais"], ["btn", "Anglais"], ["btn", "Retour"]])[0]
        drawRect(0, 0, 340, 230, (255, 255, 255))
        if Rangee == "Francais":
            Litteraire.Francais()
        if Rangee == "Anglais":
            Litteraire.Anglais()
        if Rangee == "Retour":
            Main.colonne()

    class Francais:
        def __init__(self):
            drawTxt("Litteraire/Francais :", 0, 0)
            Chapitre = menu(0, 30, [["btn", "Quelque Chose"], ["btn", "Retour"]])[0]
            drawRect(0, 0, 340, 230, (255, 255, 255))
            if Chapitre == "Quelque Chose":
                drawTxt("Quelque Chose :", 0, 0)
                Theme = menu(0, 30, [["btn", "Retour"]])[0]
                drawRect(0, 0, 340, 230, (255, 255, 255))
                if Theme == "Retour":
                    Litteraire()

    class Anglais:
        def __init__(self):
            drawTxt("Litteraire/Anglais :", 0, 0)
            Chapitre = menu(0, 30, [["btn", "Quelque Chose"], ["btn", "Retour"]])[0]
            drawRect(0, 0, 340, 230, (255, 255, 255))
            if Chapitre == "Quelque Chose":
                drawTxt("Quelque Chose :", 0, 0)
                Theme = menu(0, 30, [["btn", "Retour"]])[0]
                drawRect(0, 0, 340, 230, (255, 255, 255))
                if Theme == "Retour":
                    Litteraire()

            if Chapitre == "Retour":
                Litteraire()


class Autres:
    def __init__(self):
        drawTxt("Autres :", 0, 0)
        Rangee = menu(0, 30, [["btn", "Anniversaires"], ["btn", "Machin"], ["btn", "Bidule"], ["btn", "Credits"],
                              ["btn", "Retour"]])[0]
        drawRect(0, 0, 340, 230, (255, 255, 255))
        if Rangee == "Anniversaires":
            drawTxt("Autres/Anniversaires :", 0, 0)
            Chapitre = menu(0, 30, [["btn", "Lycée"], ["btn", "Retour"]])[0]
            drawRect(0, 0, 340, 230, (255, 255, 255))
            if Chapitre == "Lycée":
                drawTxt("Coco : 08/08/2005 \nFlo : 05/04/2006 \nLilian : 20/10/2006", 0, 0)
                time.sleep(2)
                drawRect(0, 0, 340, 230, (255, 255, 255))
            if Chapitre == "Retour":
                Autres()
        if Rangee == "Credits":
            drawTxt("Autres/Credits :", 0, 0)
            Chapitre = menu(0, 30, [["btn", "Developers"], ["btn", "Retour"]])[0]
            drawRect(0, 0, 340, 230, (255, 255, 255))
            if Chapitre == "Developers":
                drawTxt("Dev principal : Colveri \nDev secondaire : e_psi_lon", 0, 0)
                time.sleep(2)
                drawRect(0, 0, 340, 230, (255, 255, 255))
            if Chapitre == "Retour":
                Autres()

        if Rangee == "Retour":
            Main.colonne()


class Main:
    def __init__(self):
        drawTxt(
            "Bienvenue dans l'encyclopédie\nde Colveri.\nVous choisirez votre acces \nen utilisant\n les menus "
            "dédiés.\nAppuyez sur 1 ou OK pour\ncommencer ou HOME/RETOUR pour\nquitter",
            0, 0)
        while True:
            if kd(KEY_ONE) or kd(KEY_OK):
                ouvrir = 1
                drawRect(0, 0, 340, 230, (255, 255, 255))
                break
            elif kd(KEY_BACK) or kd(KEY_HOME):
                ouvrir = 0
                break
        if ouvrir == 1:
            Main.colonne()

    @staticmethod
    def colonne():
        """Permet de choisir où aller"""
        Colonne = ""
        while Colonne != "Quitter":
            drawTxt("Aller à :", 0, 0)
            Colonne = menu(0, 30, [["btn", "Sciences"], ["btn", "Littéraire"], ["btn", "Autres"], ["btn", "Quitter"]])[
                0]
            drawRect(0, 0, 340, 230, (255, 255, 255))
            if Colonne == "Sciences":
                Sciences()
            if Colonne == "Autres":
                Autres()
            if Colonne == "Littéraire":
                Litteraire()
            if Colonne == "Quitter":
                pass


try:
    Main()
    print("Exiting Program")
except Exception as e:
    print("Bug Detected : " + str(e))
