import psutil


def get_all_children(proc):
    res = []
    res += proc.children()
    for child in proc.children():
        res += get_all_children(child)
    return res


def kill_chrome_instances():
    """
    Killing instances of Google Chrome created by YandexParser
    """
    print('\nKilling Google Chrome instances...')
    found = 0
    killed = 0
    for process in psutil.process_iter():
        if 'chrome' in process.name():
            if process.name() == 'chromedriver.exe':
                children = get_all_children(process)
                for child in children:
                    child.terminate()
                    killed += 1
                process.terminate()
                killed += 1

    print(f'{killed} processes killed')


if __name__ == "__main__":
    kill_chrome_instances()