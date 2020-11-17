import winreg


def main():
    winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Search Image Online\shell\Google\command")
    winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Search Image Online\shell\Yandex\command")
    winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Search Image Online\shell\Google")
    winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Search Image Online\shell\Yandex")
    winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Search Image Online\shell")
    winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Search Image Online")


if __name__ == "__main__":
    main()
