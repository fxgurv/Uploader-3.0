import pickle
import random
import time
import logging
from config import Config
from datetime import datetime
from selenium import webdriver
from fake_useragent import UserAgent
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(name)s] - %(message)s',
    handlers=[
        logging.FileHandler(f'cookies_extraction_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def random_sleep(min_sec, max_sec):
    sleep_time = random.uniform(min_sec, max_sec)
    logger.debug(f"Sleeping for {sleep_time:.2f} seconds")
    time.sleep(sleep_time)

def spoof_navigator(driver):
    logger.info("Starting navigator spoofing")
    try:
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3]})")
        driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})")
        driver.execute_script("Object.defineProperty(navigator, 'platform', {get: () => 'Win32'})")
        logger.info("Navigator spoofing completed successfully")
    except Exception as e:
        logger.error(f"Navigator spoofing failed: {str(e)}")

def save_cookies(driver, cookies_file):
    logger.info(f"Attempting to save cookies to {cookies_file}")
    try:
        cookies = driver.get_cookies()
        with open(cookies_file, 'wb') as file:
            pickle.dump(cookies, file)
        logger.info(f"Successfully saved {len(cookies)} cookies")
    except Exception as e:
        logger.error(f"Failed to save cookies: {str(e)}")
        raise

class CookieExtractor:
    def __init__(self):
        logger.info("Initializing CookieExtractor")
        options = uc.ChromeOptions()
        ua = UserAgent()
        options.add_argument(f"user-agent={ua.random}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = uc.Chrome(options=options)
        logger.info("Chrome driver initialized successfully")

    def extract_youtube_cookies(self, email, password, cookies_file):
        logger.info("Starting YouTube cookie extraction")
        try:
            self.driver.get("https://www.youtube.com")
            random_sleep(3, 5)
            
            sign_in_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Sign in"]'))
            )
            sign_in_button.click()
            logger.info("Clicked sign in button")
            
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
            )
            email_input.send_keys(email)
            email_input.send_keys(Keys.RETURN)
            logger.info("Email entered")
            
            random_sleep(3, 5)
            
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
            )
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            logger.info("Password entered")
            
            random_sleep(5, 8)
            save_cookies(self.driver, cookies_file)
            
        except Exception as e:
            logger.error(f"YouTube cookie extraction failed: {str(e)}")
            raise

    def extract_tiktok_cookies(self, username, password, cookies_file):
        logger.info("Starting TikTok cookie extraction")
        try:
            self.driver.get("https://www.tiktok.com/login/phone-or-email/email")
            random_sleep(3, 5)
            
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            username_input.send_keys(username)
            logger.info("Username entered")
            
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
            )
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            logger.info("Password entered")
            
            random_sleep(35, 38)
            save_cookies(self.driver, cookies_file)
            
        except Exception as e:
            logger.error(f"TikTok cookie extraction failed: {str(e)}")
            raise

    def extract_instagram_cookies(self, username, password, cookies_file):
        logger.info("Starting Instagram cookie extraction")
        try:
            self.driver.get("https://www.instagram.com/accounts/login/")
            random_sleep(3, 5)
            
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            username_input.send_keys(username)
            logger.info("Username entered")
            
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            logger.info("Password entered")
            
            random_sleep(5, 8)
            save_cookies(self.driver, cookies_file)
            
        except Exception as e:
            logger.error(f"Instagram cookie extraction failed: {str(e)}")
            raise

    def extract_facebook_cookies(self, email, password, cookies_file):
        logger.info("Starting Facebook cookie extraction")
        try:
            self.driver.get("https://www.facebook.com/login")
            random_sleep(3, 5)
            
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'email'))
            )
            email_input.send_keys(email)
            logger.info("Email entered")
            
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'pass'))
            )
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            logger.info("Password entered")
            
            random_sleep(5, 8)
            save_cookies(self.driver, cookies_file)
            
        except Exception as e:
            logger.error(f"Facebook cookie extraction failed: {str(e)}")
            raise

    def extract_reddit_cookies(self, username, password, cookies_file):
        logger.info("Starting Reddit cookie extraction")
        try:
            self.driver.get("https://www.reddit.com/login")
            random_sleep(3, 5)
            
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'loginUsername'))
            )
            username_input.send_keys(username)
            logger.info("Username entered")
            
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'loginPassword'))
            )
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            logger.info("Password entered")
            
            random_sleep(5, 8)
            save_cookies(self.driver, cookies_file)
            
        except Exception as e:
            logger.error(f"Reddit cookie extraction failed: {str(e)}")
            raise

    def extract_twitch_cookies(self, username, password, cookies_file):
        logger.info("Starting Twitch cookie extraction")
        try:
            self.driver.get("https://www.twitch.tv/login")
            random_sleep(3, 5)
            
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'login-username'))
            )
            username_input.send_keys(username)
            logger.info("Username entered")
            
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'password-input'))
            )
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            logger.info("Password entered")
            
            random_sleep(5, 8)
            save_cookies(self.driver, cookies_file)
            
        except Exception as e:
            logger.error(f"Twitch cookie extraction failed: {str(e)}")
            raise

    def extract_pinterest_cookies(self, email, password, cookies_file):
        logger.info("Starting Pinterest cookie extraction")
        try:
            self.driver.get("https://www.pinterest.com/login/")
            random_sleep(3, 5)
            
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'id'))
            )
            email_input.send_keys(email)
            logger.info("Email entered")
            
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            logger.info("Password entered")
            
            random_sleep(5, 8)
            save_cookies(self.driver, cookies_file)
            
        except Exception as e:
            logger.error(f"Pinterest cookie extraction failed: {str(e)}")
            raise

    def extract_snapchat_cookies(self, username, password, cookies_file):
        logger.info("Starting Snapchat cookie extraction")
        try:
            self.driver.get("https://accounts.snapchat.com/accounts/login")
            random_sleep(3, 5)
            
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            username_input.send_keys(username)
            logger.info("Username entered")
            
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            logger.info("Password entered")
            
            random_sleep(5, 8)
            save_cookies(self.driver, cookies_file)
            
        except Exception as e:
            logger.error(f"Snapchat cookie extraction failed: {str(e)}")
            raise

    def extract_twitter_cookies(self, username, password, cookies_file):
        logger.info("Starting Twitter (X) cookie extraction")
        try:
            self.driver.get("https://twitter.com/login")
            random_sleep(3, 5)
            
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'text'))
            )
            username_input.send_keys(username)
            username_input.send_keys(Keys.RETURN)
            logger.info("Username entered")
            
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            logger.info("Password entered")
            
            random_sleep(5, 8)
            save_cookies(self.driver, cookies_file)
            
        except Exception as e:
            logger.error(f"Twitter cookie extraction failed: {str(e)}")
            raise

    def close(self):
        logger.info("Closing browser")
        self.driver.quit()

def main():
    logger.info("Starting main cookie extraction process")
    extractor = CookieExtractor()
    
    try:
        # Extract cookies for all platforms
        extractor.extract_youtube_cookies(
            Config.youtube_email,
            Config.youtube_password,
            Config.youtube_cookies_file
        )
        
        extractor.extract_tiktok_cookies(
            Config.tiktok_username,
            Config.tiktok_password,
            Config.tiktok_cookies_file
        )
        
        extractor.extract_instagram_cookies(
            Config.instagram_username,
            Config.instagram_password,
            Config.instagram_cookies_file
        )
        
        extractor.extract_facebook_cookies(
            Config.facebook_email,
            Config.facebook_password,
            Config.facebook_cookies_file
        )
        
        extractor.extract_reddit_cookies(
            Config.reddit_username,
            Config.reddit_password,
            Config.reddit_cookies_file
        )
        
        extractor.extract_twitch_cookies(
            Config.twitch_username,
            Config.twitch_password,
            Config.twitch_cookies_file
        )
        
        extractor.extract_pinterest_cookies(
            Config.pinterest_email,
            Config.pinterest_password,
            Config.pinterest_cookies_file
        )
        
        extractor.extract_snapchat_cookies(
            Config.snapchat_username,
            Config.snapchat_password,
            Config.snapchat_cookies_file
        )
        
        extractor.extract_twitter_cookies(
            Config.twitter_username,
            Config.twitter_password,
            Config.twitter_cookies_file
        )
        
        logger.info("All cookie extractions completed successfully")
        
    except Exception as e:
        logger.error(f"Main process failed: {str(e)}")
    finally:
        extractor.close()

if __name__ == "__main__":
    main()
