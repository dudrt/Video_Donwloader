from pytube import YouTube
#-----Mudar 'loca_save' para aonde você deseja salvar os arquivos--------
#-----Change 'loca_save' to where you want to save the files-------------
local_save="C:/Users/user/desktop/audio"

#--------Função que faz download do arquivo formato video--------
#--------Function that downloads the video format file-----------
def best_quality(link):
    try:
        yt=YouTube(link)
    except:
        print('Erro ao conectar, verifique sua internet!')
    try:
        print('Espere até o download estar completo!')
        stream=yt.streams.get_highest_resolution()
        stream.download(local_save)
        print(f'Download completo {yt.title} !\n--------------')
    except:
        print('erro ao baixar')

#--------Função que faz download do arquivo formato audio--------
#--------Function that downloads the audio format file-----------
def audio(link):
    try:
        yt=YouTube(link)
        tipo_audio=yt.streams.filter(only_audio=True)
    except:
        print('Erro ao conectar, verifique sua internet!')
    try:
        print('Espere até o download estar completo!')
        tamanho=len(tipo_audio)
        ser_baixado=tipo_audio[tamanho-1]
        ser_baixado=str(ser_baixado)
        ser_baixado=ser_baixado.split(' ')
        local_itag=ser_baixado[1].split('"')
        stream = yt.streams.get_by_itag(int(local_itag[1]))
        stream.download(local_save)
        print(f'Download completo {yt.title} ! \n'+
        'Caso o formato ou qualidade não for o esperado, escolha a opção 3 e veja suas opções de escolha de arquivo!'+
        '\n-------------------------------------------')
    except:
        print('erro ao baixar')

#--------Função que você escolhe o formato de arquivo--------
#--------Function you choose file format---------------------
def choose_type(link):
    try:
        yt=YouTube(link)
    except:
        print('Erro ao conectar, verifique sua internet ou link!')
    try:
        tipos=yt.streams
        for tipo in tipos:
            tipo=str(tipo)
            mostrar=tipo.split('"')
            print('ID:'+mostrar[1]+" | Tipo/Formato:"+mostrar[3]+" | Qualidade:"+mostrar[5]+" | FPS:"+mostrar[7])
        id=input("ID que você deseja baixar:")
        try:
            print('--------------\nEspere até o download estar completo!')
            stream=yt.streams.get_by_itag(int(id))
            stream.download(local_save)
            print(f'Download completo {yt.title} ! \n---------------')
        except:
            print('ID incorreto')
    except:
        print('erro ao baixar')

#--------Faz a pergunta de uso das opções--------
#--------Ask the option usage question-----------
print("\n---------------------------------\n"+
"Atenção! \nCaso você baixe o mesmo arquivo com a mesma extensão \nduas vezes, ele será automaticamente substituido pelo novo!"+
"\n---------------------------------")
continuar = True
all=input('Usar sempre a mesma opção para dowloads?(SIM/NAO)')
all=all.upper()

#--------Caso opte para sempre ser a mesma maneira de dowload--------
#--------If you choose to always be the same way to download---------
if all== 'SIM':
    tipo_arquivo=int(input('Digite como você deseja baixar:\n1-Melhor qualidade vídeo.'+
'\n2-Baixar audio.'+
'\n3-Escolher.\nR:'))
    while(continuar):
        if(tipo_arquivo==1):
            link=input('Link do video:')
            best_quality(link)
        elif(tipo_arquivo==2):
            link=input('Link do video:')
            audio(link)
        elif(tipo_arquivo==3):
            link=input('Link do video:')
            choose_type(link)
        else:
            print("------------------------\n")
            tipo_arquivo=int(input('Digite como você deseja baixar:\n1-Melhor qualidade vídeo.'+
'\n2-Baixar audio.'+
'\n3-Escolher.\nR:'))

#--------Caso opte para sempre escolher a maneira de dowload--------
#--------If you choose to always choose the way to download---------
elif all == 'NAO' or all== 'NÃO':
    while(continuar):
        tipo_arquivo=int(input('Digite como você deseja baixar:\n1-Melhor qualidade vídeo.'+
'\n2-Baixar audio.'+
'\n3-Escolher.\nR:'))
        if(tipo_arquivo==1):
            link=input('Link do video:')
            best_quality(link)
        elif(tipo_arquivo==2):
            link=input('Link do video:')
            audio(link)
        elif(tipo_arquivo==3):
            link=input('Link do video:')
            choose_type(link)
        else:
            print("------------------------\n")
            tipo_arquivo=int(input('Digite como você deseja baixar:\n1-Melhor qualidade vídeo.'+
'\n2-Baixar audio.'+
'\n3-Escolher.\nR:'))
            
else:
    print('Escolha uma opção válida')
