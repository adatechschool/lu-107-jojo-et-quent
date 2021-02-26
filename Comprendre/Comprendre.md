# Comprendre

Essayez de synthétiser en binôme votre compréhension de la notion que vous avez vue (s'il s'agissait de plusieurs notions, vous pouvez répéter ce paragraphe plusieurs fois) : 
- Quel est son rôle ? 
= créer et faire interagir des briques logicielles : "objets".

En POO : un objet né de l’instance d’une classe. 

Classe = propriétés/attributs (variables) + méthodes (fonctions internes) qui agissent entre elles pour donner un résultat

- Quel est son intérêt ? 
Principalement : Une structure de code beaucoup plus clair, mais aussi plus modulable et plus facile à maintenir + plus facile de débugger

"**Héritage**" : spécialiser/spécifier une classe du parent à l'enfant
La classe enfant réutilise tous les champs et méthodes de la classe parent (partie commune) et peut implémenter la sienne (partie unique).

"**Polymorphisme**" : pouvoir générer un code abstrait mais par héritage, créer des parties concrètes pour l'enfant; *refactoriser* (à approfondir)

"**Abstraction**" : essayer d'isoler des zones de code ; en cas de changement, cacher les détails et la complexité d'une classe en ne montrant que l'essentiel 

"**Encapsulation**" : respect des attributs d'une classe - accès privé sauf si méthode spécifique). [*private / protected  / public*]
+ sécuriser les données de l'objet, réaliser des traitements internes à l’objet sans que l’utilisateur ne le sache

- A-t-elle des désavantages ? 
Ce n'est pas très pratique pour des petits projets ou test de fonctionnalités non orienté objet. 
Son implementation reste difficile à gérer. 

- Y a-t-il plusieurs façons de s'en servir ? 
Polymorphisme + Héritage

- Quelles sont les étapes importantes pour la mettre en place ? 
cf définition
- Quelles sont les nuances d'un langage à l'autre ? 
La quasi-totalité des langages de programmation permet de faire de la POO.

Il n'existe pas, en JavaScript d'élément *class* pour créer des classes alors que c'est le cas dans plusieurs langages orientés objet. JavaScript ⇒ utilise des fonctions spéciales appelées **constructeurs** pour définir les objets et leurs propriétés. Ces constructeurs nous permettent de créer autant d'objets que nécessaire et d'y associer des données et des fonctions au fur et à mesure.

Java : obligation d'indiquer si la méthode est publique ou privée - contrairement à Python (ex.)

- Existe-t-il des contextes (langages, environnements, outils) où elle n'existe pas ? 

- Quelles sont ses alternatives ? 

