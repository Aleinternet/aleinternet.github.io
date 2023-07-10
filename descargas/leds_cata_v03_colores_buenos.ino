


// Definición de los pines
const int pinR = 9;
const int pinB = 10;
const int pinG = 11;

// Tiempos de encendido para cada color (en milisegundos)
const int tiempoRojo = 3000;
const int tiempoAzul = 4000;
const int tiempoVerde = 5000;

void setup() {
  // Configuración de los pines como salidas
  pinMode(pinR, OUTPUT);
  pinMode(pinB, OUTPUT);
  pinMode(pinG, OUTPUT);

  // Inicializar comunicación serial
  Serial.begin(9600);
}

void loop() {
  // Encender el color rojo
  digitalWrite(pinR, HIGH);
  digitalWrite(pinB, HIGH);
  digitalWrite(pinG, LOW);
  Serial.println("Rojo");
  delay(tiempoRojo);

  // Encender el color azul
  digitalWrite(pinR, HIGH);
  digitalWrite(pinB, LOW);
  digitalWrite(pinG, HIGH);
  Serial.println("Azul");
  delay(tiempoAzul);

  // Encender el color verde
  digitalWrite(pinR, LOW);
  digitalWrite(pinB, HIGH);
  digitalWrite(pinG, HIGH);
  Serial.println("Verde");
  delay(tiempoVerde);

}
