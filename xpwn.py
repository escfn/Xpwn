from splinter import *
import time
import random
# ------------------------ create list of first and last names --------------------------
Fnames = ['Richard','Axl','Ringo','Rod','Rick','Marshall','Lesane','Sean','Calvin','Andre','Curtis','Stevie','Janis','James']
FirstName = random.choice(Fnames)
Nnames = ['Ashcroft','Rose','Starr','Stewart','Ross','Mathers','Crooks','Combs','Broadus','Young','Jackson','Nicks','Joplin','Brown']
LastName = random.choice(Nnames)
UserNames = str(random.randrange(10000,99999))
# ------------------------- create list of zip codes ------------------------------------
Zipcodes = ['30008','30060','30061','30062','30063','30064','30066','30067','30068','30080','30090','30152','30126']
ZipCode = random.choice(Zipcodes)
zip_code = ZipCode
# ----------------------------- create list of emails based on song names ---------------
Emails = ['Roxanne','Layla','Angie','Lola','Beth','Rosanna','Gloria','Iris','Nikita','Maybelene','Valleri','Sherry','Julia','Delilah']
email_name = random.choice(Emails)
email_num = str(random.randrange(1000,9999))+'@gmail.com'
# ----------------------- create list of car names --------------------------------------
CarNames = ['Buick','Chevey','Ford','Toyota','Mercury','Dodge','Mercedes','Honda','Mitsubishi','Kia','Volkswagen','Subaru','Suzuki','Lincoln']
carName = random.choice(CarNames)
# --------------- setup browser and load page -------------------------------------------
browser = Browser()
browser.visit('http://google.com') # ----- it will redirect to xfinity wifi login page --
browser.find_by_xpath('//*[@id="amdocs_signup"]').click()
time.sleep(2) # pause to allow page and button to load

browser.find_by_xpath('//*[@id="offerListInput_1158900665"]').click()
browser.find_by_xpath('//*[@id="continueButton"]').click()
time.sleep(3) # pause to allow page to fully load

browser.find_by_xpath('//*[@id="registerFirstName"]').fill(FirstName)
browser.find_by_xpath('//*[@id="registerLastName"]').fill(LastName)
browser.find_by_xpath('//*[@id="registerEmail"]').fill(email_name+email_num)
browser.find_by_xpath('//*[@id="registerZipCode"]').fill(zip_code)
time.sleep(5) # pause to allow page to fully load

browser.find_by_xpath('//*[@id="registerContinueButton"]').click()
time.sleep(5)

browser.find_by_xpath('//*[@id="userName"]').fill(FirstName+UserNames+LastName)
time.sleep(1)

browser.find_by_xpath('//*[@id="password"]').fill("XPwnd6969$$$$")
time.sleep(1)

browser.find_by_xpath('//*[@id="passwordRetype"]').fill("XPwnd6969$$$$")
browser.find_by_xpath('//*[@id="dk0-combobox"]').click()
browser.find_by_xpath('//*[@id="dk0-What-was your first car (make and model)?"]').click()

browser.find_by_xpath('//*[@id="secretAnswer"]').fill(carName)
browser.find_by_xpath('//*[@id="submitButton"]').click()
time.sleep(20)

browser.find_by_xpath('//*[@id="orderConfirmationActivatePass"]').click()
time.sleep(1)

browser.quit()
# ------------------------------ End Code -------------------------------------------