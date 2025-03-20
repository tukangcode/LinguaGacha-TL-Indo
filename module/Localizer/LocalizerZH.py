from module.Localizer.LocalizerBase import LocalizerBase

class LocalizerZH(LocalizerBase):
    # Add the missing pause attribute
    pause: str = "暂停"

    # If there are other missing attributes, add them here as well