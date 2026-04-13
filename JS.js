// En JS no necesitamos importar 'random', usamos el objeto Math
// Función auxiliar para imitar a random.randint(min, max)
const randint = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

// Declaramos el arreglo vacío con 10 espacios
let enteros = new Array(10).fill(0);

