from typing import DefaultDict


data = {
    "it": {
        "menu_home": "Home",
        "menu_maker_designer": "Maker e designer",
        "menu_ecommerce": "eCommerce",
        "menu_about_us": "Chi siamo",

        "generic_keep_in_touch_title": "Restiamo connessi",
        "generic_keep_in_touch_label": "A breve saremo online, ti contatteremo solo per offrirti sconti e anticipazioni per ripagare la tua fiducia",
        "generic_keep_in_touch_email_placeholder": "La tua Email",
        "generic_keep_in_touch_btn_send": "INVIA",
        "generic_keep_in_touch_msg": "Grazie per esserti registrato",
        "generic_keep_in_touch_error_msg": "Email è un campo obbligatorio",
        "generic_keep_in_touch_disclaimer": "Il tuo indirizzo di messaggistica è usato solamente per inviarti le nostre lettere informative e le informazioni relative alle attività di Tamatara S.r.l.. Puoi usare il link di disiscrizione integrato nella newsletter in qualsiasi momento.",

        "index_title1": "Diamo valore ad ogni oggetto,<br> creato su misura per te",
        "index_label1": "Semplifichiamo l'acquisto e la vendita di oggetti artigianali, di design ed ecosostenibili",
        "index_title2": "Artigianato, innovazione, made in Italy",
        "index_label2": "Il migliore negozio online dove le idee di designer internazionali trovano il modo di essere realizzate grazie alle abilità artigiane dei migliori makers italiani",
        "index_btn1": "Voglio saperne di più",
        "index_title3": "La nostra mission",
        "index_label3-1": "Mettere in contatto persone che cercano prodotti unici e di qualità con i migliori maker del Made in Italy, ad un prezzo equo, favorendo cosi lo sviluppo dell'artigianato 4.0",
        "index_label3-2": "Valorizziamo i migliori designers internazionali e makers italiani svelando le loro creazioni ed aiutandoli a promuovere il loro business, offrendo tecnologia, user experience, strumenti di marketing e supporto logistico",
        "index_title4": "Creativi, con passione",
        "index_label4": "Ampliamo l'orizzonte dell'oggettistica artgianale semplificando il contatto tra persone",
        "index_designer": "Designer",
        "index_lbl_designer": "Trasformiamo le tue creazioni in oggetti per i nostri clienti, tutelando le tue opere digitali",
        "index_maker": "Maker",
        "index_lbl_maker": "Lavora con la tua passione, crea con la stampante 3D e mostra le tue abilità artigiane",
        "index_client": "Cliente",
        "index_lbl_client": "Uniamo artigianalità, tecnologia e design per creare oggetti unici al momento del tuo acquisto",
        "index_title5": "I migliori artigiani digitali italiani",
        "index_label5": "Per creare con cura ogni oggetto servono i migliori: la nostra rete di artigiani digitali, makers e designers, saranno in grado di realizzare tutto ciò che è pensabile. La rete è in continua espansione, se vuoi <b>lavorare</b> con le tue abilità di <b>stampa 3D</b> e di <b>design</b> sei nel posto giusto",
        "index_btn2": "Espandi il tuo business",
        "index_title6": "Molto più di un eCommerce",
        "index_title7": "Parlano di noi",

        "maker_title1": "Sei un maker e/o un designer?",
        "maker_label1": "Potresti essere tra i primi ad usufruire dei vantaggi di Tamatara",
        "maker_btn1": "Voglio saperne di più",
        "maker_title2": "La tua stampante 3D, le tue abilità artigiane, il nostro aiuto, niente di più",
        "maker_label2": "Offriamo una piattaforma innovativa in grado di proporti a clienti secondo le tue abilità artigiane",
        "maker_maker_title1": "Lavora con noi",
        "maker_maker_label1": "Approfitta dei nostri servizi gratuiti per espandere il tuo business",
        "maker_maker_title2": "Stampa in 3D",
        "maker_maker_label2": "Grazie alle tue stampanti 3D realizzerai oggetti per i nostri clienti",
        "maker_maker_title3": "Tecniche artigiane",
        "maker_maker_label3": "Crediamo nelle tue abilità e nel valore della post-produzione",
        "maker_title3": "Avrai a disposizione tutto quello che ti serve per soddisfare i tuoi clienti",
        "maker_label3-1": "Semplifichiamo il tuo lavoro fornendoti il modello 3D già pronto per la stampa, con dettagli specifici e guide per eventuali lavori di post-produzione. Tu mettici le tue abilità, noi ti portiamo i clienti",
        "maker_label3-2": "La nostra vision è rendere accessibile e semplice l'artigianato digitale. Tamatara nasce come eCommerce per clienti amanti di oggetti artigianali e su misura. Crediamo fortemente che la community di makers italiani sia pronta ad entrare con profitto nel mercato di consumo, supportata da servizi innovativi e formazione su misura",
        "maker_title4": "Designer, sei pronto a guadagnare dalle tue idee?",
        "maker_label4": "I tuoi modelli 3D comporranno il nostro catalogo, i clienti vedranno un oggetto finito con la possibilità di comprarlo come tu lo hai immaginato",
        "maker_designer_title1": "Proponi le tue creazioni",
        "maker_designer_label1": "Sei tu la mente, formiamo artigiani digitali per trasformarle in realtà",
        "maker_designer_title2": "Licenza e copyright",
        "maker_designer_label2": "Proteggiamo i tuoi file con firma digitale e contratti specifici",
        "maker_designer_title3": "Esplora il potenziale",
        "maker_designer_label3": "Lasciati guidare dai nostri servizi gratuiti per diffondere la tua idea",
        "maker_title5": "Tamatara è pensata per rendere la tua idea riproducibile in sicurezza",
        "maker_label5-1": "Saremo la tua vetrina agli occhi del mondo, proteggendo le tue idee e garantendoti che solo i migliori makers avranno accesso ai tuoi modelli 3D per soddisfare i clienti. Un singolo upload, una vetrina infinita e gratuita",
        "maker_label5-2": "Grazie a software specifici e contratti stipulati al momento dell'ordine ci impegnamo a garantire il massimo riserbo per i tuoi modelli 3D. Solo il maker incaricato dal cliente per stampare la tua idea avrà accesso esclusivo al file. Ti basterà caricarlo, inserire le informazioni utili per riprodurlo come tu lo hai pensato e impostare un prezzo per il singolo uso commerciale",
        "maker_title6": "Restiamo in contatto",
        "maker_label6": "A breve lanceremo la beta-test e ci piacerebbe averti a bordo per poterti mostrare in anteprima le potenzialità di Tamatara",
        "maker_form_firstname": "Nome <sup>*</sup>",
        "maker_form_lastname": "Cognome <sup>*</sup>",
        "maker_form_email": "Email <sup>*</sup>",
        "maker_form_phone": "Numero di telefono",
        "maker_form_ima": "Sono un <sup>*</sup>",
        "maker_form_ima_maker": "Maker",
        "maker_form_ima_designer": "Designer",
        "maker_form_ima_maker_designer": "Maker/Designer",
        "maker_form_category": "Sono specializzato in queste categorie merceologiche <sup>*</sup>",
        "maker_form_category_art": "Arte e oggetti da collezione",
        "maker_form_category_home": "Casa e arredi",
        "maker_form_category_dpi": "Dispositivi (DPI)",
        "maker_form_category_robotics": "Elettronica e robotica",
        "maker_form_category_gadgets": "Gadgets",
        "maker_form_category_games": "Giocattoli e intrattenimento",
        "maker_form_category_jewelery": "Gioielli e accessori",
        "maker_form_category_cosplay": "Miniature e Cosplay",
        "maker_form_category_other": "Altro",
        "maker_form_error_msg": "Riempi i campi obbligatori",

        "client_title1": "Prodotti unici ideati da designers internazionali creati al momento del tuo ordine da artigiani italiani",
        "client_label1": "L'unico negozio online semplice, divertente ed economico in grado di offrirti l'unicità dell'artigianato insieme alle potenzialità della stampa 3D",
        "client_title2": "Immagina le potenzialità della creatività unite alla tecnica e all'ecosostenibilità",
        "client_label2": "Acquistare un oggetto unico sfuttando le abilità degli artigiani digitali italiani non è mai stato cosi semplice",
        "client_block_title1": "Creato per te",
        "client_block_label1": "Ogni oggetto che sceglierai verrà creato al momento grazie alla stampante 3D ed a tecniche artigiane manuali. E si, potrai personalizzarlo",
        "client_block_title2": "Innovare è migliorare",
        "client_block_label2": "Offriamo una vetrina agli artigiani delle nostre città, valorizzandoli. Inoltre la stampante 3D crea oggetti a basso impatto ambientale e con materiali ecosostenibili",
        "client_block_title3": "Semplice",
        "client_block_label3": "Facilitiamo il contatto tra creatività, tecnologia e oggettistica di consumo. Acquistare oggetti innovativi non è mai stato cosi semplice",
        "client_title3": "Crediamo che la realizzazione di ogni singolo oggetto sia il valore aggiunto di un acquisto",
        "client_label3-1": "Non più oggettistica in serie, valorizziamo ogni grammo di materiale utilizzato per soddisfare le tue esigenze, aiutando il tuo territorio e la natura",
        "client_label3-2": "In Tamatara troverai un vasto catalogo di oggettistica di design, gadget, modellismo, giocattoli, gioiellistica. Tutto quello che è pensabile è realizzabile grazie alla creatività dei designers e le capacità artigiane e tecniche dei makers. Ogni acquisto aiuterà gli artigiani digitali italiani a rilanciare l'oggettistica made in Italy",

        "team_title1": "Chi siamo",
        "team_label1": "Tamatara nasce per dare lavoro e visibilità agli artigiani digitali. Le nostre competenze si intersecano al meglio per perseguire questa visione",
        "team_title2": "La vision",
        "team_label2": "Siamo una start-up innovativa nel settore dell’eCommerce che sfrutta le potenzialità della stampa 3D e le abilità dei makers italiani per rendere accessibile e sostenbile l'acquisto di prodotti artigianali realizzati al momento. Per fare ciò siamo da sempre guidati da una vision ben precisa:",
        "team_title_vision1": "Creare opportunità lavorative",
        "team_label_vision1": "Il primo concept di Tamatara è nato per formare e dare lavoro a ragazzi universitari. Siamo una vetrina gratuita per tutti i professionisti o appassionati che intendono guadagnare con le loro abilità, favorendo così lo sviluppo dell'ecosistesma dell'artigianato 4.0 italiano.",
        "team_title_vision2": "Innovare l'artigianato",
        "team_label_vision2": "Uniamo l'artigianato Made in Italy con la tecnologia della stampa 3D. Questo permette di creare oggetti unici su misura per il cliente, con materiali innovativi e ecosostenibili, con il minor spreco possibile di materiale e con tutte le potenzialità che il digitale offre.",
        "team_title_vision3": "Facilitare il contatto",
        "team_label_vision3": "La community di artigiani digitali italiani è ricca di talento e di tecnica ma fatica a trovare un linguaggio comune con il consumatore. Tamatara vuole facilitare questa comunicazione ed investire in campagne mirate a diffondere il valore aggiunto di un oggetto che viene realizzato grazie al contatto tra l'idea di un designer internazionale e le abilità di un artigiano digitale italiano.",
        "team_title3": "Il Team",
        "team_label3": "Crediamo fermamente nelle relazioni e nel creare reti positive. Ognuno con le sue capacità umane e professionali porta il valore aggiunto utile a perseguire nella nostra vision. <br>Uniti si cambia, singolarmente si eccelle",

        "team_andrea_desc": "Laureato in sociologia, con esperienze nello sviluppo front-end e nella gestione delle risorse umane. Da sempre appassionato di tecnologia e di come questa possa influire nella psicologia umana e nelle dinamiche sociali.",
        "team_andrea_cit": "“Credo fermamente che innovazione sia sinonimo di relazioni sociali ed uso etico della tecnologia”",
        "team_gabriele_desc": "Laureato in economia aziendale e management alla Bocconi con esperienze in grandi realtà aziendali, appassionato di tecnologia fin da bambino cresce con la visione che le tecnologie possano creare un mondo a misura d’uomo.",
        "team_gabriele_cit": "“Con il talento puoi avere successo, con la dedizione ed il sacrificio puoi superare ogni limite”",
        "team_fabio_desc": "Laureato in business administration e management. Esperienza professionale maturata nel settore dei servizi con una comprovata storia di lavoro nel project management, gestione del brand e sviluppo del business. Appassionato di innovazione, marketing e comunicazione d'impresa in genere, ovunque questo implichi l'utilizzo delle nuove tecnologie.",
        "team_fabio_cit": "“Non si può descrivere la passione, la si può solo vivere”",
        "team_ilario_desc": "Laureato in informatica e con una grande passione per tutto ciò che è tecnologia e innovazione, attraverso gli anni vissuti in aziende  IT, insegue e promuove a 360 gradi le nuove tecnologie e i sistemi di ultima generazione.",
        "team_ilario_cit": "“Nel momento in cui dubiti di poter volare, perdi per sempre la facoltà di farlo”"
    },
    "en": {
        "menu_home": "Home",
        "menu_maker_designer": "Maker and Designer",
        "menu_ecommerce": "eCommerce",
        "menu_about_us": "About us",
        "generic_keep_in_touch_title": "Let's stay connected",
        "generic_keep_in_touch_label": "As soon as we will be online, we will contact you just to offer you discounts and advances to return your trust",
        "generic_keep_in_touch_email_placeholder": "Your Email address",
        "generic_keep_in_touch_btn_send": "SUBMIT",
        "generic_keep_in_touch_msg": "Thank you for registering",
        "generic_keep_in_touch_error_msg": "Email is a mandatory field",
        "generic_keep_in_touch_disclaimer": "Your email address is only used to send you information about Tamatara S.r.l. activities. You can use the unsubscribe link embedded in the newsletter at any time.",
        "index_title1": "We provide value to every item,<br> tailor-made for you.",
        "index_label1": "We make it easier to buy and sell design and eco-friendly handcrafted items.",
        "index_title2": "Handcrafts, innovation, made in Italy",
        "index_label2": "The best online store where the ideas of international designers find a way to be realized thanks to the craft skills of the best Italian makers",
        "index_btn1": "I want to know more",
        "index_title3": "Our mission",
        "index_title3-1": "Connect people looking for unique and high quality products with the best makers of Made in Italy, at a fair price, thus promoting the development of the handcrafted 4.0",
        "index_title3-2": "We highlight the best international designers and Italian makers by unveiling their creations and helping them to promote their business, offering technology, user experience, marketing tools and logistical support.",
        "index_title4": "Creative, with passion",
        "index_label4": "We broaden the horizon of handcrafted items by simplifying the connection between people",
        "index_designer": "Designer",
        "index_lbl_designer": "We turn your creations into items for our customers, protecting your digital works",
        "index_maker": "Maker",
        "index_lbl_maker": "Work with passion, create with a 3D printer, and show off your craft skills",
        "index_client": "Customer",
        "index_lbl_client": "We combine craftsmanship, technology and design to create unique items at the time of your purchase",
        "index_title5": "The best Italian digital craftsmen",
        "index_label5": "To create every item with attention you need the best: our network of digital craftsmen, makers and designers will be able to make everything you can think of. The network is constantly expanding, if you want to <b>work</b> with your <b>3D printing</b> and <b>design skills</b>, you're in the best place.",
        "index_btn2": "Boost your business",
        "index_title6": "More than an eCommerce",
        "index_title7": "What people are saying about us",
        "maker_title1": "Are you a maker and/or designer?",
        "maker_label1": "You could be one of the first to enjoy the many opportunities offered by Tamatara.",
        "maker_btn1": "I want to know more",
        "maker_title2": "Your 3D printer, your craft skills, our help, nothing more.",
        "maker_label2": "We offer an innovative platform that can introduce you to customers by your craft skills",
        "maker_maker_title1": "Work with us",
        "maker_maker_label1": "Take advantage of our free services to grow your business",
        "maker_maker_title2": "3D Printing",
        "maker_maker_label2": "With a 3D printer, you'll make items for your customers.",
        "maker_maker_title3": "Handicraft skills",
        "maker_maker_label3": "We believe in your skills and the value of post-production",
        "maker_title3": "You'll have everything you need to satisfy your customers",
        "maker_title3-1": "We make your job easier by providing you with the 3D model ready for printing, with specific details and guides for post-production work. You get your skills, we provide customers.",
        "maker_title3-2": "Our vision is to making digital crafting accessible and simple. Tamatara was born as an eCommerce for customers who love handcrafted and custom objects. We strongly believe that the Italian makers community is ready to profitably enter the consumer market, supported by innovative services and customized training.",
        "maker_title4": "Designer, are you ready to make profit from your ideas?",
        "maker_label4": "Your 3D models will be part of our catalog, customers will see a ready-made item with the possibility to buy it as you imagined it.",
        "maker_designer_title1": "Suggest your designs",
        "maker_designer_label1": "You are the mastermind, we train digital craftsmen to transform them into reality",
        "maker_designer_title2": "License and copyright",
        "maker_designer_label2": "We protect your files with digital signatures and specific contracts",
        "maker_designer_title3": "Explore the potential",
        "maker_designer_label3": "Let our free services guide you in spreading your idea",
        "maker_title5": "Our marketplace is designed to make your idea safely repeatable",
        "maker_title5-1": "We'll be your showcase to the world, protecting your ideas and ensuring that only the best makers will have access to your 3D models to satisfy customers. A single upload, an infinite free showcase",
        "maker_title5-2": "With specific software and contracts in place at the time of the order, we are committed to ensuring the confidentiality of your 3D models. Only the maker assigned by the customer to print your idea will have exclusive access to the file. All you have to do is upload it, enter the information needed to reproduce it as you intended, and set a price for single commercial use.",
        "maker_title6": "Let's stay connected ",
        "maker_label6": "Soon we will launch the beta test and we would love to have you on board to preview the Tamatara potential.",
        "maker_form_firstname": "First name <sup>*</sup>",
        "maker_form_lastname": "Last name <sup>*</sup>",
        "maker_form_email": "Email <sup>*</sup>",
        "maker_form_phone": "Phone number",
        "maker_form_ima": "I'm a <sup>*</sup>",
        "maker_form_ima_maker": "Maker",
        "maker_form_ima_designer": "Designer",
        "maker_form_ima_maker_designer": "Maker/Designer",
        "maker_form_category": "I specialize in these categories <sup>*</sup>",
        "maker_form_category_art": "Art and collectibles",
        "maker_form_category_home": "Home and furnishings",
        "maker_form_category_dpi": "Devices (DPI)",
        "maker_form_category_robotics": "Electronics and robotics",
        "maker_form_category_gadgets": "Gadgets",
        "maker_form_category_games": "Toys and entertainment",
        "maker_form_category_jewelery": "Jewelery and accessories",
        "maker_form_category_cosplay": "Miniatures and Cosplay",
        "maker_form_category_other": "Other",
        "maker_form_error_msg": "Mandatory fields are missing",
        "client_title1": "Unique items from international designers created by Italian craftsmen at the time of your order",
        "client_label1": "The only simple, fun and affordable online store that offers the uniqueness of craftsmanship with the power of 3D printing.",
        "client_title2": "Imagine the creative potential combined with technology and eco-sustainability.",
        "client_label2": "Buying a unique item using the skills of Italian digital craftsmen has never been this easy",
        "client_block_title1": "Designed for you",
        "client_block_label1": "Every item you choose will be created on the spot with a 3D printer and hand crafting techniques. And yes, you can customize it",
        "client_block_title2": "To innovate is to improve",
        "client_block_label2": "We offer a platform to showcase the craftsmen of our cities, highlighting them. In addition, the 3D printer creates items with low environmental impact and sustainable materials.",
        "client_block_title3": "Easy",
        "client_block_label3": "We simplify the contact between creativity, technology and consumer items. Buying innovative items has never been so easy",
        "client_title3": "We believe that the creation of each item is the extra value of a purchase",
        "client_title3-1": "No more mass-produced items, we enhance every single gram of material used to meet your needs, helping your country and the nature",
        "client_title3-2": "In Tamatara you will find a vast catalog of design items, gadgets, models, toys, jewelry. Everything that is conceivable is achievable thanks to the creativity of designers and the craftsmanship and technical skills of the makers. Each purchase will help the Italian digital craftsmen to boost the item made in Italy.",
        "team_title1": "About us",
        "team_label1": "Tamatara was founded to provide business and visibility to digital craftsmen. Our skills cross the best to follow this vision",
        "team_title2": "Our vision",
        "team_label2": "We are an innovative start-up in the eCommerce sector that uses the potential of 3D printing and the skills of Italian makers to make the purchase of handmade items accessible and sustainable. To do this, we have always been guided by a very specific vision:",
        "team_title_vision1": "Create job opportunities",
        "team_label_vision1": "The first concept of Tamatara was created to train and give work to university students. We are a free showcase for all professionals or enthusiasts who want to earn with their skills, thus promoting the development of the ecosystem of Italian craftsmanship 4.0.",
        "team_title_vision2": "Innovate craftsmanship",
        "team_label_vision2": "We combine Made in Italy craftsmanship with 3D printing technology. This allows us to create unique items tailored to the customer, with innovative and environmentally sustainable materials, with the least possible waste of material and with all the potential that digital offers.",
        "team_title_vision3": "Facilitate contact",
        "team_label_vision3": "The community of Italian digital craftsmen is talented and technical but struggles to reach a common language with the consumer. Tamatara wants to facilitate this communication and invest in targeted campaigns to spread the added value of an item that is made thanks to the contact between the idea of an international designer and the skills of an Italian digital craftsman.",
        "team_title3": "About the Team",
        "team_label3": "We firmly believe in relationships and in creating positive networks. Each one with his human and professional skills provides the added value useful to pursue our vision. <br>Together we change, individually we excel"
    },
    "fr": {
        "menu_home": "Accueil",
        "menu_maker_designer": "Maker et designer",
        "menu_ecommerce": "eCommerce",
        "menu_about_us": "Qui sommes-nous?",
        "generic_keep_in_touch_title": "On reste connecté",
        "generic_keep_in_touch_label": "Nous serons bientôt en ligne, nous vous contacterons pour vous offrir des rabais et des promotions pour le renouvellement de votre confiance",
        "generic_keep_in_touch_email_placeholder": "Votre email",
        "generic_keep_in_touch_btn_send": "ENVOYER",
        "generic_keep_in_touch_msg": "Merci de votre inscription",
        "generic_keep_in_touch_error_msg": "L'email est un champ obligatoire",
        "generic_keep_in_touch_disclaimer": "Votre adresse de messagerie n'est utilisée que pour vous envoyer nos lettres d'information et des informations sur les activités de Tamatara S.r.l. Vous pouvez utiliser le lien de désabonnement intégré dans la lettre d'information à tout moment.",
        "index_title1": "Nous donnons de la valeur à chaque objet,<br> réalisé sur mesure pour vous. ",
        "index_label1": "Nous facilitons l'achat et la vente d'objets artisanaux, riches en design et écologiques.",
        "index_title2": "Artisanat, innovation, made in Italy",
        "index_label2": "La meilleure boutique en ligne où les idées des designers internationaux trouvent un moyen d'être réalisées grâce au savoir-faire des meilleurs makers italiens",
        "index_btn1": "J’aimerais en savoir plus",
        "index_title3": "Notre mission",
        "index_title3-1": "Mettre en relation les personnes à la recherche de produits uniques et de qualité avec les meilleurs maker du Made in Italy, à un prix équitable, encourageant ainsi le développement de l'artisanat 4.0",
        "index_title3-2": "Nous valorisons les meilleurs designers internationaux et  makers italiens en dévoilant leurs créations et en les aidant à promouvoir leur entreprise, en leur offrant la technologie, l'expérience utilisateur, les outils marketing et le soutien logistique.",
        "index_title4": "Creatifs avec passion",
        "index_label4": "Nous élargissons l'horizon des objets artisanaux en simplifiant le contact entre les personnes",
        "index_designer": "Designer",
        "index_lbl_designer": "Nous transformons vos créations en objets pour nos clients, en protégeant vos œuvres numériques",
        "index_maker": "Maker",
        "index_lbl_maker": "Travaillez avec votre passion, créez avec l'imprimante 3D et révélez vos talents d’artisans",
        "index_client": "Client",
        "index_lbl_client": "Nous conjuguons savoir-faire, technologie et design pour créer des objets uniques au moment de votre achat",
        "index_title5": "Les meilleurs artisans digital italiens du numérique",
        "index_label5": "Pour créer chaque objet avec soin, il vous faut le meilleur: notre réseau d'artisans, de makers et de designers pourra réaliser tout ce à quoi vous pouvez penser. Le réseau est en constante expansion, si vous voulez <b>travailler</b> avec vos compétences en matière d'<b>impression</b> et de <b>conception 3D</b>, vous êtes au bon endroit",
        "index_btn2": "Développez vos activités",
        "index_title6": "Bien plus qu’un eCommerce",
        "index_title7": "On parle de nous",
        "maker_title1": "Vous êtes maker et/ou designer ?",
        "maker_label1": "Vous pourriez être l'un des premiers à profiter des avantages de Tamatara.",
        "maker_btn1": "J’aimerais en savoir plus",
        "maker_title2": "Ton imprimante 3D, ton savoir-faire, notre aide, rien de plus",
        "maker_label2": "Nous offrons une plateforme innovante pour vous proposer aux clients en fonction de vos compétences artisanales",
        "maker_maker_title1": "Travailler avec nous",
        "maker_maker_label1": "Profitez de nos services gratuits pour développer votre entreprise",
        "maker_maker_title2": "Impression en 3D",
        "maker_maker_label2": "Grâce à l'imprimante 3D, vous pourrez créer des objets pour vos clients",
        "maker_maker_title3": "Techniques artisanales",
        "maker_maker_label3": "Nous croyons en vos compétences et en la valeur de la post-production",
        "maker_title3": "Vous aurez tout ce dont vous avez besoin pour satisfaire vos clients",
        "maker_title3-1": "Nous vous facilitons la tâche en vous fournissant le modèle 3D prêt à être imprimé, avec des détails et des guides spécifiques pour tout travail de post-production. Vous apportez vos compétences, nous vous apportons des clients",
        "maker_title3-2": "Notre vision est de rendre l'artisanat digital accessible et simple. Tamatara est né comme un commerce électronique pour les clients qui aiment les objets faits à la main et personnalisés. Nous croyons fermement que la communauté des makers italiens est prête à entrer avec profit sur le marché de la consommation, soutenue par des services innovants et des formations adaptées.",
        "maker_title4": "Designer êtes-vous prêt à gagner de l'argent grâce à vos idées ?",
        "maker_label4": "Vos modèles 3D composeront notre catalogue, les clients verront un objet fini avec la possibilité de l'acheter tel que vous l'avez imaginé.",
        "maker_designer_title1": "Proposez vos créations",
        "maker_designer_label1": "Vous êtes le cerveau, nous formons des artisans digital pour les transformer en réalité",
        "maker_designer_title2": "Licence et droits d'auteur",
        "maker_designer_label2": "Nous protégeons vos fichiers par des signatures numériques et des contrats spécifiques",
        "maker_designer_title3": "Explorez le potentiel",
        "maker_designer_label3": "Laissez nos services gratuits vous guider dans la diffusion de votre idée",
        "maker_title5": "Tamatara est conçu pour rendre votre idée reproductible en toute sécurité",
        "maker_title5-1": "Nous serons votre vitrine aux yeux du monde entier, en protégeant vos idées et en veillant à ce que seuls les meilleurs makers aient accès à vos modèles 3D pour satisfaire les clients. Un seul téléchargement, une vitrine infinie et gratuite",
        "maker_title5-2": "Grâce à des logiciels spécifiques et des contrats stipulés lors de la commande, nous nous engageons à garantir une confidentialité maximale pour vos modèles 3D. Seul le maker désigné par le client pour imprimer votre idée aura un accès exclusif au fichier. Il vous suffit de le télécharger, de saisir les informations nécessaires pour le reproduire comme vous le souhaitez et de fixer un prix pour l'unique utilisation commerciale.",
        "maker_title6": "Nous gardons le contact",
        "maker_label6": "Nous allons bientôt lancer le bêta-test et nous aimerions vous avoir à bord pour vous permettre de découvrir les capacités de Tamatara.",
        "maker_form_firstname": "Prénom <sup>*</sup>",
        "maker_form_lastname": "Nom de famille <sup>*</sup>",
        "maker_form_email": "Courriel <sup>*</sup>",
        "maker_form_phone": "Numéro de téléphone",
        "maker_form_ima": "Je suis un <sup>*</sup>",
        "maker_form_ima_maker": "Maker",
        "maker_form_ima_designer": "Designer",
        "maker_form_ima_maker_designer": "Maker/Designer",
        "maker_form_category": "Je suis spécialisé dans les catégories suivantes",
        "maker_form_category_art": "Art et objets de collection",
        "maker_form_category_home": "Maison et ameublement",
        "maker_form_category_dpi": "Appareils (DPI)",
        "maker_form_category_robotics": "Electronique et robotique",
        "maker_form_category_gadgets": "Gadgets",
        "maker_form_category_games": "Jouets et divertissement",
        "maker_form_category_jewelery": "Bijoux et accessoires",
        "maker_form_category_cosplay": "Miniatures et cosplay",
        "maker_form_category_other": "Autre",
        "maker_form_error_msg": "Remplissez les champs obligatoires",
        "client_title1": "Des produits uniques créés par des designers internationaux et réalisés au moment de votre commande par des artisans italiens",
        "client_label1": "Le seul magasin en ligne simple, amusant et abordable qui vous offre le caractère unique de l'artisanat combiné à la puissance de l'impression 3D.",
        "client_title2": "Imaginez le potentiel de créativité combiné à la technologie et à l'éco-durabilité.",
        "client_label2": "Acheter un objet unique en utilisant les compétences des artisans digital italiens n'a jamais été aussi facile",
        "client_block_title1": "Créé pour vous",
        "client_block_label1": "Chaque objet que vous choisissez sera créé sur place grâce à l'imprimante 3D et aux techniques d'artisanat manuel. Et oui, vous pouvez le personnaliser",
        "client_block_title2": "Innover, c'est s'améliorer",
        "client_block_label2": "Nous offrons une vitrine aux artisans de nos villes, en les mettant en valeur. De plus, l'imprimante 3D permet de créer des objets à faible impact environnemental et des matériaux éco-durables.",
        "client_block_title3": "Simple",
        "client_block_label3": "Nous facilitons le contact entre la créativité, la technologie et les biens de consommation. Acheter des objets innovants n'a jamais été aussi facile",
        "client_title3": "Nous pensons que la réalisation de chaque article est la valeur ajoutée d'un achat",
        "client_title3-1": "Finis les objets produits en série, nous valorisons chaque gramme de matériau utilisé pour répondre à vos besoins, en aidant votre territoire et la nature",
        "client_title3-2": "À Tamatara, vous trouverez un vaste catalogue d'objets de design, de gadgets, de modélisme, de jouets et de bijoux. Tout ce qui est concevable est réalisable grâce à la créativité des designers et au savoir-faire artisanal et technique des makers. Chaque achat aidera les artisans numériques italiens à relancer les objets "made in Italy".",
        "team_title1": "Qui sommes-nous?",
        "team_label1": "Tamatara est née pour donner du travail et de la visibilité aux  artisans digital. Nos compétences se croisent au mieux pour poursuivre cette vision",
        "team_title2": "Découvrez notre vision",
        "team_label2": "Nous sommes une start-up innovante dans le secteur du commerce électronique qui exploite le potentiel de l'impression 3D et les compétences des makers italiens pour rendre l'achat de produits artisanaux accessible et durable. Pour ce faire, nous avons toujours été guidés par une vision très précise :",
        "team_title_vision1": "Créer des opportunités d'emploi",
        "team_label_vision1": "Le premier concept de Tamatara est né pour former et donner du travail aux étudiants universitaires. Nous sommes une vitrine gratuite pour tous les professionnels ou amateurs qui veulent gagner de l'argent avec leurs compétences, favorisant ainsi le développement de l'écosystème de l'artisanat italien 4.0.",
        "team_title_vision2": "Innover dans l'artisanat",
        "team_label_vision2": "Nous combinons l'artisanat Made in Italy avec la technologie d'impression 3D. Cela nous permet de créer des objets uniques adaptés au client, avec des matériaux innovants et respectueux de l'environnement, avec le moins de gaspillage possible et avec tout le potentiel qu'offre la technologie numérique.",
        "team_title_vision3": "Faciliter les contacts",
        "team_label_vision3": "La communauté des artisans digital italiens est riche en talent et en technique, mais elle lutte pour trouver un langage commun avec le consommateur. Tamatara veut faciliter cette communication et investir dans des campagnes visant à diffuser la valeur ajoutée d'un objet qui est réalisé grâce au contact entre l'idée d'un designer international et les compétences d'un artisans digital italien.",
        "team_title3": "L’équipe",
        "team_label3": "Nous croyons fermement aux relations et à la création de réseaux positifs. Chacun avec ses compétences humaines et professionnelles apporte la valeur ajoutée utile à la poursuite de notre vision. <br>Unis-nous changeons, individuellement nous excellons"
    }
}
DEFAULT_LANGUAGE = "it"

def get_language(lang):
    return {
        **data[DEFAULT_LANGUAGE],
        **data.get(lang, {})
    }
