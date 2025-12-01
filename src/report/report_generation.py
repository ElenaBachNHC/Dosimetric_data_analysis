html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Dashboard Dosimétrique</title>
<style>
    body, html {
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f5f6fa;
    }

    /* Sidebar */
    .sidebar {
        height: 100%;
        width: 300px;
        position: fixed;
        top: 0;
        left: 0;
        background-color: #1a365d;
        padding-top: 20px;
        overflow-y: auto;
        box-shadow: 2px 0 5px rgba(0,0,0,0.2);
    }

    /* Sidebar title */
    .sidebar h2 {
        color: #f5f6fa;
        text-align: center;
        margin: 0 0 20px 0;
        font-size: 22px;
        letter-spacing: 1px;
    }

    /* Section subtitles */
    .sidebar .section-title {
        color: #d2dae2;
        padding: 8px 20px;
        font-size: 14px;
        font-weight: bold;
        text-transform: uppercase;
        background-color: #2c5282;
        margin-top: 15px;
        margin-bootom: 5px;
    }

    /* Links */
    .sidebar a {
        padding: 10px 20px;
        text-decoration: none;
        font-size: 16px;
        color: #f5f6fa;
        display: block;
        margin: 3px 10px;
        border-radius: 10px;
        transition: all 0.2s;
    }

    /* Hover & active */
    .sidebar a:hover {
        background-color: #485460;
        border-left: 4px solid #ffa502; /* accent orange */
        color: #fff;
    }

    .sidebar a.active {
        background-color: #57606f;
        border-left: 4px solid #ffa502;
    }

    /* Scrollbar style */
    .sidebar::-webkit-scrollbar {
        width: 8px;
    }
    .sidebar::-webkit-scrollbar-thumb {
        background-color: #718093;
        border-radius: 4px;
    }

    /* Main content */
    .content {
        margin-left: 310px;
        padding: 30px;
    }

    .content h2 {
        color: #2f3640;
        margin-top: 50px;
    }
</style>
</head>
<body>

<div class="sidebar">
    <h2>☢️ Portail dosimétrie</h2>

    <div class="section-title">NAVIGATION</div>
    <a href="#tableau">Tableau de bord</a>
    <a href="#synthèse">Synthèse globale</a>

    <div class="section-title">DOSIMETRIE</div>
    <a href="#bloc">Arceaux de bloc</a>
    <a href="#scanner">Scanner CT</a>
    <a href="#cardio">Cardiologie</a>
    <a href="#vasculaire nhc">Vasculaire NHC</a>
    <a href="#vasculaire htp">Vasculaire HTP</a>
    <a href="#neuro">Neuroradiologie</a>
    <a href="#gangi">Interventionnel Gangi</a>
    <a href="#mednuc">Médecine nucléaire</a>
    <a href="#conventionnelle">Radiologie conventionnelle</a>
    <a href="#mammo">Mammographie</a>

    <div class="section-title">PRODUCTIVITE</div>
    <a href="#scanner">Scanners</a>
    <a href="#productivité médecine nucléaire">Médecine nucléaire</a>
    <a href="#ordonnancier">Ordonnancier NHC</a>

    <div class="section-title">OPTIMISATION</div>
    <a href="#nri">NRI & plan d'optimisation</a>

    <div class="section-title">NRD</div>
    <a href="#nrd scanner">Scanner</a>
    <a href="#nrd médecine nucléaire">Médecine nucléaire</a>
    <a href="#mammo">Mammographie</a>
    <a href="#conv">Radiologie conventionnelle</a>

    <div class="section-title">ANALYSES</div>
    <a href="#arceaux">Statistiques arceaux</a>
    <a href="#approfondie">Analyse approfondie</a>
    <a href="#synthèse">Synthèse complète</a>

    <div class="section-title">RISQUE PROJETE</div>
    <a href="#cancer">Cancer pédiatrique CT</a>
        
</div>

<div class="content">
    <h1>Dashboard Dosimétrique</h1>
    <p>Contenu général du dashboard...</p>

    <h2 id="global">Vue d'ensemble - Global</h2>
    <p>Contenu de la section Global...</p>

    <h2 id="annee">Vue d'ensemble - Par année</h2>
    <p>Contenu de la section par année...</p>

    <h2 id="medecin">Vue d'ensemble - Par médecin</h2>
    <p>Contenu de la section par médecin...</p>

    <h2 id="modalites">Analyse des rendements - Par modalité</h2>
    <p>Contenu par modalité...</p>

    <h2 id="dossier">Analyse des rendements - Import dossier</h2>
    <p>Contenu import dossier...</p>

    <h2 id="about">À propos</h2>
    <p>Informations sur le projet...</p>
</div>

<script>
    // Gestion de l'activation du lien actif
    const links = document.querySelectorAll('.sidebar a');
    links.forEach(link => {
        link.addEventListener('click', () => {
            links.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
        });
    });
</script>

</body>
</html>

"""