from selenium.webdriver.common.by import By

from radish import world


class Control():
    def __init__(self, tag="*", **kwargs):
        filter = []
        filterstr = ""

        for name, value in kwargs.items():
            if name.startswith('_'):
                name = name[1:]
            if name == 'text':
                name = "."
            name = name.replace("_", "-")
            filter.append(f"contains(@{name}, '{value}')")
        if len(filter) > 0:
            filterstr = f'[{" and ".join(filter)}]'
        self.xpath = f"//{tag}{filterstr}"

    def input(self, text):
        self.locate()
        self.match.send_keys(text)

    def locate(self, timeout=30):
        self.timeout = timeout
        self.match = world.webdriver.find_element(By.XPATH, self.xpath)

    def click(self):
        self.locate()
        self.match.click()

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        world.webdriver.implicitly_wait(float(value))


class Title(Control):
    def __init__(self, **kwargs):
        super().__init__(tag='h1')


class Input(Control):
    def __init__(self, **kwargs):
        super().__init__(tag='input', **kwargs)


class Link(Control):
    def __init__(self, **kwargs):
        super().__init__(tag='a')
