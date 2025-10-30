# Gestionnaires des contacts 

# Cette application permet d'ajouter et d'afficher des contacts.

def information(nom, prenom, email, telephone): # Crée un dictionnaire pour un contact
    contact = {
        "nom": nom,
        "prenom": prenom,
        "email": email,
        "telephone": telephone
    }
    return contact

def ajouter_contacts(liste_contacts):  # Ajoute un contact à la liste
    nom = input("Entrez le nom du contact: ")
    prenom = input("Entrez le prénom du contact: ")
    
    domaines_valides = ["@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com"]

    while True:
        email = input("Entrez l'email du contact: ").strip().lower()
        if any(email.endswith(domaine) for domaine in domaines_valides):
            break
        else:
            print("Email invalide. Veuillez entrer un email avec un domaine valide (@gmail.com, @yahoo.com, @outlook.com, @hotmail.com).")
    
    
    telephone = input("Entrez le numéro de téléphone du contact: ")
    contact = information(nom, prenom, email, telephone)

    liste_contacts.append(contact)

    print("Contact ajouté avec succès !")
    return liste_contacts

def afficher_contacts(liste_contacts):  # Affiche tous les contacts de la liste
    if not liste_contacts:
        print("Aucun contact à afficher.")
        return
    for contact in liste_contacts:
        print(f"Nom: {contact['nom']}, Prénom: {contact['prenom']}, Email: {contact['email']}, Téléphone: {contact['telephone']}")
    return liste_contacts

def main():  # Boucle principale pour interagir avec l'utilisateur
    liste_contacts = []
    while True:
        print("\n1. Ajouter un contact\n2. Afficher les contacts\n3. Quitter")
        choix = input("Choix: ").strip()
        if choix == "1":
            ajouter_contacts(liste_contacts)
        elif choix == "2":
            afficher_contacts(liste_contacts)
        elif choix == "3":
            print("Au revoir.")
            break
        else:
            print("Choix invalide. Réessayez.")


main()


