from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inisialisasi WebDriver
# driver = webdriver.Chrome()
driver = webdriver.Chrome()
# Buka situs web Adinusa
driver.get("https://fly.io/app/sign-up")

# Isi formulir pendaftaran
input_username = driver.find_element(By.ID, "user_name")
input_email = driver.find_element(By.ID, "user_email")
input_password1 = driver.find_element(By.ID, "user_password")
# input_password2 = driver.find_element(By.ID, "passwordConfirmation")
button_daftar = driver.find_element(By.XPATH, "//button[contains(text(), 'Create My Account')]")

input_username.send_keys("sidiqfaisal30")  # Ganti dengan nama Anda
input_email.send_keys("sidiqfaisal30@gmail.com")  # Ganti dengan email Anda
input_password1.send_keys("g4nt3ng")  # Ganti dengan password yang diinginkan
# input_password2.send_keys("Ch#ndra680")  # Konfirmasi password
button_daftar.click()

# Tunggu beberapa detik untuk memastikan halaman pendaftaran selesai dimuat
time.sleep(5)

# Cek apakah pendaftaran berhasil
if "Selamat datang" in driver.page_source:
    print("Pendaftaran berhasil!")
else:
    print("Pendaftaran gagal.")

# Tutup browser
driver.quit()


