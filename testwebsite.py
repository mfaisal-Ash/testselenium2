from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Buka situs web Adinusa
driver.get("https://mfaisal-ash.vaidiq.me/signUp-sigIn/")

# Menunggu elemen muncul di halaman
registration_link = WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Registration"))
)

# Klik tautan "Registration"
registration_link.click()

# Isi formulir pendaftaran
input_first_name = driver.find_element(By.ID, "first_name")
input_last_name = driver.find_element(By.ID, "last_name")
input_nickname = driver.find_element(By.ID, "nickname")
input_email = driver.find_element(By.ID, "email")
input_password = driver.find_element(By.ID, "password")
button_registrasi = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")

input_first_name.send_keys("faisal")  # Ganti dengan nama depan Anda
input_last_name.send_keys("kasep")  # Ganti dengan nama belakang Anda
input_nickname.send_keys("Si Kasep")  # Ganti dengan nama belakang Anda
input_email.send_keys("faisalkasep@gmail.com")  # Ganti dengan email Anda
input_password.send_keys("12345678")  # Ganti dengan password yang diinginkan
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
