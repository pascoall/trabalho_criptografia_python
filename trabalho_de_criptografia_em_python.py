from cryptography.fernet import Fernet

#inicializando a variavel op(opção)
op = 0

#Estrutura de repetição onde o menu vai se repetir até a opção for diferente de 3
while op != 3:
    #Mostra na tela as opções que o usuario poderá escolher
    op = int(input(print("[1] - Criptografar\n[2] - Descriptografar\n[3] - Sair do Programa\n\nDigite sua Opção: ")))
    if op == 1: 
        mensagem = input("Digite sua mensangem: ")

        #Gera uma chave de criptografia  
        key = Fernet.generate_key() 
            
        #Instancia a classe Fernet com a chave de criptografia 
        fernet = Fernet(key) 

        #Criptografa a string com a instância Fernet 
        encMensagem = fernet.encrypt(mensagem.encode()) 
        
        #Mostra a mensagem criptografada
        print("Mensagem Criptografada: ", encMensagem)
    
            

    elif op == 2:
        print("")
        #Descriptografando com a instância da classe Fernet e deve ser instanciado com a mesma chave usada para criptografia
        descMensagem = fernet.decrypt(encMensagem).decode() 

        #Mostra a mensagem descriptografada   
        print("Mensagem descriptografada: ", descMensagem)
    
    #Condição que finaliza o programa    
    elif op == 3:
        print("Programa Finalizado!")
        break
    
    #Condição para uma opção invalida
    else:
        print("")
        print("Opção Invalida!")
        break
