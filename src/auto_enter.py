import pyautogui
import time

def auto_fill(solved_board,delay=0.1):
    for i in range(9):
        for j in range(9):
            pyautogui.click()
            if solved_board[i][j] != 0:
                pyautogui.write(str(solved_board[i][j]))
            pyautogui.press('right')
        # move to next row    
        pyautogui.press('down')
        for _ in range(9):
            pyautogui.press('left')
        time.sleep(delay)
