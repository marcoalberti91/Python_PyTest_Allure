# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRegistrationNavigation():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
    print("Starting Chromdriver")
  
  def teardown_method(self, method):
    self.driver.quit()
    print("Closing Chromdriver")
  
  def test_registrationNavigation(self):
    self.driver.get("https://www.toolsqa.com/")
    print("Navigating to ToolsQA website")
    self.driver.set_window_size(1552, 832)
    print("Setup screensize")
    self.driver.find_element(By.XPATH, "//a[contains(text(),\'Selenium Training\')]").click()
    print("Click on Selenium Training")
    self.driver.find_element(By.XPATH, "//a[contains(text(),\'Go To Registration\')]").click()
    print("Click on Registration button")