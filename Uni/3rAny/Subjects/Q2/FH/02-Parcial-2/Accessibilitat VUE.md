# Tema: Implementació de l'Accessibilitat en Vue.js

## 1. Recursos i Llibreries de Suport

Per no haver de reinventar la roda, és fonamental conèixer l'ecosistema de recursos disponibles per a Vue:

- **Documentació Oficial**: La guia de bones pràctiques de Vue.
    
- **Vuetify**: Una llibreria basada en _Material Design_ de Google que destaca per mantenir els seus components altament actualitzats i accessibles.
    
- **AccessiVue**: Un recurs molt interessant creat per una ex-alumna de la facultat com a TFG. Inclou 5 components funcionals (CRUD, Cercador, Drag and Drop, Formularis i Biblioteca de recursos) amb accessibilitat nativa integrada.
    
- **Vue-a11y**: Comunitat amb receptes i eines específiques per a l'accessibilitat.
    

## 2. Navegació: Skip Links i Focus


Un dels errors més comuns en les Single Page Applications (SPA) és obligar l'usuari de teclat a tabular per tots els menús cada vegada que canvia de vista.

- **Solució**: Implementar un "Skip to main content". És un vincle directe al contingut principal que apareix al principi del document.
    
- **Comportament visual**: Es pot ocultar visualment i fer que només sigui visible quan rep el focus del teclat.
    
