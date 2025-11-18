import pyautogui
import time
import os

print('Setting up environment...')

# Set default pause for safer automation
pyautogui.PAUSE = 1

# Open macOS Terminal
os.system("open -a 'Terminal'")
time.sleep(0.5)

# Navigate to Desktop
pyautogui.write('cd Desktop')
pyautogui.press('enter')

# Clone the target repository
time.sleep(0.5)
pyautogui.write('git clone https://github.com/arturbomtempo-dev/link-in-bio-react-youtube-tutorial.git')
pyautogui.press('enter')

# Enter project folder and open in Visual Studio Code
time.sleep(0.5)
pyautogui.write('cd link-in-bio-react-youtube-tutorial')
pyautogui.press('enter')
pyautogui.write('code .')
pyautogui.press('enter')

# Open VS Code integrated terminal (coordinates may vary based on screen resolution)
time.sleep(1)
pyautogui.click(x=422, y=7)
pyautogui.click(x=422, y=38)
time.sleep(3)
pyautogui.click(x=539, y=716)

# Install dependencies and start development server
pyautogui.write('npm install')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('npm run dev')
pyautogui.press('enter')

# Open browser and access local development URL
time.sleep(3)
os.system("open -a 'Google Chrome'")
time.sleep(1)
pyautogui.write('http://localhost:5173')
pyautogui.press('enter')
