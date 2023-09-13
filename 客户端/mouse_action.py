import win32api
import win32con
import win32gui 
def move(x, y): 
  win32api.SetCursorPos((x, y))
  
def left_click(): 
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def right_click(): 
  win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN | win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

def left_down(): 
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

def left_up(): 
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def right_down(): 
  win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

def right_up(): 
  win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
  
def mouse_drag(FROM ,TO):
    time.sleep(0.5)
    move( FROM[0],FROM[1] )
    time.sleep(0.5)
    left_down()
    time.sleep(1)
    move( TO[0],TO[1] )
    time.sleep(0.5)
    left_up()  
    time.sleep(0.3)
