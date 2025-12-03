
def generate_report(stats):

    html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Portail Dosimétrie & Productivité</title>
<style>
    body, html {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        background-color: f8f9fa;
    }}

    /* Sidebar */
    .sidebar {{
        height: 100%;
        width: 300px;
        position: fixed;
        top: 0;
        left: 0;
        background-color: #1a365d;
        padding-top: 20px;
        overflow-y: auto;
        box-shadow: 2px 0 5px rgba(0,0,0,0.2);
    }}

    /* Sidebar title */
    .sidebar h2 {{
        color: #f5f6fa;
        text-align: center;
        margin: 0 0 20px 0;
        font-size: 22px;
        letter-spacing: 1px;
    }}

    /* Section subtitles */
    .sidebar .section-title {{
        color: #d2dae2;
        padding: 8px 20px;
        font-size: 14px;
        font-weight: bold;
        text-transform: uppercase;
        background-color: #2c5282;
        margin-top: 15px;
        margin-bootom: 5px;
    }}

    /* Links */
    .sidebar a {{
        padding: 10px 20px;
        text-decoration: none;
        font-size: 16px;
        color: #f5f6fa;
        display: block;
        margin: 3px 10px;
        border-radius: 10px;
        transition: all 0.2s;
    }}

    /* Hover & active */
    .sidebar a:hover {{
        background-color: #485460;
        border-left: 4px solid #ffa502; /* accent orange */
        color: #fff;
    }}

    .sidebar a.active {{
        background-color: #57606f;
        border-left: 4px solid #ffa502;
    }}

    /* Scrollbar style */
    .sidebar::-webkit-scrollbar {{
        width: 8px;
    }}
    .sidebar::-webkit-scrollbar-thumb {{
        background-color: #718093;
        border-radius: 4px;
    }}

    /* header */
    .header {{
        margin-left: 300px;
        padding: 100px; 
        background-color: #1a365d;
    }}

    /* Main content */
    .content {{
        margin-left: 310px;
        padding: 30px;
    }}

    .content h2 {{
        color: #2f3640;
        margin-top: 30px;
    }}

    /* Cards metrics*/

    .metric-container {{
    display: flex;
    gap: 20px;
    flex-wrap: wrap; /* Passe à la ligne si trop de cards */
    margin-top: 20px;
    }}

    .metric-card {{
        background: #e2eafc;
        border-left: 5px solid #2c5282;
        padding: 15px 20px;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        min-width: 180px;
        flex: 1;
        max-width: 250px;
    }}

    .metric-card h3 {{
        color: #2c5282;
        font-size: 18px;
        margin-bottom: 5px;
    }}

    .metric-card p {{
        font-size: 24px;
        font-weight: bold;
        margin: 0;
        color: #1a365d;
    }}

</style>
</head>
<body>

<div class="sidebar">
    <h2>☢️ Portail dosimétrie</h2>

    <div class="section-title">NAVIGATION</div>
    <a href="#tableau-de-bord">Tableau de bord</a>
    <a href="#synthese-globale">Synthèse globale</a>

    <div class="section-title">DOSIMETRIE</div>
    <a href="#dosimetrie-arceaux-de-bloc">Arceaux de bloc</a>
    <a href="#dosimetrie-scanner-ct">Scanner CT</a>
    <a href="#dosimetrie-cardiologie">Cardiologie</a>
    <a href="#dosimetrie-vasculaire-nhc">Vasculaire NHC</a>
    <a href="#dosimetrie-vasculaire-htp">Vasculaire HTP</a>
    <a href="#dosimetrie-neuroradiologie">Neuroradiologie</a>
    <a href="#dosimetrie-interventionnel-Gangi">Interventionnel Gangi</a>
    <a href="#dosimetrie-medecine-nucleaire">Médecine nucléaire</a>
    <a href="#dosimetrie-radiologie-conventionnelle">Radiologie conventionnelle</a>
    <a href="#dosimetrie-mammographie">Mammographie</a>

    <div class="section-title">PRODUCTIVITE</div>
    <a href="#productivite-scanner">Scanners</a>
    <a href="#productivite-médecine-nucléaire">Médecine nucléaire</a>
    <a href="#ordonnancier-NHC">Ordonnancier NHC</a>

    <div class="section-title">OPTIMISATION</div>
    <a href="#NRI-&-plan-d'optimisation">NRI & plan d'optimisation</a>

    <div class="section-title">NRD</div>
    <a href="#NRD-scanner">Scanner</a>
    <a href="#NRD-médecine-nucléaire">Médecine nucléaire</a>
    <a href="#NRD-mammographie">Mammographie</a>
    <a href="#radiologie-conventionnelle">Radiologie conventionnelle</a>

    <div class="section-title">ANALYSES</div>
    <a href="#analyses-statistiques-arceaux">Statistiques arceaux</a>
    <a href="#analyse-approfondie">Analyse approfondie</a>
    <a href="#synthese-complete">Synthèse complète</a>

    <div class="section-title">RISQUE PROJETE</div>
    <a href="#cancer-pediatrique">Cancer pédiatrique CT</a>
        
</div>

<div class="header">
    <h1 style="color: #DCDCDC; font-size:28px; text-align: center;">
    Dosimétrie & Productivité</h1>
    <p style="color: #DCDCDC; font-size=20px;">
    Plateforme centralisée d'alayse dosimétrique et de productivité pour l'ensemble des services d'imagerie du CHU de Strasbourg.<br>
    Données consolidées de 2012 à 2025.</p>
</div>

<div class="content">

    <h2 id="tableau-de-bord" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    Tableau de bord</h2>
    <p>......................</p>




    <h2 id="synthese-globale" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    Sythèse globale</h2>
    <p>......................</p>




    <h2 id="dosimetrie-arceaux-de-bloc" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    Arceaux de bloc</h2>
    <div class='metric-container'>
        <div class='metric-card'>
            <h3>Nombre d'examen analysés</h3>
            <p>{stats["nombre de lignes analysées"]}</p>
        </div>

        <div class='metric-card'>
            <h3>Période analysée</h3>
            <p>{stats["période analysée"]} ({stats["nombre d'années analysées"]} ans)</p>
        </div>
    
        <div class='metric-card'>
            <h3>Nombre d'équipement</h3>
            <p>{stats["nombre d'équipement"]}</p>
        </div>
        <div class='metric-card'>
            <h3>Moyenne d'examens par an</h3>
            <p>{stats["moyenne d'examen par an"]}</p>
        </div>
        <div class='metric-card'>
            <h3>Nombre de site</h3>
            <p>{stats["nombre de site"]}</p>
        </div>
        <div class='metric-card'>
            <h3>Nombre d'alertes dosimétriques</h3>
            <p>{stats["nombre d'alerte de doses"]} ({stats["pourcentage alerte de doses"]}%)</p>
        </div>
    </div>




    <h2 id="dosimetrie-scanner-ct" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    dosimetrie-scanner-ct</h2>
    <p>........................</p>




    <h2 id="dosimetrie-cardiologie" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    dosimetrie-cardiologie</h2>
    <p>........................</p>




    <h2 id="dosimetrie-vasculaire-nhc" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    dosimetrie-vasculaire-nhc</h2>
    <p>......................</p>




    <h2 id="dosimetrie-vasculaire-htp" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    dosimetrie-vasculaire-htp</h2>
    <p>......................</p>

    


    <h2 id="dosimetrie-neuroradiologie" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    dosimetrie-neuroradiologie</h2>
    <p>..........................</p>




    <h2 id="dosimetrie-interventionnel-Gangi" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    dosimetrie-interventionnel-Gangi</h2>
    <p>........................</p>




    <h2 id="dosimetrie-medecine-nucleaire" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    dosimetrie-medecine-nucleaire</h2>
    <p>........................</p>




    <h2 id="dosimetrie-radiologie-conventionnelle" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    dosimetrie-radiologie-conventionnelle</h2>
    <p>......................</p>





    <h2 id="dosimetrie-mammographie" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    dosimetrie-mammographie</h2>
    <p>......................</p>





    <h2 id="productivite-scanner" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    productivite-scanner</h2>
    <p>..........................</p>





    <h2 id="productivite-médecine-nucléaire" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    productivite-médecine-nucléaire</h2>
    <p>........................</p>





    <h2 id="ordonnancier-NHC" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    ordonnancier-NHC</h2>
    <p>........................</p>





    <h2 id="NRI-&-plan-d'optimisation" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    NRI-&-plan-d'optimisation</h2>
    <p>......................</p>

    


    <h2 id="NRD-scanner" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    NRD-scanner</h2>
    <p>......................</p>






    <h2 id="NRD-médecine-nucléaire" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    NRD-médecine-nucléaire</h2>
    <p>..........................</p>




    <h2 id="NRD-mammographie" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    NRD-mammographie</h2>
    <p>........................</p>





    <h2 id="radiologie-conventionnelle" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    radiologie-conventionnelle</h2>
    <p>........................</p>

    




    <h2 id="analyses-statistiques-arceaux" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    analyses-statistiques-arceaux</h2>
    <p>......................</p>

    



    <h2 id="analyse-approfondie" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    analyse-approfondie</h2>
    <p>..........................</p>





    <h2 id="synthese-complete" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    synthese-complete</h2>
    <p>........................</p>






    <h2 id="cancer-pediatrique" style=
    "color: #2c5282;
    background: #ebf8ff;
    padding: 10px 14px;
    border-radius: 10px;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);">
    cancer-pediatrique</h2>
    <p>........................</p>





</div>

<script>
    // Gestion de l'activation du lien actif
    const links = document.querySelectorAll('.sidebar a');
    links.forEach(link => {{
        link.addEventListener('click', () => {{
            links.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
        }});
    }});
</script>

</body>
</html>

"""

    return html_content