# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform centro:
    zoom 0.18
    xalign 0.5
    yalign 1.0

define r = Character("Ryu", color="#41754a")    
define p = Character("Protagonista",  color="#6e1414", image="protagonista")

image side protagonista normal = Transform("protagonista.png", zoom=0.10)
image side protagonista piscando = Transform("protagonista_piscando.png", zoom=0.10)
image ryu normal = "ryu_normal.png"
image ryu piscando = "ryu_piscando.png"
image ryu sorrindo = "ryu_sorrindo.png"
image ryu piscando sorrindo = "ryu_sorrindo_piscando.png"
image ryu olhos fechados = "ryu_olhos_fechados.png"
image bg normal = "bg.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/teste.mpeg" volume 1.0
    scene bg normal:
        zoom 2.0
        
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "ryu happy.png" to the images
    # directory.

    show ryu normal at centro
    # These display lines of dialogue.

    r "Estou aprendendo a criar meu primeiro projeto no ren py"

    r "Estou gostando muito de aprender a usar essa ferramenta, é muito fácil de usar e tem muitos recursos legais para criar jogos de visual novel."

    show ryu piscando at centro


    r "Meu nome é Ryu e eu sou um personagem de teste para este projeto. Eu estou feliz por estar aqui e espero que vocês gostem do meu jogo!"

    hide ryu piscando

    p piscando "Olá, Ryu! Eu sou a protagonista do jogo. Estou animada para jogar e conhecer mais sobre você."

    show ryu piscando sorrindo at centro

    r "teste de expressão"

    show ryu olhos fechados at centro

    r "teste de expressão"

    p normal "teste de expressão"
    # This ends the game.

    return
