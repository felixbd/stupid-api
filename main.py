#!/usr/bin/env python3

from selenium import webdriver

def main():
    # Setzen Sie die Proxy-Einstellungen (Socks5) entsprechend Ihrer Umgebung
    proxy_address = "localhost"  # Ändern Sie dies auf die tatsächliche Proxy-Adresse
    proxy_port = 5055

    # Setzen Sie die URL, die Sie besuchen möchten
    url = "https://elearning.uni-bremen.de/"

    # Erstellen Sie einen Proxy mit den angegebenen Socks5-Einstellungen
    proxy = f"{proxy_address}:{proxy_port}"

    # Erstellen Sie eine WebDriver-Instanz mit dem konfigurierten Proxy für Firefox
    options = webdriver.FirefoxOptions()
    options.add_argument(f"--proxy-server=socks5://{proxy}")
    driver = webdriver.Firefox(options=options)

    try:
        # Besuchen Sie die gewünschte URL
        driver.get(url)

        # Warten Sie auf einige Sekunden (kann je nach Seite und Netzwerkgeschwindigkeit variieren)
        driver.implicitly_wait(10)

        # Drucken Sie den Seitenquelltext aus
        print(driver.page_source)

    finally:
        # Schließen Sie den WebDriver am Ende
        driver.quit()

if __name__ == "__main__":
    main()
