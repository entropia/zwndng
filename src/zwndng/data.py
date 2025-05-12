import importlib.resources as resources


def sach_pdf_path():
    return resources.files("zwndng") / "data" / "sach.pdf"


def geld_pdf_path():
    return resources.files("zwndng") / "data" / "geld.pdf"


def sammel_pdf_path():
    return resources.files("zwndng") / "data" / "sammel.pdf"


def fira_bold_path():
    return resources.files("zwndng") / "data" / "FiraSans-Bold.ttf"


def fira_italic_path():
    return resources.files("zwndng") / "data" / "FiraSans-Italic.ttf"


def fira_regular_path():
    return resources.files("zwndng") / "data" / "FiraSans-Regular.ttf"
