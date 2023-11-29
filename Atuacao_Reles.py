import RPi.GPIO as GPIO
import time

# Configurar os pinos dos relés
relay_pins = [2, 3, 4, 17]

def setup_relays():
    GPIO.setmode(GPIO.BCM)
    for pin in relay_pins:
        GPIO.setup(pin, GPIO.OUT)

def activate_relay1_and_relay4():
    GPIO.output(3, True) # Desativar IN2
    GPIO.output(4, True) # Desativar IN3
    time.sleep(0.1)      # Delay de 100ms
    GPIO.output(2, False)  # Ativar IN1
    GPIO.output(17, False) # Ativar IN4

def all_off():
    GPIO.output(2, True) # Desativar IN1
    GPIO.output(3, True) # Desativar IN2
    GPIO.output(4, True) # Desativar IN3
    GPIO.output(17, True) # Desativar IN4


def activate_relay2_and_relay3():
    GPIO.output(2, True) # Desativar IN1
    GPIO.output(17, True) # Desativar IN4
    time.sleep(0.1)       # Delay de 100ms
    GPIO.output(3, False)  # Ativar IN2
    GPIO.output(4, False)  # Ativar IN3

def cleanup():
    GPIO.cleanup()

# Exemplo de uso:
try:
 setup_relays()
 while 1:
    all_off()
    activate_relay1_and_relay4()  # Ativar IN1 e IN4
    time.sleep(2)               # Manter ativo por 20 segundos
    all_off()
    activate_relay2_and_relay3()  # Ativar IN2 e IN3
    time.sleep(2)               # Manter ativo por 20 segundos
except KeyboardInterrupt:
    cleanup()
