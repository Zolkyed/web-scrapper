import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

def extraire_liens_vers_csv(url, fichier_sortie):
    try:
        reponse = requests.get(url)
        
        if reponse.status_code == 200:
            soup = BeautifulSoup(reponse.content, 'html.parser')
            liens = soup.find_all('a')
            
            with open(fichier_sortie, mode='w', newline='', encoding='utf-8') as fichier:
                ecrivain = csv.writer(fichier)
                ecrivain.writerow(['Lien'])  
                
                for lien in liens:
                    if lien.find('i') is None:
                        href = lien.get('href')
                        if href:
                            lien_complet = urljoin(url, href)
                            ecrivain.writerow([lien_complet])
                
            print("Terminée.")
        else:
            print("Échec de la récupération de la page.")
    except Exception as e:
        print(f"Une erreur s'est produite.")

url = ''  
fichier_sortie = 'sortie.csv'  
extraire_liens_vers_csv(url, fichier_sortie)
