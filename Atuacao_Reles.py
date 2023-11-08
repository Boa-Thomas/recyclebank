import RPi.GPIO as GPIO
import time

# Configurar os pinos dos relés
relay_pins = [2, 3, 4, 17]

def setup_relays():
    GPIO.setmode(GPIO.BCM)
    for pin in relay_pins:
        GPIO.setup(pin, GPIO.OUT)

def activate_relay1_and_relay3():
    GPIO.output(2, True)  # Ativar IN1
    GPIO.output(4, True)  # Ativar IN3
    GPIO.output(3, False) # Desativar IN2
    GPIO.output(17, False) # Desativar IN4

def activate_relay2_and_relay4():
    GPIO.output(2, False) # Desativar IN1
    GPIO.output(4, False) # Desativar IN3
    GPIO.output(3, True)  # Ativar IN2
    GPIO.output(17, True)  # Ativar IN4

def cleanup():
    GPIO.cleanup()

# Exemplo de uso:
try:
    setup_relays()
    activate_relay1_and_relay3()  # Ativar IN1 e IN3
    time.sleep(5)  # Manter ativo por 5 segundos
    activate_relay2_and_relay4()  # Ativar IN2 e IN4
    time.sleep(5)  # Manter ativo por 5 segundos
except KeyboardInterrupt:
    cleanup()