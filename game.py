
import os


class Game:
    """
    Essa classe se refere ao código que engloba o jogo Simulador de Vingar Pai.

    Todas as funções "situacaoX" são usadas para definir o que acontece e a decisão
    do usuário em relação à situação!
    """
    def __init__(self):
        """
        Inicializa a classe do jogo e limpa o terminal.
        """
        self.clear()

    @staticmethod
    def clear():
        """
        Limpa o terminal do sistema.
        """
        os.system('clear' if os.name == 'posix' else 'cls')  # Ele verifica o sistema utilizado e limpa o terminal
        print('###===###===###===###')

    def perde(self):
        """
        Essa função faz com que o jogo resete quando o jogador perde o jogo.
        """
        print('Digite Enter para continuar.')
        input()
        self.inicio()

    def processar_escolha(self, escolha, opcoes):
        """
        Faz com o que o jogador escolha a opção e trata caso escolha uma opção inválida.
        """

        if escolha in opcoes:
            self.clear()
            opcoes[escolha]()
        else:
            self.clear()
            print('Por favor, insira uma escolha válida (1 ou 2).')

    def inicio(self):
        """
        Define a história inicial do jogo, dando um contexto breve.
        """
        print('###===###===###===###')
        print('SIMULADOR DE VINGAR PAI')
        print('###===###===###===###')
        print('Bem-vindo ao Simulador de Vingar Pai.')
        print()
        print('Seu pai morreu assassinado a sangue frio'
              '\nem sua frente quando você tinha apenas'
              '\n10 anos de idade.'
              '\nVocê nunca esquecerá do rosto do assassino.'
              '\nEle se chama Rudolf Viajante e é um rei da'
              '\ncrueldade do submundo da cidade. Suas ações'
              '\nnão são meramente baseadas em crimes, mas em'
              '\npura loucura e sangue desnecessário.'
              '\nVocê precisa vingar a morte de seu pai'
              '\ne dar um basta nessa era de terror'
              '\ntrazida por Rudolf Viajante.')
        print('###===###===###===###')
        print('Antes de mais nada, você deve receber instruções básicas.')
        self.instrucao()

    def instrucao(self):
        """
        Explica a mecânica báscia do jogo e questiona se o jogador entendeu ou não.
        """

        opcoes = {
            '1': self.situacao1,
            '2': self.instrucao
        }

        while True:
            print('Nesse jogo você precisa escolher entre duas alternativas.'
                  '\nResponda sempre utilizando "1" ou "2"')

            print('Você entendeu?')
            print('1 - Sim')
            print('2 - Não')
            escolha = input()

            self.processar_escolha(escolha, opcoes)

    def situacao1(self):
        """
        A etapa inicial do jogo. A primeira tomada de decisão.
        """
        opcoes = {
            '1': self.situacao1a,
            '2': self.situacao2
        }

        while True:  # Tomadas de decisão têm um loop while para que seja verificado o input do jogador.
            print('Antes de se vingar, você precisa treinar,'
                  '\njá que não passa de um jovem franzino'
                  '\nno auge de seus 19 anos de idade.')

            print('Onde você prefere treinar?')
            print('1 - Ir até o açougue treinar.')
            print('2 - Ir ao centro de treinamento.')
            escolha = input()

            self.processar_escolha(escolha, opcoes)

    def situacao1a(self):
        """
        Situação que ocorre quando decide treinar com o açougueiro.
        """

        print('Você pede para o açougueiro te treinar.'
              '\nDepois de muito se aperfeiçoar, você fica'
              '\nmais forte que ele. Um discípulo maior'
              '\nque seu próprio mestre!'
              '\nNo auge de sua inveja e perdição,'
              '\no açougueiro não pode compreender'
              '\ntamanha conquista que você obteve.'
              '\nEle se irrita com isso e não tem outra escolha'
              '\na não ser tirar sua vida enquanto você dorme.'
              '\nVocê perdeu.')
        self.perde()

    def situacao2(self):
        """
        Situação que surge ao escolher ir ao centro de treinamento.
        """

        opcoes = {
            '1': self.situacao3,
            '2': self.situacao2a
        }

        while True:
            print('Você vai ao centro de treinamento e'
                  '\nse matricula para treinar. Você fica'
                  '\nmais forte a cada dia de treinamento.'
                  '\nDepois de algumas semanas você pode'
                  '\nver os resultados de seu esforço intensivo.'
                  '\nVocê se sente pronto para lutar após treinar'
                  '\npor cerca de três meses.'
                  '\nAgora você precisa de uma arma.')

            print('1 - Ir até ao ferreiro')
            print('2 - Ir até o vendedor de armas')
            escolha = input()

            self.processar_escolha(escolha, opcoes)

    def situacao2a(self):
        """
        Situação que ocorre quando decide ir à loja de armas.
        """

        print('Você vai até a loja de armas. Chegando lá, você vê que'
              '\num garoto suicida também estava na loja de armas.'
              '\nEle mata todos os que se encontravam na loja com uma arma'
              '\nque encontrou num balcão. Isso acaba por incluir você.'
              '\nEle se matou em seguida do ato após urinar na boca do seu cadáver.'
              '\nSinto muito.')
        self.perde()

    def situacao3(self):
        """
        Situação que surge ao escolher ir até o ferreiro.
        """

        opcoes = {
            '1': self.situacao4,
            '2': self.situacao3a
        }

        while True:
            print('Você compra uma adaga e o ferreiro te dá um par de luvas de brinde.'
                  '\nVocê agora precisa saber onde está o assassino de seu pai.')

            print('1 - Perguntar pelos bares')
            print('2 - Anunciar uma recompensa pública')
            escolha = input()

            self.processar_escolha(escolha, opcoes)

    def situacao3a(self):
        """
        Situação que ocorre quando decide publicar uma recompensa ao público geral.
        """

        print('Você faz isso e se passam algumas semanas.'
              '\nÉ noticiado no jornal que o assassino de seu pai está foragido em outro país.'
              '\nVocê se vê tão burro quanto a essa atitude que acaba atirando na folha do jornal.'
              '\nA bala ricocheteia no chão e na parede e acaba te acertando.'
              '\nBurro até demais.')
        self.perde()

    def situacao4(self):
        """
        Situação que surge ao escolher perguntar pelos bares.
        """

        opcoes = {
            '1': self.situacao4a,
            '2': self.situacao5
        }

        while True:
            print('Você conversa com o bartender e alguns bêbados.'
                  '\nA melhor informação que você obtém é para procurar pelas vielas do Distrito Velho.'
                  '\nAo chegar lá, você se depara com uma bifurcação.')

            print('1 - Ir pela esquerda.')
            print('2 - Ir pela direita.')
            escolha = input()

            self.processar_escolha(escolha, opcoes)

    def situacao4a(self):
        """
        Situação que ocorre quando escolhe o caminho da esquerda.
        """

        print('O Bolsonaro aparece gritando com você.'
              '\n"Não pode ir pela esquerda, talkey? Esquerdista é tudo vagabundo mesmo!"'
              '\nEle faz uma rachadinha com seu filho Flávio justamente no seu peito.'
              '\nEssa rachadinha te gerou uma hemorragia intensa. Você morreu em poucos minutos.')
        self.perde()

    def situacao5(self):
        """
        Situação que surge ao escolher ir pela rota da direita.
        """

        opcoes = {
            '1': self.final,
            '2': self.situacao5a
        }

        while True:
            print('É ele. Você o encontrou e ele está de costas para você, andando pela viela.')
            print('1 - Atacar seu pescoço.')
            print('2 - Atacar sua lombar.')
            escolha = input()

            self.processar_escolha(escolha, opcoes)

    def situacao5a(self):
        """
        Situação que ocorre quando decide atacar a lombar do Rudolf Viajante.
        """

        print('Você descobre uma armadura de placa debaixo de suas vestes.'
              '\nEle não foi perfurado.'
              '\nO assassnio te dá um soco que te lança para longe.'
              '\nEle pega sua lâmina e atinge sua lombar. Você sangra.'
              '\nVocê morreu.')
        self.perde()

    def final(self):
        """
        O que ocorre ao fim do jogo. Explica como o jogador concluiu o objetivo e dá os créditos finais.
        """
        self.clear()
        print('Você rasga sua nuca, fazendo com que jorre muito sangue.'
              '\nAlguns gritam de horror por perto e outros gritam de felicidade.'
              '\nAlgo dentro de você clama que seu pai está vingado e orgulhoso de você.'
              '\nParabéns por terminar o jogo.'
              '\nCréditos:'
              '\nDesenvolvedor: Petrus'
              '\nArtismo: Petrus'
              '\nBarulhos e "Música": Petrus')
        input()
        quit()
