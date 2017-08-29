import threading
from queue import Queue
from time import sleep

import bs4 as bs
import urllib.request



def crawler(new_root):
    visitadas.append(new_root)
    try:
        # Aqui pegaremos a pagina inteira
        source = urllib.request.urlopen(new_root).read()
        soup = bs.BeautifulSoup(source, 'lxml')

        new_links = []

        # Aqui pegaremos os links dentro das tags "a"
        new_links = [link.get('href') for link in soup.select('a')]

        # Alguns dos sites usam Frame.
        frames = [link.get('src') for link in soup.select('frame')]
        if frames:
            for frame in frames:
                if ".htm" not in new_root:
                    new_links.append(new_root + frame)

        try:
            title = soup.title.text
            print(title)
        except:
            pass

        print(new_links[:])
        print(visitadas)

        el_validator(new_root, new_links)

        writer(new_root, title, new_links)

    except Exception as e:
        # print(e)
        pass


def el_validator(new_root, new_links):
    # o codigo ira checar os links para validacao.
    for link in new_links:
        # Validacao
        try:
            if new_root in link:
                if link not in visitadas:
                    links_por_Visitar.put(link)

            elif '/' == link[0]:
                # fix eh uma solucao que encontrei para evitar que repeticao de links
                # Sem isto os links acabam se escrevendo site.com//link.html e depois site.com///link.html
                fix = new_root[:-1]
                if fix + link not in visitadas:
                    links_por_Visitar.put(fix + link)
            elif '#' == link[0]:
                if new_root + link not in visitadas:
                    links_por_Visitar.put(new_root + link)
            elif 'http' not in link and "htm" not in new_root:
                if new_root + link not in visitadas:
                    links_por_Visitar.put(new_root + link)
            elif 'http' not in link:
                if root + link not in visitadas:
                    links_por_Visitar.put(root + link)
            elif '..' in link:
                continue
            else:
                pass
        except Exception as e:
            # print(e)
            pass



def writer(new_root, title, new_links):
    file = open("dataDump.txt", "a")
    file.write(new_root + "\n\n" + title + "\n\n" + '\n'.join(new_links) + "\n\n\n")
    # file.write(new_root + "\n")
    file.close()


def worker():
    counter = 3
    while counter > 0:
        while not links_por_Visitar.empty():
            por_visitar = links_por_Visitar.get()
            if por_visitar not in visitadas:
                crawler(por_visitar)
                counter = 3
            links_por_Visitar.task_done()
        sleep(5)
        counter -= 1


if __name__ == "__main__":

    # Craindo uma lista de paginas visitadas
    visitadas = []

    # Criando a "Queue"
    links_por_Visitar = Queue()

    # Determina o root por onde o processo se inicia
    # root = 'http://w3.ualg.pt/'
    # root = 'http://w3.ualg.pt/~paneves/'
    # root = 'http://w3.ualg.pt/~aferreir/'
    root = 'http://w3.ualg.pt/~sfernan/'
    links_por_Visitar.put(root)

    # Criamos o arquivo para guardar os dados
    file = open("dataDump.txt", "w")
    file.write("Here we go.\n\n\n")
    # Fechamos o arquivo
    file.close()

    # Chamando os workers
    for i in range(50):
        sleep(2)
        threading.Thread(target=worker, args=()).start()

    links_por_Visitar.join()
