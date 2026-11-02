# Contenido de la demo Hotel La Polar (Gijón) (es/en/fr/de). Hechos de lapolarhotel.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Matrimonial y dos camas','Triple / familiar'],'en':['Double bed and twin','Triple / family'],'fr':['Lit double et deux lits','Triple / familiale'],'de':['Doppelbett und zwei Betten','Dreibett / Familie']}
RD={
'es':['Cama de matrimonio de 135 cm (bajo petición) o dos camas individuales de 90 cm. Exteriores, luminosas y, en la mayoría, con terraza.','Con cama matrimonial y cama individual, o dobles con camas supletorias. También hay cunas, bajo petición y según disponibilidad.'],
'en':['A 135 cm double bed (on request) or two 90 cm single beds. Outward-facing, bright and mostly with a terrace.','With a double and a single bed, or doubles with extra beds. Cots are also available, on request and subject to availability.'],
'fr':['Lit double de 135 cm (sur demande) ou deux lits simples de 90 cm. Côté rue, lumineuses et le plus souvent avec terrasse.','Avec lit double et lit simple, ou doubles avec lits d’appoint. Lits bébé disponibles sur demande et selon disponibilité.'],
'de':['Doppelbett mit 135 cm (auf Anfrage) oder zwei Einzelbetten mit 90 cm. Nach außen gelegen, hell und meist mit Terrasse.','Mit Doppel- und Einzelbett oder Doppelzimmer mit Zustellbetten. Kinderbetten auf Anfrage und je nach Verfügbarkeit.']}
ART={
'hero':('waves',1211,['#16263a','#5f8fb0','#dbe8f0','#4f6577','#324657','#101b28']),
'intro':('skyline',1212,['#eef2f5','#f8fafb','#24577a','#52616d','#1d2b38']),
'r1':('arches',1221,['#e8eef2','#9fc0d6','#24577a','#52616d','#1d2b38']),
'r2':('waves',1222,['#16263a','#6a9bbd','#e0ecf3','#5a7183','#3a5163','#121e2c']),
'g1':('hills',1231,['#e3e8ec','#d3e2ec','#9fc0d6','#87929a','#5f6a72','#3e464c']),
'g2':('waves',1232,['#16263a','#5f8fb0','#dbe8f0','#4f6577','#324657','#101b28']),
'g3':('columns',1233,['#eef2f5','#f8fafb','#24577a','#52616d','#1d2b38']),
'g4':('skyline',1234,['#16263a','#6a9bbd','#e0ecf3','#5a7183','#3a5163','#121e2c'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel La Polar · Hotel junto a la playa de Poniente en Gijón',see_rooms='Ver habitaciones',hero_k='Gijón · Av. José Manuel Palacio, 20',hero_t='Duerme junto al mar, despierta en el corazón de Gijón',hero_s='A un paseo de la playa de Poniente y a tres minutos de la estación de tren.',
 intro_t='Un hotel con alma marinera',intro_p1='En una zona tranquila y bien comunicada: a pocos metros de la playa de Poniente, el Acuario y la estación de tren, y a un paseo de Cimadevilla, el puerto deportivo y el centro.',
 intro_p2='Desde La Polar la ciudad se recorre andando, y el carril bici pasa por la puerta. El Camino del Norte también: los peregrinos tienen servicios pensados para ellos.',
 stats=['24 habitaciones','Recepción 24 h','A 200 m del tren','Pet friendly'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='24 habitaciones exteriores y luminosas, la mayoría con terraza, con baño privado, wifi gratuito, calefacción y TV por cable.',
 svcs=['Recepción 24 horas','Parking privado, con suplemento y según disponibilidad','Se admite una mascota por habitación, bajo petición','Café para empezar la mañana','Servicios para peregrinos con credencial','Cunas y camas supletorias bajo petición'],
 loc_p='Avda. José Manuel Palacio Álvarez, 20 · 33212 Gijón, Asturias. Teléfono: 984 296 403. Correo: info@lapolarhotel.com.',
 chips=['¿Qué habitaciones tenéis?','¿Tenéis parking?','¿Admitís mascotas?','¿Cómo reservo?']),
'en':dict(title='Hotel La Polar · Hotel by Poniente beach in Gijón',see_rooms='See rooms',hero_k='Gijón · Av. José Manuel Palacio, 20',hero_t='Sleep by the sea, wake up in the heart of Gijón',hero_s='A short walk from Poniente beach and three minutes from the train station.',
 intro_t='A hotel with a seafaring soul',intro_p1='In a quiet, well-connected area: a few metres from Poniente beach, the Aquarium and the train station, and a walk from Cimadevilla, the marina and the centre.',
 intro_p2='From La Polar you can explore the city on foot, and the bike lane runs past the door. So does the Camino del Norte: pilgrims get services designed for them.',
 stats=['24 rooms','24-hour reception','200 m from the train','Pet friendly'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='24 bright, outward-facing rooms, most with a terrace, with private bathroom, free wifi, heating and cable TV.',
 svcs=['24-hour reception','Private parking, with a supplement and subject to availability','One pet per room allowed, on request','Café to start the morning','Services for pilgrims with a credential','Cots and extra beds on request'],
 loc_p='Avda. José Manuel Palacio Álvarez, 20 · 33212 Gijón, Asturias. Phone: +34 984 296 403. Email: info@lapolarhotel.com.',
 chips=['Which rooms do you have?','Do you have parking?','Do you allow pets?','How do I book?']),
'fr':dict(title='Hotel La Polar · Hôtel près de la plage de Poniente à Gijón',see_rooms='Voir les chambres',hero_k='Gijón · Av. José Manuel Palacio, 20',hero_t='Dormir près de la mer, se réveiller au cœur de Gijón',hero_s='À deux pas de la plage de Poniente et à trois minutes de la gare.',
 intro_t='Un hôtel à l’âme marine',intro_p1='Dans un quartier calme et bien desservi : à quelques mètres de la plage de Poniente, de l’Aquarium et de la gare, et à une promenade de Cimadevilla, du port de plaisance et du centre.',
 intro_p2='Depuis La Polar, la ville se parcourt à pied et la piste cyclable passe devant la porte. Le Camino del Norte aussi : des services sont pensés pour les pèlerins.',
 stats=['24 chambres','Réception 24 h/24','À 200 m du train','Animaux acceptés'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='24 chambres lumineuses côté rue, la plupart avec terrasse, avec salle de bains privée, wifi gratuit, chauffage et TV câblée.',
 svcs=['Réception 24 h/24','Parking privé, avec supplément et selon disponibilité','Un animal par chambre accepté, sur demande','Café pour commencer la matinée','Services pour pèlerins munis de la credencial','Lits bébé et lits d’appoint sur demande'],
 loc_p='Avda. José Manuel Palacio Álvarez, 20 · 33212 Gijón, Asturies. Téléphone : +34 984 296 403. E-mail : info@lapolarhotel.com.',
 chips=['Quelles chambres avez-vous ?','Avez-vous un parking ?','Acceptez-vous les animaux ?','Comment réserver ?']),
'de':dict(title='Hotel La Polar · Hotel am Strand von Poniente in Gijón',see_rooms='Zimmer ansehen',hero_k='Gijón · Av. José Manuel Palacio, 20',hero_t='Am Meer schlafen, im Herzen von Gijón aufwachen',hero_s='Ein kurzer Spaziergang zum Strand von Poniente, drei Minuten vom Bahnhof.',
 intro_t='Ein Hotel mit maritimer Seele',intro_p1='In ruhiger, gut angebundener Lage: wenige Meter vom Strand von Poniente, dem Aquarium und dem Bahnhof, und einen Spaziergang von Cimadevilla, dem Jachthafen und dem Zentrum.',
 intro_p2='Von La Polar aus erkunden Sie die Stadt zu Fuß, und der Radweg führt an der Tür vorbei. Ebenso der Camino del Norte: Für Pilger gibt es eigene Services.',
 stats=['24 Zimmer','Rezeption rund um die Uhr','200 m zum Bahnhof','Haustiere willkommen'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='24 helle Außenzimmer, meist mit Terrasse, mit eigenem Bad, kostenlosem WLAN, Heizung und Kabel-TV.',
 svcs=['Rezeption rund um die Uhr','Privatparkplatz gegen Aufpreis und je nach Verfügbarkeit','Ein Haustier pro Zimmer auf Anfrage','Café für den Start in den Morgen','Services für Pilger mit Credencial','Kinderbetten und Zustellbetten auf Anfrage'],
 loc_p='Avda. José Manuel Palacio Álvarez, 20 · 33212 Gijón, Asturien. Telefon: +34 984 296 403. E-Mail: info@lapolarhotel.com.',
 chips=['Welche Zimmer gibt es?','Gibt es einen Parkplatz?','Sind Haustiere erlaubt?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://lapolarhotel.greenchannel.es/lang/es';RN='https://lapolarhotel.greenchannel.es/lang/en'
BOOK=dict(mode='engine',url=dict(es=R,en=RN,fr=RN,de=RN))
D=dict(name='Hotel La Polar',ac='#16263a',ac2='#24577a',ac2_a11y='#1f4b69',book=BOOK,around=[],foot=FOOT,
 address='Avda. José Manuel Palacio Álvarez, 20 · 33212 Gijón',phones=['+34 984 296 403'],emails=['info@lapolarhotel.com'],maps='Hotel La Polar, Avenida José Manuel Palacio 20, 33212 Gijón',t=T)
META=dict(repo='demo-hotel-la-polar-gijon',name='Hotel La Polar',legal_name='ESTRELLA NORTE LA POLAR, S.L., NIF B33862418 (aviso legal de su web)',registry_ids=['B33862418'],
 url='https://lapolarhotel.com/',domain='lapolarhotel.com',municipality='Gijón',province='Asturias',sector='hotel junto a la playa de Poniente en Gijón',
 read_at='2026-11-02T09:27:00+01:00',created_at='2026-11-02T09:26:00+01:00',built_at='2026-11-02T09:40:00+01:00',audit_date='2026-11-02T09:27:00+01:00',
 rating=dict(value=4.1,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Hotel+LA+POLAR/@43.5402322,-5.6766252,17z'),
 book=dict(mode='engine',url=R,note='motor Green Channel incrustado en su pagina /reserva/ (iframe): https://lapolarhotel.greenchannel.es/lang/es (es) y /lang/en (en/fr/de), HTTP 200 (02/11/2026 09:29).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Tenéis parking?','K03'),('¿Admitís mascotas?','K04'),('¿Dónde estáis?','K05'),('¿Está cerca la estación de tren?','K06'),('¿Cómo reservo?','K07'),('¿Podéis confirmarme disponibilidad para mañana?','K07'),('¿Hay recepción 24 horas?','K08'),('Soy peregrino, ¿qué ofrecéis?','K09'),('¿Qué ver en Gijón?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Tenéis cuna?','K12'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('What do the rooms include?','K02'),('Do you have parking?','K03'),('Do you allow pets?','K04'),('Where are you?','K05'),('Is the train station close?','K06'),('How do I book?','K07'),('Can you confirm availability for tomorrow?','K07'),('Is reception open 24 hours?','K08'),('I am a pilgrim, what do you offer?','K09'),('What to see in Gijón?','K10'),('What is your phone number?','K11'),('Do you have a cot?','K12'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Que comprennent les chambres ?','K02'),('Avez-vous un parking ?','K03'),('Acceptez-vous les animaux ?','K04'),('Où êtes-vous ?','K05'),('La gare est-elle proche ?','K06'),('Comment réserver ?','K07'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K07'),('La réception est-elle ouverte 24 h/24 ?','K08'),('Je suis pèlerin, que proposez-vous ?','K09'),('Que voir à Gijón ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Avez-vous un lit bébé ?','K12'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was bieten die Zimmer?','K02'),('Gibt es einen Parkplatz?','K03'),('Sind Haustiere erlaubt?','K04'),('Wo liegt das Hotel?','K05'),('Ist der Bahnhof in der Nähe?','K06'),('Wie kann ich buchen?','K07'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K07'),('Ist die Rezeption rund um die Uhr besetzt?','K08'),('Ich bin Pilger, was bieten Sie?','K09'),('Was kann man in Gijón besichtigen?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Haben Sie ein Kinderbett?','K12'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
