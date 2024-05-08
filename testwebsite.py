from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Buka situs web pribadi
driver.get("https://mfaisal-ash.vaidiq.me/signUp-sigIn/") #mencari kemudian membuka website signUp-signin 

# Menunggu elemen muncul di halaman
registration_link = WebDriverWait(driver, 100).until( #menunggu website reload atau muncul semua elemen dalam waktu 100 deitk
    EC.element_to_be_clickable((By.LINK_TEXT, "Registration")) #mencari element link text dari Registration
)

# Klik tautan "Registration"
registration_link.click()

# Isi formulir pendaftaran
input_first_name = driver.find_element(By.ID, "first_name") #mencari element id first_name
input_last_name = driver.find_element(By.ID, "last_name")#mencari element id last_name
input_nickname = driver.find_element(By.ID, "nickname")#mencari element id nickname
input_email = driver.find_element(By.ID, "email")#mencari element id email
input_password = driver.find_element(By.ID, "password")#mencari element id password
button_registrasi = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]") #mencari element button yang bertulis Submit

input_first_name.send_keys("faisal")  # untuk mmenginputkan nama depan Anda
input_last_name.send_keys("kasep")  # untuk menginputkan nama belakang Anda
input_nickname.send_keys("Si Kasep")  # untuk menginputkan nickname Anda
input_email.send_keys("faisalkasep@gmail.com")  # untuk menginputkan email Anda
input_password.send_keys("12345678")  # untuk menginputkan password anda yang diinginkan tanpa diketahui oleh orang lain(privasi)
button_registrasi.click()

# Tunggu beberapa detik untuk memastikan halaman pendaftaran selesai dimuat
time.sleep(5)

# Cek apakah pendaftaran berhasil atau tidak
if "Your account has been created." in driver.page_source:
    print("Your Sign up success!")
else:
    print("Your Sign up failed.")

# Tutup browser
driver.quit()
