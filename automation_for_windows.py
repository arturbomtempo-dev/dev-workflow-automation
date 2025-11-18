import pyautogui
import time

print('Setting up environment...')

# Set default pause for safer automation
pyautogui.PAUSE = 1

# Open Windows Command Prompt
pyautogui.press('win')
pyautogui.write('cmd')
pyautogui.press('enter')

time.sleep(2)

# Navigate to Desktop
pyautogui.write('cd C:\\Users\\artur\\Desktop')  # Update path to your Desktop location
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
time.sleep(10)
pyautogui.click(x=367, y=48)
pyautogui.click(x=367, y=100)
time.sleep(2)
pyautogui.click(x=1102, y=837)

# Install dependencies and start development server
pyautogui.write('npm install')
pyautogui.press('enter')
time.sleep(10)
pyautogui.write('npm run dev')
pyautogui.press('enter')

# Open browser and access local development URL
time.sleep(3)
pyautogui.press('win')
pyautogui.write('Google Chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('http://localhost:5173')
pyautogui.press('enter')
