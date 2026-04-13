// En JS no necesitamos importar 'random', usamos el objeto Math
// Función auxiliar para imitar a random.randint(min, max)
const randint = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

/*
// Declaramos el arreglo vacío con 10 espacios
let enteros = new Array(10).fill(0);

// Usamos un for para recorrer y rellenar con valores aleatorios cada posicion
// for (inicio; condición; incremento)
for (let i = 0; i < 10; i++) {
    enteros[i] = randint(1, 100);
}

console.log("------------ Arreglo de enteros ------------");
for (let i = 0; i < enteros.length; i++) {
    
    console.log(`Valor encontrado: ${enteros[i]}`);
}


console.log("---Multiplicamos todos los valores por su indice---");
for (let i = 0; i < enteros.length; i++) {
    enteros[i] *= i;
}
enteros.forEach(valor => console.log(`- ${valor}`));

console.log("------- Cambiamos los impares por cero -------");
for (let i = 0; i < 10; i++) {
    if (enteros[i] % 2 !== 0) {
        enteros[i] = 0;
    }
    console.log(`Posición ${i} llenada con: ${enteros[i]}`);
}

console.log("---------------- Busqueda lineal ----------------");
let numeroBuscar = 10;

let posicion = enteros.indexOf(numeroBuscar);

if (posicion !== -1) {
    console.log(`Encontrado en la posicion: ${posicion}`);
} else {
    console.log(`El valor ${numeroBuscar} no fue encontrado`);
}

*/

console.log("\n --------Ahora se trabajara con matrices --------");

let filas = 3;
let columnas = 3;

// En lugar de for anidado, usamos Array.from.
let matriz = Array.from({ length: filas }, () => 
    Array.from({ length: columnas }, () => Math.floor(Math.random() * 9) + 1)
);

