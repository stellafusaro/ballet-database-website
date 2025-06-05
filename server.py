from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for, send_from_directory
app = Flask(__name__, static_folder="static")
#By Stella Fusaro
# Initial data
data = {
    "1": {
        "id": "1",
        "title": "Swan Lake",
        "image": "https://www.metopera.org/globalassets/season/abt/2022-abt/swan-lake/slbrandtcornejo2ro_1600x685.png",
        "year": "1877",
        "summary": "A prince falls in love with a princess cursed to live as a swan by day. He vows to break the spell, but a sorcerer tricks him into pledging his love to another. Realizing his mistake, the prince rushes to the lake, where he and the princess choose to die together, breaking the curse in death.",
	"composer": ["Pyotr Ilyich Tchaikovsky"],
        "choreographer": ["Marius Petipa", "Lev Ivanov"],
        "length": "2.5 - 3 hours",
        "genres": ["Classical", "Romantic", "Tragic", "Fantasy"],
        "similar ballet ids": ["2", "3", "10"],
        "other works by composer": ["The Nutcracker", "The Sleeping Beauty"],
        "other works by choreographer": ["Giselle", "Don Quixote"],
        "performing companies": [
            {"name": "American Ballet Theater", "location": "New York, NY", "performance_dates": "July 19-25, 2025"},
            {"name": "Royal Ballet", "location": "London, UK", "performance_dates": "March 10-15, 2025"}
        ],
        "talking points & iconic moments": [
            "Swan Lake wasn’t a big success when it premiered in 1877...",
            "The ‘32 fouettés’ in Act III, performed by Odile, is one of the most famous..."
        ],
    },
    "2": {
        "id": "2",
        "title": "The Nutcracker",
        "image": "https://static.standard.co.uk/2022/12/07/11/Isabella%20Gasparini%20as%20Clara%20and%20James%20Hay%20as%20Hans-Peter%20in%20The%20Nutcracker%2C%20The%20Royal%20Ballet%202022%20Asya%20Verzhbinsky%20%281%29.jpg?crop=8:5,smart&quality=75&auto=webp&width=1000",
        "year": "1892",
        "summary": "The plot of The Nutcracker follows a young girl named Clara, who receives a magical Nutcracker doll as a Christmas gift from her godfather, Drosselmeyer. That night, the Nutcracker comes to life and battles the Mouse King, with Clara's help. After the battle, the Nutcracker transforms into a handsome prince, and he takes Clara on a magical journey to the Land of Sweets. There, they are welcomed by the Sugar Plum Fairy, and Clara experiences various dances representing different sweets from around the world. Ultimately, Clara wakes up, and it's unclear whether the adventure was a dream or reality, but she is left with a sense of wonder and joy.",
        "composer": ["Pyotr Ilyich Tchaikovsky"],
        "choreographer": ["Marius Petipa", "Lev Ivanov"],
        "length": "2 hours",
        "genres": ["Fantasy", "Family", "Holiday"],
        "similar ballet ids": ["1", "5", "6"],
        "other works by composer": ["Swan Lake", "The Sleeping Beauty"],
        "performing companies": [
            {"name": "New York City Ballet", "location": "New York, NY", "performance_dates": "December 1-31, 2025"},
            {"name": "Mariinsky Ballet", "location": "St. Petersburg, Russia", "performance_dates": "December 10-25, 2025"}
        ],
        "talking points & iconic moments": [
            "The Sugar Plum Fairy’s pas de deux is one of the most famous ballet solos.",
            "The Nutcracker is often a child's first introduction to ballet."
        ],
    },
    "3": {
        "id": "3",
        "title": "Giselle",
        "image": "https://static01.nyt.com/images/2019/11/27/arts/22GISELLE-08/22GISELLE-08-superJumbo.jpg",
        "year": "1841",
        "summary": "Giselle follows a young peasant girl named Giselle, who falls in love with Albrecht, a nobleman disguised as a commoner. However, she discovers his true identity and that he is already promised to another woman, Bathilde. Heartbroken and devastated, Giselle dies of a broken heart.In the second act, Giselle's spirit is taken to the mystical realm of the Wilis, vengeful spirits of women who died before marriage. The Wilis, led by their queen Myrtha, try to force Albrecht to dance to his death. Giselle, still in love with him, protects him by forgiving him and dancing with him until dawn, which saves him from the curse. As the sun rises, Giselle's spirit fades, and Albrecht is left heartbroken but redeemed by her forgiveness",
        "composer": ["Adolphe Adam"],
        "choreographer": ["Jean Coralli", "Jules Perrot"],
        "length": "2 hours",
        "genres": ["Romantic", "Tragic", "Supernatural"],
        "similar ballet ids": ["1", "4", "7"],
        "performing companies": [
            {"name": "Bolshoi Ballet", "location": "Moscow, Russia", "performance_dates": "October 10-20, 2025"},
            {"name": "Paris Opera Ballet", "location": "Paris, France", "performance_dates": "November 5-15, 2025"}
        ],
        "talking points & iconic moments": [
            "Giselle Act II is one of the most ethereal and haunting sections of ballet.",
            "The role of Giselle requires both incredible technique and dramatic acting."
        ],
    },
    "4": {
    	"id": "4",
  	"title": "La Bayadère",
	"image": "https://oslodesk.com/wp-content/uploads/2022/03/la-bayadere-2019-foto-erik-berg-10-1024x684.jpg",
    	"year": "1877", 
	"summary": "La Bayadère centers on a tragic love story set in ancient India. It follows Nikiya, a temple dancer (bayadère), and her forbidden love for Solor, a noble warrior. Solor is promised to the Rajah's daughter, Gamzatti, but he is in love with Nikiya.When Gamzatti finds out about their love, she becomes jealous and schemes to get rid of Nikiya. She tricks the high priest into convincing Nikiya to dance for her, where she is poisoned by a snake hidden in a basket. Nikiya dies in Solor’s arms, and he is heartbroken.In the afterlife, Nikiya becomes a spirit and is reunited with Solor in a dream-like vision. The ballet concludes with tragedy as both Nikiya and Solor are separated forever by the forces of fate, leaving behind the haunting memory of their love.",
	"composer": ["Léo Delibes", "Frédéric Chopin (some revisions)"], 
	"choreographer": ["Marius Petipa"], 
	"length": "2.5 - 3 hours", 
	"genres": ["Romantic", "Tragic", "Ballet", "Fantasy"], 
	"similar ballet ids": ["1", "3", "4"], 
	"other works by composer": ["Coppélia", "Sylvia"],
	"other works by choreographer": ["The Nutcracker", "Sleeping Beauty"],
    	"performing companies": [
             {"name": "Mariinsky Ballet", "location": "St. Petersburg, Russia", "performance_dates": "March 5-15, 2025"},
             {"name": "American Ballet Theatre", "location": "New York, NY", "performance_dates": "April 1-10, 2025"}
    	],	
    	"talking points & iconic moments": [
            "The Kingdom of the Shades scene in Act II is one of the most iconic moments in ballet, showcasing a mass corps de ballet of 24 dancers performing a perfectly synchronized series of arabesques.",
            "La Bayadère was a critical success but not initially a box-office hit, especially due to the complexity and scale of its choreography.",
            "The ballet’s tragic ending, with Nikiya’s spirit appearing to Solor, is a powerful and poignant exploration of love beyond the grave."
    	],
    },

    "5": {
    	"id": "5",
    	"title": "Le Corsaire",
    	"image": "https://images.seattleschild.com/wp-content/uploads/2020/05/LeCorsaire2015_LT_054-scaled.jpg",
    	"year": "1856",
    	"summary": "Le Corsaire follows the story of Conrad, a pirate captain, and his love for Medora, a beautiful young woman. Conrad and his crew raid a slave market and steal Medora, who is sold to the Pasha, a wealthy ruler. Conrad and Medora fall in love, and he promises to free her from the Pasha’s control.However, the Pasha becomes infatuated with Medora and tries to keep her, leading to a series of struggles. Conrad and his pirates attempt to escape with Medora, but they are betrayed by one of the pirates, who seeks the Pasha's favor. In the end, Conrad and Medora's love triumphs, and they escape together, but the ballet ends with a dramatic, tragic twist as the consequences of betrayal and passion come to light.",
	"composer": ["Adolphe Adam"],
    	"choreographer": ["Marius Petipa", "Jean Coralli"],
    	"length": "2.5 - 3 hours",
    	"genres": ["Romantic", "Adventure", "Ballet"],
    	"similar ballet ids": ["1", "2", "4"],
    	"other works by composer": ["Giselle", "Le Roi d'Yvetot"],
    	"other works by choreographer": ["The Nutcracker", "Coppélia"],
    	"performing companies": [
            {"name": "Bolshoi Ballet", "location": "Moscow, Russia", "performance_dates": "April 10-20, 2025"},
            {"name": "Paris Opera Ballet", "location": "Paris, France", "performance_dates": "May 15-25, 2025"}
    	],
    	"talking points & iconic moments": [
            "The Grand Pas de Deux between Conrad and Medora in Act II is one of the most famous ballet duets, with intricate lifts and breathtaking partnering.",
            "The ballet's mix of comedic and dramatic moments, including the pirates' fight scenes and the auction of the slaves, provides an exciting narrative balance.",
            "Le Corsaire is known for its large-scale productions with extravagant sets and costumes, particularly in its famous scene depicting the harem."
    	],
    },

    "6": {
    	"id": "6",
    	"title": "Don Quixote",
    	"image": "https://dancetabs.com/wp-content/uploads/2017/05/roc-donq-misty-copeland-jeffrey-cirio-guitar_1000.jpg",
    	"year": "1869",
    	"summary": "Don Quixote ballet follows the adventures of the noble yet delusional Don Quixote, who, inspired by chivalric romances, embarks on a quest to revive knighthood. He believes in the ideal of true love and sets out with his loyal squire, Sancho Panza, to seek adventures. Along the way, Don Quixote encounters Kitri, a young woman, and Basilio, her true love, who is a poor but passionate barber.Kitri's father wants her to marry the wealthy but pompous suitor, Gamache, but Kitri and Basilio are determined to be together. Don Quixote mistakes Kitri for his idealized lady, Dulcinea, and tries to help her in her quest for true love. After various comedic and dramatic misunderstandings, Kitri and Basilio triumph in their love, and Don Quixote, having completed his quest, returns home, content with the belief that he has fulfilled his noble ideals.",
	"composer": ["Ludwig Minkus"],
    	"choreographer": ["Marius Petipa"],
    	"length": "2.5 - 3 hours",
    	"genres": ["Classical", "Romantic", "Comedic"],
    	"similar ballet ids": ["1", "2", "3"],
    	"other works by composer": ["La Bayadère", "Coppélia"],
    	"other works by choreographer": ["The Nutcracker", "Sleeping Beauty"],
    	"performing companies": [
            {"name": "Mariinsky Ballet", "location": "St. Petersburg, Russia", "performance_dates": "April 5-15, 2025"},
            {"name": "Royal Ballet", "location": "London, UK", "performance_dates": "May 1-10, 2025"}
    	],
	"talking points & iconic moments": [
	    "The 'Grand Pas de Deux' between Kitri and Basilio in Act III is one of the most famous and technically challenging moments in classical ballet.",
            "Don Quixote’s comedic scenes, such as his delusional battles with windmills and his mistaken encounters with Dulcinea, bring a lighthearted tone to the ballet.",
	    "The colorful Spanish folk dances in Act I and the 'Dance of the Gypsies' are a lively celebration of Spanish culture and add energy to the performance."
	],
    },

    "7": {
    	"id": "7",
    	"title": "Onegin",
    	"image": "https://dancetabs.com/wp-content/uploads/2017/06/roc-onegin-david-hallberg-hee-seo-drag_1000.jpg",
    	"year": "1965",
	"summary": "Onegin ballet is based on Alexander Pushkin's novel Eugene Onegin. It follows the story of Tatiana, a young country girl who falls in love with the sophisticated, but emotionally distant, Eugene Onegin. She writes him a passionate letter, confessing her feelings, but he rejects her, deeming her too naive and unworthy of his affection.Years later, Onegin returns to the countryside and realizes that he has fallen in love with Tatiana, who is now married to another man, Prince Gremin. Onegin, regretful and jealous, tries to win her back, but Tatiana, now a poised and self-assured woman, rejects him, understanding that her love for him is in the past. The ballet concludes with Tatiana's emotional growth, as she chooses her marriage over a romantic ideal, leaving Onegin alone with his regrets",
	"composer": ["Pyotr Ilyich Tchaikovsky"],
     	"choreographer": ["John Cranko"],
    	"length": "2.5 hours",
    	"genres": ["Romantic", "Drama", "Ballet"],
    	"similar ballet ids": ["1", "2", "4"],
    	"other works by composer": ["Swan Lake", "The Nutcracker"],
    	"other works by choreographer": ["Coppélia", "Romeo and Juliet"],
    	"performing companies": [
        	{"name": "Mariinsky Ballet", "location": "St. Petersburg, Russia", "performance_dates": "May 10-20, 2025"},
        	{"name": "Royal Ballet", "location": "London, UK", "performance_dates": "June 1-10, 2025"}
    	],
    	"talking points & iconic moments": [
            "The pas de deux between Onegin and Tatiana in Act II is one of the most emotionally charged moments in ballet, with contrasting feelings of love, regret, and rejection.",
            "The choreography in the letter scene, where Tatiana writes a passionate letter to Onegin, is a highlight of the ballet's emotional depth.",
            "The final duel between Onegin and Lensky is filled with tension and heartbreak, showcasing the tragic nature of the ballet."
    	],
    },

    "8": {
    	"id": "8",
    	"title": "Romeo and Juliet",
    	"image": "https://www.hollywoodreporter.com/wp-content/uploads/2014/07/romeo_and_juliet_ballet_a_l.jpg?w=1440&h=810&crop=1",
    	"year": "1935",
    	"summary": "The plot of Romeo and Juliet ballet follows the tragic love story of two young lovers from feuding families in Verona. Romeo, a Montague, and Juliet, a Capulet, meet at a ball and instantly fall in love, despite their families' enmity. They secretly marry the next day with the help of Juliet's nurse and Friar Laurence.However, a series of unfortunate events leads to a deadly confrontation between Romeo's friend Mercutio and Juliet's cousin Tybalt, resulting in Mercutio's death. In a fit of rage, Romeo kills Tybalt and is banished from Verona. Juliet is devastated, and her family arranges her marriage to Paris.In an attempt to escape this fate, Juliet takes a potion that makes her appear dead. Romeo, unaware of the plan, hears of her death and returns to her tomb. Believing she is truly gone, he takes poison. When Juliet awakens and finds Romeo dead beside her, she stabs herself with his dagger. The ballet ends in tragedy, with the two lovers dying in each other's arms, bringing an end to the feud between their families.",
	"composer": ["Sergei Prokofiev"],
    	"choreographer": ["Leonid Lavrovsky"],
    	"length": "2.5 - 3 hours",
    	"genres": ["Romantic", "Tragedy", "Classical"],
    	"similar ballet ids": ["1", "4", "5"],
    	"other works by composer": ["Cinderella", "The Love for Three Oranges"],
    	"other works by choreographer": ["The Nutcracker", "Coppélia"],
    	"performing companies": [
             {"name": "Mariinsky Ballet", "location": "St. Petersburg, Russia", "performance_dates": "March 20-30, 2025"},
             {"name": "Royal Ballet", "location": "London, UK", "performance_dates": "April 5-15, 2025"}
    	],
    	"talking points & iconic moments": [
            "The pas de deux between Romeo and Juliet in Act II, where they dance together in secret, is one of the most iconic and passionate duets in ballet.",
            "The ball scene, where Romeo and Juliet first meet, features a vibrant and lively group dance, contrasted with the intimate encounter between the two lovers.",
            "The tragic finale, where Romeo believes Juliet to be dead and takes his own life, followed by Juliet’s awakening and death, is a devastatingly emotional conclusion."
    	],
    },

    "9": {
    	"id": "9",
    	"title": "Sleeping Beauty",
    	"image": "https://res.cloudinary.com/sagacity/image/upload/c_crop,h_3473,w_5759,x_0,y_0/c_limit,dpr_auto,f_auto,fl_lossy,q_80,w_1080/EZ7A2487_v5l41k.jpg",
    	"year": "1890",
    	"summary": "Based on Charles Perrault’s classic fairy tale, Sleeping Beauty is a grand ballet that tells the story of Princess Aurora, who is cursed by the wicked fairy Carabosse to prick her finger and fall into an eternal sleep. The curse is only broken by the kiss of a prince, who awakens Aurora and restores peace to the kingdom.",
    	"composer": ["Pyotr Ilyich Tchaikovsky"],
    	"choreographer": ["Marius Petipa"],
    	"length": "2.5 - 3 hours",
    	"genres": ["Fairy Tale", "Classical", "Romantic"],
    	"similar ballet ids": ["1", "4", "6"],
    	"other works by composer": ["Swan Lake", "The Nutcracker"],
    	"other works by choreographer": ["The Nutcracker", "Don Quixote"],
    	"performing companies": [
            {"name": "Bolshoi Ballet", "location": "Moscow, Russia", "performance_dates": "June 10-20, 2025"},
            {"name": "Royal Ballet", "location": "London, UK", "performance_dates": "July 1-15, 2025"}
    	],
    	"talking points & iconic moments": [
            "The Rose Adagio in Act I, where Aurora is courted by four princes, is one of the most technically demanding and famous moments in ballet.",
            "Carabosse’s entrance and the curse scene is one of the most dramatic and dark sequences in the ballet, contrasting the fairy tale’s lighthearted moments.",
            "The final act, where Princess Aurora is awakened by the Prince’s kiss, is a beautiful, joyful celebration of love and restoration."
    	],
    },

    "10": {
    	"id": "10",
    	"title": "Jewels",
    	"image": "https://www.classicalsource.com/wp-content/uploads/8dd5f15c-5cb3-4abc-90e0-05722cd2fd8e_08_JEWELS_1530webAustralianBallet.jpg-1024x768.webp",
    	"year": "1967",
    	"summary": "Jewels is a full-length abstract ballet choreographed by George Balanchine, consisting of three acts, each representing a different jewel: Emeralds, Rubies, and Diamonds. The ballet showcases the elegance and beauty of each jewel through distinct choreography, set to music by composers Gabriel Fauré, Igor Stravinsky, and Pyotr Ilyich Tchaikovsky. Each section has its own distinct style—Emeralds is delicate and lyrical, Rubies is energetic and jazzy, and Diamonds is grand and classical.",
    	"composer": ["Gabriel Fauré", "Igor Stravinsky", "Pyotr Ilyich Tchaikovsky"],
    	"choreographer": ["George Balanchine"],
    	"length": "2 hours",
    	"genres": ["Neoclassical", "Abstract Ballet"],
    	"similar ballet ids": ["1", "4", "7"],
    	"other works by composer": ["Requiem (Fauré)", "Firebird (Stravinsky)", "Swan Lake (Tchaikovsky)"],
    	"other works by choreographer": ["The Four Temperaments", "Agon", "Concerto Barocco"],
    	"performing companies": [
            {"name": "New York City Ballet", "location": "New York, NY", "performance_dates": "March 10-20, 2025"},
            {"name": "Paris Opera Ballet", "location": "Paris, France", "performance_dates": "April 15-25, 2025"}
    	],
    	"talking points & iconic moments": [
            "The Emeralds section, with its lush, romantic choreography set to Fauré’s beautiful music, evokes elegance and grace.",
            "The Rubies section, with Stravinsky’s vibrant music, is known for its fast-paced, jazzy choreography and sharp, energetic movements.",
            "The Diamonds section, set to Tchaikovsky’s majestic music, is a classical showcase of grandeur and virtuosity, with stunning lines and classical poses."
    	],
    },

    "11": {
    	"id": "11",
    	"title": "Cinderella",
    	"image": "https://www.jackdevant.com/wp-content/uploads/2024/03/cinderella-tallinn.jpg",
    	"year": "1944",
    	"summary": "The plot of the *Cinderella* ballet follows the story of a young woman named Cinderella, who is mistreated by her stepmother and stepsisters. Despite her hardships, she remains kind and gentle. With the help of her Fairy Godmother, she is transformed for one magical night, able to attend the royal ball where she meets the Prince. They fall in love, but she must leave before midnight when the magic wears off. The Prince searches for her using a lost shoe, and when he finds Cinderella, they are reunited and married, bringing happiness and justice to her life.",
	"composer": ["Sergei Prokofiev"],
    	"choreographer": ["Frederick Ashton", "Lev Ivanov"],
    	"length": "2.5 hours",
    	"genres": ["Classical", "Romantic", "Fairy Tale"],
    	"similar ballet ids": ["1", "4", "10"],
    	"other works by composer": ["Romeo and Juliet", "Peter and the Wolf", "War Sonatas"],
    	"other works by choreographer": ["La Fille Mal Gardée", "The Dream", "Coppélia"],
    	"performing companies": [
            {"name": "Royal Ballet", "location": "London, UK", "performance_dates": "November 1-15, 2025"},
            {"name": "American Ballet Theater", "location": "New York, NY", "performance_dates": "March 10-20, 2025"}
        ],
    	"talking points & iconic moments": [
            "The transformation scene, where Cinderella is changed into her ballgown by her fairy godmother, is one of the most magical moments in the ballet.",
            "The 'Midnight' scene, when the clock strikes twelve and Cinderella must flee the ball, is filled with dramatic tension and beautiful choreography.",
            "The 'Glass Slipper' moment, where the prince searches for the girl who fits the slipper, is one of the most iconic and romantic parts of the story."
    	],
    },

    "12": {
    	"id": "12",
    	"title": "The Rite of Spring",
    	"image": "https://www.theparisreview.org/blog/wp-content/uploads/2017/10/rite-of-spring_5_tanztheater-wuppertal-pina-bausch_pc_stephanie-berger.jpeg",
    	"year": "1913",
    	"summary": "Rite of Spring (also known as *Le Sacre du Printemps*) is a ballet that tells the story of a pagan ritual in ancient Russia, centered around the arrival of spring. The plot revolves around the selection of a young girl who must be sacrificed to the gods to ensure the fertility of the earth.The ballet begins with a celebration of the arrival of spring, with dancers performing to invoke the spirit of nature. As the ritual progresses, the chosen girl, a maiden, is selected to be the sacrificial offering. She dances a frenzied and frantic solo, representing her acceptance of her fate. Eventually, she is overwhelmed and, in the final moments, is danced to death by the tribe, completing the ritual.The ballet, known for its intense and innovative music by Igor Stravinsky and its powerful, primal choreography by Vaslav Nijinsky, explores themes of sacrifice, fate, and the power of nature. The plot itself is secondary to the emotional and visceral impact of the performance, which evokes the raw energy and mystery of ancient rituals.",
	"composer": ["Igor Stravinsky"],
    	"choreographer": ["Vaslav Nijinsky"],
    	"length": "35 minutes",
    	"genres": ["Classical", "Avant-garde", "Modern"],
    	"similar ballet ids": ["2", "4", "12"],
    	"other works by composer": ["Firebird", "Petrushka", "The Soldier's Tale"],
    	"other works by choreographer": ["Afternoon of a Faun", "Jeux", "La Sublime"],
    	"performing companies": [
            {"name": "The Ballets Russes", "location": "Paris, France", "performance_dates": "May 29, 1913 (Premiere)"},
            {"name": "New York City Ballet", "location": "New York, NY", "performance_dates": "March 10-20, 2025"}
    ],
    	"talking points & iconic moments": [
            "The riotous premiere at the Théâtre des Champs-Élysées in Paris, where the audience reacted with shock to the ballet’s avant-garde style.",
            "The intense, primitive energy of the choreography, with its sharp, angular movements and exaggerated gestures.",
            "The iconic Sacrificial Dance, where the chosen girl dances herself to death in a frenzy of movement, symbolizing sacrifice to the earth."
    	]
    },

   
}

# ROUTES
next_id = 14

@app.route('/static/<path:filename>')
def serve_static(filename):
	return send_from_directory(os.path.join(app.root_path, 'static'), filename)

@app.route('/')
def home():
	return render_template('home.html', popular_ballets=data)

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get("query", "").strip()  # Trim whitespace

    if not query:
        return '', 204  # Return 204 No Content if the query is empty or just whitespace

    results = perform_search(query)  
    return render_template('search_results.html', results=results, query=query, result_count=len(results))

def perform_search(query):
    query = query.lower()  # Convert query to lowercase
    matched_items = []
    for item_id, item in data.items():
        matched_fields = []
        if "title" in item and query in item["title"].lower():
            matched_fields.append("title")
        if "composer" in item and any(query in composer.lower() for composer in item["composer"]):
            matched_fields.append("composer")
        if "choreographer" in item and any(query in choreographer.lower() for choreographer in item["choreographer"]):
            matched_fields.append("choreographer")

        if matched_fields:
            # Make a copy of the item and add id if it doesn't exist
            item_copy = item.copy()
            if "id" not in item_copy:
                item_copy["id"] = item_id
            matched_items.append([item_copy, matched_fields])
    return matched_items

@app.route('/view/<id>')
def view_data(id):
    item = data.get(id)
    if not item:
        return "Item not found", 404
    return render_template('view.html', item=item)


@app.route('/add', methods=['GET', 'POST'])
def add_data():
    global next_id
    if request.method == 'POST':
        title = request.form.get('title').strip()
        year = request.form.get('year').strip()
        summary = request.form.get('summary').strip()
        composer = [c.strip() for c in request.form.get('composer').split(',')]
        choreographer = [ch.strip() for ch in request.form.get('choreographer').split(',')]
        image = request.form.get('image').strip()
        length = request.form.get('length').strip()
        genres = [g.strip() for g in request.form.get('genres').split(',')]
        other_works_composer = [c.strip() for c in request.form.get('other_works_composer').split(',')]
        other_works_choreographer = [c.strip() for c in request.form.get('other_works_choreographer').split(',')]
        talking_points = [c.strip() for c in request.form.get('talking_points').split(',')]

        errors = {}
        if not title:
            errors['title'] = 'Title is required'
        if not year:
            errors['year'] = 'Year is required'
        else:
            try:
                int(year)
            except ValueError:
                errors['year'] = 'Year must be a number'
        if not summary:
            errors['summary'] = 'Summary is required'

        if errors:
            return jsonify({'errors': errors}), 400

        new_item = {
            'id': str(next_id),
            'title': title,
            'year': year,
            'summary': summary,
            'composer': composer,
            'choreographer': choreographer,
            'image': image,
            'length': length,
            'genres': genres,
            'other works by composer': other_works_composer,
            'other works by choreographer': other_works_choreographer,
            'talking points & iconic moments': talking_points,
        }

        data[str(next_id)] = new_item
        next_id += 1

        return jsonify({'success': True, 'id': new_item['id']})

    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_data(id):
    item = data.get(id)
    if not item:
        return "Item not found", 404

    if request.method == 'POST':
        title = request.form.get('title').strip()
        year = request.form.get('year').strip()
        summary = request.form.get('summary').strip()
        composer = [c.strip() for c in request.form.get('composer').split(',')]
        choreographer = [ch.strip() for ch in request.form.get('choreographer').split(',')]
        image = request.form.get('image').strip()
        length = request.form.get('length').strip()
        genres = [g.strip() for g in request.form.get('genres').split(',')]
        other_works_composer = [c.strip() for c in request.form.get('other_works_composer').split(',')]
        other_works_choreographer = [c.strip() for c in request.form.get('other_works_choreographer').split(',')]
        talking_points = [c.strip() for c in request.form.get('talking_points').split(',')]

        errors = {}
        if not title:
            errors['title'] = 'Title is required'
        if not year:
            errors['year'] = 'Year is required'
        else:
            try:
                int(year)
            except ValueError:
                errors['year'] = 'Year must be a number'
        if not summary:
            errors['summary'] = 'Summary is required'

        if errors:
            return jsonify({'errors': errors}), 400

        item['title'] = title
        item['year'] = year
        item['summary'] = summary
        item['composer'] = composer
        item['choreographer'] = choreographer
        item['image'] = image
        item['length'] = length
        item['genres'] = genres
        item['other works by composer'] = other_works_composer
        item['other works by choreographer'] = other_works_choreographer
        item['talking points & iconic moments'] = talking_points

        return jsonify({'success': True, 'id': id})

    return render_template('edit.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)


