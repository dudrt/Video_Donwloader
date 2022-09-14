from pytube import YouTube
from pytube import Playlist
#-----Mudar 'loca_save' para aonde você deseja salvar os arquivos--------
#-----Change 'loca_save' to where you want to save the files-------------
local_save="C:/Users/dudur/OneDrive/Área de Trabalho/audio"

#--------Função que faz download do arquivo formato video--------
#--------Function that downloads the video format file-----------
def best_quality(link,playlist):
    if playlist:
        try:
            p=Playlist(link)
        except:
            print('Erro ao conectar, verifique sua internet!')
        try:
            for video in p.videos:
                try:
                    print('Espere até o download estar completo!')
                    stream=video.streams.get_by_itag(22)
                    stream.download(local_save)
                    print(f'Download completo {video.title} !\n--------------')
                except:
                    print('Qualidade 1080p inexistente, tentando baixar em 720p')
                    try:
                        print('Espere até o download estar completo!')
                        stream=video.streams.get_by_itag(18)
                        stream.download(local_save)
                        print(f'Download completo {video.title} !\n--------------')
                    except:
                        print('Qualidade máxima baixa, tente baixar escolhendo a opção :3')
        except:
            print('Fim')
    else:    
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
def audio(link,playlist):
#Baixar playlist
    if playlist:
        try:
            p=Playlist(link)
        except:
            print('Erro ao conectar, verifique sua internet!')
        try:
            for video in p.videos:
                tipo_audio=video.streams.filter(only_audio=True)
                print('Espere até o download estar completo!')
                tamanho=len(tipo_audio)
                ser_baixado=tipo_audio[tamanho-1]
                ser_baixado=str(ser_baixado)
                ser_baixado=ser_baixado.split(' ')
                local_itag=ser_baixado[1].split('"')
                stream = video.streams.get_by_itag(int(local_itag[1]))
                stream.download(local_save)
                print(f'Download completo {video.title} !\n-----------------------------')
        except:
            print('Fim')
#FIM Baixar playlist
#Baixar apenas um vídeo
    else:
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
def choose_type(link,playlist):
    if playlist:
        try:
            p=Playlist(link)
        except:
            print('Erro ao conectar, verifique sua internet ou link!')
        try:
            for video in p.videos:
                tipos=video.streams
                print(f'-----{video.title}-----')
                for tipo in tipos:
                    tipo=str(tipo)
                    mostrar=tipo.split('"')
                    print('ID:'+mostrar[1]+" | Tipo/Formato:"+mostrar[3]+" | Qualidade:"+mostrar[5]+" | FPS:"+mostrar[7])
                
                try:
                    id=input("ID que você deseja baixar:")
                    print('--------------\nEspere até o download estar completo!')
                    stream=video.streams.get_by_itag(int(id))
                    stream.download(local_save)
                    print(f'Download completo {video.title} ! \n---------------')
                except:
                    erro = True
                    print('ID incorreto')
                    while erro:
                        try:
                            id=input("ID que você deseja baixar:")
                            print('--------------\nEspere até o download estar completo!')
                            stream=video.streams.get_by_itag(int(id))
                            stream.download(local_save)
                            print(f'Download completo {video.title} ! \n---------------')   
                            erro = False
                        except:
                            erro = True
                            print('ID incorreto')
            print('--------------------Fim--------------------')
        except:
            print('Erro ao baixar')
    else:
        try:
            yt=YouTube(link)
        except:
            print('Erro ao conectar, verifique sua internet ou link!')
        try:
            tipos=yt.streams
            print(f'-----{yt.title}-----')
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
                erro = True
                print('ID incorreto')
                while erro:
                    try:
                        id=input("ID que você deseja baixar:")
                        print('--------------\nEspere até o download estar completo!')
                        stream=yt.streams.get_by_itag(int(id))
                        stream.download(local_save)
                        print(f'Download completo {yt.title} ! \n---------------')   
                        erro = False
                    except:
                        erro = True
                        print('ID incorreto')
        except:
            print('erro ao baixar')
#--------Faz a pergunta de uso das opções--------
#--------Ask the option usage question-----------
print("\n---------------------------------\n"+
"Atenção! \nCaso você baixe o mesmo arquivo com a mesma extensão \nduas vezes, ele será automaticamente substituido pelo novo!"+
"\n---------------------------------")
continuar = True
playlist=int(input('Você deseja baixar:\n1-Playlist\n2-Vídeos separados\nR:'))
if playlist == 1:
    playlist=True
else:
    playlist=False

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
            link=input('Link:')
            best_quality(link,playlist)
        elif(tipo_arquivo==2):
            link=input('Link:')
            audio(link,playlist)
        elif(tipo_arquivo==3):
            link=input('Link:')
            choose_type(link,playlist)
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
            link=input('Link:')
            best_quality(link,playlist)
        elif(tipo_arquivo==2):
            link=input('Link:')
            audio(link,playlist)
        elif(tipo_arquivo==3):
            link=input('Link:')
            choose_type(link,playlist)
        else:
            print("------------------------\n")
            tipo_arquivo=int(input('Digite como você deseja baixar:\n1-Melhor qualidade vídeo.'+
'\n2-Baixar audio.'+
'\n3-Escolher.\nR:'))

else:
    print('Escolha uma opção válida')
