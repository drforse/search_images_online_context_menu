import winreg
import sys
import pathlib


def main():
    pythonw_path = (pathlib.Path(sys.executable).parent / "pythonw.exe")
    script_dir = pathlib.Path(__file__).absolute().parent.parent

    parent_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Search Image Online")
    winreg.SetValueEx(parent_key, "MUIVerb", 0, winreg.REG_SZ, "Search Image Online")
    winreg.SetValueEx(parent_key, "subcommands", 0, winreg.REG_SZ, "")
    parent_key.Close()

    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Search Image Online\shell").Close()
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Search Image Online\shell\Google").Close()
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Search Image Online\shell\Yandex").Close()

    google_command = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Search Image Online\shell\Google\command")
    winreg.SetValue(google_command, "", winreg.REG_SZ, fr'"{pythonw_path}" "{script_dir}\main.pyw" "google" "%1"')
    google_command.Close()

    yandex_command = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Search Image Online\shell\Yandex\command")
    winreg.SetValue(yandex_command, "", winreg.REG_SZ, fr'"{pythonw_path}" "{script_dir}\main.pyw" "yandex" "%1"')
    yandex_command.Close()


if __name__ == "__main__":
    main()
