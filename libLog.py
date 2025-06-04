"""
    libLog.py
"""
from LibraryPython.libColor import Color

#----------------------------------------------------------------

#----------------------------------------------------------------
class Log:
    isInfoDraw:bool = True
    isTypeDraw:bool = True

    def info(*str:str) -> None:
        if Log.isInfoDraw:
            print(f"{Color.GREEN}Info:{Color.COLOR_DEFAULT}{str}")

    def error(str:str) -> None:
        print(f"{Color.RED}Error:{Color.COLOR_DEFAULT}{str}")

    def warning(str:str) -> None:
        print(f"{Color.YELLOW}Warning:{Color.COLOR_DEFAULT}{str}")

    def message(str:str) -> None:
        print(f"{str}")

    def type(str:str) -> None:
        if Log.isTypeDraw:
            print(f"{Color.BLUE}type:{Color.COLOR_DEFAULT}{type(str)}")

#================================================================
# End of file.
#================================================================
