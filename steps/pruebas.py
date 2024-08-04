import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')

def take_screenshot(context, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_name = os.path.join(screenshot_dir, f"{step_name}_{timestamp}.png")
    context.driver.save_screenshot(screenshot_name)
    context.pdf.add_screenshot(screenshot_name, step_name)
    print(f"Screenshot taken: {screenshot_name}")
    return screenshot_name

def mark_step_as_failed(context, step_name, exception):
    print(f"Error in '{step_name}': {exception}")
    raise Exception(f"Step failed: {step_name}. Error: {exception}")

def mark_step_as_passed(context, step_name):
    print(f"Step passed: {step_name}")

@given('Se inicia el navegador')
def iniciarNavegador(context):
    context.driver = webdriver.Chrome(options=options)
    context.failed_steps = []
    print("Browser started")

@when('Entra a la seccion vehiculo')
def entrar_seccion_vehiculo(context):
    try:
        context.driver.maximize_window()
        context.driver.get("C:\\Users\\cesar\\OneDrive\\Desktop\\req\\Vehiculo\\Vehiculo.html")
        take_screenshot(context, '1. Entra a la seccion vehiculo')
        print("Entered 'Vehiculo' section")
    except Exception as e:
        mark_step_as_failed(context, 'entra_seccion_vehiculo', e)

@when('Aplasta el botón agregar')
def aplastar_boton_agregar(context):
    try:
        agregar_button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div/button')
        agregar_button.click()
        take_screenshot(context, '2. Clickar el boton agregar')
    except Exception as e:
        mark_step_as_failed(context, 'aplastar_boton_agregar', e)

@when('Rellenar el campo Marca {marca}')
def rellenar_marca(context, marca):
    try:
        marca_field = context.driver.find_element(By.XPATH, '//*[@id="marca"]')
        marca_field.send_keys(marca)
        take_screenshot(context, '3. Rellenar el campo Marca')
    except Exception as e:
        mark_step_as_failed(context, 'rellenar_marca', e)

@when('Rellenar el campo Modelo {modelo}')
def rellenar_modelo(context, modelo):
    try:
        modelo_field = context.driver.find_element(By.XPATH, '//*[@id="modelo"]')
        modelo_field.send_keys(modelo)
        take_screenshot(context, '4. Rellenar el campo Modelo')
    except Exception as e:
        mark_step_as_failed(context, 'rellenar_modelo', e)

@when('Rellenar el campo Placa {placa}')
def rellenar_placa(context, placa):
    try:
        placa_field = context.driver.find_element(By.XPATH, '//*[@id="placa"]')
        placa_field.send_keys(placa)
        take_screenshot(context, '5. Rellenar el campo Placa')
    except Exception as e:
        mark_step_as_failed(context, 'rellenar_placa', e)

@when('Rellenar el campo Año {anio}')
def rellenar_anio(context, anio):
    try:
        anio_field = context.driver.find_element(By.XPATH, '//*[@id="anio"]')
        anio_field.send_keys(anio)
        take_screenshot(context, '6. Rellenar el campo Año')
    except Exception as e:
        mark_step_as_failed(context, 'rellenar_anio', e)

@when('Rellenar el campo Kilometraje {kilometraje}')
def rellenar_kilometraje(context, kilometraje):
    try:
        kilometraje_field = context.driver.find_element(By.XPATH, '//*[@id="kilometraje"]')
        kilometraje_field.send_keys(kilometraje)
        take_screenshot(context, '7. Rellenar el campo Kilometraje')
    except Exception as e:
        mark_step_as_failed(context, 'rellenar_kilometraje', e)

@when('Seleccionar el tipo de combustible {combustible}')
def seleccionar_combustible(context, combustible):
    try:
        combustible_dropdown = Select(context.driver.find_element(By.XPATH, '//*[@id="combustible"]'))
        combustible_dropdown.select_by_visible_text(combustible)
        take_screenshot(context, '8. Seleccionar el tipo de combustible')
    except Exception as e:
        mark_step_as_failed(context, 'seleccionar_combustible', e)

@when('Rellenar el campo Peso {peso}')
def rellenar_peso(context, peso):
    try:
        peso_field = context.driver.find_element(By.XPATH, '//*[@id="peso"]')
        peso_field.send_keys(peso)
        take_screenshot(context, '9. Rellenar el campo Peso')
    except Exception as e:
        mark_step_as_failed(context, 'rellenar_peso', e)

@when('Seleccionar la foto del vehiculo {foto_path}')
def seleccionar_foto(context, foto_path):
    try:
        foto_input = context.driver.find_element(By.XPATH, '//*[@id="photo"]')
        foto_input.send_keys(foto_path)
        take_screenshot(context, '10. Seleccionar la foto del vehiculo')
    except Exception as e:
        mark_step_as_failed(context, 'seleccionar_foto', e)

@then('Aplastar el boton para guardar el vehiculo')
def aplastar_guardar_vehiculo(context):
    try:
        guardar_button = context.driver.find_element(By.XPATH, '//*[@id="addVehiculoForm"]/button')
        guardar_button.click()
        take_screenshot(context, '11. Aplastar el boton para guardar el vehiculo')
        print("Vehicle saved")
    except Exception as e:
        mark_step_as_failed(context, 'aplastar_guardar_vehiculo', e)

@then('Visualizar el auto guardado')
def visualizar_auto_guardado(context):
    try:
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="carros"]/div[4]'))
        )
        vehiculo_guardado = context.driver.find_element(By.XPATH, '//*[@id="carros"]/div[4]')
        if vehiculo_guardado.is_displayed():
            take_screenshot(context, '12. Visualizar el auto guardado')
            mark_step_as_passed(context, 'visualizar_auto_guardado')
        else:
            raise Exception("El auto guardado no es visible")
    except Exception as e:
        mark_step_as_failed(context, 'visualizar_auto_guardado', e)
