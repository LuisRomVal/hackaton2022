from django.http import HttpResponse
from selenium import webdriver
import time

def index(request):
    return HttpResponse("bye, world :(")
    

def enviar_solicitud(request):
    correo = "hackathonestic@gmail.com"
    password = "estic1234"

    target = "https://www.facebook.com/SackariasValdez"
    path_webdriver = request.GET.get('webdriver')
    driver = webdriver.Chrome(path_webdriver)
    driver.get("https://www.facebook.com")

    email_field = driver.find_element_by_name("email")
    email_field.send_keys(correo)

    pass_field = driver.find_element_by_name("pass")
    pass_field.send_keys(password)


    login_button = driver.find_element_by_name("login")
    login_button.click()
    time.sleep(2)

    driver.get(target)

    time.sleep(6)

    botones = driver.find_elements_by_css_selector("[aria-label=Agregar]")
    botones[0].click()
    return HttpResponse("solicitud enviada con exito")