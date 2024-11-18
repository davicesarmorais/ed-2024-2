from models import *
from services import *
from utils import *
from view import *


def main():
    contexto = Contexto()    
    MenuPrincipal(contexto).interact()


if __name__ == "__main__":
    main()
